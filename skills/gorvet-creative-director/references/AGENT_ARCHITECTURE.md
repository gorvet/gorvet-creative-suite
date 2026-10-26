# Arquitectura de la agencia y contrato para un agente

GORVET Creative Director 2.0 organiza diez skills con un director y nueve especialidades. Las consultas son roles de trabajo del asistente: no implican diez modelos, procesos paralelos ni agentes externos. El director selecciona solo las decisiones que necesita el encargo.

## Responsabilidades

| Responsable | Posee | No decide por los demás |
| --- | --- | --- |
| Director creativo | Encargo, recorrido, integración, autorización, ejecución y cierre. | No inventa capacidades de herramientas ni pruebas. |
| Estrategia | Objetivo, proposición, concepto y selección editorial. | No fija cámara o layout para ocultar un mensaje pendiente. |
| Dirección de imagen | Escena, medio y relaciones visuales que expresan el concepto. | No reemplaza datos o identidades protegidas. |
| Fotografía | Captura, gesto, perspectiva, luz, foco y materialidad fotográfica. | No reabre concepto, copy ni organización gráfica aprobados. |
| Diseño publicitario | Composición gráfica, tipografía y relación imagen-mensaje. | No devuelve al arte todo el brief por encontrarle espacio. |
| Identidad y referencias | Función de las fuentes y atributos protegidos. | No convierte preferencias inferidas en reglas oficiales. |
| Narrativa y campañas | Función de cada pieza, progresión, continuidad y adaptación. | No expande una imagen individual a campaña sin encargo. |
| Luces | Compilación de decisiones en prompt y parámetros. | No añade otra dirección ni genera durante una consulta. |
| QA de prompts | Redacción, cobertura y ausencia de contradicciones. | No certifica la imagen ni sustituye el diseño. |
| Crítica visual | Resultado observado, evidencia, veredicto y corrección. | No aprueba un render que no ha inspeccionado. |

Dirección de imagen decide qué se verá y con qué lenguaje. Fotografía decide cómo capturar esa solución cuando el medio es fotográfico. Diseño publicitario coordina sus masas con los textos; el director resuelve un conflicto entre ellos antes de compilar.

## Flujo y autoridad

El encargo pasa por interpretación, decisiones, propuesta visible, aprobación cuando corresponde, ejecución, observación y corrección o cierre. Una consulta a otro skill no reinicia ese estado. La solicitud puede terminar antes si se pidió solo estrategia, prompt o crítica.

El registro conserva decisiones y evidencia. Cada corrección identifica su fuente y el atributo que cambia; las fuentes de identidad aprobadas no se sustituyen por una salida fallida. Mantén un registro por pieza producida y una dirección común cuando haya una serie.

## Contrato JSON 1.0

El [ejemplo de registro](../examples/handoff.json) muestra un encargo aún sin aprobar. Los campos obligatorios para los controles de producción son:

- `schema_version`: `1.0`; `job_id`: identificador estable del encargo o pieza.
- `deliverable`: `image` o `series` para este verificador. Los entregables textuales siguen el flujo del skill correspondiente y no autorizan imágenes.
- `direction`: `message`, `concept`, `medium`, `composition`, `image_text` como lista de literales y `references` como lista de objetos con `id` y `role`. Puede contener más decisiones, incluidos color, tipografía, restricciones, apoyo y atributos protegidos; todas entran en su huella.
- `execution`: `prompt`, `reference_ids`, `parameters`, `attempt`, `authorization` y, salvo omisión expresa, `published_prompt`, `published_reference_ids`, `published_parameters`.
- `authorization.mode`: `approval` con huella aprobada o `direct` con `direct_instruction` que documente la petición expresa. Ocultar el encargo usa `visibility: omit_on_request` y `visibility_instruction` expresa; el valor normal es `shown`.
- Para una corrección: `execution.correction` contiene `restore_approved`, `direction_fingerprint`, `source_output_id` y `diagnosis`. En modo aprobado, `authorization.approved_direction_fingerprint` conserva la dirección autorizada. Las referencias de ejecución incluyen las fuentes de dirección y la salida base declarada.
- Para validar entrega: `output.id` identifica la imagen; `review` contiene `observed`, `output_id`, `direction_fingerprint`, `verdict` y `evidence` como lista de observaciones. Solo `pass` permite declarar una entrega validada.

La huella de propuesta cubre encargo, dirección, prompt, referencias y parámetros. La huella de dirección cubre encargo y decisiones. Calcula las huellas para saber qué se presentó; registra aprobación solo después de recibirla. Calcular una huella no aprueba nada.

## Verificador opcional

El script estándar de Python [check_handoff.py](../scripts/check_handoff.py) no necesita red ni paquetes externos:

```text
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --fingerprints
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage generate
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage deliver
```

Devuelve JSON con `allowed` y `errors`, y código de salida 1 si falla. Bloquea registros sin dirección, prompt diferente del mostrado, aprobación obsoleta, referencias incoherentes, literales ausentes, correcciones sin diagnóstico o entrega validada sin revisión de esa salida. El límite estándar comprobado es una generación y dos correcciones. Si un futuro agente permite otro alcance expresamente autorizado, debe adaptar su política y pruebas de límite; no basta alterar la propuesta en silencio.

Pruebas reproducibles:

```text
python -m unittest discover -s skills/gorvet-creative-director/scripts/tests -v
```

## Qué necesita implementar el futuro agente

El paquete no intercepta llamadas a herramientas por sí mismo. Para un control real, el agente debe mantener el registro, obtener la autorización desde la interacción auténtica del usuario y llamar al verificador antes de producir y de declarar una entrega validada. Una salida de control negativa impide esa transición y vuelve a la decisión pendiente.

El verificador confía en los datos del host: no puede saber si una aprobación registrada ocurrió, si se adjuntó realmente un archivo ni si una observación visual es verdadera. El host debe aportar esos hechos desde llamadas y mensajes reales; no debe delegar su fabricación al modelo. La evaluación estética requiere visión y criterio, no se demuestra por pasar un esquema ni por declarar `observed: true`.

Conecta generación, archivos, visión y persistencia según herramientas reales. Si falta una capacidad, informa del alcance que no se ejecutó. Esta versión deja instrucciones, responsabilidades y controles comprobables; no afirma haber creado o desplegado todavía ese agente.
