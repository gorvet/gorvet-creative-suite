---
name: poster-promotional-design
description: Procesa briefs para pósters y piezas promocionales estáticas: selecciona contenido, resuelve jerarquía y dirección gráfica, y prepara el encargo que guía su ejecución. Úsala para pósters, posts, stories, flyers, anuncios gráficos, banners estáticos, portadas promocionales e invitaciones visuales. Si se solicita el arte y hay herramientas disponibles, ejecuta el encargo y revisa el resultado.
---

# GORVET — Poster & Promotional Design

## Selección dentro del complemento

Cuando el usuario invoca GORVET Creative Suite para una pieza promocional estática con texto y layout, esta skill dirige la tarea aunque no se mencione su nombre interno. Incluye stories y estados de WhatsApp. No iniciar los dos flujos de `luces-camara-prompt` ni generar directamente desde la solicitud: aplicar el flujo operativo de esta skill.

Si se pide reparar un prompt existente por un fallo concreto, leer `../image-prompt-qa/SKILL.md` cuando esté disponible. Si se pide únicamente dirección de escena o un prompt de imagen sin diseño promocional, usar `../luces-camara-prompt/SKILL.md`. Una revisión del arte o su jerarquía permanece en esta skill. Las consultas de bibliotecas compartidas no cambian estas responsabilidades.

## Propósito

Skill especializado en **pósters y piezas promocionales estáticas**. Convierte una idea, un texto, una promoción o un brief parcial en una dirección gráfica clara, legible y visualmente intencional.

Su objetivo no es “decorar” el contenido ni llenar el formato. Debe **tomar decisiones de diseño**: seleccionar, priorizar, resumir, jerarquizar, componer y eliminar lo que no aporte.

Debe evitar la apariencia genérica asociada a diseño producido automáticamente por IA sin caer en un minimalismo obligatorio ni prohibir recursos expresivos. Un recurso visual puede usarse si tiene una función conceptual, narrativa, jerárquica o de marca.

---

## Alcance

Usar para:
- pósters y carteles;
- publicaciones gráficas para Instagram y otras redes;
- stories;
- flyers;
- anuncios promocionales estáticos;
- banners estáticos;
- portadas promocionales;
- invitaciones y piezas gráficas de campaña;
- otras piezas promocionales estáticas donde convivan contenido, imagen, tipografía y composición.

El formato no define el skill. Lo define la naturaleza de la pieza: **comunicación gráfica promocional estática**.

---

## Relación con GORVET Creative Suite

Este skill puede funcionar de forma autónoma, pero está preparado para integrarse en GORVET Creative Suite.

**No duplicar ni modificar `luces-camara-prompt`.**

Cuando necesite ampliar criterios ya documentados sobre carteles, portadas, composición, relación de aspecto, espacio negativo, integración o reserva para texto, consultar los recursos existentes de `luces-camara-prompt` en el apartado correspondiente.

Referencia primaria para pósters y portadas:
- `../luces-camara-prompt/references/USE_CASES_DISENO_EDITORIAL_MOCKUPS_LOGOS.md` → apartado **Carteles / portadas**.

Si hace falta resolver encuadre, composición o relación de aspecto, consultar además `../luces-camara-prompt/references/TECHNICAL_ENCUADRE_COMPOSICION_RATIO.md`.

Estos recursos son opcionales y se consultan solo si el skill hermano está instalado junto a este. Si no está disponible, resolver la pieza con las bibliotecas locales de `references/`; no exigir su instalación ni encadenar otros skills.

Usar esos recursos como apoyo. **No copiar su contenido dentro de este skill ni reconstruir el Método GORVET aquí.**

---

## Principio rector

Antes de diseñar, responder internamente:

1. ¿Qué debe entenderse primero?
2. ¿Qué debe recordarse?
3. ¿Qué acción debe provocar la pieza?
4. ¿Qué contenido es obligatorio?
5. ¿Qué puede reducirse o desaparecer?
6. ¿Qué recurso visual sostiene el concepto y cuál solo está decorando?

Una pieza puede ser expresiva, saturada, experimental, tipográfica o maximalista si esa decisión está justificada. **Lo que se rechaza es el uso automático de recursos visuales sin función.**

---

## Brief: necesario como estructura, no como barrera

El skill debe construir internamente un brief suficiente para trabajar, pero **no obligar al usuario a completar un cuestionario**.

