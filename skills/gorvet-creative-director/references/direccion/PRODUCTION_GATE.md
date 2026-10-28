# Ficha de producción: paso obligatorio antes de generar

Este paso se aplica antes de cada llamada de generación o edición, en el chat, sin código. Consiste en rellenar una ficha con decisiones reales y escribir el prompt a partir de ella. Ejecutar directamente elimina la espera de aprobación, no el trabajo de diseño. Si un bloque no se puede rellenar con una decisión concreta, el encargo sigue en diseño: no se envía al generador un prompt genérico ni el brief sin procesar.

## La ficha (seis bloques, en este orden)

**1. Selección de contenido.** Para cada dato del brief: destino (`imagen`, `apoyo` u `omitir`) y razón. Los literales de imagen se escriben exactos. El apoyo solo se propone si tiene un destino real (caption, mensaje, secuencia). Un dato verdadero no pertenece automáticamente al arte. Mantenerlo todo exige justificar su función conjunta.

**2. Diseño concreto.**
- Formato y uso de la pieza.
- Intención visible: qué se ve y qué comunica.
- Composición: reparto de masas y recorrido de lectura.
- Tratamiento: forma, color, superficie y luz pertinentes.
- Elementos, en orden: sujeto, fondo, cada texto y cada recurso gráfico, con instrucción, posición y escala. Cada texto lleva su literal exacto, voz tipográfica y peso relativo.
- Recursos gráficos elegidos (o «ninguno»). Solo existen los que se describen aquí.
- Origen de la estética: usuario, referencia o propuesta, y por qué pertenece a este encargo.

Se puede reconstruir la pieza leyendo solo este bloque. Una etiqueta de estilo o «gran personalidad» no sustituye posiciones, escalas y relaciones.

**3. Control anti-IA convertido en diseño.** Para cada riesgo relevante, qué se verá y cómo se comprobará. Decoración automática: define los recursos que sí pertenecen y dónde, o su ausencia. Materialidad sintética: luz, textura y contacto del sujeto. Saturación: vuelve a selección y peso combinado. «Evitar estilo IA», «profesional» o una lista de prohibiciones no cuentan como resolución.

**4. Prompt compilado.** Se escribe solo desde los bloques 1 a 3, en este orden: formato → intención → composición → tratamiento → elementos (cada uno con su literal, construcción, posición y escala) → recursos gráficos elegidos y límite de añadidos → controles distintos que aún hagan falta → plan temporal si es vídeo → referencias con su función. Condiciones:
- Cada texto externo aparece una sola vez, literal, con su colocación.
- No contiene el apoyo ni los descartes, ni como ejemplo negativo.
- No contiene frases que deleguen el contenido o el diseño: «los textos de la propuesta», «los textos acordados», «gran personalidad», «buena jerarquía».
- No se reescribe libremente desde el brief original.
- En edición: base aprobada, zona o elemento que cambia, mutación pedida y atributos que se conservan.

**5. Revisión de cobertura.** En ambos sentidos: cada decisión material de los bloques 1 a 3 tiene una cláusula en el prompt, y cada cláusula procede de la ficha. Reconstruye la pieza leyendo solo el prompt; si tienes que decidir dónde va un elemento principal o qué texto conservar, vuelve a diseño. Muestra una síntesis breve con las decisiones comprobadas, no razonamientos privados.

**6. Propuesta y envío.** Se muestra al usuario: recomendación editorial, dirección visual breve, el prompt completo y copiable, y las referencias y parámetros por separado. Tras la aprobación (o la orden de ejecución directa) se envía exactamente ese texto. Si algo cambia, se muestra la versión nueva. Ver [EXECUTION_PROTOCOL.md](./EXECUTION_PROTOCOL.md).

## Qué hace cada etapa

| Etapa | Producto | Condición para avanzar |
| --- | --- | --- |
| Interpretar y seleccionar | Bloque 1 | No queda contenido que el generador deba seleccionar. |
| Conceptualizar y diseñar | Bloque 2 | Se puede reconstruir la pieza sin elegir otra idea ni distribución. |
| Evaluar | Bloque 3 y bloqueos | Los bloqueos se reparan en su origen; una nota alta o la aprobación del usuario no los cancela. |
| Compilar y comprobar | Bloques 4 y 5 | Prompt autosuficiente, sin referencias a propuestas ausentes ni material descartado. |
| Producir y verificar | Llamada y salida inspeccionada | No se cierra por recibir un archivo. Los fallos requieren reparación o estado de no validado. |

Las etapas son obligatorias cuando producen una decisión pendiente; no obligan a consultar a todos los especialistas. Una edición acotada sustituye selección y nuevo concepto por alcance, mutación y protección. Un encargo solo textual no autoriza producir imágenes.

## Estética con función

No se añade una estética por asociación automática con el sector. Un estilo propuesto debe tener una función visual en este encargo; una preferencia del usuario o una referencia de marca se conserva. Texturas, pinceladas, iconos y densidad siguen siendo posibles si fueron diseñados, no añadidos para llenar huecos.

Ejemplo del tipo de evidencia que debe sobrevivir al prompt: titular alineado directamente sobre fondo liso, escala subordinada del apoyo, recursos gráficos limitados a los definidos, materialidad dirigida por la luz. No es una fórmula para copiar en todos los trabajos.

## Límites de este paso

Es un procedimiento que aplica el asistente; no intercepta llamadas del host ni garantiza que el generador obedezca. Comprueba que la instrucción es completa y fiel al diseño, no que la imagen resultante sea buena: eso lo decide la revisión de la salida real.
