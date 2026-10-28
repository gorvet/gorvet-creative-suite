> Playbook de especialista. Lo consulta el director creativo; devuelve su resultado al director y no abre aprobaciones, briefing ni producción propios.

# QA de optimización de prompts

Optimiza un prompt existente conservando su dirección visual. El resultado debe contener las instrucciones suficientes para reconstruir la misma escena y sus restricciones, con una formulación por control. No genera imágenes ni certifica su resultado.

## Trabajo en cadena y método

Aplica el [contrato común](../direccion/SPECIALIST_CONTRACT.md). Recibe un prompt existente y los controles que debe conservar; aporta una redacción consolidada. Su intervención en GORVET es principalmente E: verifica que la expresión no pierda G/O/R/V/T vigentes. No reinicia el método como ideación ni añade contexto o emoción a una dirección cerrada.


## Alcance y fuente de verdad

Lee el prompt, los cambios solicitados y el contexto disponible. Si falta el prompt, pídelo sin abrir un nuevo briefing. Distingue requisitos explícitos, decisiones aprobadas y desarrollos opcionales cuya procedencia puedas comprobar. Si solo recibes el prompt, trata sus decisiones visuales concretas como intencionales: no elimines un material, encuadre o atmósfera por preferencia propia.

Un trabajo visual completo corresponde al [director creativo](../../SKILL.md), que decide si interviene dirección de imagen o diseño publicitario. Compilar una dirección ya resuelta corresponde a Luces. Puedes depurar solamente el prompt de un cartel conservando íntegros su copy y relaciones de composición, sin rediseñarlo.

Cuando el director consulta este QA, depura internamente el encargo ya construido y devuelve el control; sus decisiones vigentes de diseño no requieren una aprobación nueva. La regla de entregar solo el prompt y la ausencia de generación describen la tarea independiente de QA.

## Procedimiento de depuración

Lee [OPTIMIZACION_PROMPT.md](../compartido/OPTIMIZACION_PROMPT.md). Trabaja sobre una única versión mediante estas comprobaciones internas:

1. **Inventario de controles:** identifica qué exige el encargo en sujeto, selección, acción, espacio, estilo, luz, composición, referencias y restricciones. No son campos que debas completar.
2. **Duplicados por significado:** localiza formulaciones que controlan el mismo atributo. Conserva la más precisa e integra en ella cualquier detalle distinto de las demás. Una frase puede contener a la vez información repetida y una condición necesaria.
3. **Aporte real:** elimina énfasis, explicaciones y detalles opcionales que no cambian el resultado pedido. Revisa también cláusulas dentro de cada frase; una frase puede aportar una decisión y arrastrar varias equivalencias.
4. **Consolidación:** reemplaza las formulaciones corregidas en su lugar. No concatenes original, modificación y cierre de refuerzo. Si detectas una contradicción material sin resolución autorizada, devuelve esa decisión al director; en una tarea independiente pregunta solo por esa elección.
5. **Continuidad temporal cuando corresponda:** conserva orden, duraciones, estados de entrada y salida, cámara y canales de audio. No confunde anclas repetidas entre clips autónomos con duplicados dentro de un prompt. Una contradicción entre planos vuelve a vídeo, sin reescribir la historia.
6. **Cobertura y ausencia de expansión:** compara con el inventario. Cada control necesario debe seguir teniendo una instrucción ejecutable; ninguna instrucción nueva puede proceder solo de querer embellecer la revisión. Verifica también el texto y el formato exigidos.

No basta con sustituir palabras por sinónimos o afirmar que el prompt quedó optimizado. Si una parte ya es suficiente, consérvala. Un prompt que ya está depurado puede devolverse sin cambios; no fuerces una reescritura para demostrar actividad.

## Producción desde un paquete de diseño

Si se consulta para generar, devuelve ajustes de redacción al paquete vigente y a Luces antes de recompilar conforme a [PRODUCTION_GATE.md](../direccion/PRODUCTION_GATE.md). No reemplaces el prompt compilado por otra versión libre ni borres controles distintos para acortarlo. Un trabajo independiente de optimización textual conserva la entrega siguiente y no activa generación.

## Entrega

Entrega el prompt optimizado completo en el idioma original o en los idiomas solicitados. Para una petición combinada, incorpora los cambios autorizados antes de depurar. Traduce únicamente la versión cerrada y comprueba que ambas versiones contienen las mismas decisiones, sin ampliaciones ni pérdidas.

Mantén copy literal, atributos protegidos, selección, exclusiones y etiquetas o estructura exigidas por el usuario o un perfil externo aportado. No importes convenciones por el nombre de una plataforma. No impongas una cuota de palabras, un único párrafo o una plantilla universal.

Entrega solo el prompt salvo que se pida explicación o exista una ambigüedad que impida cerrarlo. No añadas cierre promocional, segundo prompt de refuerzo, lista de reglas aplicadas ni garantía de fidelidad visual.
