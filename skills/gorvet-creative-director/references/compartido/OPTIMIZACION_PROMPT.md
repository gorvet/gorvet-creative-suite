# Optimización del prompt

El objetivo es la especificación mínima suficiente para ejecutar las decisiones del encargo. Una reducción de palabras no sirve si borra una relación de composición, una condición de edición o un rasgo protegido. Tampoco sirve cambiar sinónimos conservando las mismas repeticiones. Aplica esta revisión internamente antes de entregar; no crea otra fase de aprobación.

## 1. Extraer controles antes de reescribir

Identifica las decisiones existentes y las modificaciones autorizadas: sujeto y selección, acción, ubicación, referencias, atributos protegidos, cambios permitidos, composición, estilo, luz, materiales y restricciones pertinentes. No añadas un campo porque aparezca en esta enumeración.

Distingue su procedencia. Lo pedido por el usuario y lo aprobado se conserva; un desarrollo opcional del asistente puede retirarse si no resuelve una necesidad del encargo. Si no hay contexto que permita distinguirlos, conserva las decisiones concretas del prompt original. No supongas que un detalle específico es relleno por ser largo o poco habitual.

Una exigencia literal de formato o texto permanece literal. Una instrucción visual puede compactarse conservando todo su alcance. Los ejemplos muestran operaciones de edición; no son frases que debas añadir al prompt actual.

## 2. Consolidar por significado y alcance

Busca instrucciones equivalentes aunque cambien palabras o estén en apartados distintos. Incluye también equivalencias entre afirmación y negación, título y cuerpo, escena y bloque técnico, apertura y resumen final.

| Caso | Operación |
| --- | --- |
| Dos frases protegen el mismo rasgo con igual alcance. | Conservar la formulación más precisa, salvo repetición literal expresamente exigida. |
| Una frase repite un rasgo y añade una condición distinta. | Integrar la condición nueva en la formulación conservada. |
| Varias expresiones describen el mismo efecto técnico. | Elegir el control suficiente para la herramienta y la dirección solicitadas. |
| Dos instrucciones se parecen pero gobiernan aspectos distintos. | Conservar ambas, compactándolas si comparten una frase sin perder alcance. |
| Dos instrucciones se contradicen. | Aplicar una corrección o prioridad explícita del usuario; si falta y afecta a la imagen, preguntar sin inventar una resolución. |

Identidad, cantidad de personas, selección y exclusión de figuras adicionales pueden ser requisitos distintos: no reducirlos a «mantener la referencia». Tampoco son equivalentes conservar geometría, proteger marca y fijar el agarre de una mano.

No acumules dos controles equivalentes por supuesto refuerzo. Si la herramienta falló, la corrección sustituye la formulación insuficiente; no se añade como un eco. Una repetición técnica exigida por una integración específica se conserva solo cuando ese contrato se haya aportado.

## 3. Revisar el aporte de cada cláusula

Para cada fragmento, comprueba qué cambiaría si desapareciera. Conserva el que fija una decisión o restricción necesaria. Retira el que solo vuelve a nombrar el efecto ya definido, explica su intención al lector o enfatiza calidad sin control nuevo. Hazlo dentro de las frases, no solo entre párrafos.

- «Expresión alegre, feliz, llena de alegría» puede resolverse como «expresión alegre».
- «Luz suave lateral de ventana que ilumina desde un costado» conserva fuente y dirección como «luz suave de ventana desde la izquierda» solo si ese lado ya estaba decidido; si no lo estaba, no lo inventes al optimizar.
- «Poros naturales, textura de piel realista, piel sin apariencia plástica» se consolida en una instrucción de textura cuando las tres cumplen el mismo propósito. Un requisito independiente de tono de piel debe conservarse.
- «Fondo desenfocado, bokeh suave, poca profundidad de campo» puede expresar un solo control de profundidad. «Ojos enfocados y manos legibles» añade una condición de foco distinta y no debe desaparecer.
- «Cada elemento cuenta una historia y crea una experiencia visual inolvidable» se elimina si no añade una decisión visual solicitada.

Un tono como melancólico, lúdico o solemne puede ser una intención real; no lo elimines por ser abstracto si no está expresado por otros controles equivalentes. Evita desarrollarlo después mediante explicaciones repetidas. No conviertas esta revisión en una prohibición general de adjetivos.

## 4. Contener la expansión del asistente

No amplíes una dirección breve mediante catálogos de prendas, materiales, accesorios, cámaras o efectos que nadie pidió o aprobó. Completa solamente una ambigüedad necesaria dentro del alcance autorizado. En una optimización, no rediseñes una escena cerrada para hacerla más cinematográfica.

Una indicación de vestuario elegante en negro y burdeos no exige inventar chaqueta, chaleco, cuello, bordados, joyas y cinco texturas. Una dirección de luz no necesita siempre relleno, contraluz y partículas. Un retrato no exige por defecto lente de 85 mm, bokeh, poros y mirada a cámara.

