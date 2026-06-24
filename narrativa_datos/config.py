"""Módulo de Configuración de Narrativa con Datos

Define dimensiones de diagnóstico, tipos de gráficos, ruido visual, principios Gestalt y estrategias de color.
"""

from dataclasses import dataclass, field
from typing import Dict, List


# ── Tipos de Gráficos ──
TIPOS_GRAFICO = (
    "texto_simple", "tabla", "mapa_calor", "grafico_dispersion",
    "linea", "grafico_pendiente", "barras_verticales", "barras_horizontales",
    "barras_verticales_apiladas", "barras_horizontales_apiladas",
    "cascada", "area_cuadrada",
)

ETIQUETAS_GRAFICO: Dict[str, str] = {
    "texto_simple": "Texto Simple (un par de números clave)",
    "tabla": "Tabla (para consulta de valores precisos)",
    "mapa_calor": "Mapa de Calor (tabla con colores de intensidad)",
    "grafico_dispersion": "Gráfico de Dispersión (relación entre dos variables)",
    "linea": "Gráfico de Líneas (tendencias continuas en el tiempo)",
    "grafico_pendiente": "Gráfico de Pendiente (comparación rápida de dos puntos temporales)",
    "barras_verticales": "Barras Verticales (comparación de categorías con etiquetas cortas)",
    "barras_horizontales": "Barras Horizontales (comparación de categorías con etiquetas largas)",
    "barras_verticales_apiladas": "Barras Verticales Apiladas (parte del todo sobre barras verticales)",
    "barras_horizontales_apiladas": "Barras Horizontales Apiladas (parte del todo sobre barras horizontales)",
    "cascada": "Gráfico de Cascada (flujo de valores iniciales, cambios y final)",
    "area_cuadrada": "Gráfico de Área Cuadrada (comparación de magnitudes dispares)",
}

GRAFICOS_A_EVITAR = ("circular", "dona", "tres_dimensiones", "doble_eje_y")

ETIQUETAS_EVITAR: Dict[str, str] = {
    "circular": "Gráfico Circular (tarta) — El ojo humano tiene dificultades para comparar ángulos y áreas.",
    "dona": "Gráfico de Dona — Es aún más difícil estimar longitudes de arco que áreas circulares.",
    "tres_dimensiones": "Efecto 3D — Distorsiona la perspectiva de los datos de forma innecesaria.",
    "doble_eje_y": "Doble Eje Y — Causa confusión sobre qué serie corresponde a qué escala de datos.",
}

# ── Tipos de Datos ──
TIPOS_DATOS = ("numero_unico", "pocos_numeros", "categorico", "continuo", "relacion", "parte_del_todo")

# ── Atributos Preatentivos ──
ATRIBUTOS_PREATENTIVOS = (
    "orientacion", "forma", "longitud_linea", "ancho_linea",
    "tamaño", "curvatura", "marcas_añadidas", "encierro",
    "tono", "intensidad", "posicion_espacial", "movimiento",
)

ATRIBUTOS_CUANTITATIVOS = ("longitud_linea", "posicion_espacial", "ancho_linea", "tamaño", "intensidad")
ATRIBUTOS_CATEGORICOS = ("tono", "forma", "orientacion", "encierro")

# ── Principios Gestalt ──
PRINCIPIOS_GESTALT = (
    "proximidad", "similitud", "encierro", "cierre", "continuidad", "conexion",
)

ETIQUETAS_GESTALT: Dict[str, str] = {
    "proximidad": "Proximidad — Los objetos cercanos físicamente se perciben como un grupo lógico.",
    "similitud": "Similitud — Los objetos con color, forma o tamaño idéntico se asocian entre sí.",
    "encierro": "Encierro — Los elementos rodeados por una frontera visual se perciben como un conjunto.",
    "cierre": "Cierre — El cerebro tiende a completar figuras percibidas como incompletas.",
    "continuidad": "Continuidad — El ojo sigue de forma natural la trayectoria más suave y fluida.",
    "conexion": "Conexión — Los elementos unidos por una línea se perciben como un único grupo.",
}

