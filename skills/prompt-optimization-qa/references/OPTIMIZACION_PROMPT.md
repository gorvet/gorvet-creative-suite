# OPTIMIZACIÓN DEL PROMPT

Aplicar a cualquier tema en la construcción y reparación de prompts. El objetivo es el texto mínimo suficiente para ejecutar todas las decisiones del encargo, no una longitud fija. Esta revisión es interna y no añade fases, explicaciones ni bloques a la entrega.

## Redacción y depuración

1. Extraer las decisiones del encargo y de la dirección aprobada: sujeto y selección, acción, entorno, composición, acabado, luz y restricciones. Un ejemplo ilustra decisiones; no obliga a copiar su plantilla ni su redacción.
2. Asignar una formulación a cada decisión. Integrar atributos compatibles en una misma frase. No crear un bloque narrativo, otro técnico y un resumen que describan de nuevo la misma escena.
3. Comparar las frases por significado, no solo por palabras. Si dos protegen el mismo atributo o describen el mismo acabado, conservar una. Mantener requisitos diferentes aunque estén relacionados: identidad, cantidad de personas y exclusión de figuras adicionales cumplen funciones distintas.
4. Eliminar énfasis sin control visual nuevo, cadenas de adjetivos equivalentes, explicaciones del efecto emocional y reafirmaciones finales. No rematar el prompt con un resumen de su estilo, luz, composición o elementos ya descritos.
5. Resolver alternativas abiertas antes de redactar la versión final. La dirección puede proponer casa o castillo; el prompt aprobado fija uno. No usar «mismo ángulo» o «misma posición» sin un referente definido.
6. Comprobar cobertura: todas las decisiones distintas siguen presentes, ninguna se contradice y cada frase añade un cambio observable o una restricción útil. Si al quitar una frase no se pierde ninguno de esos controles, quitarla.
7. Traducir solo la versión depurada. Cada idioma contiene las mismas decisiones una sola vez y usa términos naturales en ese idioma. Las etiquetas exigidas por el usuario o una integración pueden conservarse; no inferir esa exigencia por verlas en un ejemplo.

Por defecto, un párrafo. Separar bloques cuando organizan controles independientes, referencias diferentes, zonas de edición o una plantilla expresamente solicitada. La separación no permite repetir decisiones.

## Compresión de la redacción y control de expansión

Eliminar duplicados no basta. Usar frases directas y compactas: «cheerful expressions» puede resolver una dirección alegre sin añadir «happy, celebratory, full of life, as if enjoying a party». Preferir una condición ejecutable a explicarla y después negar su opuesto: «fangs visible only in naturally open mouths» ya excluye los colmillos con la boca cerrada.

Separar requisitos del usuario y decisiones aprobadas de desarrollos opcionales del asistente. Preservar los primeros; eliminar los segundos cuando no resuelvan una ambigüedad necesaria. «Vestuario vampírico elegante en negro y burdeos» no necesita expandirse en una lista de chaquetas, cuellos, camisas, vestidos, cinco colores y adjetivos textiles si esos detalles no fueron pedidos ni aprobados. Si se necesita una prenda concreta, elegirla en vez de enumerar alternativas.

Cuando el usuario aporte un ejemplo breve como referencia de densidad, aproximarse a su concisión. Crecer solo por requisitos distintos añadidos al encargo, no por explicaciones o énfasis. No copiar sus redundancias ni imponer su longitud a tareas diferentes.

Revisar cada frase restante: ¿puede expresar el mismo control con menos palabras? Compactarla sin sustituir una condición precisa por un adjetivo vago. No ampliar de nuevo el texto al traducir o al realizar la revisión final.

## Personas y referencias

Consolidar la conservación de identidad en una instrucción que cubra los atributos protegidos. No encadenar «mismo rostro», «no alterar facciones», «no reinterpretar», «apariencia reconocible» y otras equivalencias. Añadir una prohibición específica solo si corrige un fallo diferente o es un requisito expreso.

Conservar la cantidad exacta cuando deban aparecer todas las personas de la referencia; si se solicita una selección, delimitarla. Excluir personas adicionales cuando corresponda. No confundir estas restricciones con repetir identidad.

Describir la transformación mediante los cambios permitidos: vestuario, maquillaje y accesorios. Separar esos cambios de los atributos protegidos. No repetir la protección del rostro en el bloque de caracterización.

Si dos condiciones de vestuario solo repiten un tratamiento común, describir ese tratamiento una vez. Mantener condiciones que aporten diferencias reales o que el usuario exija como plantilla.

## Fondos de series

Para fondos próximos entre generaciones, fijar anclas concretas en la dirección creativa: tipo de construcción, posición en el encuadre, ubicación de luna y decoración, punto de vista, paleta y luz. Describir cada ancla una sola vez por prompt autónomo. No añadir después otra lista para exigir que todo «se mantenga igual».

Si existe una imagen base del escenario, indicar que gobierna fondo, geometría y distribución; delimitar por separado la referencia de identidad. Si no existe, usar una descripción espacial fija como base de la serie. Explicar la limitación del texto solo cuando el usuario pida garantías de continuidad exacta; no prometer que repetir palabras produce fondos idénticos.

## Ejemplos de depuración por significado

- «Conservar identidad y facciones. Mantener el mismo rostro. No reinterpretar su estructura facial» → una instrucción de conservación de identidad y facciones.
- «Estilo cinematográfico, elegante y oscuro» seguido de «fotografía premium, sofisticada, de vampiro clásico, elegante y oscura» → un acabado dominante y los atributos distintos que realmente definen vestuario o escena.
- Una descripción de castillo, luna, calabazas y niebla seguida de la misma lista bajo «mantener constantes» → una única descripción con posiciones y anclas concretas.
- Dos condiciones de vestuario equivalentes → una descripción común, salvo que el formato condicional sea un requisito expreso.

Los ejemplos muestran operaciones de edición; no son frases que deban añadirse a todos los prompts.
