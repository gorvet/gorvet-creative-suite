# SELECTOR AUTOMÁTICO

Aplicar el selector a las solicitudes visuales sin añadir detalles de implementación innecesarios. Su contenido es público y puede explicarse cuando el usuario lo solicite.

## Selección entre skills de la suite

Seleccionar por el resultado solicitado antes de clasificar tema, estilo o estado de la idea. Invocar el complemento no equivale a elegir `luces-camara-prompt`. El usuario no necesita conocer los nombres internos.

| Resultado solicitado | Skill responsable | Acción |
| --- | --- | --- |
| Depurar solamente un prompt existente, sin rediseñar ni producir el arte | `prompt-optimization-qa` | Leer `../../prompt-optimization-qa/SKILL.md` y entregar la versión revisada. |
| Crear, dirigir o revisar una pieza publicitaria estática, con o sin texto externo, incluidos carteles, posts, stories, estados de WhatsApp, flyers, anuncios y banners | `poster-promotional-design` | Leer `../../poster-promotional-design/SKILL.md`; resolver y evaluar el diseño, generar si se pidió el arte y verificar la imagen. Si se pidió solo el prompt publicitario, entregar el diseño compilado sin generar. |
| Desarrollar una escena o construir un prompt de imagen sin resolver una pieza publicitaria completa | `luces-camara-prompt` | Aplicar el selector interno y sus dos flujos de dirección creativa y prompt. |

La depuración explícita tiene prioridad cuando el resultado pedido es solamente un prompt revisado, aunque describa un póster. Si se pide diseñar, producir o corregir el arte, `poster-promotional-design` mantiene la dirección y utiliza la depuración como operación interna. La existencia de un prompt o de una imagen previa no cambia por sí sola el responsable.

El tema, la presencia de copy y el tipo de archivo no deciden la ruta. Un anuncio basado solo en una foto sigue necesitando dirección publicitaria; una fotografía aislada no se convierte en cartel por mostrar un producto o destinarse a una red social. Decide por la función comunicativa y el entregable solicitado. Si esa distinción es materialmente ambigua, hacer una pregunta breve; no pedir al usuario que elija un skill.

Cargar solo el skill responsable y sus referencias necesarias. Consultar una biblioteca compartida no activa los flujos del skill que la contiene, aunque el recurso enlace a su propio `SKILL.md`: esas remisiones explican su uso de origen, no transfieren la tarea. No encadenar dirección creativa, QA y diseño como fases obligatorias. Respetar una elección explícita del usuario y, al cambiar de tarea, seleccionar de nuevo; una iteración del mismo arte conserva su skill y encargo.

Usar un ejemplo no determina el skill: crear una escena nueva y diseñar una pieza publicitaria nueva conservan sus respectivas rutas. Las restricciones de un perfil externo solicitado se incorporan al encargo si están disponibles; no activar automáticamente ese perfil por el tema ni importar el contrato de conservación de una reparación. Al iterar, reemplazar decisiones modificadas sin concatenar las versiones anteriores.

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
En la fase correspondiente de Luces:
- dirección creativa → `references/CORE_METODO_GORVET.md`;
- redacción del prompt → `references/CORE_ESTRUCTURA_PROMPT.md` y `references/WORKFLOWS_CONTROL_CALIDAD.md`;
- problema concreto → `references/CORE_ERRORES_REGLAS.md`.

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
