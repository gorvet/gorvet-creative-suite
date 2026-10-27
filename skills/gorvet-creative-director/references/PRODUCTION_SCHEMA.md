# Paquete de producción 1.3

El registro conserva los campos de brief, dirección, autorización, ejecución y revisión de [AGENT_ARCHITECTURE.md](AGENT_ARCHITECTURE.md). El contrato 1.3 añade selección explícita, representación de diseño y revisión vinculada a su versión. Las versiones 1.1/1.2 se pueden consultar como historia, pero ya no autorizan producción con el verificador actual. No se migran inventando decisiones faltantes.

## Inventario y selección

`brief.content_items` es una lista de datos o textos candidatos, no cada palabra del mensaje. Cada entrada tiene `id`, `text`, `protected_literals` como lista opcional y `required_in_image` como booleano opcional. Usa esta última marca para exigencias reales de texto visible, no por el mero hecho de recibir información. Datos exclusivamente visuales se conservan en referencias y dirección; una imagen sin contenido textual puede usar lista vacía.

`direction.content_decisions` tiene una decisión por id del inventario: `destination: image|support|omit`, `reason` y `literals`. Solo el destino imagen contiene literales; los demás usan lista vacía. Apoyo añade `copy` y `support_destination` realmente viable. Un literal protegido debe sobrevivir en el texto seleccionado para imagen o apoyo; omitir un dato opcional no obliga a enviarlo al generador. La lista plana `direction.image_text` coincide, en orden, con los literales seleccionados. Un nuevo titular propuesto se identifica como propuesta dentro del inventario, sin atribuirlo al usuario ni inventar hechos.

Esta estructura asegura trazabilidad, no impone cuotas de palabras ni omisiones. La revisión editorial evalúa si mantenerlo todo responde al uso o evita decidir. El compilador no recibe la orden de adornar el brief bruto.

## Representación final

`direction.production_spec` contiene:

- `canvas`: formato y uso de la pieza, sin inventar parámetros de plataforma.
- `intent`: proposición visible de esta solución.
- `composition`: relación concreta de masas y recorrido; coincide con `direction.composition`.
- `treatment`: construcción de forma, color, superficie y luz pertinentes.
- `style_basis`: `origin: user|reference|proposal`, `evidence` y `reason`. Documenta por qué pertenece ese tratamiento al encargo. Su explicación no se copia al generador.
- `elements`: lista ordenada con `id` único, `kind: subject|background|text|graphic`, `instruction`, `placement` y `scale`. Un bloque de texto añade `literal` y define voz tipográfica, colocación y peso. Los literales de estos bloques coinciden exactamente y en orden con `image_text`.
- `graphic_devices`: ids de los elementos `graphic`, en el mismo orden. Lista vacía significa que no se eligieron recursos gráficos externos. Los recursos presentes se describen una vez en sus elementos; no se añaden brochas, emblemas o soportes por asociación con una etiqueta estética.
- `constraints`: controles de ejecución distintos que aún hagan falta; lista vacía si el diseño ya los expresa. No se rellenan con sinónimos de calidad.

El director integra esta representación desde las contribuciones: no rediseña durante la compilación. Arte, fotografía y gráfica conservan su autoridad sobre las decisiones que aportaron. Luces ensambla la versión cerrada; si QA textual descubre una redundancia, se corrige la cláusula de la representación y se recompila, sin modificar a escondidas el resultado final.

Los atributos `direction.protected_attributes`, si existen, son una lista de controles textuales ejecutables y se incorporan al prompt; no quedan solo en el análisis. El director integra en los elementos y tratamiento los controles materiales de captura, identidad, gráfica y demás contribuciones. La revisión de cobertura contrasta con esas fuentes: completar la estructura sin trasladar una decisión no es un aprobado. No se copian al generador historiales, inferencias de marca ni bibliotecas completas.

En vídeo se incluye el plan `direction.motion` ya resuelto y validado por su control temporal; cada llamada corresponde a su alcance real. En edición, el compilador utiliza el contrato `edit_scope` existente y los literales protegidos, sin exigir una nueva ideación. En correcciones añade la base, intervención visible y conservación de la dirección vigente.

## Revisión previa y autorización

`production_review` contiene `direction_fingerprint`, `prompt_fingerprint`, `blockers: []` y `checks`. En creación, las claves exactas son `selection`, `design`, `anti_ai`, `coverage`; en edición, `scope`, `preservation`, `coverage`. Cada control aporta `status: pass` y una lista `evidence` no vacía con decisiones verificadas. Un control pendiente o un bloqueo impide avanzar. No fabriques evidencia ni apruebes por rellenar el campo.

La huella de dirección procede de `check_handoff.py --fingerprints`; la del prompt, de `compile_production.py`. Cambiar contenido, diseño, prompt o fuentes exige repetir la revisión afectada sobre la versión actual. La autorización del usuario se obtiene después de presentar la propuesta; calcular hashes no genera consentimiento. La orden de producir directamente conserva los demás controles.

`check_handoff.py` compila de nuevo, compara el resultado con `execution.prompt` y comprueba la revisión vinculada. Después aplica autorización, coincidencia de versión publicada, fuentes y parámetros. También verifica la integridad del paquete al entregar, junto con observación y rúbrica de la salida. Los datos de observación y aprobación deben proceder del host real.

## Compilación manual

Si Python no está disponible, conserva el mismo inventario y representación como decisiones en contexto. Construye el prompt en este orden: formato → intención visible → composición → tratamiento → elementos, cada uno con literal si corresponde, construcción, posición y escala → recursos gráficos elegidos y límite de añadidos → controles distintos → plan temporal si corresponde → referencias y funciones. No reescribas libremente desde el brief original después de este paso.

Comprueba en ambos sentidos: cada decisión material tiene una cláusula y cada cláusula procede del diseño vigente. El texto externo se limita a los literales elegidos; el apoyo y los descartes no se mencionan ni como ejemplos negativos. No utiliza «los textos acordados» ni referencias a análisis ausentes. La representación debe permitir redactar esa instrucción sin decisiones nuevas. Una etiqueta o comparación de estilos puede acompañar controles concretos, pero no sustituirlos.

La revisión manual conserva evidencia de selección, diseño, anti-IA y cobertura; muestra una síntesis factual antes de producir conforme al protocolo. No inventes huellas, resultados de scripts ni llamadas a especialistas externos. La ausencia de Python cambia el medio de comprobación, no permite saltar la selección o el diseño.
