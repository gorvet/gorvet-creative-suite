# Rúbrica GORVET para comparar y corregir

Las puntuaciones sirven para localizar debilidades, comparar alternativas del mismo encargo y comprobar una mejora. Son juicios ordinales con evidencia, no porcentajes de exactitud ni predicciones de ventas, premios o reacción del público. Se separan evaluación de concepto y evaluación visual.

## Escala común

| Nota | Ancla de evaluación |
| --- | --- |
| 0 | Falta el requisito o contradice materialmente el encargo. |
| 1 | Hay un problema grave que impide cumplir la función del criterio. |
| 2 | La función se reconoce, pero necesita una corrección concreta antes de cerrar. |
| 3 | Cumple la función con ejecución coherente y evidencia suficiente para este encargo. |
| 4 | Además de cumplir, una decisión específica mejora de forma clara la solución; se identifica su evidencia. |

No uses decimales ni subas notas para alcanzar un resultado deseado. Cada criterio necesita evidencia concreta; en concepto, procede de la solución descrita; en revisión visual, de la imagen observada. `No aplicable` requiere una razón y se excluye del cálculo. Si un criterio importa pero no puede observarse, el estado es no verificable, no un aprobado supuesto.

Una edición localizada comprueba primero base, objetivo, cambio, conservación y aceptación. No se puntúa su novedad como si fuera otra campaña. Su resultado visual se compara con el alcance aprobado: conservar carácter y función puede ser la decisión correcta.

## Concepto y preflight

| Criterio | Peso base | Qué se evalúa |
| --- | --- | --- |
| Adecuación | 25 | Responde al objetivo, al contenido real y al destinatario pertinente. |
| Especificidad | 20 | El argumento contiene una decisión propia del encargo, más allá de un estilo intercambiable. |
| Interés | 20 | Existe un motivo visible o conceptual para detenerse y una intención perceptiva concreta. |
| Claridad | 20 | Se comprende la proposición sin una explicación que la imagen no puede representar. |
| Viabilidad | 15 | La idea puede producirse con las referencias, el soporte y las herramientas disponibles. |

En series, añade al diagnóstico la función de cada pieza y el desarrollo de la idea; no penalices una imagen individual por no ser una plataforma de campaña. Una hipótesis sobre el público se identifica como hipótesis. La nota no transforma esa inferencia en investigación.

## Arte producido

| Criterio | Peso base | Qué se evalúa |
| --- | --- | --- |
| Comunicación | 20 | Mensaje, contenido seleccionado y propósito se reconocen a escala de uso. |
| Carácter e interés | 20 | El resultado tiene intención visual específica y la ejecución la sostiene. |
| Estructura | 20 | Jerarquía, composición, agrupación, espacio y recorte funcionan conjuntamente. |
| Tipografía | 15 | Texto correcto, agrupación, forma, alineación y legibilidad; solo si hay texto pertinente. |
| Fidelidad | 15 | Se conserva lo que gobiernan las referencias y los hechos del encargo; si hay fuentes o atributos verificables. |
| Oficio visual | 10 | Color, acabado, perspectiva y materiales o coherencia gráfica pertenecen al medio elegido. |

El índice se calcula como la suma ponderada de notas dividida por la suma de pesos aplicables, multiplicada por 25 y redondeada al entero. Se presenta como índice sobre 100, sin símbolo de porcentaje. Con notas 3 en todos los criterios el índice es 75: ejecución apta según estas anclas, no excelencia universal.

## Bloqueos y decisión

Antes de puntuar, identifica contradicciones materiales: texto exigido incorrecto, dato falso, condición necesaria eliminada, identidad protegida alterada, intervención fuera del alcance o fallo focal que impida comprender la pieza. Un bloqueo obliga a corregir aunque el resto tenga nota alta.

La decisión es apta cuando no hay bloqueos, todos los criterios aplicables alcanzan 3 y existe la evidencia requerida. El índice ayuda a ordenar opciones aptas; no permite promediar un fallo hasta hacerlo desaparecer. En revisión visual, además se necesita haber inspeccionado esa salida y compararla con la dirección vigente.

Si un criterio queda en 2 o menos, formula evidencia, consecuencia, responsable y cambio concreto. Corrige ese ámbito y vuelve a comparar, incluyendo posibles regresiones. Si el concepto falla, no lo maquilles mediante luz o tipografía. Si falla un literal, no reinicies estrategia.

Por defecto usa esta rúbrica. Si el usuario aporta otra, registra cuál se aplica y conserva las verificaciones factuales y de alcance. Las fuentes y la diferencia respecto a las escalas de Designly y de Serge Shima están en [SOURCE_ADAPTATION.md](SOURCE_ADAPTATION.md). La evaluación automática del formato y cálculo está en [score_review.py](../scripts/score_review.py); el script no observa ni juzga imágenes.
