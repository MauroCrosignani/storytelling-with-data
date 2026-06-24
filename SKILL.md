---
name: narrativa-datos
version: "1.0.0"
description: >
  Habilidad de Visualización y Narrativa con Datos en español, basada en la
  metodología de Cole Nussbaumer Knaflic «Storytelling with Data».
  Permite realizar análisis de contexto, seleccionar el gráfico adecuado,
  diagnosticar ruido visual, planificar la atención y estructurar historias.
author: "Antigravity"
permissions:
  - read_file: c:/Users/mcros/Documents/storytelling-with-data
  - write_file: c:/Users/mcros/Documents/storytelling-with-data
---

# 📖 Habilidad de Narrativa con Datos (`narrativa_datos`)

Esta habilidad ayuda a transformar datos crudos en historias con impacto comercial, aplicando de forma estricta los principios del libro *Storytelling with Data* de Cole Nussbaumer Knaflic.

## 🛠️ Capacidades Principales

La habilidad expone la clase fachada `NarrativaDatos` que proporciona las siguientes 8 funciones:

1. **Creación de Contexto (`crear_contexto`)**:
   Define con precisión la audiencia principal, el tomador de decisiones, la Idea Fuerza (Big Idea) y la historia de 3 minutos.

2. **Recomendación de Gráfico (`recomendar_grafico`)**:
   Analiza el perfil físico de los datos (tipo, cantidad de series/categorías, componente temporal, etc.) y sugiere la visualización ideal. También avisa sobre gráficos desaconsejados (ej. circulares, dona, 3D o doble eje Y).

3. **Diagnóstico de Ruido Visual (`diagnosticar_ruido`)**:
   Evalúa el gráfico en busca de cuadrículas pesadas, bordes innecesarios, leyendas lejanas u otros factores que eleven la carga cognitiva del lector.

4. **Planificación de Atención Visual (`planificar_atencion`)**:
   Define puntos de enfoque clave mediante el uso selectivo de atributos preatentivos (color, tamaño, negrita) y la estrategia de color base gris.

5. **Evaluación de Diseño (`evaluar_diseno`)**:
   Evalúa el gráfico en tres dimensiones: asequibilidad, accesibilidad (título de acción, unidades, texto legible) y estética (alineación izquierda, espacios en blanco).

6. **Construcción de Historias (`construir_historia`)**:
   Estructura la narrativa de datos en el clásico arco de tres actos: Inicio (Contexto/Conflicto), Nudo (Evidencia/Opciones) y Desenlace (Llamado a la acción).

7. **Diagnóstico Completo (`diagnostico_completo`)**:
   Matriz cuantitativa de 5 dimensiones sobre 100 puntos que evalúa la calidad total de la visualización y propone un plan de acción priorizado.

8. **Rediseño de Gráficos (`rediseñar_grafico`)**:
   Genera una guía paso a paso de transformación (makeover) partiendo de problemas identificados hacia un diseño final efectivo.

---

## 🚀 Guía de Uso en Python

```python
from narrativa_datos import NarrativaDatos

# 1. Inicializar la fachada con el título del proyecto
narrativa = NarrativaDatos("Reporte de Desempeño Anual")

# 2. Recomendar un gráfico según el perfil de datos
sugerencia = narrativa.recomendar_grafico(
    tipo_datos="continuo", 
    tiene_tiempo=True, 
    cantidad_series=2
)
print(sugerencia)

# 3. Diagnosticar ruido visual en un diseño preliminar
diagnostico_ruido = narrativa.diagnosticar_ruido(
    tiene_bordes=True, 
    tiene_cuadriculas=True,
    tiene_leyenda_separada=True
)
print(diagnostico_ruido)

# 4. Estructurar el arco narrativo en tres actos
historia = narrativa.construir_historia(
    protagonista="Comité Ejecutivo",
    desequilibrio="La retención bajó del 85% al 79% por lentitud de soporte",
    evidencia=["Tiempo de respuesta subió a 48 horas", "NPS bajó a 20 puntos"],
    llamado_accion="Aprobar contratación de 3 agentes de soporte en Q1"
)
print(historia)
```
