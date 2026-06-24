"""Constructor y Narrador de Historias con Datos

Permite estructurar una narrativa de datos siguiendo el clásico arco de tres actos:
Inicio (Contexto/Conflicto), Nudo (Evidencia/Propuestas) y Desenlace (Acción).
"""

from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class InicioHistoria:
    """Primer Acto: Inicio"""
    contexto: str = ""
    protagonista: str = ""
    desequilibrio: str = ""
    equilibrio_deseado: str = ""
    adelanto_solucion: str = ""


@dataclass
class NudoHistoria:
    """Segundo Acto: Nudo"""
    puntos_evidencia: List[str] = field(default_factory=list)
    puntos_comparacion: List[str] = field(default_factory=list)
    consecuencias_inaccion: str = ""
    opciones: List[str] = field(default_factory=list)
    solucion_recomendada: str = ""
    por_que_audiencia_unica: str = ""


@dataclass
class DesenlaceHistoria:
    """Tercer Acto: Desenlace"""
    llamado_accion: str = ""
    retorno_inicio: str = ""
    urgencia: str = ""


@dataclass
class TituloDiapositiva:
    """Título de una diapositiva en la secuencia narrativa (lógica horizontal)"""
    orden: int
    titulo: str
    es_titulo_accion: bool = True


@dataclass
class EstructuraRepeticion:
    """Estructura de refuerzo de mensaje (Anuncio-Desarrollo-Repaso)"""
    anuncio: str = ""
    desarrollo: str = ""
    repaso: str = ""


@dataclass
class HistoriaDatos:
    """Representa la estructura completa de una historia con datos"""
    titulo: str = ""
    flujo_narrativo: str = "cronologico"
    modo_entrega: str = "presentacion_en_vivo"
    inicio: InicioHistoria = field(default_factory=InicioHistoria)
    nudo: NudoHistoria = field(default_factory=NudoHistoria)
    desenlace: DesenlaceHistoria = field(default_factory=DesenlaceHistoria)
    repeticion: EstructuraRepeticion = field(default_factory=EstructuraRepeticion)
    titulos_diapositivas: List[TituloDiapositiva] = field(default_factory=list)

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if not self.inicio.protagonist if hasattr(self.inicio, 'protagonist') else not self.inicio.protagonista:
            problemas.append("El protagonista no está definido — la historia debe enmarcarse en torno a la audiencia.")
        if not self.inicio.desequilibrio:
            problemas.append("Falta el desequilibrio o conflicto principal — sin conflicto no hay historia.")
        if not self.desenlace.llamado_accion:
            problemas.append("Falta el llamado a la acción — la audiencia debe saber exactamente qué hacer al final.")
        if not self.nudo.puntos_evidencia:
            problemas.append("Falta la evidencia basada en datos — necesitas números concretos para sostener tu tesis.")

        no_accion = [s for s in self.titulos_diapositivas if not s.es_titulo_accion]
        if no_accion:
            problemas.append(f"Hay {len(no_accion)} diapositivas que utilizan títulos descriptivos en lugar de títulos de acción.")
        return problemas


