"""Módulo Principal de Narrativa con Datos

Fachada unificada en español para acceder a las 8 capacidades basadas en la metodología
de Cole Nussbaumer Knaflic «Storytelling with Data».
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from narrativa_datos.contexto import CreadorContexto
from narrativa_datos.seleccionador_grafico import SeleccionadorGrafico, PerfilDatos
from narrativa_datos.depurador_ruido import DepuradorRuido
from narrativa_datos.atencion import AnalizadorAtencion
from narrativa_datos.narrador import ConstructorHistoria
from narrativa_datos.diagnostico import MotorDiagnostico
from narrativa_datos.redisenador import RedisenadorGrafico
from narrativa_datos.evaluador_diseno import EvaluadorDiseno

__version__ = "1.0.0"

__all__ = ["NarrativaDatos", "__version__"]


class NarrativaDatos:
    """Fachada unificada (Facade) para acceder a las 8 capacidades de la metodología SWD.

    Cada método sirve como envoltura directa sobre los submódulos específicos del dominio,
    manteniendo la API homogénea, simple y 100% en español.
    """

    def __init__(self, titulo: str) -> None:
        self.titulo = titulo

    # ── Capacidad 1: Análisis de Contexto ──
    def crear_contexto(
        self,
        audiencia: str = "",
        llamado_accion: str = "",
        idea_fuerza: str = "",
        historia_tres_minutos: str = "",
        mecanismo: str = "",
        datos_soporte: Optional[List[str]] = None,
        riesgos: Optional[List[str]] = None,
        **_kwargs: Any,
    ) -> str:
        """Crea el contexto de comunicación del proyecto (受众/Big Idea/Llamado a la acción)."""
        creador = CreadorContexto(self.titulo)
        if audiencia:
            creador.establecer_audiencia(audiencia)
        if llamado_accion:
            creador.establecer_llamado_accion(llamado_accion)
        if idea_fuerza:
            creador.establecer_idea_fuerza(
                punto_vista=idea_fuerza, interes=idea_fuerza, frase=idea_fuerza
            )
        if historia_tres_minutos:
            creador.establecer_historia_tres_minutos(historia_tres_minutos)
        if mecanismo:
            creador.establecer_mecanismo(mecanismo)
        if datos_soporte:
            for d in datos_soporte:
                creador.agregar_dato_soporte(d)
        if riesgos:
            for r in riesgos:
                creador.agregar_riesgo(r)
        return CreadorContexto.renderizar_markdown(creador.construir())

    # ── Capacidad 2: Selección del Gráfico ──
    def recomendar_grafico(
        self,
        tipo_datos: str = "",
        tiene_tiempo: bool = False,
        cantidad_series: int = 0,
        cantidad_categorias: int = 0,
        tipo_comparacion: str = "",
        muestra_parte_del_todo: bool = False,
        **_kwargs: Any,
    ) -> str:
        """Recomienda el tipo de gráfico idóneo basado en las propiedades físicas de los datos."""
        selector = SeleccionadorGrafico()
        perfil = PerfilDatos(
            tipo_datos=tipo_datos or "categorico",
            cantidad_series=cantidad_series,
            cantidad_categorias=cantidad_categorias,
            tiene_dimension_tiempo=tiene_tiempo,
            muestra_parte_del_todo=muestra_parte_del_todo,
        )
        recomendaciones = selector.recomendar(perfil)
        if not recomendaciones:
            return "No hay ninguna recomendación disponible para el perfil ingresado."

        lineas = []
        for r in recomendaciones:
            simbolo = "⭐" if r.prioridad == 1 else "  "
            lineas.append(f"{simbolo} **{r.etiqueta}**")
            lineas.append(f"   {r.motivo}")
            for nota in r.notas_diseno:
                lineas.append(f"   - {nota}")
            lineas.append("")
        return "\n".join(lineas)

    # ── Capacidad 3: Depuración de Ruido Visual ──
    def diagnosticar_ruido(
        self,
        tiene_cuadriculas: bool = False,
        tiene_bordes: bool = False,
        tiene_leyenda_separada: bool = False,
        tiene_3d: bool = False,
        tiene_sombreado_fondo: bool = False,
        **_kwargs: Any,
    ) -> str:
        """Identifica elementos de distracción en el gráfico y sugiere su depuración."""
        depurador = DepuradorRuido()
        depurador.auto_detectar(
            tiene_cuadriculas=tiene_cuadriculas,
            tiene_bordes=tiene_bordes,
            tiene_leyenda_separada=tiene_leyenda_separada,
            tiene_efecto_3d=tiene_3d,
            tiene_sombreado_fondo=tiene_sombreado_fondo,
        )
        return DepuradorRuido.renderizar_markdown(depurador.construir())

    # ── Capacidad 4: Dirección de la Atención ──
    def planificar_atencion(
        self,
        elementos_enfoque: Optional[List[tuple]] = None,
        estrategia_color: str = "",
        preatentivo: bool = True,
        **_kwargs: Any,
    ) -> str:
        """Diseña el plan de estímulos visuales (atributos preatentivos) para enfocar al lector."""
        analizador = AnalizadorAtencion()
        if elementos_enfoque:
            for elemento, importancia in elementos_enfoque:
                analizador.agregar_enfoque(str(elemento), importancia)
        if preattentive := preatentivo:
            analizador.auto_sugerir()
        return AnalizadorAtencion.renderizar_markdown(analizador.construir())

    # ── Capacidad 5: Evaluación del Diseño ──
    def evaluar_diseno(
        self,
        tiene_titulo: bool = False,
        color_estrategico: bool = False,
        tiene_etiquetas: bool = False,
        sin_ruido: bool = False,
        flujo_narrativo: bool = False,
        **_kwargs: Any,
    ) -> str:
        """Inspecciona el gráfico bajo las tres normas de asequibilidad, accesibilidad y estética."""
        evaluador = EvaluadorDiseno()
        evaluador.auto_evaluar(
            tiene_titulo=tiene_titulo,
            color_estrategico=color_estrategico,
            tiene_anotaciones=tiene_etiquetas,
            distracciones_eliminadas=sin_ruido,
            jerarquia_clara=flujo_narrativo,
        )
        return EvaluadorDiseno.renderizar_markdown(evaluador.construir())

    # ── Capacidad 6: Construcción de la Historia ──
    def construir_historia(
        self,
        protagonista: str = "",
        desequilibrio: str = "",
        evidencia: Optional[List[str]] = None,
        llamado_accion: str = "",
        equilibrio_deseado: str = "",
        flujo_narrativo: str = "cronologico",
        comparacion: Optional[Dict[str, Any]] = None,
        **_kwargs: Any,
    ) -> str:
        """Estructura la narrativa de datos en un arco clásico de tres actos."""
        constructor = ConstructorHistoria(self.titulo)
        if protagonista or desequilibrio:
            constructor.establecer_inicio(
                contexto=self.titulo,
                protagonista=protagonista,
                desequilibrio=desequilibrio,
                equilibrio_deseado=equilibrio_deseado or llamado_accion,
            )
        if llamado_accion:
            constructor.establecer_desenlace(llamado_accion=llamado_accion)
        if flujo_narrativo:
            constructor.establecer_flujo_narrativo(flujo=flujo_narrativo)
        if evidencia:
            for e in evidencia:
                constructor.agregar_evidencia(e)
        if comparacion:
            constructor.agregar_comparacion(
                f"{comparacion.get('titulo', '')}: {comparacion.get('opcion_a', '')} vs {comparacion.get('opcion_b', '')}"
            )
        return ConstructorHistoria.renderizar_markdown(constructor.construir())

    # ── Capacidad 7: Diagnóstico Completo ──
    def diagnostico_completo(
        self,
        calificaciones: Optional[Dict[str, Dict[str, int]]] = None,
        **_kwargs: Any,
    ) -> str:
        """Realiza un diagnóstico integral cuantitativo de 5 dimensiones."""
        motor = MotorDiagnostico(self.titulo)
        if calificaciones:
            for dimension, items in calificaciones.items():
                for clave_item, puntaje in items.items():
                    motor.calificar(dimension, clave_item, puntaje)
            motor.auto_mejoras()
        return MotorDiagnostico.renderizar_markdown(motor.construir())

    # ── Capacidad 8: Rediseño de Gráficos (Makeover) ──
    def rediseñar_grafico(
        self,
        problemas: Optional[List[str]] = None,
        especificacion_diseno: str = "",
        **_kwargs: Any,
    ) -> str:
        """Recomienda pasos específicos de rediseño para solucionar problemas detectados."""
        redisenador = RedisenadorGrafico(self.titulo)
        if problemas:
            for p in problemas:
                redisenador.agregar_problema(p)
            redisenador.auto_pasos_desde_problemas()
        if especificacion_diseno:
            redisenador.establecer_especificacion_diseno(titulo=especificacion_diseno)
        return RedisenadorGrafico.renderizar_markdown(redisenador.construir())

    # ── Utilidad: Comparativa de Decisiones para Negocios ──
    def construir_comparativa_decisiones(
        self,
        titulo: str = "Comparativa de Opciones",
        opcion_a: str = "Opción A",
        opcion_b: str = "Opción B",
        criterios: Optional[List[str]] = None,
        **_kwargs: Any,
    ) -> str:
        """Construye una estructura narrativa específica para contrastar alternativas estratégicas."""
        constructor = ConstructorHistoria(self.titulo)
        constructor.agregar_comparacion(f"{titulo}: {opcion_a} vs {opcion_b}")
        if criterios:
            for c in criterios:
                constructor.agregar_comparacion(c)
        return ConstructorHistoria.renderizar_markdown(constructor.construir())
