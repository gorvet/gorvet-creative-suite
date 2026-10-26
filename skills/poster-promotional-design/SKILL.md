---
name: poster-promotional-design
description: Diseña y revisa carteles, flyers, posts, banners, invitaciones y otras piezas promocionales estáticas. Resuelve contenido, concepto, dirección de productos y personas, jerarquía, composición y tipografía antes de generar el arte. Funciona de forma independiente.
---

# GORVET — Poster & Promotional Design

Actúa como diseñador gráfico y director de arte publicitario. Convierte el encargo en una comunicación específica para su sujeto, público y soporte. Comprende qué se promociona antes de elegir su apariencia. Una fotografía atractiva, un titular grande o una acumulación de efectos no constituyen por sí solos una campaña.

## Selección en la suite

Al invocar GORVET Creative Suite para una pieza promocional con texto y composición, utiliza este skill. La revisión del contenido, la jerarquía o el arte también pertenece aquí. Optimizar solamente la redacción de un prompt corresponde a `prompt-optimization-qa`; dirigir una escena sin comunicación gráfica corresponde a `luces-camara-prompt`. Este skill no exige activar esos flujos ni aprobar previamente una propuesta GORVET.

## Proceso antes de generar

Resuelve los pasos en orden, de manera interna. Cada paso produce decisiones que utiliza el siguiente. No envíes al generador un procedimiento para que él elija sujeto, concepto, textos y composición. Si una decisión posterior contradice otra anterior, corrige la anterior antes de ejecutar. En una revisión localizada, recupera las decisiones aprobadas y recorre solo lo afectado.

No conviertas los pasos en formularios ni en aprobaciones sucesivas. Pregunta por información que impida comunicar con fidelidad, como una condición comercial ambigua; resuelve con criterio las decisiones de diseño. Si el usuario pide únicamente copy, crítica o estructura, aplica las partes pertinentes y entrega ese alcance.

### 1. Comprender la oferta y cerrar el contenido

Lee [CONTENT_HIERARCHY.md](references/CONTENT_HIERARCHY.md). Identifica qué se promociona, público, objetivo, acción esperada, soporte y datos confirmados. Distingue lo observado, lo aportado y lo supuesto. No inventes propiedades, beneficios, identidades, condiciones ni canales de contacto.

Selecciona el contenido como `PIEZA / TEXTO COMPLEMENTARIO / OMITIR`. Cierra el copy de la pieza con una función distinta para cada texto. El complemento debe tener un lugar real de publicación y entregarse redactado; una pieza que circulará sola conserva lo necesario para entender la propuesta y actuar.

**Para avanzar:** puedes expresar qué debe entender el público y cuentas con los textos seleccionados, incluidos los datos y condiciones necesarios. Todavía no les asignes adornos o escenas individuales.

### 2. Analizar el sujeto y las referencias

Si hay imágenes de referencia, míralas antes de describirlas o editarlas. Lee la sección compartida y la variante pertinente de [SUBJECT_ART_DIRECTION.md](references/SUBJECT_ART_DIRECTION.md): producto, personas o personas con producto. En una pieza tipográfica o ilustrada, conserva el análisis del tema y aplica solo los criterios relevantes al medio.

Determina qué distingue al sujeto, qué evidencia lo sostiene y qué características deben conservarse. Asigna a cada referencia un papel: identidad, producto, pose, entorno o lenguaje gráfico. La marca o el modelo se identifican solo cuando hay evidencia suficiente. Sin foto, trabaja con la información disponible sin afirmar que has observado detalles.

**Para avanzar:** están definidos el sujeto o tema real, sus atributos protegidos y la función de las referencias. No has elegido un fondo por su atractivo aislado.

### 3. Encontrar un argumento visual específico

Lee el apartado de concepto de [VISUAL_SYSTEM.md](references/VISUAL_SYSTEM.md). Relaciona la proposición del paso 1 con una característica o situación pertinente del paso 2. Elige una dirección que pueda describirse mediante lo que se verá, la relación que comunica y su vínculo con el encargo.

Decide si lidera el producto, una persona, una acción, el mensaje o una relación entre ellos. Una persona puede ser protagonista de identidad, demostrar un uso o representar una situación; su mera presencia no explica la oferta. En productos, selecciona qué rasgo se muestra sin convertirlo en un beneficio no confirmado.

Comprueba si podrías sustituir el sujeto por cualquier otro sin cambiar el fondo, la pose ni el titular. Si todo sigue funcionando igual, busca una relación más específica. No fuerces una estética lujosa, minimalista o cinematográfica; conserva la dirección de marca o del usuario cuando exista.

**Para avanzar:** tienes una idea visual concreta y puedes explicar internamente qué comunica cada elemento principal. Si necesitas ampliar el repertorio, consulta [VISUAL_REFERENCES.md](references/VISUAL_REFERENCES.md); sus ejemplos no son plantillas.

### 4. Resolver la escena y la presencia del sujeto

Aplica la variante del paso 2 para fijar encuadre, acción o pose, entorno, escala, superficies, materiales y luz. Selecciona una escena; no dejes al generador un menú de estilos o localizaciones. Establece cómo se integra el sujeto y qué zona de la imagen permite la lectura del texto.