# ── Elementos de Ruido Visual (Clutter) ──
ELEMENTOS_RUIDO = (
    "borde_grafico", "lineas_cuadricula", "marcadores_datos", "ceros_finales",
    "texto_diagonal", "leyenda_separada", "etiquetas_redundantes",
    "sombreado_fondo", "marcas_eje", "efectos_3d",
)

ETIQUETAS_RUIDO: Dict[str, str] = {
    "borde_grafico": "Borde del gráfico — En la mayoría de los casos es innecesario (principio de cierre).",
    "lineas_cuadricula": "Líneas de cuadrícula — Si son necesarias para leer valores, deben ser muy tenues (gris claro).",
    "marcadores_datos": "Marcadores de datos en cada punto — Sobrecargan visualmente la línea sin aportar claridad.",
    "ceros_finales": "Ceros finales redundantes — Aumentan la complejidad numérica sin añadir precisión útil.",
    "texto_diagonal": "Texto en diagonal — Reduce la velocidad de lectura un 52%. Prefiere barras horizontales.",
    "leyenda_separada": "Leyenda alejada de los datos — Obliga a la vista a hacer saltos constantes. Etiqueta directamente.",
    "etiquetas_redundantes": "Etiquetas de datos redundantes — Mostrar etiquetas y mantener el eje al mismo tiempo.",
    "sombreado_fondo": "Sombreado de fondo — Distrae del contenido principal sin justificación.",
    "marcas_eje": "Marcas de eje excesivas — Sobrecargan las líneas de escala.",
    "efectos_3d": "Efectos en 3D — Distorsionan la lectura de valores.",
}

# ── Dimensiones de Diagnóstico ──
DIMENSIONES_DIAGNOSTICO = (
    "contexto", "seleccion_visual", "ruido", "atencion", "diseno_narrativa",
)

ETIQUETAS_DIAGNOSTICO: Dict[str, str] = {
    "contexto": "Evaluación del Contexto",
    "seleccion_visual": "Evaluación de Selección Visual",
    "ruido": "Evaluación de Ruido Visual",
    "atencion": "Evaluación de Dirección de Atención",
    "diseno_narrativa": "Evaluación de Diseño y Narrativa",
}

# ── Estructura de Historia ──
ACTOS_HISTORIA = ("inicio", "nudo", "desenlace")

ETIQUETAS_HISTORIA: Dict[str, str] = {
    "inicio": "Inicio — Define el contexto, el protagonista y el desequilibrio.",
    "nudo": "Nudo — Presenta los datos y la evidencia para argumentar el caso.",
    "desenlace": "Desenlace — Llamado a la acción y resolución esperada.",
}

FLUJOS_NARRATIVOS = ("cronologico", "comenzar_por_el_final")

# ── Estrategias de Color ──
ESTRATEGIAS_COLOR = ("gris_mas_uno", "secuencial", "divergente", "categorico_limitado")

ETIQUETAS_COLOR: Dict[str, str] = {
    "gris_mas_uno": "Gris como base + un único color de énfasis (recomendado)",
    "secuencial": "Gris a color con gradiente (ideal para mapas de calor/clasificación)",
    "divergente": "Dos colores opuestos (ideal para contrastar valores positivos y negativos)",
    "categorico_limitado": "Colores categóricos limitados (máximo de 3 a 4 colores)",
}


@dataclass
class ConfiguracionAnalisis:
    """Configuración en tiempo de ejecución para las tareas de análisis"""
    dimensiones_incluidas: List[str] = field(
        default_factory=lambda: list(DIMENSIONES_DIAGNOSTICO))
    formato_salida: str = "markdown"
    idioma: str = "es"
    estrategia_color: str = "gris_mas_uno"
    limite_elementos_ruido: int = 10

    def validar(self) -> None:
        for d in self.dimensiones_incluidas:
            if d not in DIMENSIONES_DIAGNOSTICO:
                raise ValueError(f"Dimensión de diagnóstico desconocida: {d}，opciones: {DIMENSIONES_DIAGNOSTICO}")
        if self.formato_salida not in ("markdown", "json", "texto"):
            raise ValueError(f"Formato de salida desconocido: {self.formato_salida}")
        if self.estrategia_color not in ESTRATEGIAS_COLOR:
            raise ValueError(f"Estrategia de color desconocida: {self.estrategia_color}")