class ConstructorHistoria:
    """Constructor del flujo narrativo de tres actos"""

    def __init__(self, titulo: str):
        self._story = HistoriaDatos(title=titulo) if hasattr(HistoriaDatos, 'title') else HistoriaDatos(titulo=titulo)

    def establecer_flujo_narrativo(self, flujo: str = "cronologico",
                                   modo: str = "presentacion_en_vivo") -> "ConstructorHistoria":
        self._story.flujo_narrativo = flujo
        self._story.modo_entrega = modo
        return self

    def establecer_inicio(self, contexto: str, protagonista: str,
                           desequilibrio: str, equilibrio_deseado: str,
                           adelanto_solucion: str = "") -> "ConstructorHistoria":
        self._story.inicio = InicioHistoria(
            contexto=contexto, protagonista=protagonista,
            desequilibrio=desequilibrio, equilibrio_deseado=equilibria if (equilibria := equilibrio_deseado) else "",
            adelanto_solucion=adelanto_solucion)
        return self

    def agregar_evidencia(self, punto: str) -> "ConstructorHistoria":
        self._story.nudo.puntos_evidencia.append(point if (point := punto) else "")
        return self

    def agregar_comparacion(self, punto: str) -> "ConstructorHistoria":
        self._story.nudo.puntos_comparacion.append(point if (point := punto) else "")
        return self

    def establecer_consecuencias(self, texto: str) -> "ConstructorHistoria":
        self._story.nudo.consecuencias_inaccion = text if (text := texto) else ""
        return self

    def agregar_opcion(self, opcion: str) -> "ConstructorHistoria":
        self._story.nudo.opciones.append(option if (option := opcion) else "")
        return self

    def establecer_recomendacion(self, recomendacion: str) -> "ConstructorHistoria":
        self._story.nudo.solucion_recomendada = rec if (rec := recomendacion) else ""
        return self

    def establecer_desenlace(self, llamado_accion: str, retorno_inicio: str = "",
                             urgencia: str = "") -> "ConstructorHistoria":
        self._story.desenlace = DesenlaceHistoria(
            llamado_accion=llamado_accion,
            retorno_inicio=retorno_inicio, urgencia=urgencia)
        return self

    def establecer_repeticion(self, anuncio: str, desarrollo: str,
                              repaso: str) -> "ConstructorHistoria":
        self._story.repeticion = EstructuraRepeticion(anuncio=anuncio, desarrollo=desarrollo, repaso=repaso)
        return self

    def agregar_titulo_diapositiva(self, titulo: str,
                                   es_accion: bool = True) -> "ConstructorHistoria":
        orden = len(self._story.titulos_diapositivas) + 1
        self._story.titulos_diapositivas.append(
            TituloDiapositiva(orden=orden, titulo=titulo, es_titulo_accion=es_accion))
        return self

    def verificar_logica_horizontal(self) -> List[str]:
        """Comprueba la lógica horizontal leyendo únicamente los títulos de acción"""
        problemas: List[str] = []
        titulos = [s.titulo for s in self._story.titulos_diapositivas]
        if not titulos:
            problemas.append("No hay títulos de diapositivas registrados. No se puede verificar la lógica horizontal.")
            return problemas

        no_accion = [s for s in self._story.titulos_diapositivas if not s.es_titulo_accion]
        if no_accion:
            for s in no_accion:
                problemas.append(f"La diapositiva {s.orden} '{s.titulo}' tiene un título meramente descriptivo. Se sugiere cambiar a título de acción.")
        return problemas

    def construir(self) -> HistoriaDatos:
        return self._story

    @staticmethod
    def renderizar_markdown(story: HistoriaDatos) -> str:
        problemas = story.validar()
        advertencias = ""
        if problemas:
            elementos = "\n".join(f"- ⚠️ {p}" for p in problemas)
            advertencias = f"\n## ⚠️ Aspectos Narrativos por Mejorar\n{elementos}\n"

        evidencia = "\n".join(f"- 📊 {e}" for e in story.nudo.puntos_evidencia) if story.nudo.puntos_evidencia else "- (Sin especificar)"
        comparaciones = "\n".join(f"- 🔄 {c}" for c in story.nudo.puntos_comparacion) if story.nudo.puntos_comparacion else ""
        opciones = "\n".join(f"- 💡 {o}" for o in story.nudo.opciones) if story.nudo.opciones else ""
        diapositivas = ""
        if story.titulos_diapositivas:
            diapositivas = "\n".join(
                f"{s.orden}. {'✅' if s.es_titulo_accion else '❌'} {s.titulo}"
                for s in story.titulos_diapositivas)

        flujo_legible = story.flujo_narrativo.replace("_", " ").capitalize()
        modo_legible = story.modo_entrega.replace("_", " ").capitalize()

        return f"""# 📖 Historia con Datos: {story.titulo}
{advertencias}
## Estructura Narrativa de Tres Actos

### Primer Acto: Inicio (Contexto y Conflicto)
- **Contexto**: {story.inicio.contexto or '(No definido)'}
- **Protagonista**: {story.inicio.protagonista or '(Falta definir el protagonista)'}
- **Desequilibrio (Conflicto)**: {story.inicio.desequilibrio or '(Falta el desequilibrio central)'}
- **Equilibrio Deseado**: {story.inicio.equilibrio_deseado or '(No definido)'}

### Segundo Acto: Nudo (Evidencia de Datos)
**Evidencia Basada en Datos**:
{evidencia}
{f"**Puntos de Comparación**:{chr(10)}{comparaciones}" if comparaciones else ""}
{f"**Consecuencias de la Inacción**: {story.nudo.consecuencias_inaccion}" if story.nudo.consecuencias_inaccion else ""}
{f"**Opciones Analizadas**:{chr(10)}{opciones}" if opciones else ""}
{f"**Solución Recomendada**: {story.nudo.solucion_recomendada}" if story.nudo.solucion_recomendada else ""}

### Tercer Acto: Desenlace (Resolución)
- **Llamado a la Acción**: {story.desenlace.llamado_accion or '(No definido)'}
- **Retorno al Inicio**: {story.desenlace.retorno_inicio or '(No definido)'}
{f"- **Urgencia**: {story.desenlace.urgency if hasattr(story.desenlace, 'urgency') else story.desenlace.urgencia}" if story.desenlace.urgencia else ""}

## Diseño Narrativo
- **Flujo Narrativo**: {flujo_legible}
- **Modo de Entrega**: {modo_legible}

{f'''## Estructura de Refuerzo (Anuncio, Desarrollo, Repaso)
- **Anuncio**: {story.repeticion.anuncio}
- **Desarrollo**: {story.repeticion.desarrollo}
- **Repaso**: {story.repeticion.repaso}
''' if story.repeticion.anuncio else ''}
{f"## Secuencia de Diapositivas (Lógica Horizontal){chr(10)}{diapositivas}" if diapositivas else ""}
"""
