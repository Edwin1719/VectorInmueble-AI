import streamlit as st
import os
from pathlib import Path
import time
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Adjust the path to import from the src directory
import sys
sys.path.append(str(Path(__file__).parent / "src"))
from agente_inmobiliario.crew import AgenteInmobiliarioCrew

# =============================================================================
# CONFIGURACIÓN DE LA APLICACIÓN STREAMLIT
# =============================================================================

st.set_page_config(
    page_title="🏠 Análisis Inmobiliario con CrewAI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        background-color: #0068C9;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
    .st-emotion-cache-1y4p8pa {
        width: 100%;
    }
    .st-emotion-cache-1v0mbdj {
        width: 100%;
    }
    .analysis-output {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# =============================================================================
# TÍTULO Y DESCRIPCIÓN
# =============================================================================

st.title("🤖 Análisis Inmobiliario con Agentes CrewAI")
st.markdown("### 📍 Pereira, Risaralda - Colombia")
st.markdown("*Encuentra las mejores oportunidades de inversión inmobiliaria usando un equipo de agentes de IA.*")

# =============================================================================
# SIDEBAR - CONFIGURACIÓN
# =============================================================================

with st.sidebar:
    st.header("⚙️ Configuración de Búsqueda")
    
    st.info("Las API Keys se cargan desde el archivo `.env` en la raíz del proyecto.")
    
    st.divider()
    
    # Parámetros de búsqueda
    st.subheader("🎯 Parámetros de Búsqueda")
    
    col1, col2 = st.columns(2)
    with col1:
        precio_min = st.number_input(
            "💰 Precio Mínimo (COP)", 
            value=200_000_000, 
            step=10_000_000,
            format="%d"
        )
    with col2:
        precio_max = st.number_input(
            "💰 Precio Máximo (COP)", 
            value=600_000_000, 
            step=10_000_000,
            format="%d"
        )
    
    col3, col4 = st.columns(2)
    with col3:
        area_min = st.number_input("📐 Área Mín (m²)", value=80, step=10)
    with col4:
        area_max = st.number_input("📐 Área Máx (m²)", value=150, step=10)
    
    sectores = st.multiselect(
        "🏘️ Sectores de Interés",
        ["Centro", "Cuba", "Pinares", "Ciudad Jardín", "Villa Santana", "Álamos", "Parque Industrial"],
        default=["Cuba", "Pinares", "Ciudad Jardín", "Álamos"]
    )
    
    estratos = st.multiselect(
        "🏛️ Estratos",
        [2, 3, 4, 5, 6],
        default=[3, 4, 5]
    )
    
    tipos_propiedad = st.multiselect(
        "🏡 Tipo de Propiedad",
        ["Casa", "Apartamento", "Apartaestudio", "Terreno"],
        default=["Casa", "Apartamento"]
    )

# =============================================================================
# CONTENIDO PRINCIPAL
# =============================================================================

# Métricas principales
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Rango de Inversión", 
        f"${precio_min/1_000_000:.0f}M - ${precio_max/1_000_000:.0f}M COP"
    )

with col2:
    st.metric(
        "📐 Área Objetivo", 
        f"{area_min} - {area_max} m²"
    )

with col3:
    st.metric(
        "🏘️ Sectores", 
        f"{len(sectores)} seleccionados"
    )

with col4:
    st.metric(
        "🏛️ Estratos", 
        f"{len(estratos)} estratos"
    )

st.divider()

# =============================================================================
# BOTÓN DE ANÁLISIS Y EJECUCIÓN
# =============================================================================

col_center = st.columns([1, 2, 1])[1]

with col_center:
    if st.button("🚀 INICIAR ANÁLISIS CON CREWAI", type="primary", use_container_width=True):
        # --- Validación de Entorno y Entradas ---
        if not os.getenv("OPENAI_API_KEY") or not os.getenv("SERPER_API_KEY") or not os.getenv("TAVILY_API_KEY"):
            st.error("⚠️ Claves API no encontradas. Asegúrate de tener un archivo `.env` con `OPENAI_API_KEY`, `SERPER_API_KEY` y `TAVILY_API_KEY`.")
            st.stop()
        
        if not sectores:
            st.error("⚠️ Por favor selecciona al menos un sector de interés.")
            st.stop()
            
        if not estratos:
            st.error("⚠️ Por favor selecciona al menos un estrato.")
            st.stop()
            
        if not tipos_propiedad:
            st.error("⚠️ Por favor selecciona al menos un tipo de propiedad.")
            st.stop()

        # --- Preparación de Entradas ---
        inputs = {
            'precio_min': f"{precio_min:,}",
            'precio_max': f"{precio_max:,}",
            'area_min': area_min,
            'area_max': area_max,
            'sectores': ", ".join(sectores),
            'estratos': ", ".join(map(str, estratos)),
            'tipos_propiedad': ", ".join(tipos_propiedad)
        }

        # --- Ejecución del Crew ---
        with st.spinner("🤖 El equipo de agentes de IA ha comenzado a trabajar... Esto puede tardar varios minutos..."):
            try:
                # Instanciar y ejecutar el crew
                inmobiliario_crew = AgenteInmobiliarioCrew()
                result = inmobiliario_crew.crew().kickoff(inputs=inputs)
                
                st.success("✅ ¡Análisis completado exitosamente!")
                
                # --- Mostrar Resultados ---
                st.markdown("### 🎯 Reporte Final del Equipo de Agentes")
                st.markdown(result)
                
                st.divider()
                
                # --- Mostrar Archivo Final para Descarga ---
                st.markdown("### 📁 Descargar Reporte Completo")
                final_report_path = "reporte_inversion_pereira.md"
                if os.path.exists(final_report_path):
                    try:
                        with open(final_report_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        st.download_button(
                            "⬇️ Descargar Reporte Final",
                            content,
                            file_name=final_report_path,
                            mime='text/markdown',
                            use_container_width=True
                        )
                    except Exception as e:
                        st.error(f"Error al leer el archivo de reporte final: {e}")
                else:
                    st.warning("No se encontró el archivo de reporte final para descargar. El resultado principal se muestra arriba.")

            except Exception as e:
                st.error(f"❌ Ocurrió un error durante el análisis: {e}")
                st.exception(e) # Muestra el traceback para depuración

# = ancla para el footer
st.markdown('<a name="footer"></a>', unsafe_allow_html=True)
st.divider()
st.markdown(
    "<p style='text-align: center; color: #666;'>Powered by CrewAI & Streamlit</p>", 
    unsafe_allow_html=True
)
