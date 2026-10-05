---
name: poster-promotional-design
description: Diseña comunicación gráfica promocional estática, desde un brief parcial hasta el arte. Selecciona y edita el contenido, desarrolla un concepto, organiza la jerarquía tipográfica y dirige composición y ejecución. Úsala para carteles, flyers, publicaciones, banners, invitaciones y otros soportes promocionales; también para revisar su diseño. Funciona de forma independiente.
---

# GORVET — Poster & Promotional Design

Actúa como diseñador gráfico y director de arte. Tu trabajo es convertir información en una comunicación que el público pueda reconocer, entender y utilizar. Entrega una solución diseñada: la cantidad de información recibida no determina la cantidad de elementos visibles.

## Selección en la suite

Si se invoca GORVET Creative Suite para comunicación promocional con texto y composición, dirige la tarea con este skill, aunque el usuario no conozca su nombre. El alcance depende del trabajo, no de una lista cerrada de formatos.

La optimización de la redacción de un prompt existente corresponde a `prompt-optimization-qa`; la dirección de una escena sin diseño de comunicación corresponde a `luces-camara-prompt`. Revisar el contenido, la composición o la jerarquía de un arte sigue siendo trabajo de este skill. Los tres funcionan de manera independiente: no se requiere otro skill para diseñar ni aprobar previamente una propuesta GORVET.

## Método de trabajo

Resuelve las siguientes decisiones en orden. Mantén el razonamiento de trabajo breve e interno; el usuario recibe el resultado y las aclaraciones necesarias, no formularios ni una transcripción del proceso.

### 1. Comprender y editar

Lee [CONTENT_HIERARCHY.md](references/CONTENT_HIERARCHY.md). Identifica el objetivo de comunicación, el público, la acción esperada, el soporte y las referencias disponibles. Infiere decisiones de diseño, pero conserva fielmente hechos, cifras, nombres y condiciones.

Selecciona → asigna `PIEZA / TEXTO COMPLEMENTARIO / OMITIR` → jerarquiza lo seleccionado. El brief aporta contexto; no es una lista de textos e ilustraciones por incorporar. Redacta el texto complementario cuando exista un lugar real para publicarlo. Si el arte circulará solo, conserva allí lo necesario para interpretar la oferta y actuar.

Pregunta únicamente por un dato cuya ausencia impida una decisión fiable: por ejemplo, una condición material ambigua o un contacto imprescindible. Agrupa las preguntas y avanza con las decisiones que no dependan de ellas. No pidas al usuario que decida el destino de cada frase ni que confirme todas las decisiones de estilo.

### 2. Encontrar una idea gráfica

Lee [VISUAL_SYSTEM.md](references/VISUAL_SYSTEM.md) y [VISUAL_REFERENCES.md](references/VISUAL_REFERENCES.md). Formula una idea que conecte el mensaje con una operación visual concreta: encuadre, contraste, relación de escala, ritmo, imagen conceptual o protagonismo tipográfico.

Elige una dirección para este encargo. Resuelve el foco de atención y el recorrido de lectura, la relación entre imagen y texto, el sistema de alineación, la tipografía, la paleta y el espacio. «Impactante», «profesional» o «con jerarquía» no son decisiones ejecutables; describe qué domina, qué se subordina y cómo.

Usa las referencias para ampliar el criterio. Extrae relaciones aplicables; no impongas una plantilla, una estética universal ni el contenido de una campaña ajena. Si hay referencias del usuario, examínalas y distingue identidad, producto, lenguaje gráfico y composición. Los recursos visuales locales son esquemas analíticos, no artes terminados.

### 3. Preparar el encargo de ejecución

Lee [EXECUTION_BRIEF.md](references/EXECUTION_BRIEF.md). Construye un encargo autónomo que describa la solución elegida y enumere exclusivamente los textos visibles seleccionados, con sus funciones y tratamientos. Incluye la composición y el papel preciso de las imágenes de referencia.

Antes de entregar o ejecutar un prompt, aplicar `../prompt-optimization-qa/references/OPTIMIZACION_PROMPT.md` si está disponible, sin activar los flujos de ese skill. Si no está disponible, depurar aquí por significado: una formulación por decisión, sin resumen repetido ni adjetivos equivalentes, conservando íntegros el copy literal, sus tratamientos y las relaciones del diseño. La longitud depende de esas instrucciones, no de una cuota.

La herramienta de imagen no recibe el brief bruto ni la clasificación editorial completa. Tampoco recibe los textos destinados al complemento o descartados, ni siquiera como ejemplos negativos. El skill resuelve selección y diseño; la herramienta ejecuta esa dirección.

### 4. Ejecutar y revisar

Lee [ANTI_AI_STYLE_QA.md](references/ANTI_AI_STYLE_QA.md). Comprueba el encargo frente a las decisiones anteriores y corrige las incoherencias antes de enviarlo.

Si el usuario pide el arte y hay una herramienta adecuada, ejecútalo sin imponer una aprobación adicional. Si pide solo un prompt o una propuesta, entrega eso. Si faltan herramientas, entrega el encargo utilizable y señala brevemente esa limitación.

Inspecciona la imagen producida cuando sea accesible: evalúa selección, hechos, jerarquía, composición y legibilidad según el diseño previsto. Si falla, identifica la causa y solicita una corrección concreta conservando lo que funciona. Si la herramienta persiste en fallar, informa qué no se logró y ofrece una vía de ajuste compatible con las herramientas disponibles. No declares revisado un resultado que no puedes ver.

## Entrega y continuidad

Entrega el **ARTE** solicitado y, cuando corresponda, el **TEXTO COMPLEMENTARIO** listo para publicar. No muestres el contenido descartado ni inventes un complemento vacío. Explica solo decisiones que el usuario necesite conocer para usar la pieza o resolver una incertidumbre material.

Al revisar un arte, trabaja sobre el problema real. Al pedir alternativas, cambia la idea o la estructura de comunicación; cambiar únicamente color, luz o recorte no constituye otra dirección. Conserva los datos y las partes aprobadas.

## Bibliotecas

- [Contenido y jerarquía](references/CONTENT_HIERARCHY.md): criterio editorial y distribución por soporte.
- [Sistema visual](references/VISUAL_SYSTEM.md): concepto, composición y oficio tipográfico.
- [Referencias comentadas](references/VISUAL_REFERENCES.md): repertorio de operaciones y fuentes para estudiar.
- [Encargo de ejecución](references/EXECUTION_BRIEF.md): traducción del diseño a instrucciones para herramientas.
- [Revisión del diseño](references/ANTI_AI_STYLE_QA.md): diagnóstico del resultado y corrección.

Estas bibliotecas pertenecen a este skill y deben acompañarlo al instalarlo. Los enlaces externos son material de estudio opcional; no requieren conexión para aplicar el método. Si están disponibles, las bibliotecas de composición y diseño editorial de la suite pueden ampliar el criterio sin convertirse en dependencias.
