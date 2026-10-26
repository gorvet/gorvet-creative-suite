# Traducir las decisiones a un encargo ejecutable

La herramienta recibe una especificación del resultado, no comparte el razonamiento del diseñador ni lee automáticamente estas bibliotecas. Resuelve antes de redactar. No envíes «analiza el producto y crea un concepto apropiado» cuando el skill todavía no ha elegido el concepto.

## Orden y cobertura del encargo

Organiza las instrucciones para que la herramienta entienda el conjunto y sus relaciones. Esta estructura admite bloques independientes; no es una cuota de palabras ni obliga a rellenar controles irrelevantes.

| Componente | Decisiones que deben llegar resueltas |
| --- | --- |
| Pieza y argumento | Formato, uso y relación visual que comunica la propuesta. |
| Sujeto y referencias | Qué aparece, qué hace o cómo se presenta, y qué archivo gobierna cada aspecto. |
| Escena y tratamiento | Encuadre, escala, entorno, luz, materiales y acabado pertinentes al medio. |
| Layout y recorrido | Qué se reconoce primero, dónde continúa la lectura y dónde se consulta la información práctica. |
| Copy literal y tratamiento | Cada cadena visible una vez, con su posición, escala relativa, alineación y voz tipográfica. |
| Fidelidad y exclusiones específicas | Atributos protegidos o cambios permitidos que no quedaron fijados en los componentes anteriores. |

Empieza por lo que organiza la pieza. Describe afirmativamente lo que debe existir; usa exclusiones para requisitos distintos o fallos concretos, no como sustituto de una dirección. Un inventario de cosas prohibidas deja abierta la solución.

## Concretar la imagen

Fija una escena y un encuadre, no «estudio o arquitectura, cálido o cinematográfico». La dirección del sujeto debe especificar los controles relevantes de SUBJECT_ART_DIRECTION.md. Para producto, los detalles que identifican el objeto y su presencia física. Para personas, papel, identidad si hay referencia, conducta, expresión y encuadre. En uso de producto, añade escala y contacto entre ambos.

Describe luz y materiales cuando afecten al resultado. «Luz difusa lateral que conserva la textura de piel y genera una sombra suave en el lado opuesto» aporta un control distinto de «fotografía de alta calidad». No repitas la misma decisión como sinónimos o como un resumen final.

Si se conserva una foto original, delimita qué zona o atributo puede transformarse. Adjunta las referencias pertinentes mediante la herramienta: un archivo mencionado pero no suministrado, un enlace inaccesible o una ficha Markdown no equivalen a una referencia visual.

## Concretar jerarquía y composición

Vincula el orden de atención con posiciones y pesos observables. «Título dominante» requiere especificar masa y relación con la imagen; «datos secundarios», una ubicación y un tratamiento legible. Define qué bordes comparten los bloques y qué área del encuadre permite leerlos. Evita pedir al generador que «encuentre el mejor layout» después de haber elegido la dirección.

Incluye suficiente relación de escala para distinguir las funciones sin imponer coordenadas que la herramienta no puede cumplir. Si el rostro ocupa casi todo el formato, no describas también un titular de varias líneas a gran escala en ese mismo espacio. Resuelve el conflicto moviendo, recortando o redimensionando antes de ejecutar.

Precio, marca o llamada a la acción pueden dominar si ese es el objetivo. Si se eligieron como secundarios, no les asignes después colores, soportes o efectos que los conviertan en entradas rivales. La palabra «secundario» no compensa una instrucción visual contradictoria.

## Transferir el criterio a controles visibles

Antes de cerrar el encargo, contrasta internamente el plano de arte con las instrucciones. Para cada decisión relevante, identifica una instrucción que la haga ejecutable y el resultado que debería poder observarse. No muestres esa matriz salvo petición ni la añadas completa al prompt: su función es detectar pérdida de diseño durante el traspaso.

