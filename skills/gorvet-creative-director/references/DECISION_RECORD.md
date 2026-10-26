# Registro de decisiones y traspasos

Conserva el estado vigente del trabajo como decisiones y evidencia, sin registrar razonamiento privado. Puede mantenerse en contexto para una pieza sencilla; usa un archivo si el trabajo continúa entre sesiones y el entorno permite guardarlo. No inventes persistencia.

## Información que debe sobrevivir

| Grupo | Contenido |
| --- | --- |
| Encargo | Entregable, propósito, público pertinente, soporte, datos confirmados y restricciones. |
| Estrategia | Mensaje principal, concepto elegido y selección de contenido. |
| Arte | Medio, escena, encuadre, relaciones espaciales, color, tratamiento y luz pertinente. |
| Gráfica | Literales de la imagen, agrupaciones, posición, tipografía y orden de lectura. |
| Referencias | Identificador disponible, función, atributos protegidos y cambios permitidos. |
| Serie | Elementos constantes, variaciones y función de cada pieza, si existe una serie. |
| Ejecución | Prompt y parámetros por intento, referencias suministradas y autorización aplicable. |
| Revisión | Imagen realmente inspeccionada, evidencia, veredicto y siguiente corrección. |

Un especialista recibe lo pertinente y devuelve **decisiones**, **elementos que conserva** y **dudas materiales pendientes**. No devuelve otra versión completa del brief ni un prompt competidor. Una recomendación pendiente no modifica en silencio una decisión aprobada.

## Trabajo en cadena

Aplica el [contrato de consulta](SPECIALIST_CONTRACT.md). Conserva el contexto GORVET y la revisión vigente; cada contribución devuelve decisiones de su ámbito, conservación, conflictos y controles de aceptación. Cuando se use el registro JSON, [chain_handoff.py](../scripts/chain_handoff.py) comprueba que una contribución no reescriba otra especialidad ni parta de una versión obsoleta.

## Cobertura en ambas direcciones

Antes de compilar, cada requisito material debe tener un control suficiente; cada decisión nueva debe responder al encargo o a una necesidad visual concreta. Antes de ejecutar, cada control pertinente debe sobrevivir en el prompt o en los parámetros y referencias que realmente se adjuntan. El copy de apoyo y los descartes quedan fuera del generador.

Para una edición, añade la imagen base aprobada, la zona o elemento que cambia, la mutación solicitada y los atributos que se conservan. Una salida fallida no se convierte automáticamente en la nueva referencia de identidad.

El contrato 1.1 legible por máquina del futuro agente está documentado en [AGENT_ARCHITECTURE.md](AGENT_ARCHITECTURE.md). El registro no garantiza obediencia del generador; permite identificar dónde se perdió una decisión y comparar versiones.
