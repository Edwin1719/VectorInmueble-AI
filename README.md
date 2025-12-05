# Agente Inmobiliario Crew

This project uses crewAI to create a team of AI agents for real estate analysis in Pereira, Colombia.

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Set your API keys in the `.env` file.

Run the crew:
```bash
python src/agente_inmobiliario/main.py
```

## Adaptabilidad

Este proyecto está diseñado para ser flexible y adaptable a diferentes ciudades, regiones o incluso países. La configuración inicial se centra en Pereira, Colombia, pero puedes personalizarla fácilmente para realizar análisis inmobiliarios en cualquier otra área.

### ¿Cómo adaptarlo a otra región?

Para enfocar el análisis en una nueva ubicación, debes ajustar las instrucciones y los datos de entrada proporcionados a los agentes. Principalmente:

1.  **Modifica los `inputs` en `src/agente_inmobiliario/main.py`**: Cambia los valores de las variables como `sectores`, `estratos`, `precio_min`, y `precio_max` para que coincidan con las características de la nueva área de interés.

2.  **Ajusta los `prompts` en `src/agente_inmobiliario/config/tasks.yaml`**: Las descripciones de las tareas (`description`) contienen los prompts que guían a los agentes. Puedes hacer estas instrucciones más específicas para la nueva región, mencionar fuentes de datos locales, o cambiar los criterios de análisis.

### Mejorando los Resultados

Para obtener informes más detallados y mejor estructurados, puedes:

-   **Refinar los prompts**: Experimenta con prompts más detallados en `tasks.yaml`. Por ejemplo, puedes solicitar un formato de salida específico, pedir un análisis comparativo entre diferentes zonas, o requerir la inclusión de gráficos y tablas en el informe final.
-   **Crear nuevos agentes o tareas**: Si necesitas un análisis más profundo, puedes añadir nuevos agentes especializados (por ejemplo, un "Especialista en Zonificación y Normativa Urbana") o nuevas tareas que cubran aspectos adicionales del mercado inmobiliario.
