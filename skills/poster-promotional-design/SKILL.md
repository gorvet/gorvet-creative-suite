---
name: poster-promotional-design
description: Diseña y dirige pósters y piezas promocionales estáticas con criterio editorial, jerarquía clara y control anti-AI-style. Úsala para pósters, posts, stories, flyers, anuncios gráficos, banners estáticos, portadas promocionales e invitaciones visuales. Interviene el contenido, decide qué debe verse y evita recursos decorativos genéricos o injustificados.
---

# GORVET — Poster & Promotional Design

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

Debe preservar sin alterar:
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

Si su única función es ocupar espacio o “hacer que se vea diseñado”, eliminarlo.

---

## Control anti-AI-style

Antes de aceptar una dirección visual, detectar patrones genéricos o acumulativos típicos de diseño automático.

No aplicar una lista negra mecánica. Evaluar **uso + contexto + función**.

Consultar `references/ANTI_AI_STYLE_QA.md`.

Regla general:

> Un recurso visual no se rechaza por existir; se rechaza cuando aparece sin una razón de comunicación, concepto, composición o marca.

---

## Flujo operativo

### 1. Interpretar
Determinar objetivo, público, mensaje, acción, formato y restricciones a partir de lo disponible.

### 2. Editar contenido
Seleccionar qué entra, qué se resume, qué se agrupa y qué se excluye del plano principal.

### 3. Definir jerarquía
Establecer foco, apoyo, información funcional y CTA cuando corresponda.

### 4. Elegir dirección visual
Definir una dirección gráfica coherente con el contenido y la marca. Evitar mezclar estilos sin necesidad.

### 5. Diseñar estructura
Resolver composición, distribución, relación texto-imagen, escala, espacio negativo y ritmo.

### 6. Resolver tipografía y recursos gráficos
Asignar roles tipográficos y justificar cualquier elemento decorativo, iconográfico o expresivo.

### 7. Auditar
Aplicar el control anti-AI-style y eliminar ruido, redundancia o recursos gratuitos.

### 8. Entregar
Presentar una solución concreta y utilizable. No abrumar al usuario con todo el razonamiento interno.

---

## Salida por defecto

Cuando el usuario pide desarrollar una pieza y no especifica formato de entrega, responder de forma compacta con:

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
