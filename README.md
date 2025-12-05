# VectorInmueble AI

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.x](https://img.shields.io/badge/Python-3.x-3776AB.svg)
![Framework: CrewAI](https://img.shields.io/badge/Framework-CrewAI-orange.svg)
![Frontend: Streamlit](https://img.shields.io/badge/Frontend-Streamlit-ff69b4.svg)

> La plataforma de análisis inmobiliario con IA, adaptable a cualquier mercado del mundo. Despliega un equipo de agentes especializados que generan informes detallados sobre precios, zonas de alto valor y proyecciones de rentabilidad para que descubras oportunidades ocultas y tomes decisiones de inversión estratégicas.

## Descripción General

**VectorInmueble AI** es un sistema avanzado que utiliza un equipo de agentes de inteligencia artificial (CrewAI) para realizar análisis de mercado inmobiliario de forma autónoma. La plataforma es capaz de investigar, analizar y generar informes de inversión detallados para cualquier ciudad o región, proporcionando una ventaja estratégica a inversores, analistas y entusiastas del sector inmobiliario.

## Características

- **Análisis Autónomo**: Un equipo de agentes de IA especializados que trabajan en conjunto para recopilar y procesar datos.
- **Adaptabilidad Global**: Fácilmente configurable para analizar el mercado inmobiliario de cualquier ciudad o país.
- **Informes Detallados**: Generación de reportes en formato Markdown con análisis de precios, zonas, rentabilidad y conclusiones estratégicas.
- **Interfaz Interactiva**: Una interfaz de usuario amigable construida con Streamlit para facilitar la interacción y visualización de resultados.
- **Doble Interfaz de Uso**: Puede ser ejecutado a través de una interfaz web o como un script de consola.

## Arquitectura del Proyecto

El proyecto está estructurado para separar la lógica de los agentes, la configuración y la interfaz de usuario.

```
VectorInmueble AI/
├── app.py                   # Interfaz de usuario con Streamlit
├── requirements.txt         # Dependencias del proyecto
├── .env.example             # Plantilla para variables de entorno
├── src/
│   └── agente_inmobiliario/
│       ├── __init__.py
│       ├── crew.py          # Define los agentes, tareas y el "Crew"
│       ├── main.py          # Punto de entrada para ejecución por consola
│       ├── config/
│       │   ├── agents.yaml  # Configuración y prompts de los agentes
│       │   └── tasks.yaml   # Configuración de las tareas
│       └── tools/
│           └── custom_tools.py # Herramientas personalizadas para los agentes
└── ...
```

- **`app.py`**: El frontend de la aplicación. Se encarga de capturar las entradas del usuario y mostrar los resultados generados por el Crew.
- **`src/agente_inmobiliario/crew.py`**: El núcleo del backend. Aquí se definen los agentes (con sus roles y herramientas) y las tareas que deben ejecutar.
- **`src/agente_inmobiliario/config/`**: Los archivos YAML permiten modificar los prompts, roles y descripciones de las tareas de forma sencilla, sin necesidad de cambiar el código.
- **`src/agente_inmobiliario/tools/`**: Directorio para herramientas personalizadas que los agentes pueden utilizar para interactuar con APIs o realizar acciones específicas.

## Tecnologías Utilizadas

- **Backend**: Python, CrewAI, LangChain
- **Frontend**: Streamlit
- **Modelos de Lenguaje**: OpenAI GPT-4o-mini (configurable)
- **Herramientas de Búsqueda**: Tavily & Serper

## Guía de Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

**1. Clona el Repositorio**
```bash
git clone https://github.com/tu-usuario/VectorInmueble-AI.git
cd VectorInmueble-AI
```

**2. Crea y Activa un Entorno Virtual**
Es una buena práctica aislar las dependencias del proyecto.
```bash
# Para Windows
python -m venv venv
venv\Scripts\activate

# Para macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instala las Dependencias**
```bash
pip install -r requirements.txt
```

**4. Configura las Variables de Entorno**
Copia el archivo de ejemplo y añade tus claves de API.
```bash
# Para Windows
copy .env.example .env

# Para macOS/Linux
cp .env.example .env
```
Abre el archivo `.env` y añade tus claves para `OPENAI_API_KEY`, `TAVILY_API_KEY`, y `SERPER_API_KEY`.

## Instrucciones de Uso

Puedes ejecutar la aplicación de dos maneras:

**A) A través de la Interfaz Web (Recomendado)**
Este comando iniciará una aplicación web local en tu navegador.
```bash
streamlit run app.py
```

**B) A través de la Consola**
Esta opción ejecuta el proceso directamente en tu terminal y muestra el resultado al final.
```bash
python -m src.agente_inmobiliario.main
```

## Personalización y Adaptabilidad

Este proyecto está diseñado para ser flexible. Para adaptarlo a una nueva ciudad o país:

1.  **Modifica los `inputs`**: Si usas la versión de consola, ajusta las variables de entrada en `src/agente_inmobiliario/main.py` (sectores, precios, etc.). En la versión de Streamlit, estos valores se introducen directamente en la interfaz.
2.  **Ajusta los Prompts**: Para un análisis más enfocado, edita los archivos `agents.yaml` y `tasks.yaml` en la carpeta `config`. Puedes refinar las instrucciones, cambiar el tono o solicitar un formato de salida específico.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
