"""Motor de Análisis de Contexto

Permite perfilar a la audiencia, definir el mecanismo de comunicación,
formular la Idea Fuerza (Big Idea) y estructurar la historia de 3 minutos.
"""

from dataclasses import dataclass, field
from typing import List, Optional


NIVELES_CONOCIMIENTO = ("experto", "general", "principiante")
RELACIONES = ("primer_contacto", "establecida", "requiere_credibilidad")
MECANISMOS = ("presentacion_en_vivo", "reporte_escrito", "correo_electronico", "mixto")
TONOS = ("serio", "urgente", "celebracion", "informal", "neutral")
MOTIVACIONES = (
    "ahorrar_dinero", "incrementar_ingresos", "superar_competencia",
    "ganar_mercado", "mitigar_riesgo", "innovar", "mejorar_eficiencia",
)


@dataclass
class PerfilAudiencia:
    """Perfil de la audiencia objetivo"""
    audiencia_principal: str = ""
    tomador_decision: str = ""
    nivel_conocimiento: str = "general"
    relacion: str = "primer_contacto"
    sesgos: str = ""
    motivacion: str = ""

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if not self.audiencia_principal:
            problemas.append("Debe especificar la audiencia principal (roles o cargos específicos).")
        if self.nivel_conocimiento not in NIVELES_CONOCIMIENTO:
            problemas.append(f"El nivel de conocimiento '{self.nivel_conocimiento}' no es válido: {NIVELES_CONOCIMIENTO}")
        if self.relacion not in RELACIONES:
            problemas.append(f"La relación '{self.relacion}' no es válida: {RELACIONES}")
        return problemas


@dataclass
class IdeaFuerza:
    """Idea Fuerza (Big Idea) — Consta de un punto de vista único y del interés en juego"""
    punto_vista_unico: str = ""
    interes_en_juego: str = ""
    frase_completa: str = ""

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if not self.punto_vista_unico:
            problemas.append("La Idea Fuerza debe incluir tu punto de vista único.")
        if not self.interes_en_juego:
            problemas.append("La Idea Fuerza debe incluir el interés en juego (lo que se arriesga).")
        if not self.frase_completa:
            problemas.append("La Idea Fuerza debe redactarse en una única frase completa.")
        elif len(self.frase_completa) < 10:
            problemas.append("La frase de la Idea Fuerza es demasiado corta. Intenta ser más descriptivo.")
        return problemas

    def renderizar(self) -> str:
        return self.frase_completa


@dataclass
class AnalisisContexto:
    """Análisis completo del contexto de la comunicación"""
    titulo: str = ""
    audiencia: PerfilAudiencia = field(default_factory=PerfilAudiencia)
    mecanismo: str = "presentacion_en_vivo"
    tono: str = "neutral"
    historia_tres_minutos: str = ""
    idea_fuerza: IdeaFuerza = field(default_factory=IdeaFuerza)
    datos_soporte: List[str] = field(default_factory=list)
    riesgos: List[str] = field(default_factory=list)
    llamado_accion: str = ""

    def validar(self) -> List[str]:
        problemas: List[str] = []
        if not self.titulo:
            problemas.append("Debe asignar un título al análisis de contexto.")
        problemas.extend(self.audiencia.validar())
        problemas.extend(self.idea_fuerza.validar())
        if self.mecanismo not in MECANISMOS:
            problemas.append(f"El mecanismo de comunicación '{self.mecanismo}' no es válido: {MECANISMOS}")
        if self.tono not in TONOS:
            problemas.append(f"El tono '{self.tono}' no es válido: {TONOS}")
        if not self.historia_tres_minutos:
            problemas.append("Falta la historia de 3 minutos (resumen ejecutivo inmediato).")
        if not self.llamado_accion:
            problemas.append("Debe especificar un llamado a la acción (qué debe hacer la audiencia).")
        if not self.datos_soporte:
            problemas.append("Debe identificar al menos un dato de soporte que valide su tesis.")
        return problemas


