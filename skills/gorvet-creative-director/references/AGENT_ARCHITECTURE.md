# Arquitectura de la agencia y contratos 1.1 / 1.2

GORVET Creative Director 2.2 encadena responsabilidades sobre un solo encargo. Las consultas son roles del asistente, no once procesos paralelos ni agentes externos. El director elige el recorrido por entregable y conserva autorización, versiones y cierre.

## Cadena y responsabilidad

[WORKFLOW_CHAINS.md](WORKFLOW_CHAINS.md) define los recorridos y retornos. [SPECIALIST_CONTRACT.md](SPECIALIST_CONTRACT.md) define entradas, autoridad y salidas. Estrategia entrega argumento y contenido; arte, sistema visual y esquema; fotografía, captura; gráfica, construcción tipográfica y espacial. Arte integra las incompatibilidades antes de compilar. Crítica visual devuelve el defecto al ámbito menor que lo explica.

No se ejecuta toda la cadena para depurar un prompt, criticar una imagen o corregir una palabra. El marco GORVET se hereda y se aplica donde aporta decisiones; los controles de autorización, archivos o exportación no necesitan una nueva ideación.

## Registro y contribuciones

El registro contiene `job_id`, `revision`, dirección vigente, referencias, autorización, ejecución y revisión. Una contribución contiene `job_id`, `base_revision`, `role` y un objeto `updates` con campos concretos. El [ejemplo](../examples/specialist-packet.json) aporta arte al [registro sin aprobar](../examples/handoff.json).

[chain_handoff.py](../scripts/chain_handoff.py) comprueba encargo y versión, rechaza escrituras fuera de la autoridad del rol y campos protegidos, aplica una copia de las decisiones y registra la cadena. No modifica los archivos de entrada. Su mapa `OWNERS` especifica campos autorizados. La composición consolidada y el contexto GORVET pertenecen a la integración del director, que conserva la procedencia de fotografía y gráfica; no son otro encargo independiente.

```text
python skills/gorvet-creative-director/scripts/chain_handoff.py registro.json contribucion.json
```

El verificador controla ámbitos de escritura, no el significado del contenido ni la bondad de una decisión. Que un campo pertenezca al especialista no le permite contradecir el objetivo: preflight y crítica deben detectar esa incoherencia.

## Contrato de producción 1.1

- `schema_version`: `1.1`; `job_id`: identificador estable de la pieza.
- `brief`: encargo organizado con `status: ready` y `material_questions: []` antes de producir. Los datos confirmados, propuestas y supuestos se conservan separados; la preparación del brief no sustituye la aprobación de la dirección.
- `deliverable`: `image` o `series` para este control. Un entregable textual no autoriza producir una imagen.
- `task_mode`: `create` o `edit`; si se omite, se interpreta como creación.
- `direction`: `message`, `concept`, `medium`, `composition`, `image_text` como lista de literales y `references` como objetos con `id` y `role`. Incluye el contexto `gorvet` con G/O/R/V/E/T ya resueltos o conservados; no exige que cada especialista vuelva a desarrollarlos.
- Los demás campos de dirección pueden registrar escena, sistema, captura, layout, tipografía, apoyo, omisiones, reglas de referencia y serie. Todos entran en la huella de dirección.
- `preflight`: para creación, una rúbrica `concept` apta. Para edición, un objeto `kind: edit_scope`, `source_output_id`, `target`, `mutation`, `protected` como lista, `acceptance` y `ready: true`. La base debe estar declarada entre las fuentes. No se exige inventar otro concepto al editar.
- `execution`: `prompt`, `reference_ids`, `parameters`, `attempt`, `authorization` y, salvo omisión expresa, `published_prompt`, `published_reference_ids`, `published_parameters`.
- `authorization.mode`: `approval` con `approved_fingerprint`, o `direct` con `direct_instruction` expresa. Ocultar el prompt exige `visibility: omit_on_request` y `authorization.visibility_instruction`; el modo normal es `shown`.
- Una corrección registra `restore_approved`, `direction_fingerprint`, `source_output_id` y `diagnosis` en `execution.correction`. En modo aprobado conserva `authorization.approved_direction_fingerprint`. Sus referencias incluyen fuentes de dirección y salida base declarada.
- Para entrega validada: `output.id`; `review.observed`, `output_id`, `direction_fingerprint`, `verdict`, `evidence` y `scorecard` visual apta de esa salida.

