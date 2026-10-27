# GORVET Creative Director

Agencia creativa visual de **Juank de Gorvet**, basada en el Método G.O.R.V.E.T. Se centra en diseño y dirección creativa visual, sin planificación de marketing. Un director interpreta el encargo, selecciona las especialidades necesarias, integra sus decisiones y conduce propuesta, producción y revisión. El libro aporta conocimientos de fotografía, estilos, imagen conceptual, visualización, identidad y narrativa; no limita el complemento a crear o editar fotografías.

## Once skills con responsabilidades distintas

| Skill | Responsabilidad |
| --- | --- |
| `gorvet-creative-director` | Coordinar el encargo y conservar decisiones, autorización, ejecución y cierre. |
| `gorvet-creative-strategy` | Resolver concepto visual, mensaje de la pieza y selección editorial; sin planificación de marketing. |
| `image-art-direction` | Definir el sistema de arte y el esquema global, e integrar fotografía y diseño gráfico. |
| `photography-direction` | Dirigir captura, acción, óptica, luz, foco, materiales e integración fotográfica. |
| `poster-promotional-design` | Resolver composición gráfica, tipografía, jerarquía y relación imagen-mensaje. |
| `brand-reference-direction` | Crear identidad y sistemas de marca; delimitar referencias, protección y transformaciones. |
| `campaign-storytelling` | Diseñar conjuntos de piezas, series, narrativa visual y adaptaciones coherentes. |
| `video-motion-direction` | Dirigir acción temporal, planos, cámara en movimiento, montaje, sonido y continuidad. |
| `luces-camara-prompt` | Compilar decisiones resueltas en prompts y parámetros utilizables. |
| `prompt-optimization-qa` | Depurar prompts existentes sin perder controles. |
| `visual-quality-review` | Juzgar el resultado observado y dirigir correcciones con evidencia. |

Fotografía es una especialidad propia. Dirección de arte integra la solución visual y su esquema; fotografía desarrolla la captura de esa solución cuando sea fotográfica. Diseño publicitario integra la escena con tipografía y contenido. El director resuelve conflictos y conserva la responsabilidad; una consulta no reinicia el trabajo ni abre otra aprobación.

## Paso de producción de la versión 2.3

Antes de generar, el director aplica [PRODUCTION_GATE.md](skills/gorvet-creative-director/references/PRODUCTION_GATE.md). La selección de contenido y el diseño son productos concretos: cada dato tiene un destino y cada literal una construcción, posición y escala. La estética tiene procedencia y criterio; los recursos gráficos se eligen antes de producir.

El [compilador](skills/gorvet-creative-director/scripts/compile_production.py) construye el prompt desde la representación final; el verificador recompila y rechaza diferencias, etapas previas pendientes o revisiones de otra versión. Los textos de apoyo y descartes no se envían. No acepta remisiones como «los textos establecidos en la propuesta» en las instrucciones de ejecución. Los contratos anteriores ya no permiten eludir este control.

Si no hay Python, el asistente aplica el mismo recorrido manual y muestra decisiones y una comprobación breve antes de producir. El paquete exige ese comportamiento mediante instrucciones; no intercepta herramientas de ChatGPT ni garantiza obediencia del host. La estructura, compilación y pruebas se distinguen de verificar la calidad de una imagen real.

## Cómo trabaja

El director [prepara el brief con el usuario](skills/gorvet-creative-director/references/BRIEF_INTAKE.md): extrae lo disponible, separa hechos y supuestos y pregunta por incertidumbres materiales. Estrategia convierte ese encargo en argumento y selección; arte desarrolla el sistema visual. El equipo propone decisiones de diseño sin pedir al usuario que haga ese trabajo. No hay un cuestionario completo obligatorio ni una aprobación adicional rutinaria del brief.


El recorrido se adapta al entregable. Una crítica puede empezar por la imagen existente, un prompt resuelto puede ir directamente a depuración y un conjunto necesita relaciones entre piezas. No se activan los once skills para cada petición.

Antes de producir una imagen nueva, el director resuelve la idea y el diseño. Si el brief contiene mucha información, recomienda qué aparece en la imagen, qué pasa al apoyo con un destino viable y qué se omite. Después muestra la dirección visual, el prompt completo, las referencias y los parámetros aplicables para aprobarlos. Una petición expresa de ejecución directa permite omitir la espera; el prompt sigue visible salvo petición de ocultarlo.