class CreadorContexto:
    """Constructor y validador del contexto de comunicación"""

    def __init__(self, titulo: str):
        self._analisis = AnalisisContexto(titulo=titulo)

    def establecer_audiencia(self, principal: str, tomador_decision: str = "",
                             nivel_conocimiento: str = "general",
                             relacion: str = "primer_contacto",
                             sesgos: str = "", motivacion: str = "") -> "CreadorContexto":
        self._analisis.audiencia = PerfilAudiencia(
            audiencia_principal=principal, tomador_decision=tomador_decision,
            nivel_conocimiento=nivel_conocimiento, relacion=relacion,
            sesgos=sesges if (sesges := sesgos) else "", motivacion=motivacion,
        )
        return self

    def establecer_mecanismo(self, mecanismo: str, tono: str = "neutral") -> "CreadorContexto":
        self._analisis.mecanismo = mecanismo
        self._analisis.tono = tono
        return self

    def establecer_historia_tres_minutos(self, historia: str) -> "CreadorContexto":
        self._analisis.historia_tres_minutos = historia
        return self

    def establecer_idea_fuerza(self, punto_vista: str, interes: str,
                               frase: str) -> "CreadorContexto":
        self._analisis.idea_fuerza = IdeaFuerza(
            punto_vista_unico=punto_vista, interes_en_juego=interes,
            frase_completa=frase,
        )
        return self

    def agregar_dato_soporte(self, dato: str) -> "CreadorContexto":
        self._analisis.datos_soporte.append(dato)
        return self

    def agregar_riesgo(self, riesgo: str) -> "CreadorContexto":
        self._analisis.riesgos.append(riesgo)
        return self

    def establecer_llamado_accion(self, llamado: str) -> "CreadorContexto":
        self._analisis.llamado_accion = llamado
        return self

    def construir(self) -> AnalisisContexto:
        return self._analisis

    @staticmethod
    def renderizar_markdown(ctx: AnalisisContexto) -> str:
        problemas = ctx.validar()
        advertencias = ""
        if problemas:
            elementos = "\n".join(f"- ⚠️ {p}" for p in problemas)
            advertencias = f"\n## ⚠️ Elementos por Completar o Corregir\n{elementos}\n"

        lista_datos = "\n".join(f"- {d}" for d in ctx.datos_soporte) if ctx.datos_soporte else "- (Sin especificar)"
        lista_riesgos = "\n".join(f"- {r}" for r in ctx.riesgos) if ctx.riesgos else "- (Sin especificar)"

        mecanismo_legible = ctx.mecanismo.replace("_", " ").capitalize()
        tono_legible = ctx.tono.capitalize()

        return f"""# 📋 Reporte de Análisis de Contexto: {ctx.titulo}
{advertencias}
## Perfil de la Audiencia
| Dimensión | Detalle |
|-----------|---------|
| Audiencia Principal | {ctx.audiencia.audiencia_principal or '(Sin especificar)'} |
| Tomador de Decisiones | {ctx.audiencia.tomador_decision or '(Sin especificar)'} |
| Nivel de Conocimiento | {ctx.audiencia.nivel_conocimiento.capitalize()} |
| Estado de Relación | {ctx.audiencia.relacion.replace('_', ' ').capitalize()} |
| Sesgos o Preferencias | {ctx.audiencia.sesgos or '(Ninguno conocido)'} |
| Motivación Principal | {ctx.audiencia.motivacion or '(Sin especificar)'} |

## Mecanismo de Comunicación
- **Formato**: {mecanismo_legible}
- **Tono General**: {tono_legible}

## Mensaje Central

### Historia de 3 Minutos
{ctx.historia_tres_minutos or '(No redactada aún)'}

### Idea Fuerza (Big Idea)
> {ctx.idea_fuerza.renderizar() or '(No definida)'}

- **Punto de Vista Único**: {ctx.idea_fuerza.punto_vista_unico or '(No definido)'}
- **Interés en Juego**: {ctx.idea_fuerza.interes_en_juego or '(No definido)'}

### Datos de Soporte
{lista_datos}

### Riesgos y Contraevidencia
{lista_riesgos}

## Llamado a la Acción (Call to Action)
{ctx.llamado_accion or '(Sin especificar)'}
"""
