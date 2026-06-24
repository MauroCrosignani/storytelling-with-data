"""Motor de Diagnóstico Completo

Proporciona un diagnóstico integral de 5 dimensiones con escala cuantitativa de 0 a 100 puntos
y sugerencias de mejora automatizadas.
"""

from dataclasses import dataclass, field
from typing import List, Dict

from .config import DIMENSIONES_DIAGNOSTICO, ETIQUETAS_DIAGNOSTICO


@dataclass
class PuntajeDimension:
    """Puntuación en una dimensión específica"""
    dimension: str
    elementos: List[tuple] = field(default_factory=list)  # (nombre, puntaje, maximo, nota)

    @property
    def puntaje(self) -> int:
        return sum(s for _, s, _, _ in self.elementos)

    @property
    def puntaje_maximo(self) -> int:
        return sum(m for _, _, m, _ in self.elementos)

    @property
    def etiqueta(self) -> str:
        return ETIQUETAS_DIAGNOSTICO.get(self.dimension, self.dimension)


@dataclass
class ResultadoDiagnostico:
    """Consolidado de resultados del diagnóstico"""
    titulo: str = ""
    dimensiones: Dict[str, PuntajeDimension] = field(default_factory=dict)
    mejoras_prioritarias: List[str] = field(default_factory=list)
    sugerencias_rediseño: List[str] = field(default_factory=list)

    @property
    def puntaje_total(self) -> int:
        return sum(d.puntaje for d in self.dimensiones.values())

    @property
    def maximo_total(self) -> int:
        return sum(d.puntaje_maximo for d in self.dimensiones.values())

    @property
    def insignia(self) -> str:
        s = self.puntaje_total
        t = self.maximo_total
        pct = s / t * 100 if t else 0
        if pct >= 90: return f"🟢 {s}/{t} Excelente (Listo para reportar)"
        if pct >= 70: return f"🟡 {s}/{t} Aceptable (Se sugiere pulir)"
        if pct >= 50: return f"🟠 {s}/{t} Requiere Mejoras"
        return f"🔴 {s}/{t} Debe Rediseñarse"


# ── Items de Puntuación por Dimensión ──
ITEMS_CONTEXTO = [
    ("audiencia_clara", "¿La audiencia objetivo está definida y los mensajes están dirigidos a ella?"),
    ("accion_clara", "¿El llamado a la acción es preciso y fácil de comprender?"),
    ("idea_fuerza_visible", "¿La Idea Fuerza se reconoce fácilmente en los primeros 5 segundos?"),
    ("datos_sostienen_tesis", "¿Los datos demuestran y sostienen la historia en lugar de solo mostrarse?"),
]

ITEMS_VISUAL = [
    ("tipo_grafico_correcto", "¿El tipo de gráfico es adecuado para el perfil de los datos y el propósito?"),
    ("evita_graficos_complejos", "¿Se han evitado gráficos circulares, 3D o con doble eje Y?"),
    ("linea_base_cero", "¿Las barras tienen su línea base fija exactamente en cero?"),
    ("orden_logico", "¿Las categorías están ordenadas de forma lógica y estructurada?"),
]

ITEMS_RUIDO = [
    ("sin_elementos_redundantes", "¿Se han eliminado bordes, cuadrículas y etiquetas redundantes?"),
    ("sin_texto_diagonal", "¿Se han evitado los textos en inclinaciones diagonales y alineaciones centradas?"),
    ("espacio_libre_adecuado", "¿El espacio en blanco rodea y equilibra los bloques del gráfico?"),
    ("leyendas_integradas", "¿Se evitan leyendas separadas etiquetando directamente los datos?"),
]

ITEMS_ATENCION = [
    ("uso_resaltado_preatentivo", "¿Se usan atributos preatentivos de forma intencional para captar la mirada?"),
    ("escasez_color", "¿El uso del color es sobrio y con fines de contraste (gris de fondo)?"),
    ("jerarquia_visual_clara", "¿Se reconoce la jerarquía de lectura del gráfico a primera vista?"),
    ("prueba_ojos_cerrados", "¿La prueba de enfoque ('dónde mira primero') coincide con el dato clave?"),
]

