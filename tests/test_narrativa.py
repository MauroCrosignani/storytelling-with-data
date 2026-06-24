"""Conjunto de Pruebas Unitarias de Narrativa con Datos

Valida las 8 capacidades y métodos de utilidad de la fachada principal `NarrativaDatos`.
Cada prueba unitaria contiene aserciones e imprime su estado en español.
"""

import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')
from pathlib import Path

# Agregar la raíz del proyecto al sys.path para poder importar el módulo localmente
raiz_proyecto = str(Path(__file__).resolve().parent.parent)
if raiz_proyecto not in sys.path:
    sys.path.insert(0, raiz_proyecto)

from narrativa_datos import NarrativaDatos


# ────────────────────────────────────────────
# Prueba 1: Análisis de Contexto
# ────────────────────────────────────────────
def test_crear_contexto():
    narrativa = NarrativaDatos("Reporte de Ventas Q4")
    resultado = narrativa.crear_contexto(
        audiencia="Comité Ejecutivo",
        llamado_accion="Aprobar presupuesto de optimización",
        idea_fuerza="La caída en la conversión se debe al flujo de registro; invertir 50k recuperará un 10% de transacciones.",
        historia_tres_minutos="Nuestra conversión web cayó tras el rediseño. Necesitamos corregir el formulario de registro.",
        datos_soporte=["Tasa de abandono de formulario subió al 65%", "NPS cayó 15 puntos"],
        riesgos=["La corrección tomará 3 semanas de desarrollo"],
    )

    assert isinstance(resultado, str), "El resultado debe ser una cadena de texto"
    assert len(resultado) > 50, "El reporte no debe estar vacío"
    assert "Comité Ejecutivo" in resultado, "El reporte debe incluir la audiencia"
    assert "Aprobar" in resultado, "El reporte debe contener el llamado a la acción"
    assert "Contexto" in resultado, "El reporte debe incluir el título de contexto"
    print("✅ test_crear_contexto passed")


# ────────────────────────────────────────────
# Prueba 2: Recomendación de Tipo de Gráfico
# ────────────────────────────────────────────
def test_recomendar_grafico():
    narrativa = NarrativaDatos("Evaluación Visual")

    # Caso A: Tendencia temporal continua
    resultado_lineas = narrativa.recomendar_grafico(
        tipo_datos="continuo", tiene_tiempo=True, cantidad_series=2, cantidad_categorias=12
    )
    assert isinstance(resultado_lineas, str), "Debe retornar una cadena de texto"
    assert "Línea" in resultado_lineas, "Los datos continuos temporales deben sugerir líneas"

    # Caso B: Datos categóricos con etiquetas largas
    resultado_barras = narrativa.recomendar_grafico(
        tipo_datos="categorico", cantidad_categorias=7, nombres_categorias_largos=True
    )
    assert "Horizontales" in resultado_barras, "Etiquetas largas deben sugerir barras horizontales"
    print("✅ test_recomendar_grafico passed")


# ────────────────────────────────────────────
# Prueba 3: Depuración de Ruido Visual
# ────────────────────────────────────────────
def test_diagnosticar_ruido():
    narrativa = NarrativaDatos("Gráfico de Clientes")
    resultado = narrativa.diagnosticar_ruido(
        tiene_bordes=True,
        tiene_cuadriculas=True,
        tiene_leyenda_separada=True,
        tiene_3d=True,
        tiene_sombreado_fondo=True,
    )

    assert isinstance(resultado, str), "Debe retornar una cadena de texto"
    assert "3D" in resultado or "efectos" in resultado, "Debe detectar efectos 3D"
    assert "leyenda" in resultado or "separada" in resultado, "Debe alertar sobre leyenda separada"
    print("✅ test_diagnosticar_ruido passed")


# ────────────────────────────────────────────
# Prueba 4: Planificación de Atención Visual
# ────────────────────────────────────────────
def test_planificar_atencion():
    narrativa = NarrativaDatos("Foco de Pérdidas")
    resultado = narrativa.planificar_atencion(
        elementos_enfoque=[
            ("Línea de pérdidas", 5),
            ("Línea de metas", 2),
        ],
        estrategia_color="gris_mas_uno",
    )

    assert isinstance(resultado, str), "Debe retornar una cadena de texto"
    assert "pérdidas" in resultado.lower(), "Debe incluir el elemento de pérdidas"
    print("✅ test_planificar_atencion passed")