Resolver, si es posible a partir de la solicitud:
- objetivo de la pieza;
- público;
- mensaje principal;
- acción esperada;
- formato o canal;
- contenido obligatorio;
- identidad visual o referencias disponibles;
- tono o carácter deseado.

### Regla de fricción mínima

- Si la solicitud contiene información suficiente, **proceder sin preguntar**.
- Inferir decisiones visuales razonables cuando no alteren hechos, marca o intención.
- Preguntar solo cuando una ausencia cambie sustancialmente el resultado o impida diseñar con precisión.
- Agrupar las dudas críticas en una sola intervención breve.
- No pedir al usuario datos que puedan resolverse con criterio de diseño.
- No inventar fechas, precios, lugares, nombres, condiciones legales, promociones ni datos comerciales ausentes. Usar un marcador o señalar el dato faltante cuando sea imprescindible.

El usuario puede aportar un brief completo si desea mayor control, pero no es requisito de entrada.

---

## Intervención editorial sobre el contenido

El contenido entregado por el usuario **no es una orden de incluirlo todo**.

Distinguir antes de componer el mensaje público, los datos necesarios para decidir o actuar, el contexto que orienta el diseño y las instrucciones dirigidas al asistente. No convertir automáticamente comentarios, anécdotas o bromas en copy. Seleccionar contenido por su utilidad para el público y el objetivo; la selección precede a la jerarquía visual.

Antes de componer, clasificar internamente la información en:
- **dominante**: mensaje que gobierna la pieza;
- **apoyo**: completa o contextualiza el mensaje;
- **información funcional**: fecha, precio, lugar, CTA u otros datos necesarios;
- **prescindible visualmente**: información válida que no necesita aparecer en la pieza principal.

El skill puede:
- resumir;
- condensar;
- reorganizar;
- agrupar;
- reducir repeticiones;
- convertir párrafos en una formulación breve;
- retirar contenido secundario del plano principal;
- recomendar mover información extensa al copy, caption, landing o pieza complementaria.

En el contenido seleccionado, preservar sin alterar los hechos siguientes. Conservar además todo texto declarado obligatorio y comunicar las condiciones que cambien la oferta o el acceso al servicio; preservar datos no significa publicar cada frase del brief:
- nombres propios;
- fechas y cifras;
- precios;
- condiciones comerciales;
- datos legales;
- direcciones;
- URLs;
- nombres de marca o producto;
- cualquier texto que el usuario marque como literal u obligatorio.

Consultar `references/CONTENT_HIERARCHY.md`.

---

## Jerarquía y composición

Cada pieza debe tener un recorrido de lectura reconocible.

Por defecto:
1. un foco dominante;
2. un nivel de apoyo;
3. un bloque funcional o de detalle cuando haga falta;
4. un CTA solo si la pieza lo necesita.

No convertir cada dato en un elemento protagonista.

Jerarquizar es ordenar los textos por su importancia para el objetivo y hacer visible ese orden mediante tamaño, grosor, color, contraste, posición y agrupación. Definir qué se lee primero, qué apoya y qué se consulta después. Los datos obligatorios deben conservarse, pero no tienen todos la misma importancia visual. Diferenciar niveles sin sacrificar legibilidad y relacionarlos con el peso de la imagen. Consultar `references/CONTENT_HIERARCHY.md` para aplicar estos criterios.

Elegir la composición según contenido e intención, no según una plantilla repetida. La solución puede ser centrada, asimétrica, editorial, tipográfica, fotográfica, modular, de alto contraste, experimental u otra, siempre que mantenga lectura y propósito.

El espacio negativo es una herramienta compositiva. **No rellenar una zona vacía solo porque está vacía.**

Consultar `references/VISUAL_SYSTEM.md`.

---

## Tipografía

La tipografía debe construir jerarquía y carácter, no ruido.

Principios:
- preferir una familia bien utilizada antes que varias familias compitiendo;
- introducir una segunda voz tipográfica solo cuando exista una razón clara;
- construir contraste mediante escala, peso, ancho, tracking, caja, posición y ritmo antes de recurrir a efectos;
- mantener coherencia entre título, apoyo, datos y CTA;
- elegir mayúsculas, minúsculas o caja de oración según función, tono y legibilidad; no usar mayúsculas en todos los niveles por defecto ni confundirlas con importancia;
- evitar que cada palabra tenga un tratamiento diferente;
- no inclinar, deformar, contornear o decorar texto automáticamente para “dar dinamismo”.