Si un dato técnico fue solicitado, consérvalo. Si fue añadido como explicación del mismo efecto ya fijado y no aporta otro control, consolídalo. No elimines todos los números por sistema ni añadas números para que el texto parezca preciso.

## 5. Redactar desde la versión vigente

Reúne las decisiones finales y redacta una única versión. Cada control tiene un lugar; no construyas un bloque narrativo, otro técnico y un cierre que vuelvan a describir la misma imagen. Mantén las relaciones entre sujetos, zonas, apoyos, luz y texto que definen el resultado.

En una edición, sustituye la condición modificada donde corresponde y conserva las demás. Si se pide el prompt completo, entrega la versión consolidada; si se pide solo la frase de reemplazo, entrega esa unidad sin un segundo prompt de refuerzo.

Usa párrafos o bloques cuando separen instrucciones independientes, referencias, zonas de edición o copy literal. Su cantidad no demuestra optimización. No fuerces una frase única si vuelve ambiguo qué referencia o restricción gobierna cada elemento.

No finalices con un resumen de estilo, emoción, iluminación, fidelidad o composición ya fijados. El material de entrega ajeno al prompt, como una explicación solicitada o el cierre propio de otro playbook, queda fuera del texto destinado al generador.

## 6. Referencias y continuidad

Consolida la protección de identidad en una instrucción que cubra los atributos necesarios. Mantén por separado los cambios permitidos y las condiciones distintas de selección o cantidad. No extiendas una referencia facial a fondo, vestuario y pose por inercia.

En una serie, reutilizar una misma ancla entre prompts autónomos es necesario para que cada uno se entienda por sí solo. Repetir esa ancla dentro de un mismo prompt con sinónimos es redundante. Depura cada prompt individualmente y conserva la base común de la serie.

Para continuidad de fondo, usa una referencia de escenario realmente disponible o anclas espaciales concretas ya decididas: distribución, punto de vista, posición de elementos, paleta y luz. No añadas un segundo bloque que repita todo bajo «mantener constantes». Si el referente de «mismo ángulo» no está definido, identifícalo desde el contexto o señala lo que falta; no inventes el ángulo.

No prometas que repetir palabras produce fondos o rostros idénticos. Una revisión textual no valida continuidad visual.

## 7. Comparar cobertura y traducir sin expansión

Antes de entregar, contrasta la versión con las decisiones de origen en ambas direcciones:

- Cada requisito necesario sigue teniendo una instrucción suficiente, incluida su condición, referente y relación espacial cuando proceda.
- Cada instrucción de salida procede del encargo, la dirección aprobada o un cambio autorizado; no se añadió solo para llenar un apartado.
- No quedan formulaciones equivalentes, contradicciones ni un resumen que duplique controles.
- Se conservan copy literal, cifras, nombres, etiquetas y formato exigidos. El texto destinado a aparecer en la imagen no se traduce si debe conservarse literal.

Traduce después de cerrar esta versión. Compara decisiones, no número de palabras: un idioma puede necesitar más palabras sin añadir controles. No desarrolles una escena distinta al traducir ni vuelvas a expandirla en la revisión final. Cuando ya no haya un cambio que mejore precisión, cobertura o concisión, detente.

## Ejemplo completo de consolidación

**Contexto supuesto:** dos personas de una referencia deben conservar identidad y cantidad, con vestuario negro y burdeos; no se han aprobado accesorios concretos. Se solicita el prompt completo depurado.

**Antes:**

> Conserva la identidad de las dos personas de la imagen adjunta. Mantén sus mismos rostros y facciones reconocibles, sin reinterpretar sus rasgos. Ambas llevan vestuario elegante en negro y burdeos. Su ropa es refinada y sofisticada, con elegancia oscura. Están de pie ante un muro de piedra, miran a cámara y muestran expresiones alegres y felices. Luz lateral suave desde la izquierda, iluminación delicada y difusa que llega del lado izquierdo. Plano medio de las dos personas y fondo ligeramente desenfocado. No añadas otras personas. El resultado debe mantener sus rostros, una estética elegante, expresiones felices y una iluminación suave. Formato vertical 4:5.

**Después:**

> Plano medio de las dos personas de la imagen adjunta, conservando su identidad y facciones. Vestuario elegante en negro y burdeos; de pie ante un muro de piedra, mirando a cámara con expresión alegre. Luz lateral suave desde la izquierda y fondo ligeramente desenfocado. Sin personas adicionales. Formato vertical 4:5.

Se conservaron selección, cantidad, identidad, vestuario, pose, fondo, expresión, luz, plano, profundidad, exclusión y formato. Se retiraron equivalencias y el cierre repetido sin añadir cámara, prendas, accesorios ni otra localización. Esta comparación textual no prueba el comportamiento de un generador.
