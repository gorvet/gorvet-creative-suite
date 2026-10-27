# Arquitectura y contrato de producción 1.3

GORVET Creative Director conserva un encargo vigente y once roles de diseño. Las consultas son responsabilidades del asistente; no equivalen a once agentes externos ni a once procesos ejecutados automáticamente. El director coordina la cadena por decisiones pendientes y aplica [PRODUCTION_GATE.md](PRODUCTION_GATE.md) antes de producir.

## Productos y responsabilidades

[SCOPE_AND_ROUTING.md](SCOPE_AND_ROUTING.md) delimita el alcance de diseño; [SPECIALIST_CONTRACT.md](SPECIALIST_CONTRACT.md) define la autoridad y retorno; [WORKFLOW_CHAINS.md](WORKFLOW_CHAINS.md) selecciona recorridos. Concepto/contenido resuelve selección; arte, sistema y masas; fotografía, captura; gráfica, construcción tipográfica; identidad, fuentes y sistema estable; series, relaciones entre piezas; vídeo, realización temporal. El director integra; Luces compila; QA ajusta redacción de las decisiones sin rediseñar; crítica evalúa antes de generar y después de observar la salida.

[chain_handoff.py](../scripts/chain_handoff.py) aplica contribuciones con `job_id`, `base_revision`, `role` y `updates`. Comprueba versión vigente, autoridad y campos protegidos; conserva las demás decisiones y añade la traza. Su mapa `OWNERS` permite a estrategia aportar `direction.content_decisions`, al director integrar `direction.production_spec` y a crítica aportar `production_review`. Compilación no tiene autoridad para cambiar diseño.

## Registro vigente

El formato actual es `schema_version: "1.3"`. Los contratos 1.1 y 1.2 son históricos; no pasan el control de producción actual. Para migrar, resuelve las decisiones y controles ausentes: no completa automáticamente una dirección a partir del prompt anterior.

El registro contiene `job_id`, `revision`, `brief`, `direction`, `task_mode`, `deliverable`, `execution`, `preflight`, `production_review`, `output` y `review`. `deliverable` puede ser `image`, `series` o `video`; un encargo textual no autoriza generación. `task_mode` distingue `create` y `edit`. El brief está `ready` y sin `material_questions` antes de producir; las hipótesis no materiales se conservan identificadas.

La dirección conserva `message`, `concept`, `medium`, `composition`, `image_text`, `references` y contexto `gorvet`. Las letras registran intención heredada o resuelta, no una nueva ideación en cada especialista. [PRODUCTION_SCHEMA.md](PRODUCTION_SCHEMA.md) especifica inventario, selección, representación del diseño y revisión previa vinculada. En edición se utiliza `preflight` de tipo `edit_scope` con base, objetivo, mutación, protección y aceptación; no se abre otro concepto.

## Compilación y control

[compile_production.py](../scripts/compile_production.py) ensambla una instrucción autosuficiente desde la representación final. No diseña ni llama a modelos. Devuelve `compiled`, `prompt` y `prompt_fingerprint`; no modifica el registro ni autoriza producción. El director incorpora la salida exacta, crítica comprueba selección, diseño, anti-IA y cobertura, y se presenta la propuesta según [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md).

`execution` conserva prompt, fuentes, parámetros, intento, autorización y sus versiones publicadas. El modo `approval` necesita una huella aprobada desde la interacción real; `direct` necesita una instrucción expresa. Ocultar el prompt exige petición expresa. La huella de dirección cubre encargo, brief, alcance y decisiones; la de propuesta añade prompt, fuentes y parámetros. Las huellas no constituyen consentimiento.

[check_handoff.py](../scripts/check_handoff.py) recompila la dirección, exige coincidencia exacta del prompt y revisión previa vigente, y comprueba concepto o alcance de edición, autorización, fuentes, parámetros y límite de intentos. Los valores enviados coinciden con los publicados. Las correcciones registran base, diagnóstico, conservación y huella de la dirección autorizada; un cambio de dirección necesita otra propuesta. El límite normal es una generación y dos correcciones.

Para entregar exige paquete íntegro, `output.id`, inspección de esa salida y dirección vigente, evidencia, veredicto apto y rúbrica visual o audiovisual sin bloqueos. [score_review.py](../scripts/score_review.py) comprueba estructura, cálculo y decisión de las rúbricas de concepto, visual y motion; no asigna notas ni observa medios.

## Vídeo

`direction.motion` contiene duración positiva, planos consecutivos con id, inicio/fin, función, acción, cámara, transición y continuidad; audio con modo y especificación; entrega con proporción y formato. [check_motion.py](../scripts/check_motion.py) valida coherencia del plan y alcance registrado de inspección. El control principal lo invoca en vídeo.

Una salida audiovisual necesita `output.media_type: video`, duración observada concordante con tolerancia de registro de 0,05 s, reproducción completa, transiciones revisadas y audio escuchado cuando esté previsto. La rúbrica es `motion`; un fotograma no valida vídeo. Cada llamada de clips separados corresponde a su registro y alcance mostrados. El plan y los parámetros usan capacidades comprobadas de la herramienta real.

## Uso

```text
python skills/gorvet-creative-director/scripts/compile_production.py registro.json
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --fingerprints
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage generate
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage deliver
python -m unittest discover -s skills/gorvet-creative-director/scripts/tests -v
```

Los scripts usan Python estándar. El código de salida 1 rechaza la transición. El [ejemplo](../examples/handoff.json) tiene diseño compilable pero carece de evaluación y autorización: debe fallar antes de generar. El director usa el mismo [procedimiento manual](PRODUCTION_SCHEMA.md#compilación-manual) si el host no permite ejecutar Python; no inventa un resultado del verificador.

## Límite de imposición

El paquete no intercepta herramientas del host. Las instrucciones exigen aplicar el paso; los scripts lo imponen cuando se invocan. Un futuro agente puede llamar obligatoriamente al control antes de sus herramientas de producción y entrega. Incluir los archivos en el ZIP no instala ese agente ni añade un hook en ChatGPT.

Los datos de autorización, inspección y evidencia deben provenir de interacción y herramientas reales. La estructura impide pérdida mecánica de decisiones, contenido sin seleccionar y sustitución libre del prompt; no determina por sí sola que la composición sea atractiva ni demuestra que se observó una imagen. Esas decisiones exigen revisión con evidencia y no se certifican rellenando campos o subiendo notas.
