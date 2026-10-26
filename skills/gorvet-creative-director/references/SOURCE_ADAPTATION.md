# Revisión de referencias y adaptación a GORVET

Esta revisión se realizó sobre instrucciones y workflows publicados, no sobre resultados que se hayan ejecutado con esos proyectos. Las decisiones siguientes se aplican a los skills de GORVET 2.1. El contenido nuevo se redacta para este complemento; no se importan repositorios ni campañas completas.

## Designly

Archivos estudiados: [director](https://github.com/imMamdouhaboammar/designly/blob/main/skills/designly-director/SKILL.md), [recepción y normalización del brief](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/marketing-brief.md), [estrategia](https://github.com/imMamdouhaboammar/designly/blob/main/skills/creative-strategy/SKILL.md), [routing y estado](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/routing-and-state.md), [dirección de arte](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/art-direction.md), [preflight](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/design-preflight.md), [layout](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/layout-grid-and-spacing.md), [tipografía](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/typography.md), [referencias](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/reference-analysis.md), [taste engine](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/taste-engine.md) y [QA y revisiones](https://github.com/imMamdouhaboammar/designly/blob/main/shared/references/visual-qa-and-revisions.md).

| Mecanismo observado | Adaptación concreta | Límite |
| --- | --- | --- |
| Recorridos según trabajo y responsable | Cadenas condicionales: creación, fotografía resuelta, pieza gráfica, serie, edición acotada, revisión y depuración. | No activar una secuencia completa de campaña para una imagen individual. |
| Recepción y normalización del brief | El director conduce las aclaraciones con el usuario y estrategia organiza proposición, evidencia y contenido. | No pedir al usuario que decida arte ni convertir cada encargo en un cuestionario completo. |
| Estado compartido y restricciones conservadas | Un contrato de consulta con entrada vigente, campos que el especialista puede modificar y conflictos devueltos al director. | Consultar no transfiere la responsabilidad ni autoriza cambios en decisiones ajenas. |
| Especificación de arte ejecutable | Proposición visible, sistema visual, esquema de masas, papeles tipográficos y controles de acabado. | Una especificación no acredita haber visto un render; no fijar coordenadas sin utilidad. |
| Revisión antes de producir | Verificar propósito, selección, estructura, tipografía y física pertinentes antes de compilar. | Separar decisiones pendientes de defectos observados en una imagen. |
| Referencias por trabajos | Separar preservación de identidad y transferencia de relaciones visuales, con evidencia y límites. | No copiar íntegramente una referencia estética ni inventar reglas de marca. |
| Revisión dirigida al origen | Clasificar fallo de mensaje, arte, gráfica, captura, referencia o compilación y reparar el menor ámbito suficiente. | No regenerar todo ni añadir prohibiciones genéricas ante cada fallo. |
| Fuente aprobada para editar | Intervención acotada con base, objetivo, cambio, conservación y comparación de daño colateral. | No continuar automáticamente desde una salida fallida. |

No se adoptan sus umbrales numéricos de calidad, porcentajes de fidelidad ni la obligación de un esquema de tres luces. Tampoco se incorporan sus sintaxis de modelos sin comprobarlas en herramientas reales. El control estético necesita juicio y evidencia; no lo prueba una suma de números.

## Creative Director de Serge Shima

Archivos estudiados: [skill principal](https://github.com/smixs/creative-director-skill/blob/main/creative-director/SKILL.md), [insight](https://github.com/smixs/creative-director-skill/blob/main/creative-director/references/insight-mining.md), [matriz de métodos](https://github.com/smixs/creative-director-skill/blob/main/creative-director/references/method-selection-matrix.md), [catálogo](https://github.com/smixs/creative-director-skill/blob/main/creative-director/references/methods-catalog.md) y [constitución creativa](https://github.com/smixs/creative-director-skill/blob/main/creative-director/references/creative-constitution.md). Autor: Serge Shima; licencia declarada CC BY 4.0. La adaptación de sus principios de trabajo se atribuye aquí; no se distribuye su base de campañas.

Se incorpora a estrategia la distinción entre problema, observación, hipótesis sobre el público, ventaja respaldada y argumento. Se desarrollan procedimientos de sustracción, transformación, conexión estructural e inversión: cada uno necesita material de entrada, pasos, prueba y condición de abandono. Se elige por el bloqueo, no por una cuota de técnicas.

Se adapta su separación entre cumplimiento y excelencia: una idea que contradice el brief no se rescata por ser ingeniosa. Para elegir entre ideas viables se compara claridad, especificidad, interés, viabilidad y desarrollo, sin atribuir métricas de audiencia inexistentes. Si la idea se estanca, se revisa la premisa o cambia el método; no se cambian solo adjetivos.

No se adoptan la generación obligatoria de numerosas ideas, la rotación fija de tripletas, la exigencia de impacto cultural para todo anuncio ni los niveles de premios como condición universal. Su recomendación de no intervenir en ejecución corresponde a una revisión de conceptos; nuestro QA visual sí necesita diagnosticar tipografía, composición y fotografía.

## Amir Design Judgment

Se estudió [el skill](https://github.com/amirmushichge/amir-design-judgment/blob/main/SKILL.md). Se adapta su forma de revisar: conjunto a escala de uso, detalles decisivos y regreso al conjunto. Una observación debe producir una consecuencia perceptiva y una intervención concreta. Se distinguen corrección local, reconstrucción de un componente y replanteamiento de la composición.

El especialista visual entrega un veredicto basado en evidencia, no defiende la propuesta por haber participado en ella ni inventa medias ponderadas. No se afirma reproducir el juicio personal del autor. Ver una imagen comprimida no permite certificar tipografía o marca exactas.

## Frontend Design de Anthropic

Se estudió [el skill](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md). Se adapta su secuencia de plan visual específico, revisión frente al encargo y construcción. El sistema visual describe color, tipografía, estructura y el gesto distintivo que sirve al tema. Antes de producir se comprueba si la propuesta sería el mismo diseño para casi cualquier cliente.

No se importan sus reglas de interfaz, motion o CSS a todas las imágenes. Sus señales de diseño genérico se utilizan como diagnóstico contextual, no como prohibiciones universales de mayúsculas, paletas, bordes o estilos.

## Marketing Design de vanducng

Se estudiaron [el skill](https://github.com/vanducng/skills/blob/main/skills/marketing-design/SKILL.md), [posters](https://github.com/vanducng/skills/blob/main/skills/marketing-design/references/poster-design.md), [compilación de posters](https://github.com/vanducng/skills/blob/main/skills/marketing-design/references/poster-prompt-engineering.md) y [social photos](https://github.com/vanducng/skills/blob/main/skills/marketing-design/references/social-photos-design.md).

Se adapta su distinción entre entregables y su alternativa de imagen más maquetación determinista. Si el texto requiere exactitud, se contempla producir la base visual y componer tipografía en una superficie editable disponible, con inspección del resultado. Una imagen de un mockup se distingue del diseño aplicado. Para series, se separan constantes y variaciones.

No se adopta aleatorizar la jerarquía, añadir formas o girar elementos para garantizar variedad. La composición cambia por el argumento y el formato. Tampoco se importan sus APIs, rutas, versiones, tamaños de plataformas ni la regla del porcentaje de texto como hechos actuales sin verificación.

## Figma

Se estudió la [descripción oficial del agente de feedback](https://www.figma.com/solutions/ai-design-feedback-agent/). Se incorpora la revisión del arte real en contexto, conservando la distinción entre estructura editable e imagen plana. No se presupone que GORVET tenga acceso a capas o componentes ni se transforma esa página de producto en un skill propio.

## Papel del Método GORVET

GORVET integra intención y tratamiento visual en creación. No reemplaza el análisis de un brief, la investigación, la extracción de referencias, los contratos de edición ni las verificaciones de ejecución. En tareas cerradas conserva G, O, V y T; no las reinventa. Luces y QA de prompts aplican principalmente E para trasladar las decisiones, sin volver a dirigir la escena. El detalle por rol está en [SPECIALIST_CONTRACT.md](SPECIALIST_CONTRACT.md).

El director creativo coordina; estrategia resuelve argumento y contenido; dirección de arte integra el sistema visual; fotografía resuelve captura; diseño gráfico resuelve la construcción tipográfica y espacial. Son niveles de decisión y entregables distintos, no varios autores rehaciendo la misma composición.

## Ampliación 2.2: diseño, identidad y realización temporal

La agencia se limita a diseño y dirección creativa visual conforme a [SCOPE_AND_ROUTING.md](SCOPE_AND_ROUTING.md). Tras revisar también `insight-mining`, `campaign-canon` y `brand-activation` de Designly, no se incorporan especialistas de investigación de consumidores, análisis de mercado, activación ni planificación de campañas. La capacidad de diseñar conjuntos visuales sí se mantiene. Las fuentes no fijan el alcance del producto.

- [Designly video-director](https://github.com/imMamdouhaboammar/designly/blob/main/skills/video-director/SKILL.md): se adapta la separación entre argumento, puesta en escena, evolución temporal, cámara, montaje y compilación. Se desarrolla un procedimiento propio para motion, registros por clip y revisión audiovisual. No se copian fichas, adaptadores de modelos, cantidades obligatorias, porcentajes de montaje ni promesas de capacidades. La fuente atribuye esta línea a Visual Skills de Serge Shima, CC BY 4.0; se mantiene ese crédito.
- [Marketing Design: logos](https://github.com/vanducng/skills/blob/main/skills/marketing-design/references/logo-design.md) y [CIP](https://github.com/vanducng/skills/blob/main/skills/marketing-design/references/cip-design.md): se adopta la relación entre brief de diseño, marca base, variantes, aplicaciones y presentación. El procedimiento propio añade pruebas de reproducción, separación maestro/mockup y verificación de archivos. Se descartan presets de sector, psicología universal de color, fondo blanco obligatorio, cantidades fijas de aplicaciones y dependencias no disponibles.
- Composición, tipografía, integración, control de edición y referencia/memoria permanecen dentro de los especialistas que poseen esas decisiones. No se duplican como roles por imitar el número de skills externos. La memoria solo se declara cuando existe persistencia real.

Se amplían once procedimientos con entradas, autoridad, desarrollo, entregables, aceptación y retorno; las pruebas de cadena verifican versiones, protección y escrituras ajenas. Las pruebas de vídeo verifican plan, autorización y alcance registrado de reproducción, no calidad de un vídeo generado.