La herramienta recibe el prompt mostrado. Tras generar, el asistente inspecciona la imagen y compara propósito, contenido, atractivo, composición y fidelidad. Las correcciones para restablecer la dirección aprobada muestran su instrucción antes de ejecutarse y no abren otra aprobación. Un cambio de concepto, contenido o composición requiere renovar la propuesta. El límite estándar es una generación y dos correcciones.

Una revisión textual no valida el arte. Si faltan herramientas de generación, inspección o edición, el asistente informa del alcance pendiente. La suite aporta skills y recursos; no incorpora su propio motor de generación ni garantiza obediencia del modelo anfitrión.

## Workflows adaptados y puntuaciones

La [revisión de fuentes](skills/gorvet-creative-director/references/SOURCE_ADAPTATION.md) compara los workflows y skills estudiados y documenta qué se incorpora, qué se adapta y qué se descarta. Las [cadenas](skills/gorvet-creative-director/references/WORKFLOW_CHAINS.md) separan creación gráfica, fotografía definida, ilustración, conjuntos visuales, edición acotada, crítica y depuración. El [contrato común](skills/gorvet-creative-director/references/SPECIALIST_CONTRACT.md) delimita entradas, autoridad y salidas para conservar las decisiones del trabajo anterior.

La [rúbrica](skills/gorvet-creative-director/references/SCORING_RUBRIC.md) evalúa concepto, resultado visual y realización audiovisual con anclas, pesos y evidencia. Los fallos bloqueantes o un criterio pendiente impiden cerrar aunque el índice total sea alto. Una edición localizada verifica alcance y protección; no necesita inventar otra idea creativa.

## Bibliotecas y recetas

Se conservan las 28 bibliotecas de Luces y los recursos de diseño publicitario. Las especialidades consultan solo lo pertinente. Las recetas de ideación, escena y captura nuevas relacionan una necesidad con decisiones y controles de aceptación; no asignan una estética fija por sector ni obligan a añadir técnica, objetos o efectos.

El [Método G.O.R.V.E.T. dentro de la agencia](skills/gorvet-creative-director/references/METODO_GORVET.md) conecta guion visual, observación, recursos técnicos, valor emocional, estructura narrativa y tono. El director integra su aplicación entre especialidades y lo utiliza también para diagnosticar fallos. No exige seis párrafos en cada prompt. Las bibliotecas públicas son recursos de conocimiento; el documento fuente privado del libro no se distribuye.

Consulta [fuentes y adaptación](skills/gorvet-creative-director/references/SOURCES.md) para las referencias estudiadas. Los proyectos externos no son dependencias instaladas ni una garantía de resultados.

## Descarga e instalación