ITEMS_DISENO = [
    ("texto_descriptivo_adecuado", "¿El gráfico incluye título de acción, títulos de eje y fuentes legibles?"),
    ("alineacion_profesional", "¿Las tipografías y ejes visuales se alinean correctamente?"),
    ("estructura_tres_actos", "¿La presentación de los datos tiene una estructura de Inicio, Nudo y Desenlace?"),
    ("titulo_de_accion", "¿El título principal concluye en lugar de solo describir el tema del gráfico?"),
]

TODOS_ITEMS_DIMENSION = {
    "contexto": ITEMS_CONTEXTO,
    "seleccion_visual": ITEMS_VISUAL,
    "ruido": ITEMS_RUIDO,
    "atencion": ITEMS_ATENCION,
    "diseno_narrativa": ITEMS_DISENO,
}


class MotorDiagnostico:
    """Motor de evaluación de 5 dimensiones"""

    def __init__(self, titulo: str = "") -> None:
        self._resultado = ResultadoDiagnostico(titulo=titulo)
        for dim in DIMENSIONES_DIAGNOSTICO:
            self._resultado.dimensiones[dim] = PuntajeDimension(dimension=dim)

    def calificar(self, dimension: str, clave_item: str, puntaje: int,
                  nota: str = "") -> "MotorDiagnostico":
        if dimension not in self._resultado.dimensiones:
            raise ValueError(f"Dimensión de diagnóstico desconocida: {dimension}")
        items = TODOS_ITEMS_DIMENSION.get(dimension, [])
        nombre = next((desc for k, desc in items if k == clave_item), clave_item)
        self._resultado.dimensiones[dimension].elementos.append((nombre, puntaje, 5, nota))
        return self

    def auto_calificar(self, puntajes: Dict[str, Dict[str, int]]) -> "MotorDiagnostico":
        """Calificación por lotes"""
        for dim, items in puntajes.items():
            for clave_item, sc in items.items():
                self.calificar(dim, clave_item, sc)
        return self

    def agregar_mejora(self, sugerencia: str) -> "MotorDiagnostico":
        self._resultado.mejoras_prioritarias.append(sugerencia)
        return self

    def agregar_rediseño(self, sugerencia: str) -> "MotorDiagnostico":
        self._resultado.sugerencias_rediseño.append(sugerencia)
        return self

    def auto_mejoras(self) -> "MotorDiagnostico":
        """Identifica ítems con baja calificación para proponer mejoras recomendadas"""
        elementos_bajos = []
        for dim, ds in self._resultado.dimensiones.items():
            for nombre, sc, maximo, nota in ds.elementos:
                if sc <= 2:
                    elementos_bajos.append((sc, dim, nombre, nota))
        elementos_bajos.sort(key=lambda x: x[0])
        for sc, dim, nombre, nota in elementos_bajos[:5]:
            etiqueta = ETIQUETAS_DIAGNOSTICO.get(dim, dim)
            self._resultado.mejoras_prioritarias.append(f"[{etiqueta}] {nombre}" + (f" — {nota}" if nota else ""))
        return self

    def construir(self) -> ResultadoDiagnostico:
        return self._resultado

    @staticmethod
    def renderizar_markdown(result: ResultadoDiagnostico) -> str:
        lineas = [f"# 🔍 Reporte de Diagnóstico Completo SWD: {result.titulo}\n"]
        lineas.append(f"## Evaluación General: {result.insignia}\n")

        for dim in DIMENSIONES_DIAGNOSTICO:
            ds = result.dimensiones.get(dim)
            if not ds or not ds.elementos:
                continue
            lineas.append(f"### {ds.etiqueta} ({ds.puntaje}/{ds.puntaje_maximo})\n")
            lineas.append("| Aspecto Evaluado | Calificación | Comentario |")
            lineas.append("|------------------|--------------|------------|")
            for nombre, sc, mx, note in ds.elementos:
                barra = "█" * sc + "░" * (mx - sc)
                lineas.append(f"| {nombre} | {barra} {sc}/{mx} | {note or ''} |")
            lineas.append("")

        if result.mejoras_prioritarias:
            lineas.append("## Plan de Mejoras Prioritarias\n")
            for i, imp in enumerate(result.mejoras_prioritarias, 1):
                lineas.append(f"{i}. {imp}")

        if result.sugerencias_rediseño:
            lineas.append("\n## Sugerencias de Rediseño Avanzado\n")
            for s in result.sugerencias_rediseño:
                lineas.append(f"- {s}")

        return "\n".join(lineas)
