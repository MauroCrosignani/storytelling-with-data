"""Analizador y Depurador de Ruido Visual (Clutter)

Identifica elementos innecesarios en la visualización basándose en los
principios Gestalt y en la reducción de carga cognitiva para el lector.
"""

from dataclasses import dataclass, field
from typing import List, Dict

from .config import ELEMENTOS_RUIDO, ETIQUETAS_RUIDO, PRINCIPIOS_GESTALT, ETIQUETAS_GESTALT


@dataclass
class ElementoRuido:
    """Representa un elemento individual que causa ruido visual"""
    tipo_elemento: str
    descripcion: str
    gravedad: int = 3                # Escala 1-5 (5 siendo el ruido más grave)
    recomendacion: str = ""

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if self.tipo_elemento not in ELEMENTOS_RUIDO:
            problemas.append(f"Elemento de ruido desconocido: {self.tipo_elemento}. Válidos: {ELEMENTOS_RUIDO}")
        if not 1 <= self.gravedad <= 5:
            problemas.append(f"La gravedad {self.gravedad} está fuera del rango permitido (1-5).")
        return problemas


@dataclass
class AplicacionGestalt:
    """Propuesta de aplicación de un principio Gestalt para corregir un diseño"""
    principio: str
    problema_actual: str
    sugerencia: str

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if self.principio not in PRINCIPIOS_GESTALT:
            problemas.append(f"Principio Gestalt desconocido: {self.principio}. Válidos: {PRINCIPIOS_GESTALT}")
        return problemas


@dataclass
class ReporteDepuracion:
    """Contiene el resultado completo del análisis de ruido visual"""
    elementos_ruido: List[ElementoRuido] = field(default_factory=list)
    aplicaciones_gestalt: List[AplicacionGestalt] = field(default_factory=list)
    problemas_alineacion: List[str] = field(default_factory=list)
    problemas_espacio_blanco: List[str] = field(default_factory=list)
    problemas_contraste: List[str] = field(default_factory=list)