Tipografías góticas, script, display, condensadas, ultra-bold, inclinadas o experimentales no están prohibidas. Exigen una justificación conceptual y deben preservar lectura y coherencia.

---

## Iconos y elementos gráficos

No añadir iconos por costumbre.

Un icono, figura, flecha, estrella, brochazo, sticker, marco, línea, textura, objeto 3D, destello, blob, patrón o forma abstracta debe cumplir al menos una función:
- identificar;
- jerarquizar;
- agrupar;
- dirigir la mirada;
- reforzar el concepto;
- expresar la identidad visual;
- aportar narrativa o información.

La función por sí sola no basta: comparar el recurso con una solución sin él. Si la tipografía, la posición o el espacio resuelven igual de bien esa función, preferir esa solución. No justificar a posteriori un brochazo como «jerarquía» o un sello como «identificación» si no mejora la comunicación en esta pieza. La excepción expresiva debe apoyarse en el brief, la marca o el concepto concreto, no en palabras genéricas como «impacto» o «dinamismo».

Elegir los recursos a partir del contenido y sus prioridades, sin adoptar un layout fijo para una categoría. Mejorar una fotografía no implica crear vistas del sujeto o producto que no estén documentadas.

---

## Control anti-AI-style

Antes de aceptar una dirección visual, detectar patrones genéricos o acumulativos típicos de diseño automático.

No aplicar una lista negra mecánica. Evaluar **uso + contexto + función**.

Consultar `references/ANTI_AI_STYLE_QA.md`.

Regla general:

> Un recurso visual no se rechaza por existir; se rechaza cuando aparece sin una razón de comunicación, concepto, composición o marca.

---

## Flujo operativo: del brief a la ejecución

El asistente aplica este skill antes de llamar a una herramienta de imagen o diseño. El generador no recibe ni interpreta automáticamente las bibliotecas del skill: las decisiones deben quedar expresadas en el encargo que el asistente le envía. No utilizar el mensaje original del usuario como prompt de generación ni añadirle simplemente «aplica el skill».

### 1. Interpretar y seleccionar
Determinar objetivo, público, formato y restricciones. Separar contenido público, contexto e instrucciones; decidir qué se incluye, se resume o se traslada fuera del arte. Consultar `references/CONTENT_HIERARCHY.md`. Preguntar solo por ausencias o ambigüedades que cambien hechos, condiciones o intención. No generar una pieza final mientras una aclaración imprescindible esté pendiente.

### 2. Resolver la dirección gráfica
Elegir estilo, foco, jerarquía textual, composición, tipografía y recursos pertinentes. Consultar `references/VISUAL_SYSTEM.md`. Concretar las relaciones de importancia con diferencias de escala, peso, caja, contraste, posición y agrupación. La dirección debe estar resuelta antes de ejecutar; no pedir al generador que seleccione por su cuenta qué contenido importa o qué estilo corresponde.

### 3. Preparar y revisar el encargo de ejecución
Construir internamente un encargo compacto con:

- **Formato:** soporte, orientación y proporción o dimensiones necesarias.
- **Texto visible:** lista cerrada de textos finales; para cada bloque, indicar función, importancia y tratamiento, diferenciándolo de las instrucciones.
- **Composición:** foco, recorrido, posiciones y relaciones de escala entre imagen y textos, agrupaciones y espacio útil.
- **Lenguaje visual:** estilo elegido, paleta por función, tipografía y tratamiento de imagen.
- **Referencias:** cuáles se utilizarán y qué debe conservarse de cada una; adjuntarlas a la herramienta cuando lo admita.
- **Límites pertinentes:** recursos excluidos de esta dirección y elementos que no deben inventarse.

No adjuntar el brief bruto, comentarios descartados ni el razonamiento interno. Los datos trasladados al caption quedan fuera del encargo de imagen. Indicar que solo los textos de la lista son contenido visible y que no se añadan eslóganes, etiquetas, iconos, escenas o personajes que no se hayan decidido.

Revisar este encargo con `references/ANTI_AI_STYLE_QA.md`: debe contener la selección editorial y traducir las decisiones a instrucciones ejecutables, no limitarse a «buena jerarquía», «sin estilo IA» o una lista de prohibiciones. Si falta una decisión necesaria, resolverla antes de llamar a la herramienta.

