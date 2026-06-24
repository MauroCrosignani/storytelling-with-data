"""Motor de Rediseño y Transformación de Gráficos (Makeover)

Guía el proceso de transformación paso a paso desde un gráfico original deficiente
hasta una historia con datos efectiva utilizando el método de las seis lecciones SWD.
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class PasoRediseño:
    """Representa un paso individual en la transformación del gráfico"""
    orden: int
    leccion: str                   # Nombre corto de la lección SWD correspondiente
    accion: str
    antes_desc: str = ""
    despues_desc: str = ""
    fundamento: str = ""


@dataclass
class EspecificacionDiseno:
    """Normas de diseño del gráfico final rediseñado"""
    tipo_grafico: str = ""
    titulo: str = ""
    tipo_titulo: str = "accion"     # accion / descriptivo
    color_base: str = "Gris"
    color_enfasis: str = "Azul"
    alineacion: str = "Alineado a la izquierda (arriba)"
    fuente: str = "Sans-serif (ej. Arial, Helvetica)"
    etiquetas_datos: str = "Etiquetado directo sobre las series"
    tratamiento_ejes: str = "Gris claro, sin marcas de división innecesarias"
    anotaciones: List[str] = field(default_factory=list)
    fuente_datos: str = ""


@dataclass
class DiapositivaNarrativa:
    """Representa una diapositiva en una secuencia de revelación progresiva"""
    orden: int
    titular: str
    enfasis: str = ""
    voz_en_off: str = ""


@dataclass
class PlanRediseño:
    """Plan integral de rediseño de un gráfico"""
    titulo: str = ""
    problemas_originales: List[str] = field(default_factory=list)
    pasos: List[PasoRediseño] = field(default_factory=list)
    especificacion_diseno: EspecificacionDiseno = field(default_factory=EspecificacionDiseno)
    diapositivas_narrativas: List[DiapositivaNarrativa] = field(default_factory=list)


class RedisenadorGrafico:
    """Motor de rediseño — Implementación paso a paso de las seis lecciones SWD"""

    SEIS_LECCIONES = [
        ("contexto", "Comprender el contexto", "Identificar a la audiencia, el propósito y destilar la Idea Fuerza."),
        ("visual", "Elegir la visualización adecuada", "Seleccionar el tipo de gráfico idóneo según la naturaleza de los datos."),
        ("ruido", "Eliminar el ruido visual", "Remover bordes, cuadrículas de fondo, marcas divisorias y decimales redundantes."),
        ("atencion", "Dirigir la atención", "Guiar la mirada del lector usando color de forma selectiva y variando tamaños de fuente."),
        ("diseno", "Pensar como un diseñador", "Optimizar la alineación a la izquierda, usar títulos declarativos e incluir notas directas."),
        ("historia", "Contar una historia", "Estructurar un arco de tres actos y usar la revelación progresiva en la presentación."),
    ]

    def __init__(self, titulo: str = "") -> None:
        self._plan = PlanRediseño(titulo=titulo)

    def agregar_problema(self, problema: str) -> "RedisenadorGrafico":
        self._plan.problemas_originales.append(problema)
        return self

    def agregar_paso(self, leccion: str, accion: str,
                     antes: str = "", despues: str = "",
                     fundamento: str = "") -> "RedisenadorGrafico":
        orden = len(self._plan.pasos) + 1
        self._plan.pasos.append(PasoRediseño(
            orden=orden, leccion=leccion, accion=accion,
            antes_desc=antes, despues_desc=despues, fundamento=fundamento))
        return self

    def establecer_especificacion_diseno(self, tipo_grafico: str = "", titulo: str = "",
                                         color_enfasis: str = "Azul",
                                         anotaciones: Optional[List[str]] = None,
                                         fuente_datos: str = "") -> "RedisenadorGrafico":
        self._plan.especificacion_diseno = EspecificacionDiseno(
            tipo_grafico=tipo_grafico, titulo=titulo,
            color_enfasis=color_enfasis,
            anotaciones=anotaciones or [],
            fuente_datos=fuente_datos)
        return self

    def agregar_diapositiva_narrativa(self, titular: str, enfasis: str = "",
                                      voz_en_off: str = "") -> "RedisenadorGrafico":
        orden = len(self._plan.diapositivas_narrativas) + 1
        self._plan.diapositivas_narrativas.append(DiapositivaNarrativa(
            orden=orden, titular=titular,
            enfasis=enfasis, voz_en_off=voz_en_off))
        return self

    def auto_pasos_desde_problemas(self) -> "RedisenadorGrafico":
        """Genera de forma automática los pasos del plan de rediseño a partir de los problemas ingresados"""
        mapa_problemas = {
            "circular": ("visual", "Sustituir el gráfico circular por un gráfico de barras horizontales", "El ojo humano no compara áreas ni ángulos con facilidad."),
            "tarta": ("visual", "Sustituir el gráfico de tarta por barras horizontales", "El ojo humano no compara áreas ni ángulos con facilidad."),
            "pie": ("visual", "Sustituir el gráfico circular por barras horizontales", "El ojo humano no compara áreas de sectores circulares con facilidad."),
            "dona": ("visual", "Reemplazar el gráfico de dona por barras horizontales", "Las donas dificultan aún más la lectura al tener que evaluar longitudes de arco."),
            "3d": ("visual", "Eliminar efectos 3D y cambiar a versión 2D plana", "Los efectos tridimensionales distorsionan la escala visual de los datos y confunden."),
            "doble eje": ("visual", "Separar en dos gráficos individuales con eje común o etiquetar puntos", "El doble eje y dificulta asociar cada serie a su eje numérico correspondiente."),
            "sin titulo": ("diseno", "Añadir un título declarativo de acción", "El título de acción informa inmediatamente a la audiencia sobre la conclusión clave."),
            "sin etiquetas de eje": ("diseno", "Agregar etiquetas explícitas a los ejes", "Los ejes deben tener nombres descriptivos claros para entender las escalas de medida."),
            "leyenda": ("ruido", "Etiquetar directamente las series de datos y quitar la leyenda alejada", "Se elimina el esfuerzo mental de saltar constantemente de la leyenda al gráfico."),
            "cuadricula": ("ruido", "Atenuar o remover las líneas de cuadrícula del fondo", "Las cuadrículas gruesas compiten con el elemento principal de datos."),
            "borde": ("ruido", "Quitar los bordes limitantes exteriores del gráfico", "Uso del principio de cierre Gestalt: el espacio blanco ya delimita el gráfico."),
            "muchos colores": ("atencion", "Reducir la paleta a tonos de gris y un único color de énfasis", "El exceso de colores satura y destruye el efecto preatentivo de focalización."),
            "colorines": ("atencion", "Reducir la paleta a tonos de gris y un único color de énfasis", "Demasiados colores compiten entre sí y anulan la atención selectiva."),
            "texto inclinado": ("ruido", "Abreviar etiquetas del eje X para ponerlas horizontales", "Los textos inclinados o en diagonal reducen un 52% la velocidad de lectura."),
            "diagonal": ("ruido", "Abreviar etiquetas del eje X para ponerlas horizontales", "Los textos inclinados o en diagonal reducen un 52% la velocidad de lectura."),
            "centrado": ("diseno", "Alinear todos los bloques de texto a la izquierda", "La alineación izquierda crea líneas virtuales limpias para un escaneo visual ordenado."),
            "sin llamado a la accion": ("historia", "Definir e incluir un llamado a la acción final nítido", "La narrativa debe cerrarse siempre indicando qué acción o decisión se espera."),
        }
        for problema in self._plan.problemas_originales:
            problema_lc = problema.lower()
            for clave_busqueda, (leccion, accion, fundamento) in mapa_problemas.items():
                if clave_busqueda in problema_lc:
                    self.agregar_paso(leccion, accion, antes=problema, fundamento=fundamento)
                    break
        return self

    def construir(self) -> PlanRediseño:
        return self._plan

    @staticmethod
    def renderizar_markdown(plan: PlanRediseño) -> str:
        lineas = [f"# ✨ Plan de Rediseño y Transformación: {plan.titulo}\n"]

        if plan.problemas_originales:
            lineas.append("## Diagnóstico de Defectos Originales\n")
            for i, issue in enumerate(plan.problemas_originales, 1):
                lineas.append(f"{i}. ❌ {issue}")

        if plan.pasos:
            lineas.append("\n## Pasos de Transformación (Método SWD)\n")
            for paso in plan.pasos:
                etiqueta_leccion = next(
                    (etiqueta for clave, etiqueta, _ in RedisenadorGrafico.SEIS_LECCIONES
                     if clave == paso.leccion), paso.leccion)
                lineas.append(f"### Paso {paso.orden}: [{etiqueta_leccion}] {paso.accion}")
                if paso.antes_desc:
                    lineas.append(f"- **Estado anterior**: {paso.antes_desc}")
                if paso.despues_desc:
                    lineas.append(f"- **Mejora aplicada**: {paso.despues_desc}")
                if paso.fundamento:
                    lineas.append(f"- **Fundamento teórico**: {paso.fundamento}")
                lineas.append("")

        ds = plan.especificacion_diseno
        if ds.tipo_grafico or ds.titulo:
            lineas.append("## Especificaciones del Diseño Propuesto\n")
            lineas.append("| Dimensión de Diseño | Especificación Recomenda |")
            lineas.append("|---------------------|--------------------------|")
            if ds.tipo_grafico:
                lineas.append(f"| Tipo de Gráfico | {ds.tipo_grafico} |")
            if ds.titulo:
                lineas.append(f"| Título del Gráfico | {ds.titulo} (Título de {ds.tipo_titulo.capitalize()}) |")
            lineas.append(f"| Paleta Base | {ds.color_base} |")
            lineas.append(f"| Color de Contraste | {ds.color_enfasis} |")
            lineas.append(f"| Alineación Textos | {ds.alineacion} |")
            lineas.append(f"| Familia Tipográfica | {ds.fuente} |")
            lineas.append(f"| Rotulado de Datos | {ds.etiquetas_datos} |")
            lineas.append(f"| Tratamiento de Ejes | {ds.tratamiento_ejes} |")
            if ds.fuente_datos:
                lineas.append(f"| Origen de Datos | {ds.fuente_datos} |")
            if ds.anotaciones:
                lineas.append("\n**Notas y Anotaciones en el Gráfico**:")
                for a in ds.anotaciones:
                    lineas.append(f"- {a}")

        if plan.diapositivas_narrativas:
            lineas.append("\n## Secuencia Narrativa de Diapositivas (Revelación Progresiva)\n")
            for slide in plan.diapositivas_narrativas:
                lineas.append(f"### Diapositiva {slide.orden}")
                lineas.append(f"**Titular**: {slide.titular}")
                if slide.enfasis:
                    lineas.append(f"**Elemento a destacar**: {slide.enfasis}")
                if slide.voz_en_off:
                    lineas.append(f"**Guion de voz en off (Discurso)**: {slide.voz_en_off}")
                lineas.append("")

        return "\n".join(lineas)