| Decisión interna | Traspaso insuficiente | Control que sí transfiere la decisión |
| --- | --- | --- |
| El tema del taller introduce la lectura antes que la ponente. | «Jerarquía clara, retrato y título protagonistas». | Titular en un bloque de mayor masa tipográfica a la izquierda; retrato contenido en el área derecha sin invadirlo; nombre junto al retrato con peso menor que el titular. |
| La mano demuestra el uso sin ocultar el producto. | «Persona natural usando el producto, mantener fidelidad». | Fijar qué mano lo sostiene, el punto de agarre, la cara visible del objeto y el encuadre que incluye el contacto. |
| La condición se entiende al leer el precio. | «Precio destacado y condición legible». | Condición inmediatamente debajo del precio, en el mismo grupo y sobre fondo tranquilo; el espacio la vincula al precio y la separa del contacto. |
| El acabado mate sigue siendo reconocible. | «Iluminación profesional, materiales realistas». | Luz amplia lateral con reflejo suave y contenido, textura visible y sombras que revelan el volumen sin convertir la superficie en metal pulido. |

Los controles se adaptan a la solución elegida; no copies el contenido de la tabla a todos los encargos. Observa que cada relación se expresa con elementos y posiciones, no con una explicación de por qué sería buena.

Delimita también lo que podría deshacer el diseño: qué zona queda disponible para el texto, qué rasgo debe mantenerse visible y qué elementos comparten un grupo. Si un titular largo entra en conflicto con el rostro, resuelve el ancho, el recorte o la distribución antes de enviar el encargo. No delegues la solución con «ajusta lo necesario sin perder calidad».

### Prueba de lectura aislada

Lee únicamente el encargo final. Intenta reconstruir sujeto, escena, distribución de masas y recorrido usando solo sus frases. Pregúntate qué resultado distinto seguiría cumpliéndolas: por ejemplo, una foto que llena todo el formato y comprime los textos abajo, o un precio que domina pese a estar llamado secundario. Si ese resultado contradice la dirección, falta un control o existe una contradicción. Corrige eso, no añadas más énfasis general.

No hace falta eliminar toda libertad de ejecución: conserva la variación que no altera el concepto, las relaciones de composición o la fidelidad. La prueba revisa la suficiencia del traspaso, no garantiza obediencia del generador. El resultado todavía requiere inspección.

## Copy cerrado con tratamiento

Enumera cada texto literal una sola vez y acompáñalo de su función y tratamiento. Los nombres de roles son instrucciones y no deben dibujarse. No repitas las cadenas en la descripción de escena. Si necesitas fijar saltos de línea, indícalos en esa misma entrada, conservando el literal y sus unidades de sentido.

No inventes un slogan para completar la estructura ni añadas datos por convención publicitaria. Incluye precio y condición como unidades relacionadas cuando hagan falta. No envíes TEXTO COMPLEMENTARIO o descartes, tampoco como ejemplos de lo que no debe aparecer.

Si el generador falla repetidamente con tipografía exacta y las herramientas disponibles permiten componer el texto aparte, conserva una imagen base adecuada y aplica el copy mediante maquetación. Utiliza ese recurso solo si puedes ejecutarlo; no entregues una imagen sin textos como si fuera el cartel terminado.

## Depuración sin pérdida de diseño

Aplica la referencia opcional de optimización después de cerrar las decisiones. Elimina repeticiones, adjetivos sin control y explicaciones de intención ya expresadas visualmente. Conserva requisitos independientes: identidad, cantidad de personas, acción y zona de texto no son duplicados. Tampoco son equivalentes una luz coherente y una sombra de contacto.

Un párrafo sirve si mantiene claras las relaciones. Separa escena, composición y textos cuando esa organización evita confusiones. No comprimas todos los controles hasta obtener «persona fiel, fondo apropiado, tipografía premium». La longitud la determina la especificación necesaria, no una preferencia por prompts cortos o extensos.

## Revisión previa y traspaso

Reconstruye mentalmente la pieza desde el encargo sin acudir al brief: debe permitir saber qué aparece, dónde, con qué papel y qué se lee. Comprueba cobertura de las decisiones de contenido, sujeto, concepto, escena y layout. Si quedan alternativas, falta zona de lectura o hay contradicciones de peso, corrige antes de generar.

Si al depurar desapareció una relación que distinguía la solución, restáurala. Una versión más corta que permite un diseño diferente no es una optimización equivalente.

Aplica la revisión previa de ANTI_AI_STYLE_QA.md. La llamada a la herramienta debe recibir el encargo depurado y las referencias necesarias, sin notas internas, razonamientos o contenido de otros destinos.

Después, una corrección debe señalar el fallo observable y el cambio que lo resuelve, conservando lo logrado. No reescribas toda la campaña por una palabra incorrecta. Si falla el argumento o la distribución completa, vuelve al paso correspondiente del skill antes de generar otra versión.
