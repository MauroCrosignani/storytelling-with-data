"""Selector y Recomendador de Gráficos

Analiza las propiedades del conjunto de datos y las intenciones de comunicación
para recomendar el mejor tipo de gráfico basándose en la metodología SWD.
"""

from dataclasses import dataclass, field
from typing import List, Optional

from .config import ETIQUETAS_GRAFICO, GRAFICOS_A_EVITAR, ETIQUETAS_EVITAR


@dataclass
class RecomendacionGrafico:
    """Resultado de la recomendación de un gráfico"""
    tipo_grafico: str
    etiqueta: str
    motivo: str
    notas_diseno: List[str] = field(default_factory=list)
    prioridad: int = 1  # 1=Primera opción (recomendado), 2=Alternativa razonable


@dataclass
class PerfilDatos:
    """Descriptor de las propiedades físicas y lógica del conjunto de datos"""
    tipo_datos: str = "categorico"               # categorico/continuo/relacion/numero_unico
    cantidad_series: int = 1
    cantidad_categorias: int = 0
    tiene_dimension_tiempo: bool = False
    tiene_valores_negativos: bool = False
    muestra_parte_del_todo: bool = False
    nombres_categorias_largos: bool = False
    compara_dos_puntos: bool = False
    muestra_cambios_inicio_fin: bool = False
    gran_diferencia_magnitud: bool = False