### 4. Ejecutar según la petición
Si el usuario pide una imagen o un arte y hay una herramienta apropiada disponible, enviarle el encargo procesado y las referencias pertinentes. Si pide solo un prompt, copy, dirección o crítica, entregar ese resultado sin generar una imagen. No añadir una aprobación obligatoria entre estas fases; proceder cuando haya información suficiente y autorización para la tarea.

El campo de instrucciones o prompt de la llamada a la herramienta debe contener ese encargo como fuente de dirección. No sustituirlo por un resumen del mensaje del usuario, no anexar ese mensaje y no remitir a archivos del skill que el generador no pueda leer. Los textos seleccionados pueden coincidir con los del usuario; lo que debe cambiar es que su inclusión y tratamiento ya estén decididos. Antes de enviar, comprobar que todos los bloques visibles y sus prioridades están especificados y que el material excluido no reaparece en la llamada.

Si no hay herramienta de ejecución, entregar el encargo utilizable y señalar que la imagen no se ha generado. Este skill no instala herramientas ni exige otro skill como intermediario.

### 5. Verificar y entregar
Si el resultado es accesible, contrastar el arte con el encargo: textos y datos, selección, jerarquía, composición, fidelidad de referencias y recursos excluidos. Conservar lo que funciona y corregir la capa que se desvió. La corrección también se envía como encargo procesado; no volver al brief bruto ni aceptar una plantilla genérica porque la fotografía esté lograda.

Si la herramienta permite corregir, realizar una corrección dirigida y volver a comprobar. Si persiste una desviación relevante, indicar qué sigue fallando y proponer composición o ajuste en un editor, sin ciclos de regeneración indefinidos ni afirmar que el arte está validado. Si no se puede inspeccionar el resultado, declarar esa limitación. Entregar el arte o el encargo solicitado con información breve y útil; la selección y la revisión internas no se convierten en un cuestionario o una auditoría pública.

Si la selección trasladó información necesaria a un caption o texto complementario, entregarlo junto al arte para que esa información no se pierda. En una revisión o iteración, actualizar el encargo existente y mantenerlo como referencia de ejecución; no reiniciar desde el mensaje original.

---

## Salida por defecto

Si el usuario pide crear una imagen o un arte, aplicar el flujo de ejecución y entregar el resultado cuando exista una herramienta disponible. Cuando pide desarrollar la dirección de una pieza sin solicitar ejecución, responder de forma compacta con:

- **concepto / dirección visual**;
- **contenido final recomendado**, ya intervenido y jerarquizado;
- **estructura del layout**;
- **dirección tipográfica**;
- **tratamiento visual principal**;
- **elementos que conviene evitar en esa pieza concreta**.

No mostrar una auditoría extensa, puntuaciones o checklist salvo que el usuario las solicite.

Si el usuario pide únicamente una idea, copy, estructura, crítica, prompt o revisión, entregar solamente lo necesario para esa tarea.

---

## Iteración

Cuando el usuario pida cambios:
- conservar las decisiones que funcionan;
- modificar solo la capa afectada;
- no reconstruir toda la pieza si basta con ajustar contenido, jerarquía, tipografía o composición;
- no reintroducir elementos ya eliminados sin una razón nueva;
- si el usuario pide deliberadamente una dirección expresiva o maximalista, respetarla y controlar su jerarquía en lugar de simplificarla automáticamente.

Distinguir refinamiento de alternativa: una corrección conserva lo que funciona; una alternativa de diseño cambia una decisión estructural reconocible, como el foco, la relación texto-imagen o la distribución. Cambiar solo la luz, el fondo o el recorte mantiene el mismo layout y debe presentarse como una variación de ese diseño. Si el usuario rechaza sellos o inclinaciones, no repetirlos en la siguiente versión.

---

## Validación interna final

Antes de entregar, comprobar:
- ¿se entiende qué mirar primero?;
- ¿hay un mensaje dominante real?;
- ¿el contenido fue editado en lugar de simplemente acomodado?;
- ¿cada tratamiento tipográfico tiene una función?;
- ¿cada elemento decorativo puede justificarse?;
- ¿hay suficiente respiración para el tipo de pieza?;
- ¿el diseño responde al concepto y no a una plantilla automática?;
- ¿se evitó añadir iconos o efectos por costumbre?;
- ¿la pieza sigue siendo legible y accionable?;
- ¿algún elemento podría eliminarse sin perder información o intención? Si sí, considerar eliminarlo.

La validación es interna. No mostrarla salvo petición explícita.
