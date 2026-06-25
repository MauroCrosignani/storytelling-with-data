# Narrativa con Datos (Storytelling with Data) en Español

> **Transforma datos en decisiones. Transforma gráficos en historias.**

Este proyecto es una biblioteca de Python y una habilidad de agente de IA diseñada al 100% en español. Recrea los principios fundamentales expuestos por Cole Nussbaumer Knaflic en su libro *Storytelling with Data*, proporcionando herramientas analíticas para estructurar, auditar y rediseñar visualizaciones de datos para entornos ejecutivos.

---

## 📑 Tabla de Contenidos
- [Características](#características)
- [Instalación](#instalación)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Uso Básico](#uso-básico)
- [Las 8 Capacidades Explicadas](#las-8-capacidades-explicadas)
- [Licencia](#licencia)

---

## Características
*   **Cero dependencias de ejecución**: Escrita utilizando únicamente la biblioteca estándar de Python, haciéndola segura, ligera y libre de vulnerabilidades externas.
*   **100% en Español**: Toda la interfaz pública, reportes de salida, diagnósticos, constantes, excepciones y documentación están exclusivamente en idioma español.
*   **Enfoque en Seguridad**: Remueve cualquier tipo de enlaces externos, dependencias desactualizadas o accesos no declarados.
*   **Fachada Unificada**: Ofrece acceso simple a todo el flujo de trabajo mediante la clase unificada `NarrativaDatos`.

---

## Instalación
Para instalar la biblioteca en modo editable en un entorno virtual de desarrollo:

```bash
# Crear entorno virtual si no existe
python -m venv .venv

# Activar entorno virtual
# En Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# Instalar dependencias de desarrollo y empaquetar localmente
python -m pip install -e ".[desarrollo]"
```

Para ejecutar la suite de pruebas unitarias:
```bash
python -m pytest tests/ -v
```

---

## Estructura del Proyecto
```
storytelling-with-data/
├── pyproject.toml              # Definición de empaquetado seguro con Hatchling
├── README.md                   # Documentación en español (este archivo)
├── SKILL.md                    # Definición de la habilidad para agentes IA en español
├── narrativa_datos/            # Módulo principal
│   ├── __init__.py             # Fachada principal NarrativaDatos
│   ├── config.py               # Constantes Gestalt, gráficos, colores y configuraciones
│   ├── contexto.py             # Análisis de contexto y audiencia
│   ├── seleccionador_grafico.py # Árbol de decisión para selección de gráficos
│   ├── depurador_ruido.py      # Detección de ruido visual y carga cognitiva
│   ├── atencion.py             # Planificación de atributos preatentivos
│   ├── evaluador_diseno.py     # Auditoría de accesibilidad, estética y asequibilidad
│   ├── narrador.py             # Arco narrativo de tres actos
│   ├── diagnostico.py          # Motor cuantitativo sobre 100 puntos
│   ├── redisenador.py          # Guía paso a paso de rediseño (makeover)
│   └── plantillas.py           # Plantillas Markdown de reportes
└── tests/                      # Suite de pruebas unitarias
    └── test_narrativa.py       # Pruebas en español
```

---

## Uso Básico
```python
from narrativa_datos import NarrativaDatos

# Inicializar proyecto
proyecto = NarrativaDatos("Estudio de Conversión")

# Recomendar un gráfico
reporte_grafico = proyecto.recomendar_grafico(
    tipo_datos="continuo", 
    tiene_tiempo=True, 
    cantidad_series=2
)
print(reporte_grafico)
```

---

## Las 8 Capacidades Explicadas

1.  **Análisis de Contexto**: Identificar quién es tu audiencia principal, el tomador de decisiones clave y redactar la Idea Fuerza (Big Idea) que resuma tu tesis en una sola frase con intereses claros.
2.  **Selección de Gráficos**: Recomendar la visualización idónea evitando gráficos problemáticos como circulares (tartas), donas, 3D o doble eje Y.
3.  **Depuración de Ruido**: Remover ruido visual (bordes, cuadrículas, ceros flotantes) que consume capacidad cognitiva del receptor.
4.  **Dirección de la Atención**: Planificar el uso de color selectivo (base gris y un único color destacado) y variaciones de tamaño de texto.
5.  **Pensar como un Diseñador**: Evaluar la legibilidad, la alineación a la izquierda y el uso inteligente del espacio en blanco.
6.  **Contar una Historia**: Estructurar los datos en un arco de tres actos: Inicio (Contexto/Conflicto), Nudo (Datos/Comparativas) y Desenlace (Acción).
7.  **Diagnóstico Completo**: Medir cuantitativamente la calidad visual de un gráfico en una escala de 0 a 100 basada en 5 dimensiones.
8.  **Rediseño de Gráficos**: Generar recetas y pasos incrementales de transformación para reconstruir gráficos mal diseñados.

---

## Uso con Asistentes de IA (Copilot, ChatGPT, Claude)

Puedes utilizar el archivo unificado [contexto_completo.txt](texto/contexto_completo.txt) para proporcionar a un asistente de IA todo el contexto de esta biblioteca. A continuación se presenta un ejemplo de instrucción (prompt) en español para iniciar una consultoría guiada por los principios de *Storytelling with Data*:

> *Actúa como un consultor experto en Storytelling with Data (SWD). Adjunto el código fuente y las directrices de mi proyecto en español (`narrativa_datos`). Quiero que me hagas una entrevista interactiva, pregunta por pregunta, para extraer los detalles de mi caso de negocio actual (audiencia, Idea Fuerza, conflicto, datos de soporte, etc.). Basándote en mis respuestas y aplicando estrictamente las reglas definidas en el código de este contexto, guíame para generar el reporte de contexto y el arco narrativo final de mi presentación.*

---

## Licencia
Este proyecto está licenciado bajo la Licencia MIT.