La huella de propuesta cubre encargo y brief, tipo de trabajo, dirección, prompt, referencias y parámetros. La de dirección cubre el mismo encargo, brief y decisiones. Calcular una huella no obtiene aprobación; el host registra esa aprobación solo desde la interacción auténtica del usuario.

## Puntuación y evidencia

[SCORING_RUBRIC.md](SCORING_RUBRIC.md) define perfiles de concepto, imagen y audiovisual y anclas 0–4. Un criterio contiene `grade` y `evidence` como lista. Solo los criterios expresamente opcionales permiten `applicable: false` con `reason`, sin nota. Cada tarjeta contiene `kind`, `criteria` y `blockers`; la visual añade `observed: true`.

El perfil `concept` contiene `fit`, `specificity`, `interest`, `clarity`, `feasibility`. El perfil `visual` contiene `communication`, `character`, `structure`, `typography`, `fidelity`, `craft`. La suma se normaliza por los pesos aplicables. Un bloqueo o una nota menor de 3 impiden cerrar aunque la media sea alta.

[score_review.py](../scripts/score_review.py) comprueba estructura, evidencia registrada, cálculo y decisión. No observa imágenes ni asigna notas. Una rúbrica incompleta no produce un índice supuesto.

```text
python skills/gorvet-creative-director/scripts/score_review.py evaluacion.json
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --fingerprints
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage generate
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage deliver
python -m unittest discover -s skills/gorvet-creative-director/scripts/tests -v
```

Los scripts usan Python estándar y no llaman a modelos ni redes. El código de salida 1 indica transición rechazada. El ejemplo distribuido está incompleto y sin aprobar: debe ser rechazado antes de generar.

## Integración del futuro agente

El paquete no intercepta herramientas por sí mismo. Para imponer los controles, el agente mantiene el registro, encadena contribuciones, obtiene autorización de mensajes reales, registra archivos y llamadas reales y ejecuta el control antes de producir y de declarar una entrega validada. Si el control falla, vuelve a la decisión pendiente, sin saltarla.

Los verificadores confían en los hechos del host. No pueden saber si una aprobación declarada ocurrió ni si la evidencia visual es verdadera. El host debe aportar esas señales desde interacción y herramientas auténticas; el modelo no debe fabricarlas. Las pruebas de ámbitos, puntuación y autorización son distintas de comprobar la calidad creativa del resultado.

El límite estándar comprobado es una generación y dos correcciones. Otro alcance autorizado requiere una política explícita del agente y pruebas correspondientes; no basta alterar una nota o un dato del registro. Si faltan herramientas o visión, informa del alcance que no se ejecutó.

## Extensión audiovisual 1.2 y responsabilidad de identidad

La versión 2.2 mantiene los registros de imagen 1.1 y añade contrato 1.2 para `deliverable: video`. Son once roles: el nuevo `video-motion-direction` posee únicamente `direction.motion`; identidad incorpora `direction.identity` para el sistema estable. [SCOPE_AND_ROUTING.md](SCOPE_AND_ROUTING.md) delimita entradas, autoridad, aceptación y exclusión de planificación de marketing.

En vídeo, `direction.motion` contiene `duration` positiva en segundos, `shots` consecutivos con `id` único, `start`, `end`, `function`, `action`, `camera`, `transition`, `continuity`; `audio` con `mode: silent|sound` y `spec`; y `delivery` con `aspect_ratio` y `format`. Se registra el montaje final sin huecos; los solapes de fuentes se describen dentro de la transición. Los parámetros solo usan capacidades comprobadas en la herramienta real.

`check_handoff.py` aplica el control temporal integrado antes de generar y al entregar, además de brief, dirección, aprobación y coincidencia de prompt/fuentes/parámetros. Para vídeo la salida requiere `output.media_type: video`, `output.duration` observada concordante (tolerancia de registro de 0,05 s), inspección `review.playback` completa y tarjeta `motion` apta. Esta tarjeta lleva también su alcance de reproducción. El audio previsto no admite marcarse como no aplicable. Los campos son declaraciones del host; los scripts no observan ni escuchan archivos.

`check_motion.py registro.json --stage generate|deliver` permite comprobar el plan temporal por separado. No reemplaza el control completo de autorización ni el veredicto. Un plan maestro puede organizar múltiples clips; cada llamada necesita su registro y autorización vinculada al alcance mostrado. No permite declarar vídeo con una salida de imagen o storyboard.
