# Paso efectivo de diseño a generación

Este paso se aplica antes de cada llamada de generación o edición. No consiste en anunciar etapas ni en marcar una lista sin resolverlas. El director conserva un paquete de decisiones comprobable; los especialistas aportan a ese paquete. La instrucción de generar directamente elimina la espera de aprobación, no el trabajo de diseño ni su control.

## Productos de las etapas

| Etapa | Producto concreto | Condición para avanzar |
| --- | --- | --- |
| Interpretar y seleccionar | Inventario de contenidos relevantes; destino y razón de cada uno; literales elegidos y apoyo con destino real. | No queda contenido que el generador deba seleccionar. Una condición material no se oculta; conservar todos los datos exige justificar su función conjunta. |
| Conceptualizar y diseñar | Representación final: formato, intención visible, composición, tratamiento, elementos con posición, escala y tipografía real; origen de la estética. | Se puede reconstruir la pieza sin elegir otra idea ni distribución. Una etiqueta de estilo o «gran personalidad» no reemplaza esas relaciones. |
| Evaluar | Evidencia de selección, diseño y riesgos de automatismo visual; bloqueos concretos. | Los bloqueos se reparan en su origen. Una nota alta o la aprobación del usuario no los cancela. |
| Compilar y comprobar | Prompt autosuficiente formado exclusivamente desde las decisiones finales; literales y referencias explícitos. | No contiene referencias a propuestas ausentes, material descartado, opciones competidoras ni instrucciones que deleguen el diseño principal. |
| Producir y verificar | Llamada con la versión mostrada; salida inspeccionada y comparada con los criterios. | No se cierra por recibir un archivo. Los fallos observados requieren reparación o un estado de no validado. |

Las etapas son obligatorias cuando producen una decisión pendiente; no obligan a consultar a todos los especialistas. Una edición acotada sustituye selección y nuevo concepto por alcance, mutación y protección. Un encargo solo textual no autoriza producir imágenes.

## Convertir el control anti-IA en diseño

Para cada riesgo relevante, decide **qué se verá y cómo se comprobará**. Si el problema es decoración automática, define los recursos gráficos que sí pertenecen al concepto y su ubicación; si no hacen falta, deja explícita su ausencia. Si es materialidad sintética, fotografía resuelve comportamiento de luz, textura y contacto del sujeto. Si es saturación, vuelve a selección y peso combinado, en vez de reducir todo a letra pequeña.

«Evitar estilo IA», «diseño profesional», «editorial» o una lista de prohibiciones no constituyen esa resolución. No se añade una estética por asociación automática con el sector. Un estilo propuesto debe tener una función visual para este encargo; una preferencia del usuario o referencia de marca se conserva. Texturas, pinceladas, iconos y densidad siguen siendo posibles si fueron diseñados, no añadidos para llenar huecos.

En la revisión previa identifica los controles que efectivamente sobrevivieron al prompt. Ejemplo de tipo de evidencia: titular alineado directamente sobre fondo liso, escala subordinada del apoyo, recursos gráficos limitados a los definidos, materialidad dirigida por la luz. No es una fórmula estética para copiar en todos los trabajos.

## Ejecución con y sin Python

Si el entorno puede ejecutar Python y acceder al paquete, utiliza el contrato 1.3 descrito en [PRODUCTION_SCHEMA.md](PRODUCTION_SCHEMA.md):

```text
python skills/gorvet-creative-director/scripts/compile_production.py registro.json
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage generate
```

El compilador construye el prompt; el director lo incorpora al registro y crítica revisa su cobertura. Si el control devuelve errores, vuelve al producto que falta. No renombres la misma instrucción como «prompt final» ni uses contratos antiguos para evitar el control. Tras producir utiliza `--stage deliver` con la salida y evidencia reales.

Sin ejecución de scripts, aplica exactamente los mismos productos y verificaciones en el contexto, mediante el procedimiento de [compilación manual](PRODUCTION_SCHEMA.md#compilación-manual). No simules una llamada al verificador ni afirmes que el código aprobó la pieza. Antes de generar, presenta selección editorial, dirección concreta, prompt autosuficiente y una comprobación breve con decisiones verificadas; el JSON interno no necesita mostrarse. Este resumen contiene decisiones y evidencia, no razonamientos privados. Si falta un producto, permanece en diseño aunque el entorno permita llamar al generador.

La propuesta y autorización siguen [EXECUTION_PROTOCOL.md](EXECUTION_PROTOCOL.md). Los scripts comprueban integridad y correspondencia; la valoración de atractivo, pertinencia, selección y materialidad requiere criterio real. Ningún script de este paquete intercepta herramientas del host: el asistente debe aplicar el paso antes de invocarlas. El mecanismo de software de un futuro agente puede imponerlo desde su ejecución, pero no se declara instalado por incluirlo en el ZIP.
