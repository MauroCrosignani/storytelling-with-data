"""Planificador de Atención Visual

Permite definir puntos de enfoque, planificar la jerarquía visual de los
elementos y aplicar atributos preatentivos y estrategias de color SWD.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict

from .config import (
    ATRIBUTOS_PREATENTIVOS, ATRIBUTOS_CUANTITATIVOS,
    ATRIBUTOS_CATEGORICOS, ESTRATEGIAS_COLOR, ETIQUETAS_COLOR,
)


@dataclass
class PuntoEnfoque:
    """Representa un punto de enfoque visual en el gráfico"""
    elemento: str
    importancia: int = 3             # Nivel de importancia del elemento (1 a 5)
    enfasis_actual: int = 1          # Grado de énfasis actual en el gráfico (1 a 5)
    enfasis_deseado: int = 5         # Grado de énfasis deseado en el gráfico (1 a 5)
    atributos_usados: List[str] = field(default_factory=list)

    @property
    def brecha_enfasis(self) -> int:
        return self.enfasis_deseado - self.enfasis_actual


@dataclass
class PlanColor:
    """Especificación de la paleta de colores para la narrativa"""
    estrategia: str = "gris_mas_uno"
    color_base: str = "Gris (#808080)"
    color_enfasis: str = "Azul (#4472C4)"
    color_negativo: str = "Naranja (#ED7D31)"
    notas: List[str] = field(default_factory=list)
    seguro_daltonicos: bool = True


@dataclass
class NivelJerarquiaVisual:
    """Nivel en la jerarquía de lectura del gráfico"""
    nivel: int
    elementos: List[str] = field(default_factory=list)
    tratamiento: str = ""


@dataclass
class PlanAtencion:
    """Reporte estructurado del plan de atención visual"""
    puntos_enfoque: List[PuntoEnfoque] = field(default_factory=list)
    plan_color: PlanColor = field(default_factory=PlanColor)
    jerarquia: List[NivelJerarquiaVisual] = field(default_factory=list)
    sugerencias_preatentivas: List[str] = field(default_factory=list)


class AnalizadorAtencion:
    """Planificador y optimizador de la atención visual"""

    def __init__(self) -> None:
        self._plan = PlanAtencion()

    def agregar_enfoque(self, elemento: str, importancia: int = 3,
                        enfasis_actual: int = 1,
                        enfasis_deseado: int = 5) -> "AnalizadorAtencion":
        self._plan.puntos_enfoque.append(PuntoEnfoque(
            elemento=elemento, importancia=importancia,
            enfasis_actual=enfasis_actual,
            enfasis_deseado=enfasis_deseado))
        return self

    def establecer_plan_color(self, estrategia: str = "gris_mas_uno",
                              enfasis: str = "Azul (#4472C4)",
                              negativo: str = "Naranja (#ED7D31)",
                              seguro_daltonicos: bool = True) -> "AnalizadorAtencion":
        self._plan.plan_color = PlanColor(
            estrategia=estrategia, color_enfasis=enfasis,
            color_negativo=negativo, seguro_daltonicos=seguro_daltonicos)
        return self

    def agregar_nivel_jerarquia(self, nivel: int, elementos: List[str],
                                tratamiento: str) -> "AnalizadorAtencion":
        self._plan.jerarquia.append(NivelJerarquiaVisual(
            nivel=nivel, elementos=elementos, tratamiento=tratamiento))
        return self

    def auto_sugerir(self) -> "AnalizadorAtencion":
        """Genera sugerencias automáticas de atributos preatentivos según las brechas de énfasis"""
        sugerencias: List[str] = []
        brecha_alta = [f for f in self._plan.puntos_enfoque if f.brecha_enfasis >= 3]
        brecha_media = [f for f in self._plan.puntos_enfoque if 1 <= f.brecha_enfasis < 3]

        if brecha_alta:
            sugerencias.append("Para elementos con brechas altas de énfasis, superponga atributos preatentivos: color + tamaño + texto en negrita.")
            sugerencias.append("Mande primero todos los elementos secundarios al fondo pintándolos de gris claro, y luego resalte el foco con color.")
        if brecha_media:
            sugerencias.append("Para elementos de importancia media, un único atributo preatentivo (negrita o color tenue) suele ser suficiente.")

        cantidad_focos = len(self._plan.puntos_enfoque)
        if cantidad_focos > 3:
            sugerencias.append(f"⚠️ Actualmente tiene {cantidad_focos} focos definidos. Redúzcalos a 1-3 elementos para no sobrecargar la atención.")
            sugerencias.append("Los atributos preatentivos funcionan mejor bajo escasez: cuanto más cosas intente resaltar, menos resaltará cada una.")

        sugerencias.append("Aplique la prueba de 'dónde se dirigen los ojos primero' cerrando y abriendo los ojos rápidamente frente al gráfico.")
        sugerencias.append("Recuerde: un cambio de color debe significar un cambio de información, no cambie colores solo por estética.")

        self._plan.sugerencias_preatentivas = sugerencias
        return self

    def diagnosticar_mirada(self) -> List[str]:
        """Diagnóstico de coherencia visual basado en la prioridad y el énfasis real"""
        diagnosticos: List[str] = []
        ordenados_por_enfasis = sorted(self._plan.puntos_enfoque,
                                       key=lambda x: -x.enfasis_actual)

        if ordenados_por_enfasis:
            mas_destacado = ordenados_por_enfasis[0]
            mas_importante = max(self._plan.puntos_enfoque, key=lambda x: x.importancia)
            if mas_destacado.elemento != mas_importante.elemento:
                diagnosticos.append(
                    f"⚠️ El elemento más destacado actualmente es '{mas_destacado.elemento}', "
                    f"pero el más importante es '{mas_importante.elemento}'. Ajuste los pesos visuales.")
            else:
                diagnosticos.append(f"✅ El elemento más destacado coincide con el más importante: '{mas_destacado.elemento}'.")

        elementos_muy_enfáticos = sum(1 for f in self._plan.puntos_enfoque if f.enfasis_actual >= 4)
        if elementos_muy_enfáticos > 2:
            diagnosticos.append(
                f"⚠️ Hay {elementos_muy_enfáticos} elementos con énfasis alto. "
                "Resaltar demasiadas cosas anula el efecto de enfoque (efecto rebaño).")

        return diagnosticos

    def construir(self) -> PlanAtencion:
        if not self._plan.sugerencias_preatentivas:
            self.auto_sugerir()
        return self._plan

    @staticmethod
    def renderizar_markdown(plan: PlanAtencion) -> str:
        lineas = ["# 🎯 Planificación de Atención Visual\n"]

        if plan.puntos_enfoque:
            lineas.append("## Análisis de Focos de Atención\n")
            lineas.append("| Elemento | Importancia | Énfasis Actual | Énfasis Deseado | Brecha |")
            lineas.append("|----------|-------------|----------------|-----------------|--------|")
            for f in sorted(plan.puntos_enfoque, key=lambda x: -x.importancia):
                imp = "█" * f.importancia + "░" * (5 - f.importancia)
                cur = "█" * f.enfasis_actual + "░" * (5 - f.enfasis_actual)
                des = "█" * f.enfasis_deseado + "░" * (5 - f.enfasis_deseado)
                brecha = f.brecha_enfasis
                icono = "🔴" if brecha >= 3 else "🟡" if brecha >= 1 else "🟢"
                lineas.append(f"| {f.elemento} | {imp} | {cur} | {des} | {icono} {brecha} |")

        cp = plan.plan_color
        lineas.append("\n## Estrategia de Color\n")
        lineas.append(f"- **Estrategia**: {ETIQUETAS_COLOR.get(cp.estrategia, cp.estrategia)}")
        lineas.append(f"- **Color Base (Fondo)**: {cp.color_base}")
        lineas.append(f"- **Color de Énfasis**: {cp.color_enfasis}")
        lineas.append(f"- **Color para Negativos**: {cp.color_negativo}")
        lineas.append(f"- **Optimizado para Daltonismo**: {'✅ Sí' if cp.seguro_daltonicos else '❌ No'}")
        for n in cp.notes if hasattr(cp, 'notes') else []:
            lineas.append(f"- {n}")

        if plan.jerarquia:
            lineas.append("\n## Diseño de Jerarquía Visual de Lectura\n")
            for h in sorted(plan.jerarquia, key=lambda x: x.level if hasattr(x, 'level') else x.nivel):
                elementos = ", ".join(h.elementos)
                lineas.append(f"**Nivel {h.nivel}**: {elementos}")
                lineas.append(f"  Tratamiento visual: {h.tratamiento}\n")

        if plan.sugerencias_preatentivas:
            lineas.append("## Consejos sobre Atributos Preatentivos\n")
            for s in plan.sugerencias_preatentivas:
                lineas.append(f"- {s}")

        return "\n".join(lineas)
