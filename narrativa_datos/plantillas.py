"""Plantillas de Reportes de Narrativa con Datos

Define las estructuras de textos en Markdown y las listas de comprobación en español.
"""

from typing import Dict, List

# ── Plantilla de Reporte de Contexto ──
REPORTE_CONTEXTO_PLANTILLA = """# 📋 Reporte de Análisis de Contexto: {title}

## Perfil de la Audiencia
| Dimensión | Detalle |
|-----------|---------|
| Audiencia Principal | {audience} |
| Tomador de Decisiones | {decision_maker} |
| Nivel de Conocimiento | {knowledge_level} |
| Estado de Relación | {relationship} |
| Motivación Principal | {motivation} |

## Mecanismo de Comunicación
- **Formato**: {mechanism}
- **Tono General**: {tone}

## Mensaje Central
### Historia de 3 Minutos
{three_min_story}

### Idea Fuerza (Big Idea)
> {big_idea}

### Datos de Soporte
{supporting_data}

### Riesgos y Contraevidencia
{risks}

## Llamado a la Acción (Call to Action)
{call_to_action}
"""

# ── Plantilla de Reporte de Selección de Gráfico ──
REPORTE_SELECCION_GRAFICO_PLANTILLA = """# 📊 Recomendación de Tipo de Gráfico

## Propiedades de los Datos
- **Tipo de datos**: {data_type}
- **Número de series de datos**: {series_count}
- **Número de categorías**: {category_count}
- **Contiene dimensión temporal**: {has_time}

## Gráficos Recomendados
### Gráfico Recomendado (Principal): {primary_chart}
{primary_reason}

### Alternativa: {secondary_chart}
{secondary_reason}

## Gráficos a Evitar
{avoid_charts}

## Puntos Clave de Diseño
{design_notes}
"""

# ── Plantilla de Reporte de Depuración de Ruido Visual ──
REPORTE_DEPURACION_RUIDO_PLANTILLA = """# 🧹 Reporte de Depuración de Ruido Visual

## Resumen del Diagnóstico
- **Elementos de ruido detectados**: {clutter_count}
- **Porcentaje de reducción de carga cognitiva estimado**: {reduction_pct}%

## Inventario de Ruido Visual Detectado
{clutter_items}

## Pasos Recomendados de Depuración
{declutter_steps}

## Propuestas de Aplicación Gestalt
{gestalt_suggestions}
"""

# ── Plantilla de Reporte de Atención Visual ──
REPORTE_ATENCION_PLANTILLA = """# 🎯 Planificación de Atención Visual

## Análisis de Focos de Atención
{current_focus}

## Recomendaciones sobre Atributos Preatentivos
{preattentive_suggestions}

## Estrategia de Color Recomendada
- **Estrategia sugerida**: {color_strategy}
- **Color Base (Fondo)**: {base_color}
- **Color de Énfasis**: {accent_color}
{color_notes}

## Jerarquía Visual de Lectura
{visual_hierarchy}
"""

# ── Plantilla de Reporte de Evaluación de Diseño ──
REPORTE_EVALUACION_DISENO_PLANTILLA = """# 🎨 Reporte de Evaluación de Diseño Visual

## Asequibilidad (Percepción de Funciones)
{affordances}

## Accesibilidad
{accessibility}

## Estética y Formato
{aesthetics}

## Plan de Mejoras
{improvements}
"""

# ── Plantilla de Construcción de Historia ──
REPORTE_HISTORIA_PLANTILLA = """# 📖 Construcción de Historia con Datos

## Estructura Narrativa de Tres Actos

### Primer Acto: Inicio (Contexto y Conflicto)
- **Contexto**: {setting}
- **Protagonista**: {protagonist} (enfocado en la audiencia)
- **Desequilibrio (Conflicto)**: {imbalance}
- **Equilibrio Deseado**: {desired_balance}

### Segundo Acto: Nudo (Evidencia de Datos)
{middle_content}

### Tercer Acto: Desenlace (Resolución)
- **Llamado a la Acción**: {call_to_action}
- **Retorno al Inicio**: {tie_back}

## Diseño Narrativo
- **Flujo Narrativo**: {narrative_flow}
- **Modo de Entrega**: {delivery_mode}

## Estructura de Refuerzo (Anuncio, Desarrollo, Repaso)
- **Anuncio (Bing)**: {bing}
- **Desarrollo (Bang)**: {bang}
- **Repaso (Bongo)**: {bongo}

## Secuencia de Diapositivas (Lógica Horizontal)
{slide_titles}
"""