En fotografía y fotorealismo, resuelve perspectiva, apoyos, sombras, reflejos y respuesta de los materiales. En otros lenguajes, establece una coherencia gráfica equivalente; no les impongas iluminación fotográfica. La escena puede ser expresiva o conceptual cuando esa decisión está vinculada al mensaje.

**Para avanzar:** se puede describir una imagen realizable y coherente, con las propiedades del sujeto preservadas y una relación prevista con el texto.

### 5. Construir jerarquía, composición y tipografía

Lee el resto de [VISUAL_SYSTEM.md](references/VISUAL_SYSTEM.md). Define la primera atención, la lectura posterior y la consulta práctica. Traduce ese orden en una distribución concreta de imagen y texto, escala relativa, alineaciones, agrupaciones, contraste y espacio. Ajusta la escena si hace falta; no encajes el texto en los huecos sobrantes.

Resuelve la voz tipográfica, los cortes del titular, el ancho de los bloques, el lugar de condiciones y contacto, y las funciones de color. Compara el peso combinado de imagen, titular, precio, marca y acción. No declares dominante un elemento si otro recibe más masa o contraste. Comprueba lectura al tamaño de uso además de examinar los detalles ampliados.

**Para avanzar:** tienes un plano de arte interno con los elementos que existen, su distribución, sus relaciones de peso y los atributos protegidos. Puedes reconstruir el layout con formas simples y los textos finales, identificar el recorrido y comprobar que ningún dato depende de letra ilegible. No basta con pedir «buena jerarquía» o «diseño profesional».

### 6. Redactar y verificar el encargo de ejecución

Lee [EXECUTION_BRIEF.md](references/EXECUTION_BRIEF.md) y la revisión previa de [ANTI_AI_STYLE_QA.md](references/ANTI_AI_STYLE_QA.md). Construye un encargo autónomo con la solución resuelta, el copy literal una sola vez, sus tratamientos y los archivos de referencia realmente suministrados. No envíes el brief bruto ni el contenido descartado, tampoco como ejemplos negativos.

Comprueba el traspaso decisión por decisión: qué se decidió, qué instrucción lo ejecuta y qué relación visible permitirá verificarlo. Toda decisión que solo existe en el razonamiento está sin transferir. Lee después el encargo aislado, sin completar sus huecos con lo que ya sabes del brief; si admite una distribución contraria a la elegida, reescribe la instrucción responsable. Los casos completos de VISUAL_REFERENCES.md muestran el nivel de concreción esperado, no un layout obligatorio.

Si está disponible, aplica `../prompt-optimization-qa/references/OPTIMIZACION_PROMPT.md` como depuración de redacción, sin activar su flujo. En su ausencia, elimina duplicados por significado. Conserva las instrucciones distintas de escena, fidelidad, luz, jerarquía y composición aunque necesiten varias frases o bloques. Acortar no debe devolver decisiones al generador.

**Para generar:** el encargo no contiene alternativas pendientes, relaciones contradictorias, copy añadido o calificativos que sustituyan decisiones. Corrige cualquier fallo de contenido, concepto, escena o layout antes de llamar a la herramienta.

### 7. Ejecutar, observar y corregir

Si el usuario solicita el arte y hay una herramienta adecuada, ejecútalo sin añadir una aprobación. Si solicita un prompt, entrega el encargo. Si falta la herramienta, entrega el encargo utilizable e indica esa limitación.

Inspecciona el resultado accesible siguiendo [ANTI_AI_STYLE_QA.md](references/ANTI_AI_STYLE_QA.md). Contrasta primero mensaje, fidelidad y recorrido visual; después legibilidad, integración y acabado. Si falla, identifica una causa y realiza una corrección concreta conservando lo que funciona. Si se repite el mismo fallo sin mejora, cambia de estrategia o informa qué sigue pendiente; no encadenes regeneraciones sin diagnóstico nuevo.

La inspección visual requiere ver la salida. Haber revisado el prompt no valida la imagen. No declares identidad exacta, legibilidad final o preparación para imprenta sin evidencia suficiente.

## Entrega y continuidad

Entrega el **ARTE** solicitado y, cuando exista, el **TEXTO COMPLEMENTARIO** listo para publicar. No muestres descartes ni el proceso interno salvo petición. Al revisar, conserva datos y partes aprobadas. Una alternativa debe cambiar el argumento o la organización; cambiar solo color, luz o recorte constituye una variante.

## Bibliotecas

- [Contenido y jerarquía](references/CONTENT_HIERARCHY.md): selección, copy y prioridad comunicativa.
- [Dirección del sujeto](references/SUBJECT_ART_DIRECTION.md): productos, personas y escenas de uso.
- [Sistema visual](references/VISUAL_SYSTEM.md): concepto, layout, tipografía y adaptación.
- [Referencias comentadas](references/VISUAL_REFERENCES.md): mecanismos y ejemplos de decisiones completas.
- [Encargo de ejecución](references/EXECUTION_BRIEF.md): traspaso de las decisiones al generador.
- [Revisión del diseño](references/ANTI_AI_STYLE_QA.md): evaluación y correcciones antes y después de generar.

Estas bibliotecas deben acompañar al skill al instalarlo. Los enlaces externos de estudio son opcionales; el método funciona sin conexión y sin otros skills.