class SeleccionadorGrafico:
    """Selector de gráficos según el perfil de los datos"""

    def __init__(self) -> None:
        self._perfil: Optional[PerfilDatos] = None

    def establecer_perfil(self, **valores) -> "SeleccionadorGrafico":
        self._perfil = PerfilDatos(**valores)
        return self

    def verificar_evitar(self, grafico_propuesto: str) -> List[str]:
        """Comprueba si el gráfico propuesto está en la lista de prácticas desaconsejadas"""
        advertencias: List[str] = []
        clave = grafico_propuesto.lower().strip().replace(" ", "_")

        # Conversiones para tolerar variaciones comunes de nombres en español
        if "pie" in clave or "circular" in clave or "tarta" in clave:
            clave = "circular"
        elif "dona" in clave or "rosquilla" in clave:
            clave = "dona"
        elif "3d" in clave or "dimensiones" in clave:
            clave = "tres_dimensiones"
        elif "doble" in clave or "dos_ejes" in clave or "eje_secundario" in clave:
            clave = "doble_eje_y"

        if clave in GRAFICOS_A_EVITAR:
            advertencias.append(f"⚠️ {ETIQUETAS_EVITAR.get(clave, grafico_propuesto)} — Se aconseja buscar una alternativa.")

        if clave == "circular":
            advertencias.append("Alternativa recomendada: Gráfico de barras horizontales (ordenado de mayor a menor) o destacar directamente un número en texto simple.")
        elif clave == "dona":
            advertencias.append("Alternativa recomendada: Gráfico de barras horizontales o gráfico de barras horizontales apiladas al 100%.")
        elif clave == "tres_dimensiones":
            advertencias.append("Alternativa recomendada: Utilice siempre la versión equivalente en 2 dimensiones planas.")
        elif clave == "doble_eje_y":
            advertencias.append("Alternativa recomendada 1: Etiquete directamente los puntos de datos y omita el segundo eje.")
            advertencias.append("Alternativa recomendada 2: Divida la visualización verticalmente en dos gráficos individuales que compartan el eje X.")

        return advertencias

    def recomendar(self, perfil: Optional[PerfilDatos] = None) -> List[RecomendacionGrafico]:
        """Recomienda tipos de gráficos basados en el perfil de datos"""
        p = perfil or self._perfil
        if not p:
            raise ValueError("Debe establecer un perfil de datos mediante establecer_perfil() antes de recomendar.")

        recomendaciones: List[RecomendacionGrafico] = []

        # 1. Un único número o muy pocos valores
        if p.tipo_datos == "numero_unico" or (p.cantidad_series <= 2 and p.cantidad_categorias == 0):
            recomendaciones.append(RecomendacionGrafico(
                "texto_simple", ETIQUETAS_GRAFICO["texto_simple"],
                "Cuando solo tienes uno o dos números que comunicar, el texto directo tiene el mayor impacto.",
                ["Acompaña el número con un texto explicativo claro y conciso.",
                 "Usa un tamaño de fuente significativamente grande para destacar el valor central.",
                 "Puedes usar color para indicar la dirección del cambio (ej. incremento o descenso)."], 1))
            return recomendaciones

        # 2. Relación entre variables independientes
        if p.tipo_datos == "relacion":
            recomendaciones.append(RecomendacionGrafico(
                "grafico_dispersion", ETIQUETAS_GRAFICO["grafico_dispersion"],
                "Ideal para mostrar la relación entre dos variables distintas en un plano bidimensional.",
                ["Añade líneas de referencia (como promedios) para ayudar a categorizar cuadrantes de interés.",
                 "Etiqueta directamente los puntos excepcionales o casos de estudio de interés."], 1))
            return recomendaciones

        # 3. Datos continuos o de series de tiempo
        if p.tiene_dimension_tiempo or p.tipo_datos == "continuo":
            if p.compara_dos_puntos:
                recomendaciones.append(RecomendacionGrafico(
                    "grafico_pendiente", ETIQUETAS_GRAFICO["grafico_pendiente"],
                    "Perfecto para comparar dos momentos en el tiempo, mostrando tanto el cambio absoluto como la inclinación de la pendiente.",
                    ["Evita este gráfico si hay demasiadas líneas que se cruzan y confunden al lector.",
                     "Utiliza colores para destacar una o dos líneas de interés principal."], 1))

            recomendaciones.append(RecomendacionGrafico(
                "linea", ETIQUETAS_GRAFICO["linea"],
                "La opción predilecta para visualizar la evolución de tendencias a lo largo del tiempo de forma continua.",
                ["Asegúrate de que los intervalos de tiempo en el eje X sean constantes y uniformes.",
                 "Coloca las etiquetas de las series al final de cada línea en lugar de usar una leyenda separada.",
                 "Si incluye proyecciones o datos futuros, dibújelos con líneas discontinuas.",
                 "Evita cruzar más de 4 o 5 líneas en un mismo gráfico (evita el efecto espagueti)."],
                1 if not p.compara_dos_puntos else 2))
            return recomendaciones

        # 4. Proporción o Parte del todo
        if p.muestra_parte_del_todo:
            recomendaciones.append(RecomendacionGrafico(
                "barras_horizontales_apiladas", ETIQUETAS_GRAFICO["barras_horizontales_apiladas"],
                "La versión apilada al 100% permite comparar la estructura de componentes con una línea base alineada en ambos extremos.",
                ["Ideal para representar escalas Likert (encuestas de opinión).",
                 "Alinea las respuestas positivas a la derecha y las negativas a la izquierda para un contraste directo."], 1))

            if p.gran_diferencia_magnitud:
                recomendaciones.append(RecomendacionGrafico(
                    "area_cuadrada", ETIQUETAS_GRAFICO["area_cuadrada"],
                    "Cuando las magnitudes difieren en órdenes de tamaño insalvables para una barra ordinaria, el área cuadrada es una opción compacta.",
                    ["Utilice esta opción con cautela, ya que estimar diferencias de área es más difícil que diferencias de longitud."], 2))
            return recomendaciones

        # 5. Evolución incremental (Casos acumulativos)
        if p.muestra_cambios_inicio_fin:
            recomendaciones.append(RecomendacionGrafico(
                "cascada", ETIQUETAS_GRAFICO["cascada"],
                "Excelente para desglosar un valor inicial, sus incrementos o decrementos intermedios y el resultado final acumulado.",
                ["Utilice colores diferenciados para aumentos (ej. verde), disminuciones (ej. rojo) y totales globales (ej. gris oscuro)."], 1))
            return recomendaciones

        # 6. Datos categóricos ordinarios (Opción por defecto)
        if p.nombres_categorias_largos or p.cantidad_categorias > 5:
            recomendaciones.append(RecomendacionGrafico(
                "barras_horizontales", ETIQUETAS_GRAFICO["barras_horizontales"],
                "El gráfico estándar por excelencia para datos categóricos. Las etiquetas se leen de izquierda a derecha de forma natural.",
                ["Ordena las categorías de forma lógica: por orden alfabético natural o por magnitud descendente.",
                 "El ancho de las barras debe ser mayor que el espacio en blanco que las separa.",
                 "El eje de valores siempre debe comenzar de forma estricta en el cero absoluto."], 1))
        else:
            recomendaciones.append(RecomendacionGrafico(
                "barras_verticales", ETIQUETAS_GRAFICO["barras_verticales"],
                "Adecuado para pocas categorías con nombres cortos.",
                ["El eje numérico base debe comenzar obligatoriamente en cero para evitar distorsiones visuales.",
                 "Asegúrese de dejar un espacio moderado y equilibrado entre las barras."], 1))

            recomendaciones.append(RecomendacionGrafico(
                "barras_horizontales", ETIQUETAS_GRAFICO["barras_horizontales"],
                "Las barras horizontales siguen siendo una alternativa de comparación excelente y muy legible.",
                ["Permite un escaneo visual rápido en forma de Z.",
                 "Facilita la lectura de etiquetas incluso si se expanden en el futuro."], 2))

        # 7. Comparaciones multicategoría complejas
        if p.cantidad_series > 1 and p.cantidad_categorias > 0:
            recomendaciones.append(RecomendacionGrafico(
                "barras_verticales_apiladas", ETIQUETAS_GRAFICO["barras_verticales_apiladas"],
                "Permite ver totales de grupo junto con los componentes internos, aunque su legibilidad disminuye después de la primera serie base.",
                ["Utilícelo con cuidado, ya que los segmentos superiores carecen de una línea de referencia común.",
                 "No apile demasiados segmentos en una misma barra."], 2))

        return recomendaciones

    @staticmethod
    def renderizar_markdown(recs: List[RecomendacionGrafico],
                            advertencias_evitar: Optional[List[str]] = None) -> str:
        lineas = ["# 📊 Recomendaciones de Selección de Gráfico\n"]

        principales = [r for r in recs if r.prioridad == 1]
        alternativas = [r for r in recs if r.prioridad == 2]

        if principales:
            lineas.append("## ✅ Gráficos Recomendados (Prioridad Alta)")
            for r in principales:
                lineas.append(f"\n### {r.etiqueta}")
                lineas.append(f"**Motivo de selección**: {r.motivo}\n")
                if r.notas_diseno:
                    lineas.append("**Recomendaciones de diseño**:")
                    for n in r.notas_diseno:
                        lineas.append(f"- {n}")

        if alternativas:
            lineas.append("\n## 🔄 Alternativas Razonables")
            for r in alternativas:
                lineas.append(f"\n### {r.etiqueta}")
                lineas.append(f"**Motivo**: {r.motivo}\n")
                if r.notas_diseno:
                    lineas.append("**Recomendaciones de diseño**:")
                    for n in r.notas_diseno:
                        lineas.append(f"- {n}")

        if advertencias_evitar:
            lineas.append("\n## ⛔ Prácticas Desaconsejadas")
            for w in advertencias_evitar:
                lineas.append(f"- {w}")

        return "\n".join(lineas)
