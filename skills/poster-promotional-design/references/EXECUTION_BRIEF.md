# Del diseño resuelto al encargo de ejecución

El generador no conoce el análisis ni las bibliotecas del skill. Recibe la descripción ejecutable de una pieza que el asistente ya ha diseñado y evaluado. No debe tener que decidir el argumento publicitario, seleccionar el contenido ni inventar la composición principal.

## Transmitir la prioridad elegida

Abre el encargo con el resultado publicitario que gobierna el trabajo: qué se anuncia, mediante qué argumento y qué debe reconocerse primero. Incluye el medio elegido y la relación de imagen y mensaje. Usa el criterio de la biblioteca principal; no encadenes todas las bibliotecas en un mismo prompt.

La prioridad debe ser ejecutable. Si el sujeto protagoniza, su presentación, escala y separación tienen que sostenerlo. Si lidera la propuesta, la distribución y el peso de los apoyos tienen que permitir entenderla. No llames secundario a un elemento al que después asignas todos los recursos de atención.

Después de esa orientación, describe directamente la imagen final. El argumento explica la elección; las posiciones, escalas y tratamientos hacen que se ejecute. El generador puede resolver detalles de representación que no alteren ese diseño. No puede elegir otro reparto de masas o contenido por falta de instrucciones.

## Contenido necesario del encargo

| Control | Qué debe quedar claro |
| --- | --- |
| Propósito | Sujeto o proposición, público y función publicitaria pertinentes. |
| Argumento | Qué idea organiza la pieza y por qué la imagen o el mensaje la hacen visible. |
| Protagonismo | Posición, escala relativa, orientación y recorte del foco; tamaño, contraste y separación que subordinan los apoyos. |
| Medio y escena | Tratamiento, encuadre, perspectiva, contexto y acción; dirección y carácter de luz cuando corresponde. |
| Referencias | Archivos realmente suministrados, función de cada uno, atributos protegidos y cambios permitidos. |
| Diseño | Zonas y extensión de imagen y texto, alineaciones, espacios libres, superposiciones, color y soportes gráficos elegidos. |
| Copy | Cada literal seleccionado con ubicación, anchura o extensión, cortes pertinentes, rasgos tipográficos y peso relativo. Si no hay copy externo, indícalo. |

La tabla comprueba cobertura de los componentes presentes; no obliga a añadirlos ni a escribir un bloque por fila. La longitud depende de las decisiones necesarias. Una versión más corta solo sirve si permite reconstruir el mismo diseño; no elimines relaciones concretas por considerarlas exceso de detalle.

## Resolver sin sobreespecificar

Fija las relaciones que diferencian esta solución. Describir dónde se concentra la masa principal y dónde se lee el apoyo aporta más que exigir «buena jerarquía». Definir contacto y luz compartida aporta más que «integración perfecta». No reemplaces requisitos distintos por calificativos generales.

Usa instrucciones de colocación y tratamiento: qué ocupa cada zona, cuánto pesa respecto al resto, con qué se alinea y sobre qué fondo se lee. Elige los lados y proporciones según el encargo, no desde una plantilla universal. Si un bloque debe ir abajo, dilo; si va directamente sobre el fondo, describe ese tratamiento en lugar de dejar que la herramienta elija una cartela.

Formula primero la solución positiva: tipografía, contraste y espacio que destacan el texto. Añade una exclusión solo cuando protege esa decisión frente a una desviación relevante o responde a una petición expresa. «Sin brochazos» no especifica por sí solo cómo va compuesto el titular. No copies una lista anti-IA completa en todos los prompts.

Selecciona una dirección, sin menús de escenas o estilos incompatibles. Si hay una decisión material sin resolver, aclárala desde el contexto o pregunta por ella antes de inventarla. Mantén libres los detalles que no cambian intención, orden de atención o fidelidad.

No añadas componentes para demostrar que aplicaste una biblioteca. Si una instrucción solo repite otra con sinónimos, consolídala. Si añade un control diferente, consérvala aunque esté relacionado con otro. La fidelidad de una referencia, su cantidad de sujetos y su relación con el entorno no son una sola decisión.

## Distinguir el copy de la dirección

Escribe cada cadena externa una sola vez, como literal del arte, con su función y tratamiento. No la repitas en la descripción de escena ni confundas nombres de roles con palabras que deben dibujarse. Conserva unidades de sentido y saltos pertinentes.

Los textos integrados en objetos de referencia siguen formando parte de ellos. No se transcriben automáticamente como copy externo. Si la presentación del sujeto y su gráfica existente bastan, el encargo puede comunicar esa intención sin inventar slogans o beneficios.

No envíes TEXTO COMPLEMENTARIO ni descartes al generador, tampoco como ejemplos negativos. La herramienta no tiene que volver a editar el inventario original del brief. Tampoco debe completar la pieza con contenido comercial propio.

## Comprobar el traspaso

Lee el encargo por sí solo y reconstruye la pieza: localiza sujeto, bloques, escala relativa, recorrido, tratamiento y espacios libres sin consultar tu análisis. Compara esa reconstrucción con la previsualización elegida. Si todavía debes inventar dónde poner un elemento principal, qué texto conservar o cómo distinguir los niveles, completa el diseño antes de ejecutar. Si una salida opuesta a la dirección seguiría cumpliendo esas frases, identifica qué control falta o se contradice.

No confundas revisión textual con resultado visual. Esta lectura detecta un encargo insuficiente, pero no prueba que el generador lo seguirá. La salida requiere inspección contra esas mismas prioridades.

Antes de la primera generación, muestra la dirección visual resuelta, el copy seleccionado y este encargo completo como texto copiable, con las referencias previstas y los parámetros aplicables identificados por separado. Espera la aprobación de ese conjunto según `../SKILL.md`; no basta haber anunciado que vas a generar. Si el usuario ha pedido expresamente ejecución directa, aplica esa excepción sin ocultar el prompt salvo petición expresa de omitirlo.

El texto enviado en el campo de prompt de la herramienta debe coincidir con el mostrado. Completa la depuración y cualquier traducción antes de presentarlo; no añadas instrucciones ocultas después. Las referencias y parámetros documentados deben corresponder a los que realmente suministras. No afirmes conocer reescrituras internas del servicio de generación.

## Ejecución e iteración

Adjunta referencias que la herramienta pueda utilizar. Mencionar un archivo o un enlace inaccesible no equivale a suministrarlo. Si se trabaja con una imagen base, delimita la transformación en lugar de redescribirla con versiones contradictorias.

Inspecciona la salida y contrástala con la distribución y tratamiento enviados, además de con el objetivo. Para corregir, identifica el elemento afectado, el cambio visible requerido y las relaciones que se conservan. Usa la imagen generada como referencia de edición cuando la herramienta lo permita; adjunta también la referencia de identidad si se necesita recuperar fidelidad.

Cada intento debe tener su instrucción visible antes de la llamada, también las correcciones automáticas. Muestra el prompt completo utilizado en ese intento, no solo «voy a simplificarlo» ni un resumen del cambio. Si la herramienta recibe únicamente una instrucción de edición, muestra esa instrucción completa e identifica la imagen base. No reconstruyas a posteriori un supuesto prompt distinto del enviado.

Un error de texto no exige reinterpretar la campaña; un argumento fallido no se resuelve solo cambiando color o luz. Cada nueva salida vuelve a verificarse. Aplica el límite de correcciones y la gestión de impedimentos definidos en `SKILL.md`. Si se necesitan exactitud tipográfica o conservación de imagen que el generador no consigue, utiliza composición o maquetación cuando las herramientas disponibles permitan ejecutarlas y su uso esté autorizado.
