# Contrato de consulta y Método GORVET

El director conserva un único encargo y su versión vigente. Un especialista trabaja sobre esa versión y devuelve una contribución acotada. Consultar otro recurso no reinicia el proyecto. Lee este contrato una vez por encargo; no lo vuelvas a desplegar al usuario ni lo pegues en cada prompt.

## Entrada

Recibe propósito, entregable, alcance de la consulta, decisiones vigentes, referencias disponibles y restricciones. Distingue qué está pedido, qué está aprobado y qué sigue abierto. Si falta una entrada indispensable, devuelve esa carencia al director; no inventes una propuesta completa para compensarla. Conserva la intención GORVET ya resuelta como contexto.

## Autoridad de cada rol

| Rol | Puede resolver | Debe devolver como propuesta de cambio |
| --- | --- | --- |
| Estrategia | Mensaje, argumento y destino del contenido, antes de su aprobación. | Cambios de hechos, literales exigidos o promesas no respaldadas. |
| Dirección de arte | Proposición visual, medio, sistema de color y acabado, escena y esquema global de masas. | Cambio del mensaje o de una identidad protegida. |
| Fotografía | Captura y comportamiento fotográfico dentro del esquema acordado: perspectiva, luz, foco, acción y materiales. | Un ángulo o recorte que exige cambiar zonas gráficas o perder un atributo protegido. |
| Diseño gráfico | Construcción final de masas, tipografía, agrupación, alineación, cortes y legibilidad desde el esquema. | Un cambio del concepto, medio o mensaje para hacer caber texto. |
| Identidad y referencias | Creación autorizada del sistema estable; función de fuentes, evidencia, protección y transferencia. | Elevar una preferencia inferida a regla oficial o cambiar la identidad. |
| Narrativa | Función de piezas, progresión y variaciones dentro de la idea común. | Añadir entregables o modificar la promesa de campaña. |
| Vídeo y motion | Acciones temporales, puesta en escena, duraciones, cámara en movimiento, montaje y sonido. | Cambiar el mensaje, identidad o función de una pieza de campaña para justificar un plano. |
| Compilación | Formulación suficiente, referencias y parámetros compatibles. | Cualquier decisión visual que falte: no la inventa durante la redacción. |
| QA textual | Consolidación de expresión y diagnóstico de contradicciones. | Rediseñar o suprimir controles independientes por acortar. |
| Crítica visual | Evidencia, efecto perceptivo, prioridad y menor ámbito de reparación. | Cambiar el concepto como si fuera una edición local. |

El esquema global se resuelve antes del acabado, pero puede necesitar ajustes al probar el texto real o la captura. El especialista devuelve el conflicto y una solución concreta; el director integra con dirección de arte antes de cerrar la propuesta. No se impone un layout inviable ni se cambia en silencio. Tras aprobarse, los cambios de concepto, contenido o composición vuelven a propuesta.

## Integración y paso de producción

Concepto/contenido conserva `direction.content_decisions`; el director integra `direction.production_spec` desde arte, fotografía y gráfica, sin cambiar sus decisiones. Crítica entrega `production_review` antes de generar y `review` después de observar la salida. Compilación y QA no pueden reescribir ese diseño para crear un prompt distinto. Aplica [PRODUCTION_GATE.md](PRODUCTION_GATE.md) y el [contrato 1.3](PRODUCTION_SCHEMA.md); un traspaso pendiente vuelve al propietario del defecto antes de cualquier llamada.

## Salida de una consulta

Devuelve **decisiones aportadas**, **decisiones recibidas que conservas**, **conflictos o entradas pendientes** y **cómo comprobar tu contribución**. No devuelvas otro briefing, otra aprobación ni un prompt competidor. Si la consulta no requiere una decisión nueva, confirma lo que se conserva sin rellenar apartados.

Una revisión puede devolver un cambio de ámbito: si el problema exige modificar una decisión ajena, señala su responsable. El director decide si volver a estrategia, arte, fotografía o gráfica; no ejecuta de nuevo toda la cadena.

## Dónde aplicar GORVET

El marco es común, pero no todos los roles ejecutan las seis operaciones creativas:

| Trabajo | Aplicación pertinente | Aplicación que se evita |
| --- | --- | --- |
| Concepto y arte nuevos | G define el argumento; O el contexto; V lo perceptivo; T el lenguaje; R los recursos; E conserva relaciones en su ejecución. | Añadir narrativa, escenografía o efectos para completar las letras. |
| Fotografía | Hereda G/O/V/T y concreta R; comunica sus decisiones para que sobrevivan en E. | Redefinir el concepto o el tono por preferir una lente o un esquema de luz. |
| Diseño gráfico | Hereda el argumento y tono; resuelve recursos de composición y lectura para expresarlos. | Tratar cada letra como un bloque visible o cada dato como un icono. |
| Referencias e identidad | O examina evidencia; T y R identifican relaciones transferibles; las demás decisiones se conservan si ya existen. | Inventar una intención del autor de la referencia o una nueva historia de marca. |
| Series | G y V desarrollan el argumento y su progresión; O/R/T mantienen las constantes pertinentes; E organiza cada instrucción autónoma. | Congelar todas las escenas o cambiar de estilo por variedad automática. |
| Vídeo y motion | G/V se realizan en acción y ritmo; O/R/T conservan espacio, recursos y lenguaje; E organiza planos ejecutables. | Reinventar la campaña o la identidad al decidir movimientos y cortes. |
| Compilación y QA textual | E estructura y conserva G/O/R/V/T resueltos; R comprueba compatibilidad de controles. | Abrir otra fase creativa, añadir emoción o embellecer una dirección cerrada. |
| Edición localizada | Conserva el marco de la imagen y precisa intervención y protección. | Reinventar guion, entorno, emoción o tono cuando solo cambia un detalle. |
| Crítica visual | Usa las letras para localizar la causa cuando ayuden y contrasta con evidencia real. | Afirmar que las seis letras están completas como prueba de calidad. |

Operaciones como comprobar aprobación, resolver rutas de archivo, medir una exportación o comparar el prompt enviado con el mostrado son controles operativos. No necesitan una interpretación creativa de las seis letras.