El paquete de esta versión es `gorvet-creative-suite-2.3.0.zip`, con manifiesto, once skills, referencias, scripts de control, pruebas, icono y licencia. Su identificador técnico sigue siendo `gorvet-creative-suite` y el nombre visible es GORVET Creative Director. El autor y desarrollador son Juank de Gorvet; la web es [gorvet.com](https://gorvet.com).

Los paquetes publicados aparecen en [GitHub Releases](https://github.com/gorvet/gorvet-creative-suite/releases). Para probar una versión local usa el ZIP entregado con esa versión; crear un archivo local no lo publica en GitHub.

Importa el ZIP completo en una aplicación compatible con este formato de complemento. Para un host que instala Agent Skills por carpetas, conserva las once carpetas hermanas de `skills/` con sus recursos: la agencia utiliza referencias entre especialidades. La aplicación decide su ubicación, activación y formato de importación. Adjuntar el ZIP a un chat no equivale necesariamente a instalarlo.

Después de actualizar, comprueba que la aplicación muestre la versión 2.3.0 y el skill `gorvet-creative-director`. Abre una sesión nueva si el host conserva instrucciones anteriores. No necesitas elegir manualmente un especialista para pedir un trabajo completo.

## Migración desde 1.7

Se conservan los identificadores de los tres skills originales. El skill de pósters pasa a especializarse en diseño gráfico dentro de la agencia. Luces conserva el Método GORVET y todas sus bibliotecas, y concentra la compilación de prompts; sus decisiones de arte y fotografía tienen responsabilidades y entregables delimitados. El director coordina una sola propuesta y aprobación. QA de prompts mantiene su uso independiente para depuración textual.

La versión 2.0 cambia el recorrido: una escena ya resuelta que solo necesita un prompt no exige volver a aprobar una dirección nueva. Los idiomas son los solicitados o, por defecto, el de la conversación. El desglose del método se entrega cuando se pide; las consultas entre especialistas no añaden cierres promocionales.

## Base para un agente

[Arquitectura y contrato](skills/gorvet-creative-director/references/AGENT_ARCHITECTURE.md) documenta el contrato 1.3, responsabilidades, contribuciones en cadena, puntuación, autorización, huellas y revisión. El [verificador de traspasos](skills/gorvet-creative-director/scripts/check_handoff.py) permite comprobar antes de producir y antes de declarar una entrega validada que el registro está completo y corresponde a la versión vigente.

```text
python -m unittest discover -s skills/gorvet-creative-director/scripts/tests -v
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage generate
python skills/gorvet-creative-director/scripts/check_handoff.py registro.json --stage deliver
```

Los scripts de traspaso, puntuación y autorización usan solo la biblioteca estándar de Python. El [ejemplo sin aprobar](skills/gorvet-creative-director/examples/handoff.json) debe ser rechazado antes de generar. Los controles verifican ámbitos de decisión, versiones, estructura y cálculo de las notas e información de autorización; no asignan el juicio visual ni prueban que una aprobación declarada sea auténtica.

Para imponer controles efectivos, el futuro agente debe obtener autorización de mensajes reales, registrar llamadas y archivos reales, invocar el verificador en sus transiciones y disponer de visión para juzgar el resultado. El paquete no intercepta herramientas automáticamente ni despliega todavía ese agente.

## Distribución

Después de confirmar los cambios, ejecuta `./scripts/build-release.ps1` desde PowerShell. Genera el ZIP y `SHA256SUMS.txt` en `dist/` desde el commit actual. Rechaza cambios pendientes y archivos de distribución existentes para evitar paquetes ambiguos.

La publicación existente usa `.github/workflows/release.yml`: al subir una etiqueta como `v2.3.0`, comprueba su coincidencia con el manifiesto, genera el ZIP, verifica integridad y crea la Release. Un commit o un ZIP local no publican esa Release. La identidad, el icono y los metadatos se conservan en `plugin.json`.

## Licencia

Consulta [LICENSE](LICENSE). La documentación de fuentes identifica los proyectos estudiados; no se incluye el documento privado del libro ni se han importado repositorios externos como código de la suite.

## Alcance y ampliación 2.2

El [mapa de responsabilidades](skills/gorvet-creative-director/references/SCOPE_AND_ROUTING.md) limita el complemento a diseño y dirección creativa visual. Puede diseñar anuncios y varias piezas relacionadas; no investiga consumidores, define estrategias comerciales, planifica medios, activaciones ni calendarios de marketing. Los nombres históricos de estrategia y campañas se conservan por compatibilidad, con alcance de concepto/contenido y series visuales.

Identidad desarrolla creación de marca, sistema, variantes, aplicaciones y pruebas de reproducción. Arte amplía desarrollo por medio; fotografía, captura e integración; gráfica, layout con contenido real, tipografía, adaptación e iconos; series, encargos y continuidad; compilación y QA, cobertura sin rediseñar. Vídeo/motion tiene realización temporal propia y crítica audiovisual; los verificadores rechazan validar vídeo con fotogramas o una revisión incompleta registrada.

Los procedimientos están enlazados desde cada skill y comparten traspasos y límites. El paquete no incluye motores audiovisuales ni despliega un agente autónomo: producir requiere herramientas disponibles. Las pruebas de contratos no equivalen a comprobar calidad generativa en ChatGPT.

## Memoria y diseño multilingüe

Identidad y referencias incorpora un [procedimiento de memoria de proyecto](skills/brand-reference-direction/references/REFERENCE_MEMORY.md): procedencia, alcance, estados, versiones y recuperación de criterios aplicables. Si el entorno permite archivos, se conserva en el proyecto; sin persistencia disponible no promete memoria entre sesiones. No requiere servicios externos ni guarda preferencias de clientes en el complemento.

Diseño gráfico incorpora [composición multilingüe y RTL](skills/poster-promotional-design/references/MULTILINGUAL_RTL.md), con textos fuente, jerarquía entre versiones, mezcla de escrituras y números, dirección, tipografía y revisión de salida. Crítica utiliza el mismo procedimiento. Se mantienen once roles; estas capacidades no añaden aprobaciones ni planificación de marketing.