# ────────────────────────────────────────────
# Prueba 5: Evaluación del Diseño
# ────────────────────────────────────────────
def test_evaluar_diseno():
    narrativa = NarrativaDatos("Panel de Control")

    # Evaluación positiva
    resultado_bien = narrativa.evaluar_diseno(
        tiene_titulo=True,
        color_estrategico=True,
        tiene_etiquetas=True,
        sin_ruido=True,
        flujo_narrativo=True,
    )
    assert isinstance(resultado_bien, str), "Debe retornar una cadena"

    # Evaluación con fallos
    resultado_mal = narrativa.evaluar_diseno(
        tiene_titulo=False,
        color_estrategico=False,
    )
    assert "❌" in resultado_mal, "La evaluación debe marcar los fallos con tachas"
    print("✅ test_evaluar_diseno passed")


# ────────────────────────────────────────────
# Prueba 6: Construcción de la Historia
# ────────────────────────────────────────────
def test_construir_historia():
    narrativa = NarrativaDatos("Proyecto de Retención")
    resultado = narrativa.construir_historia(
        protagonista="Equipo de Soporte",
        desequilibrio="La pérdida de clientes creció un 20% este mes",
        evidencia=["Tasa de respuesta lenta en tickets", "Aumento de quejas de facturación"],
        llamado_accion="Autorizar contratación de 3 agentes de soporte",
    )

    assert isinstance(resultado, str), "Debe retornar una cadena"
    assert "Soporte" in resultado, "Debe incluir el protagonista"
    assert "pérdida" in resultado or "creció" in resultado, "Debe contener la descripción del conflicto"
    print("✅ test_construir_historia passed")


# ────────────────────────────────────────────
# Prueba 7: Diagnóstico Completo
# ────────────────────────────────────────────
def test_diagnostico_completo():
    narrativa = NarrativaDatos("Diagnóstico Anual")
    resultado = narrativa.diagnostico_completo(calificaciones={
        "contexto": {
            "audiencia_clara": 5,
            "accion_clara": 4,
            "idea_fuerza_visible": 2,
            "datos_sostienen_tesis": 5,
        },
        "seleccion_visual": {
            "tipo_grafico_correcto": 4,
            "evita_graficos_complejos": 5,
            "linea_base_cero": 5,
            "orden_logico": 4,
        },
    })

    assert isinstance(resultado, str), "Debe retornar una cadena"
    assert "Diagnóstico" in resultado, "El reporte debe incluir la palabra Diagnóstico"
    assert "Mejoras" in resultado or "Sugerencias" in resultado, "Debe proponer planes de mejora"
    print("✅ test_diagnostico_completo passed")


# ────────────────────────────────────────────
# Prueba 8: Rediseño de Gráficos (Makeover)
# ────────────────────────────────────────────
def test_redisenar_grafico():
    narrativa = NarrativaDatos("Rediseño de Gráfico de Pastel")
    resultado = narrativa.rediseñar_grafico(
        problemas=[
            "Se usó un gráfico circular para 8 categorías",
            "Uso de colores muy llamativos y aleatorios",
            "Leyenda separada a la derecha",
        ]
    )

    assert isinstance(resultado, str), "Debe retornar una cadena"
    assert len(resultado) > 50, "El reporte no debe estar vacío"
    print("✅ test_redisenar_grafico passed")


# ────────────────────────────────────────────
# Prueba 9: Comparativa de Decisiones
# ────────────────────────────────────────────
def test_construir_comparativa_decisiones():
    narrativa = NarrativaDatos("Decisión de Alojamiento")
    resultado = narrativa.construir_comparativa_decisiones(
        titulo="Evaluación de Proveedor",
        opcion_a="Servidor Físico Local",
        opcion_b="Nube Pública",
        criterios=["Costo de mantenimiento", "Escalabilidad", "Seguridad física"],
    )

    assert isinstance(resultado, str), "Debe retornar una cadena"
    assert "Nube Pública" in resultado, "Debe contener la opción B"
    assert "Escalabilidad" in resultado, "Debe incluir los criterios de comparación"
    print("✅ test_construir_comparativa_decisiones passed")


# ────────────────────────────────────────────
# Ejecución Principal
# ────────────────────────────────────────────
if __name__ == "__main__":
    pruebas = [
        test_crear_contexto,
        test_recomendar_grafico,
        test_diagnosticar_ruido,
        test_planificar_atencion,
        test_evaluar_diseno,
        test_construir_historia,
        test_diagnostico_completo,
        test_redisenar_grafico,
        test_construir_comparativa_decisiones,
    ]

    exitos = 0
    fallos = 0
    for prueba_func in pruebas:
        try:
            prueba_func()
            exitos += 1
        except Exception as err:
            fallos += 1
            print(f"❌ Falló {prueba_func.__name__}: {err}")

    print(f"\n{'='*50}")
    print(f"Resultado de Pruebas: {exitos} exitosas, {fallos} fallidas, {len(pruebas)} en total")
    if fallos == 0:
        print("🎉 ¡Excelente! Las 9 pruebas unitarias se ejecutaron con éxito en español.")
    else:
        print(f"⚠️ Se detectaron {fallos} fallas de aserción.")
        sys.exit(1)