# ── Plantilla de Diagnóstico Completo ──
REPORTE_DIAGNOSTICO_PLANTILLA = """# 🔍 Reporte de Diagnóstico Completo SWD: {title}

## Calificación General: {total_score}/100 {score_badge}

{dimension_details}

## Plan de Mejoras Prioritarias (Top 3)
{top_improvements}

## Recomendaciones de Transformación Antes/Después
{makeover_suggestions}
"""

# ── Plantilla de Reporte de Rediseño (Makeover) ──
REPORTE_REDISEÑO_PLANTILLA = """# ✨ Plan de Rediseño y Transformación: {title}

## Diagnóstico de Defectos Originales
{original_issues}

## Pasos de Transformación (Método SWD)
{makeover_steps}

## Especificaciones del Diseño Propuesto
{design_spec}

## Secuencia Narrativa de Diapositivas
{narrative_enhancement}
"""

# ── Lista de Comprobación de Gráficos SWD ──
LISTA_COMPROBACION_GRAFICO: List[tuple] = [
    ("Título de acción", "Usar título declarativo con conclusión en lugar de descriptivo."),
    ("Títulos de eje", "Cada eje debe tener una etiqueta clara que indique las unidades."),
    ("Línea base cero", "Los gráficos de barra deben comenzar estrictamente en cero."),
    ("Intervalos de tiempo", "Mantener intervalos temporales constantes y proporcionales."),
    ("Etiquetado directo", "Rotular directamente las series de datos y evitar leyendas externas."),
    ("Bordes de gráfico", "Remover bordes limitantes exteriores innecesarios."),
    ("Líneas de cuadrícula", "Remover o atenuar líneas de fondo haciéndolas de color gris tenue."),
    ("Marcadores de datos", "Remover puntos en cada coordenada, usándolos solo para énfasis."),
    ("Ceros decimales", "Quitar decimales finales redundantes en los ejes numéricos."),
    ("Esquema de color", "Usar colores selectivos (gris de base y un único color destacado)."),
    ("Unidades legibles", "Mantener símbolos de porcentaje, moneda y comas de millares."),
    ("Fuente de datos", "Citar el origen de los datos al pie del gráfico."),
]

# ── Plantillas de Detalles de Estrategias de Color ──
PLANTILLAS_ESTRATEGIAS_COLOR: Dict[str, Dict[str, str]] = {
    "gris_mas_uno": {
        "nombre": "Gris como base + un único color de énfasis",
        "base": "Gris claro o medio (#808080)",
        "enfasis": "Azul (#4472C4)",
        "negativo": "Naranja (#ED7D31)",
        "descripcion": "Todos los elementos secundarios en tonos grises; el foco se colorea con un color llamativo. Es la técnica más recomendada.",
    },
    "secuencial": {
        "nombre": "Gradiente secuencial monocromático",
        "base": "Celeste claro (#D6E4F0)",
        "enfasis": "Azul oscuro (#1F4E79)",
        "negativo": "",
        "descripcion": "Variación de brillo e intensidad de un mismo tono. Ideal para mapas de calor o tablas ordenadas.",
    },
    "divergente": {
        "nombre": "Gradiente divergente bicolor",
        "base": "Gris neutro (#808080)",
        "enfasis": "Azul para positivos (#4472C4)",
        "negativo": "Naranja para negativos (#ED7D31)",
        "descripcion": "Dos tonos de color opuestos que contrastan desde un punto medio gris. Ideal para saldos de caja o ganancias y pérdidas.",
    },
    "categorico_limitado": {
        "nombre": "Colores categóricos selectivos",
        "base": "Gris (#808080)",
        "enfasis": "Azul (#4472C4)",
        "negativo": "",
        "descripcion": "Uso de máximo 3 o 4 colores bien diferenciados para distinguir categorías sin confundir visualmente.",
    },
}
