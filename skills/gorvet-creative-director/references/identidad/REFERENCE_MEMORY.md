# Memoria de referencias y preferencias

## Función y límites

Conserva evidencia y decisiones reutilizables del proyecto. No transforma una referencia estética en manual de marca ni una elección puntual en preferencia permanente. Identidad y referencias mantiene esta memoria; el director decide qué registros aplican al encargo. Arte, fotografía y gráfica reciben solo los criterios pertinentes, no una colección de instrucciones históricas.

## Persistencia disponible

Cuando el entorno permita archivos y exista una ubicación de proyecto, conserva un archivo UTF-8 `reference-memory.json` en el directorio de continuidad del proyecto; puede usarse `.gorvet/` dentro de ese proyecto si no hay una convención existente. No escribas preferencias de un cliente dentro del complemento instalado ni las mezcles con otros proyectos. Comprueba primero si ya existe un registro y conserva su contenido. La memoria local no requiere servicios ni conectores externos.

Sin almacenamiento disponible, conserva las decisiones en el contexto y entrega un registro portable si se solicita. Indica ese alcance: no prometas recuperación en otra sesión. Un archivo guardado solo es utilizable después si el entorno vuelve a dar acceso a él.

## Registro mínimo

El archivo contiene `schema_version: "1.0"`, `project_id`, `revision` entero y listas `references` y `preferences`. Usa identificadores estables y distintos para cada registro. Guarda la evidencia y decisiones suficientes, no razonamientos privados ni copias innecesarias de materiales.

Cada referencia registra:

- `id`, `source` con ruta o URL realmente disponible, y `source_version` mediante huella o versión conocida cuando pueda obtenerse.
- `roles`: qué gobierna, como identidad, composición, luz o acabado.
- `observations`: evidencia visible; `transfer_rules`: relaciones transferibles; `protected_attributes`: lo que se conserva.
- `scope`: proyecto, serie o pieza concreta; `status`: disponible, sustituida o no disponible.

Cada preferencia registra:

- `id`, `criterion`, `scope` y `source`: mensaje o decisión que la respalda.
- `status`: propuesta, confirmada, sustituida o retirada.
- `conditions`: dónde se aplica y cuándo deja de ser pertinente; `supersedes` si reemplaza una decisión anterior.

Una propuesta del asistente sigue siendo propuesta. Una elección de diseño aprobada confirma ese uso; no acredita por sí sola una preferencia global. Solo una instrucción explícita de alcance general puede registrarse como tal. Las observaciones de fuentes y las preferencias del usuario son tipos distintos.

## Incorporar y actualizar

1. Inspecciona el material antes de registrar observaciones. Si solo hay una URL inaccesible o una imagen ilegible, registra la limitación sin inventar su contenido.
2. Asigna función y alcance. Formula cada regla como relación útil y condición, por ejemplo separación de valores para un sujeto concreto, sin prescribir el mismo layout a todos los encargos.
3. Registra procedencia y estado. Integra una corrección confirmada sustituyendo la regla contradictoria; no acumules dos órdenes vigentes incompatibles.
4. Conserva la revisión leída y comprueba que no haya cambiado antes de guardar. Si cambió, relee e integra; no sobrescribas otra actualización. Incrementa la revisión al guardar y vuelve a leer el archivo para comprobarlo. Usa reemplazo atómico si la herramienta lo permite y conserva una versión recuperable antes de cambios amplios.

Retirar una preferencia impide reutilizarla como criterio activo. No sustituye borrar datos si el usuario pide eliminarlos; aplica entonces el alcance de eliminación autorizado. No reconstruyas información retirada desde notas antiguas.

## Recuperar para una cadena

Al iniciar o retomar el proyecto, carga solo la memoria correspondiente. Selecciona referencias disponibles y preferencias confirmadas cuyo alcance y condiciones coincidan. Las propuestas no tienen autoridad de regla aprobada. Comprueba acceso a los archivos antes de declararlos referencias adjuntas; recordar una ruta no proporciona la imagen al generador. Una fuente modificada exige revisar sus observaciones.

Resuelve conflictos por instrucción vigente del usuario, reglas documentadas y alcance más específico. La antigüedad o una preferencia inferida no vencen una decisión expresa. Si dos instrucciones confirmadas del mismo alcance siguen siendo incompatibles, el director aclara esa elección material.

Entrega identificadores consultados, criterios aplicables, fuentes disponibles y conflictos. Compilación recibe únicamente la selección vigente. Crítica contrasta el resultado con esas fuentes reales; recordar que algo fue aprobado no certifica fidelidad de una salida nueva.
