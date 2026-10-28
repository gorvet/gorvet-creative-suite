# Producción y revisión audiovisual

## Compatibilidad real

Antes de compilar registra herramienta disponible y controles comprobados: modos de entrada, duración por clip, proporción, referencia inicial/final, audio, edición y formato de salida cuando sean relevantes. Verifica capacidades en documentación vigente o en el contrato de herramienta; una receta externa no las acredita. No envíes parámetros inventados. Si el plano excede la capacidad, propone dividirlo conservando continuidad o usa un montaje disponible; no altera silenciosamente el ritmo aprobado.

Para image-to-video, separa atributos protegidos de la base, movimiento del sujeto, evolución del entorno y movimiento de cámara. Si una región fuera de cuadro debe aparecer, comprueba que pueda definirse sin inventar detalles protegidos. Para animatic, indica qué prueba: composición, duración, transición; no lo presentes como vídeo final acabado.

## Traspaso por clip

El registro maestro conserva la dirección y duración de la pieza. Cada llamada de producción usa un registro hijo con identificador, intervalo, prompt exacto, fuentes reales, parámetros mostrados, autorización y salida. Una aprobación conjunta puede abarcar esos clips identificados; una nueva dirección requiere renovar la propuesta. No declares que un prompt largo se ejecuta como múltiples clips si la herramienta hace una sola llamada.

Compilación organiza estado inicial, acción en el tiempo, cámara, salida y audio compatible. Los guiones de apoyo y tomas descartadas no van al generador. Repetir anclas entre clips independientes es necesario; duplicarlas dentro de uno no aporta control.

## Inspección

Reproduce la salida completa a velocidad prevista, con audio cuando existe. Comprueba inicio, desarrollo, final, todas las uniones y bucle cuando corresponda. Localiza hallazgos con tiempos: deformación, deslizamiento, contacto, manos, cambio de identidad, continuidad de trayectoria, legibilidad y permanencia, cortes o sincronía. Fotogramas aislados ayudan a localizar defectos pero no demuestran movimiento, duración ni sincronía.

Crítica entrega `review.playback` con `full_duration: true`, `transitions_checked: true` y `audio_checked: true` cuando se necesita audio, junto con evidencia temporal auténtica y rúbrica `motion`. Si solo se pueden ver fotogramas, emite revisión parcial y estado no verificable para el vídeo completo. Una afirmación del generador no es inspección.

## Reparar y cerrar

Determina si el defecto viene de puesta en escena, captura, gráfica, compilación, generación o montaje. Repara el menor tramo que permita recuperar el resultado sin romper los adyacentes. Revisa los puntos de unión y luego la reproducción completa; volver a generar el plano puede cambiar identidad o estado final. La entrega incluye el archivo realmente producido, duración y formato comprobados, y límites pendientes. Un storyboard no satisface una entrega de vídeo.
