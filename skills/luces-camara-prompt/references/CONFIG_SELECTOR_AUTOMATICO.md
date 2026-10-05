# SELECTOR AUTOMÁTICO

Aplicar el selector a las solicitudes visuales sin añadir detalles de implementación innecesarios. Su contenido es público y puede explicarse cuando el usuario lo solicite.

## Selección entre skills de la suite

Seleccionar por el resultado solicitado antes de clasificar tema, estilo o estado de la idea. Invocar el complemento no equivale a elegir `luces-camara-prompt`. El usuario no necesita conocer los nombres internos.

| Resultado solicitado | Skill responsable | Acción |
| --- | --- | --- |
| Optimizar la redacción, reducir extensión o repetición, o resolver contradicciones de un prompt existente | `prompt-optimization-qa` | Leer `../../prompt-optimization-qa/SKILL.md` y depurar una única versión; no iniciar un briefing ni generar imágenes. |
| Crear, dirigir o revisar una pieza promocional estática con texto y layout, incluidos carteles, posts, stories, estados de WhatsApp, flyers, anuncios y banners | `poster-promotional-design` | Leer `../../poster-promotional-design/SKILL.md`; seleccionar contenido y resolver diseño antes de ejecutar o entregar el encargo. |
| Desarrollar una escena o construir un prompt de imagen sin resolver una pieza gráfica promocional | `luces-camara-prompt` | Aplicar el selector interno y sus dos flujos de dirección creativa y prompt. |

La depuración explícita de un prompt ya existente tiene prioridad aunque el prompt describa un póster. Revisar o rediseñar el arte de un póster pertenece al skill de diseño gráfico; la existencia de una imagen de resultado no convierte la tarea automáticamente en optimización de redacción.

El tema no decide la ruta: fotografía de un producto o comida y publicidad de ese producto con precio, horarios y contacto son tareas diferentes. Un canal social tampoco implica por sí solo diseño gráfico si se pide únicamente una fotografía. Si el resultado esperado es ambiguo y cambia el flujo, hacer una pregunta breve; no pedir al usuario que elija un skill.

Cargar solo el skill responsable y sus referencias necesarias. Consultar una biblioteca compartida no activa los flujos del skill que la contiene. No encadenar dirección creativa, QA y diseño como fases obligatorias. Respetar una elección explícita del usuario y, al cambiar de tarea, seleccionar de nuevo; una iteración del mismo arte conserva su skill y encargo.

Crear un tema nuevo usando un ejemplo sigue siendo creación de escena: `luces-camara-prompt` redacta. Las restricciones de un perfil externo solicitado se incorporan al encargo si están disponibles; no activar automáticamente ese perfil por el tema ni importar el contrato de conservación de una reparación. Al iterar, reemplazar decisiones modificadas sin concatenar las versiones anteriores.

Si el skill elegido no está disponible en la instalación, indicar qué falta; no afirmar que se aplicó ni reemplazarlo silenciosamente por una generación directa.

## Selector interno de luces-camara-prompt

Aplicar los apartados siguientes solo después de asignar la tarea a este skill.

## A. Estado de la solicitud
### IDEA_ABIERTA
El usuario no sabe exactamente qué imagen quiere.
- proponer escenas;
- inferir estilo, luz, plano, atmósfera y ratio;
- presentar propuesta antes del prompt.

### IDEA_SEMIDEFINIDA
Existe intención, pero faltan decisiones.
- preservar intención;
- completar lenguaje visual;
- no cambiar el concepto sin necesidad.

### DIRECCION_CERRADA
El usuario ya define la escena.
- optimizar jerarquía, consistencia y técnica;
- no reinterpretar lo que ya está decidido.

## B. Tipo principal
Clasificar:
- RETRATO
- MARCA_PERSONAL
- PRODUCTO
- GASTRONOMIA_BEBIDA
- MODA_LIFESTYLE
- PUBLICIDAD_CAMPANA
- CARTEL_PORTADA
- MOCKUP
- LOGO_SIMBOLO
- CONCEPTUAL_SURREAL
- ARQUITECTURA_INTERIOR
- BOCETO_RENDER
- BOCETO_IMAGEN
- TEXTURA_PBR
- PROTOTIPO
- RETOQUE_COMPOSICION
- RESTAURACION
- EDITORIAL_INTIMO

## C. Referencias
Clasificar cada referencia por función:
- IDENTIDAD
- PRODUCTO_BRANDING
- POSE
- ENCUADRE
- COMPOSICION
- VESTUARIO
- ENTORNO
- ESTILO_MOOD
- BOCETO_GEOMETRIA
- IMAGEN_BASE_EDICION

## D. Bibliotecas
Siempre:
- `references/CORE_METODO_GORVET.md`
- `references/CORE_ESTRUCTURA_PROMPT.md`
- `references/CORE_ERRORES_REGLAS.md`

Según necesidad:
- técnica → módulos `TECHNICAL_*`;
- estilos → módulos `STYLES_*`;
- referencias → módulos `REFERENCES_*`;
- nichos → módulos `USE_CASES_*`;
- secuencias o campañas narrativas → `references/USE_CASES_ARTE_CONCEPTUAL_STORYTELLING.md`;
- refinamiento → `references/WORKFLOWS_ITERACION_DIAGNOSTICO.md`;
- salida final → `references/WORKFLOWS_CONTROL_CALIDAD.md`;
- sentencias reutilizables → `references/WORKFLOWS_PHRASE_BANK.md`;
- íntimo/editorial → `references/WORKFLOWS_EDITORIAL_INTIMO.md`.

## E. Densidad técnica
### SIMPLE
- escena cotidiana;
- técnica mínima;
- 1 estilo + luz + plano si aportan.

### MEDIA
Seleccionar según el encargo; no completar todos los elementos:
- estilo;
- iluminación;
- plano;
- profundidad;
- composición;
- materialidad cuando corresponda.

### AVANZADA
- producto/publicidad;
- múltiples referencias;
- render;
- retoque;
- continuidad;
- problemas técnicos concretos.

## F. Prioridades
1. intención;
2. sujeto/objeto prioritario;
3. propósito de referencia;
4. estilo dominante;
5. luz;
6. composición;
7. materialidad;
8. técnica;
9. microdetalle.

La categoría indica qué recursos considerar, no cuántos añadir. Producto, publicidad o continuidad no exige por sí solo un prompt largo ni completar todos los campos técnicos. Para continuidad puede bastar reutilizar las anclas ya fijadas, una vez por prompt. La técnica no debe desplazar a la idea; aplicar «Construcción del prompt final» de `../SKILL.md`.
