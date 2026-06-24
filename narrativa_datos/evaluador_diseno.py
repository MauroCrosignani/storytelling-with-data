"""Evaluador de Diseño Visual

Evalúa la calidad visual de un gráfico a través de tres dimensiones clave:
asequibilidad (percepción de funciones), accesibilidad y estética.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class VerificacionAsequibilidad:
    """Item de verificación de asequibilidad (affordance)"""
    nombre: str
    aprobada: bool = False
    nota: str = ""


@dataclass
class VerificacionAccesibilidad:
    """Item de verificación de accesibilidad"""
    nombre: str
    aprobada: bool = False
    nota: str = ""


@dataclass
class VerificacionEstetica:
    """Item de verificación de estética y armonía"""
    nombre: str
    aprobada: bool = False
    nota: str = ""


@dataclass
class EvaluacionDiseno:
    """Resultado estructurado de la evaluación del diseño"""
    asequibilidades: List[VerificacionAsequibilidad] = field(default_factory=list)
    accesibilidades: List[VerificacionAccesibilidad] = field(default_factory=list)
    esteticas: List[VerificacionEstetica] = field(default_factory=list)
    mejoras: List[str] = field(default_factory=list)

    @property
    def total_verificaciones(self) -> int:
        return len(self.asequibilidades) + len(self.accesibilidades) + len(self.esteticas)

    @property
    def verificaciones_aprobadas(self) -> int:
        return (sum(1 for c in self.asequibilidades if c.aprobada)
                + sum(1 for c in self.accesibilidades if c.aprobada)
                + sum(1 for c in self.esteticas if c.aprobada))

    @property
    def puntaje_porcentaje(self) -> int:
        return int(self.verificaciones_aprobadas / self.total_verificaciones * 100) if self.total_verificaciones else 0


class EvaluadorDiseno:
    """Evaluador cuantitativo y cualitativo de la calidad de diseño"""

    ITEMS_ASEQUIBILIDAD = [
        ("resalta_importante", "Destacar lo importante: El contenido crítico resalta visualmente (máximo 10% del total)."),
        ("elimina_distracciones", "Eliminar distracciones: Se han removido todos los elementos que no aportan datos."),
        ("jerarquia_visual", "Jerarquía visual: Existe una clara jerarquía de lectura establecida."),
        ("datos_sobresalen", "Datos en primer plano: El elemento de datos destaca por encima de los ejes y bordes."),
        ("uso_preatentivo", "Uso preatentivo estratégico: Se aplican atributos preatentivos para guiar al lector."),
    ]

    ITEMS_ACCESIBILIDAD = [
        ("tiene_titulo_grafico", "Título de gráfico claro: El gráfico posee un título legible."),
        ("tiene_titulos_eje", "Títulos en los ejes: Cada eje posee una etiqueta descriptiva clara."),
        ("titulo_accion", "Título declarativo: El título describe la conclusión o acción en lugar de ser meramente descriptivo."),
        ("fuente_legible", "Legibilidad de fuente: La tipografía y el tamaño de letra permiten leer sin esfuerzo."),
        ("lenguaje_sencillo", "Lenguaje sencillo: Se evitan tecnicismos innecesarios o abreviaturas confusas."),
        ("anotaciones_presentes", "Anotaciones en puntos clave: Existen notas explicativas directas sobre puntos sobresalientes."),
        ("sin_sobrecomplicacion", "Diseño accesible: Se ha evitado añadir demasiadas series o niveles de complejidad."),
    ]

    ITEMS_ESTETICA = [
        ("color_inteligente", "Color intencional: Uso de color moderado y estratégico (color para énfasis, gris para fondo)."),
        ("alineacion_limpia", "Alineación limpia: Los textos y ejes se alinean formando líneas virtuales rectas."),
        ("espacio_blanco_adecuado", "Preservación del espacio libre: El espacio en blanco permite que el diseño respire."),
        ("evita_texto_centrado", "Sin bloques de texto centrados: El texto explicativo largo se alinea a la izquierda."),
        ("consistencia_tamaño", "Consistencia de escala de texto: Los tamaños de letra son homogéneos excepto para énfasis."),
        ("sensacion_profesional", "Estilo profesional: La combinación de colores y trazos transmite orden y seriedad."),
    ]

    def __init__(self) -> None:
        self._evaluacion = EvaluacionDiseno()

    def verificar_asequibilidad(self, clave_item: str, aprobada: bool,
                                nota: str = "") -> "EvaluadorDiseno":
        nombre = next((desc for k, desc in self.ITEMS_ASEQUIBILIDAD if k == clave_item), clave_item)
        self._evaluacion.asequibilidades.append(VerificacionAsequibilidad(nombre=nombre, aprobada=aprobada, nota=nota))
        return self

    def verificar_accesibilidad(self, clave_item: str, aprobada: bool,
                                nota: str = "") -> "EvaluadorDiseno":
        name = next((desc for k, desc in self.ITEMS_ACCESIBILIDAD if k == clave_item), clave_item)
        self._evaluacion.accesibilidades.append(VerificacionAccesibilidad(nombre=name, aprobada=aprobada, nota=nota))
        return self

    def verificar_estetica(self, clave_item: str, aprobada: bool,
                           nota: str = "") -> "EvaluadorDiseno":
        name = next((desc for k, desc in self.ITEMS_ESTETICA if k == clave_item), clave_item)
        self._evaluacion.esteticas.append(VerificacionEstetica(nombre=name, aprobada=aprobada, nota=nota))
        return self

    def auto_evaluar(self, tiene_titulo: bool = False, tiene_titulos_eje: bool = False,
                     tiene_titulo_accion: bool = False, tiene_anotaciones: bool = False,
                     color_estrategico: bool = False, alineacion_limpia: bool = False,
                     espacio_blanco_ok: bool = False, jerarquia_clara: bool = False,
                     resaltado_limitado: bool = False, distracciones_eliminadas: bool = False,
                     fuente_legible: bool = True, lenguaje_sencillo: bool = True) -> "EvaluadorDiseno":
        """Realiza una evaluación automática a partir de banderas de diseño comunes"""
        self.verificar_asequibilidad("resalta_importante", resaltado_limitado)
        self.verificar_asequibilidad("elimina_distracciones", distracciones_eliminadas)
        self.verificar_asequibilidad("jerarquia_visual", jerarquia_clara)
        self.verificar_accesibilidad("tiene_titulo_grafico", tiene_titulo)
        self.verificar_accesibilidad("tiene_titulos_eje", tiene_titulos_eje)
        self.verificar_accesibilidad("titulo_accion", tiene_titulo_accion)
        self.verificar_accesibilidad("fuente_legible", fuente_legible)
        self.verificar_accesibilidad("lenguaje_sencillo", lenguaje_sencillo)
        self.verificar_accesibilidad("anotaciones_presentes", tiene_anotaciones)
        self.verificar_estetica("color_inteligente", color_estrategico)
        self.verificar_estetica("alineacion_limpia", alineacion_limpia)
        self.verificar_estetica("espacio_blanco_adecuado", espacio_blanco_ok)
        return self

    def agregar_mejora(self, propuesta: str) -> "EvaluadorDiseno":
        self._evaluacion.mejoras.append(propuesta)
        return self

    def auto_mejoras(self) -> "EvaluadorDiseno":
        """Genera sugerencias de mejora automatizadas para los ítems fallidos"""
        for c in self._evaluacion.asequibilidades:
            if not c.aprobada:
                self._evaluacion.mejoras.append(f"[Asequibilidad] Falló: {c.nombre}")
        for c in self._evaluacion.accesibilidades:
            if not c.aprobada:
                self._evaluacion.mejoras.append(f"[Accesibilidad] Falló: {c.nombre}")
        for c in self._evaluacion.esteticas:
            if not c.aprobada:
                self._evaluacion.mejoras.append(f"[Estética] Falló: {c.nombre}")
        return self

    def construir(self) -> EvaluacionDiseno:
        return self._evaluacion

    @staticmethod
    def _renderizar_verificaciones(verificaciones: list, titulo: str) -> str:
        lineas = [f"### {titulo}\n"]
        for c in verificaciones:
            icono = "✅" if c.aprobada else "❌"
            linea = f"- {icono} {c.nombre}"
            if c.nota:
                linea += f" — {c.nota}"
            lineas.append(linea)
        aprobadas = sum(1 for c in verificaciones if c.aprobada)
        lineas.append(f"\nAprobadas: {aprobadas}/{len(verificaciones)}")
        return "\n".join(lineas)

    @staticmethod
    def renderizar_markdown(evaluacion: EvaluacionDiseno) -> str:
        lineas = ["# 🎨 Reporte de Evaluación de Diseño Visual\n"]
        porcentaje = evaluacion.puntaje_porcentaje
        etiqueta_calidad = (
            "🟢 Excelente" if porcentaje >= 90 else
            "🟡 Bueno" if porcentaje >= 70 else
            "🟠 Requiere Mejoras" if porcentaje >= 50 else
            "🔴 Necesita Rediseño Completo"
        )
        lineas.append(f"**Resultado Global: {evaluacion.verificaciones_aprobadas}/{evaluacion.total_verificaciones} ({porcentaje}%) — {etiqueta_calidad}**\n")

        if evaluacion.asequibilidades:
            lineas.append(EvaluadorDiseno._renderizar_verificaciones(evaluacion.asequibilidades, "Asequibilidad y Enfoque"))
        if evaluacion.accesibilidades:
            lineas.append("\n" + EvaluadorDiseno._renderizar_verificaciones(evaluacion.accesibilidades, "Accesibilidad"))
        if evaluacion.esteticas:
            lineas.append("\n" + EvaluadorDiseno._renderizar_verificaciones(evaluacion.esteticas, "Estética y Formato"))

        if evaluacion.mejoras:
            lineas.append("\n## Recomendaciones de Mejora\n")
            for i, imp in enumerate(evaluacion.mejoras, 1):
                lineas.append(f"{i}. {imp}")

        return "\n".join(lineas)