class DepuradorRuido:
    """Diagnosticador de ruido visual e implementador de reglas de depuración"""

    PASOS_DEPURACION = [
        ("Eliminar bordes de gráficos", "borde_grafico", "Usa el principio de cierre Gestalt: el espacio en blanco actúa como frontera natural."),
        ("Atenuar o quitar cuadrículas", "lineas_cuadricula", "Las líneas de cuadrícula compiten con los datos. Si se conservan, deben ser muy tenues."),
        ("Remover marcadores excesivos", "marcadores_datos", "Los marcadores de datos en cada punto crean ruido. Deja solo los puntos clave."),
        ("Simplificar etiquetas de ejes", "ceros_finales", "Quita ceros decimales innecesarios, abrevia nombres de mes y evita textos en diagonal."),
        ("Etiquetar datos directamente", "leyenda_separada", "Evita que la vista salte constantemente de la leyenda al gráfico; etiqueta directamente las series."),
        ("Mantener consistencia visual", "etiquetas_redundantes", "Elimina duplicaciones de información (por ejemplo, etiquetas numéricas de datos junto a un eje numérico completo).")
    ]

    def __init__(self) -> None:
        self._reporte = ReporteDepuracion()

    def agregar_ruido(self, tipo_elemento: str, descripcion: str,
                      gravedad: int = 3, recomendacion: str = "") -> "DepuradorRuido":
        if not recomendacion:
            recomendacion = ETIQUETAS_RUIDO.get(tipo_elemento, "Se aconseja eliminar o atenuar.")
        item = ElementoRuido(tipo_elemento=tipo_elemento, descripcion=descripcion,
                             gravedad=gravedad, recomendacion=recomendacion)
        self._reporte.elementos_ruido.append(item)
        return self

    def agregar_gestalt(self, principio: str, problema_actual: str,
                        sugerencia: str) -> "DepuradorRuido":
        self._reporte.aplicaciones_gestalt.append(
            AplicacionGestalt(principio=principio, problema_actual=problema_actual,
                              sugerencia=sugerencia))
        return self

    def agregar_problema_alineacion(self, detalle: str) -> "DepuradorRuido":
        self._reporte.problemas_alineacion.append(detalle)
        return self

    def agregar_problema_espacio_blanco(self, detalle: str) -> "DepuradorRuido":
        self._reporte.problemas_espacio_blanco.append(detalle)
        return self

    def agregar_problema_contraste(self, detalle: str) -> "DepuradorRuido":
        self._reporte.problemas_contraste.append(detalle)
        return self

    def auto_detectar(self, tiene_bordes: bool = False, tiene_cuadriculas: bool = False,
                      tiene_marcadores: bool = False, tiene_ceros_finales: bool = False,
                      tiene_texto_diagonal: bool = False, tiene_leyenda_separada: bool = False,
                      tiene_efecto_3d: bool = False, tiene_sombreado_fondo: bool = False) -> "DepuradorRuido":
        """Identifica de forma automática elementos de ruido a partir de banderas booleanas"""
        verificaciones = [
            (tiene_bordes, "borde_grafico", "Se detectó borde limitante alrededor del gráfico", 2),
            (tiene_cuadriculas, "lineas_cuadricula", "Se detectaron líneas de cuadrícula explícitas", 2),
            (tiene_marcadores, "marcadores_datos", "Se detectaron marcadores individuales en cada punto", 2),
            (tiene_ceros_finales, "ceros_finales", "Se detectaron ceros decimales repetitivos en los ejes (ej. 10.00)", 3),
            (tiene_texto_diagonal, "texto_diagonal", "Se detectaron etiquetas rotadas en diagonal", 4),
            (tiene_leyenda_separada, "leyenda_separada", "Se detectó leyenda alejada del conjunto de datos principal", 3),
            (tiene_efecto_3d, "efectos_3d", "Se detectaron efectos visuales 3D o de profundidad", 5),
            (tiene_sombreado_fondo, "sombreado_fondo", "Se detectó un fondo de color u oscurecido", 2),
        ]
        for condicion, etipo, desc, gravedad in verificaciones:
            if condicion:
                self.agregar_ruido(etipo, desc, gravedad)
        return self

    def construir(self) -> ReporteDepuracion:
        return self._reporte

    def calcular_carga_cognitiva_total(self) -> int:
        """Suma de gravedad de todos los problemas para estimar la carga cognitiva"""
        return sum(item.gravedad for item in self._reporte.elementos_ruido)

    def estimar_reduccion_carga(self) -> int:
        """Porcentaje estimado de reducción de carga mental para el lector al aplicar la limpieza"""
        total = self.calcular_carga_cognitiva_total()
        if total == 0:
            return 0
        return min(int(total / (total + 5) * 100), 90)

    @staticmethod
    def renderizar_markdown(reporte: ReporteDepuracion) -> str:
        lineas = ["# 🧹 Reporte de Depuración de Ruido Visual\n"]

        carga_total = sum(item.gravedad for item in reporte.elementos_ruido)
        lineas.append("## Resumen del Diagnóstico")
        lineas.append(f"- **Elementos redundantes detectados**: {len(reporte.elementos_ruido)}")
        lineas.append(f"- **Carga cognitiva de partida (Gravedad total)**: {carga_total}")
        lineas.append("")

        if reporte.elementos_ruido:
            lineas.append("## Inventario de Ruido Visual\n")
            lineas.append("| Elemento | Descripción | Gravedad | Recomendación SWD |")
            lineas.append("|----------|-------------|----------|-------------------|")
            for item in sorted(reporte.elementos_ruido, key=lambda x: -x.gravedad):
                barra = "█" * item.gravedad + "░" * (5 - item.gravedad)
                tipo_formateado = item.tipo_elemento.replace("_", " ").capitalize()
                lineas.append(f"| {tipo_formateado} | {item.descripcion} | {barra} | {item.recomendacion} |")

        lineas.append("\n## Los Seis Pasos de la Depuración SWD\n")
        for i, (paso, etype, detalle) in enumerate(DepuradorRuido.PASOS_DEPURACION, 1):
            detectado = any(c.tipo_elemento == etype for c in reporte.elementos_ruido)
            icono = "🔴" if detectado else "🟢"
            lineas.append(f"{i}. {icono} **{paso}** — {detalle}")

        if reporte.aplicaciones_gestalt:
            lineas.append("\n## Aplicación de Principios Gestalt\n")
            for g in reporte.aplicaciones_gestalt:
                titulo_principio = ETIQUETAS_GESTALT.get(g.principio, g.principle if hasattr(g, 'principle') else g.principio)
                lineas.append(f"### {titulo_principio}")
                lineas.append(f"- **Defecto observado**: {g.problema_actual}")
                lineas.append(f"- **Propuesta Gestalt**: {g.sugerencia}\n")

        if reporte.problemas_alineacion:
            lineas.append("## Alineación Inconsistente\n")
            for a in reporte.problemas_alineacion:
                lineas.append(f"- ❌ {a}")

        if reporte.problemas_espacio_blanco:
            lineas.append("\n## Uso del Espacio en Blanco\n")
            for w in reporte.problemas_espacio_blanco:
                lineas.append(f"- ❌ {w}")

        if reporte.problemas_contraste:
            lineas.append("\n## Problemas de Contraste y Enfoque\n")
            for c in reporte.problemas_contraste:
                lineas.append(f"- ❌ {c}")

        return "\n".join(lineas)
