---
name: prompt-optimization-qa
description: Depura prompts de imagen eliminando duplicados semánticos, relleno, expansión innecesaria y contradicciones, sin perder decisiones, restricciones ni textos literales. Úsalo para optimizar un prompt existente. No dirige una escena nueva ni impone convenciones de una plataforma.
---

# QA de optimización de prompts

Optimiza un prompt existente conservando su dirección visual. El resultado debe contener las instrucciones suficientes para reconstruir la misma escena y sus restricciones, con una formulación por control. No genera imágenes ni certifica su resultado.

## Alcance y fuente de verdad

Lee el prompt, los cambios solicitados y el contexto disponible. Si falta el prompt, pídelo sin abrir un nuevo briefing. Distingue requisitos explícitos, decisiones aprobadas y desarrollos opcionales cuya procedencia puedas comprobar. Si solo recibes el prompt, trata sus decisiones visuales concretas como intencionales: no elimines un material, encuadre o atmósfera por preferencia propia.

Una escena nueva corresponde a `../luces-camara-prompt/SKILL.md`; dirigir, producir o revisar una pieza publicitaria estática corresponde a `../poster-promotional-design/SKILL.md`, con o sin texto externo. Puedes depurar solamente el prompt de un cartel conservando íntegros su copy y relaciones de composición, sin rediseñarlo.

Consultar este QA desde otro skill no transfiere la tarea ni activa un segundo flujo. En esa consulta, depura internamente el encargo ya construido y devuelve el control al recorrido que lo solicitó; sus decisiones vigentes de diseño no requieren una aprobación nueva. La regla de entregar solo el prompt y la ausencia de generación describen la tarea independiente de QA, no el cierre del skill que lo consulta.

## Procedimiento de depuración

Lee [OPTIMIZACION_PROMPT.md](references/OPTIMIZACION_PROMPT.md). Trabaja sobre una única versión mediante estas comprobaciones internas:

1. **Inventario de controles:** identifica qué exige el encargo en sujeto, selección, acción, espacio, estilo, luz, composición, referencias y restricciones. No son campos que debas completar.
2. **Duplicados por significado:** localiza formulaciones que controlan el mismo atributo. Conserva la más precisa e integra en ella cualquier detalle distinto de las demás. Una frase puede contener a la vez información repetida y una condición necesaria.
3. **Aporte real:** elimina énfasis, explicaciones y detalles opcionales que no cambian el resultado pedido. Revisa también cláusulas dentro de cada frase; una frase puede aportar una decisión y arrastrar varias equivalencias.
4. **Consolidación:** reemplaza las formulaciones corregidas en su lugar. No concatenes original, modificación y cierre de refuerzo. Si detectas una contradicción material sin resolución autorizada, pregunta solo por esa elección.
5. **Cobertura y ausencia de expansión:** compara con el inventario. Cada control necesario debe seguir teniendo una instrucción ejecutable; ninguna instrucción nueva puede proceder solo de querer embellecer la revisión. Verifica también el texto y el formato exigidos.

No basta con sustituir palabras por sinónimos o afirmar que el prompt quedó optimizado. Si una parte ya es suficiente, consérvala. Un prompt que ya está depurado puede devolverse sin cambios; no fuerces una reescritura para demostrar actividad.

## Entrega

Entrega el prompt optimizado completo en el idioma original o en los idiomas solicitados. Para una petición combinada, incorpora los cambios autorizados antes de depurar. Traduce únicamente la versión cerrada y comprueba que ambas versiones contienen las mismas decisiones, sin ampliaciones ni pérdidas.

Mantén copy literal, atributos protegidos, selección, exclusiones y etiquetas o estructura exigidas por el usuario o un perfil externo aportado. No importes convenciones por el nombre de una plataforma. No impongas una cuota de palabras, un único párrafo o una plantilla universal.

Entrega solo el prompt salvo que se pida explicación o exista una ambigüedad que impida cerrarlo. No añadas cierre promocional, segundo prompt de refuerzo, lista de reglas aplicadas ni garantía de fidelidad visual.
