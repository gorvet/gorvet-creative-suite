---
name: poster-promotional-design
description: Diseña carteles, anuncios, flyers y piezas gráficas de productos, personas o promociones, con o sin texto externo. Construye jerarquía, composición y tipografía desde el contenido seleccionado por estrategia. Úsalo para el diseño publicitario o gráfico y su revisión; bajo gorvet-creative-director aporta el layout sin abrir otro flujo.
---

# GORVET — Diseño gráfico y dirección publicitaria

Construye la comunicación como una pieza completa. Imagen y tipografía se diseñan conjuntamente desde un concepto y contenido seleccionados. Estandariza el criterio de dirección, no una composición, acabado o cantidad de elementos idénticos para todos los encargos.

## Trabajo en cadena y método

Aplica el [contrato común](../gorvet-creative-director/references/SPECIALIST_CONTRACT.md). Recibe concepto, contenido seleccionado, sistema visual y esquema global cuando estén resueltos. Aporta construcción gráfica y tipográfica. Conserva G/V/T; concreta recursos de lectura y sus relaciones para E. La distribución debe probar el texto real: si revela un conflicto, devuelve una modificación concreta al director y a arte, sin cambiar por su cuenta el mensaje o el medio.


## Responsabilidad y contexto

Cuando el [director creativo](../gorvet-creative-director/SKILL.md) consulta este skill, recibe sus decisiones vigentes y devuelve el diseño resuelto. No reinicies estrategia, aprobación o ejecución. Si el usuario pide directamente un cartel, el [director creativo](../gorvet-creative-director/SKILL.md) conduce ese alcance y consulta este rol para la construcción gráfica. No crees dos responsables para la misma pieza.

Si ya hay una estrategia seleccionada, compón desde ella y señala cualquier conflicto material. Si falta, resuelve la selección mediante [estrategia creativa](../gorvet-creative-strategy/SKILL.md) o [CONTENT_HIERARCHY.md](references/CONTENT_HIERARCHY.md). Presenta una recomendación editorial, no el brief íntegro por defecto: literales de imagen, copy de apoyo con destino real y omisiones pertinentes. Un dato verdadero no pertenece automáticamente al arte.

## Elegir la dirección de la pieza

Selecciona la biblioteca por la función principal, no por recibir una foto o un texto:

| Función principal | Biblioteca | Prioridad |
| --- | --- | --- |
| Presentar o hacer deseable un objeto | [Productos](references/ART_DIRECTION_PRODUCTS.md) | Reconocimiento y argumento del producto. |
| Comunicar mediante identidad o acción humana | [Personas](references/ART_DIRECTION_PEOPLE.md) | Papel de la persona o actividad en el anuncio. |
| Comunicar una oferta, negocio, evento o servicio | [Promociones](references/ART_DIRECTION_PROMOTIONS.md) | Proposición seleccionada y comprensión de la comunicación. |

En un encargo mixto elige qué lidera y aplica los requisitos pertinentes de las demás familias. No acumules tres campañas en una imagen. Una instrucción expresa o una identidad existente prevalecen sobre los valores por defecto de la biblioteca.

## Diseñar antes de compilar

La pieza solo pasa a generación mediante [PRODUCTION_GATE.md](../gorvet-creative-director/references/PRODUCTION_GATE.md). Entrega posiciones, escalas y construcción de cada literal; los recursos gráficos que se usarán deben estar descritos, no añadidos por el generador. No acepta «textos establecidos en la propuesta» como contenido de ejecución: incluye los textos reales. Una selección que conserve todo un brief abundante vuelve a evaluación editorial antes de repartirlo en bloques.

Lee [VISUAL_SYSTEM.md](references/VISUAL_SYSTEM.md) y resuelve la pieza con el contenido real. Una intención genérica o un inventario de reglas no constituyen una dirección terminada. Antes de pasar a producción deben estar decididos:

- Protagonista y argumento visual; relación entre lo que se ve y lo que se comunica.
- Formato, encuadre, posiciones, escala relativa, recortes y superposiciones.
- Literales seleccionados, ubicación, extensión, agrupación, alineación, voz tipográfica y diferencias de peso.
- Fondo, espacios de lectura, color, contraste y recursos gráficos que realmente aparecerán.
- Papel de las referencias, atributos protegidos y transformaciones permitidas.

Estas decisiones gobiernan los componentes presentes; no exigen añadirlos. Si no necesita copy externo, decide su ausencia. No inventes slogans, beneficios o llamadas a la acción para completar una estructura.

Evalúa también el atractivo: qué forma, relación, escena o tratamiento hace detenerse y sostiene el interés. Una foto correcta y textos legibles pueden seguir sin fuerza publicitaria. Las operaciones de [VISUAL_REFERENCES.md](references/VISUAL_REFERENCES.md) son recursos, no plantillas. Una composición centrada, asimétrica, densa o sencilla puede ser pertinente si comunica con intención.

Para construir la imagen que sostiene el diseño, consulta [dirección de imagen](../image-art-direction/SKILL.md); cuando la captura fotográfica importe, consulta [fotografía](../photography-direction/SKILL.md). Ambos trabajan dentro de las zonas y relaciones acordadas. Usa [identidad y referencias](../brand-reference-direction/SKILL.md) si no están claros los atributos protegidos. Consultar no importa otros flujos ni autoriza reorganizar el diseño aprobado.

## Evaluar y transmitir

Aplica [ANTI_AI_STYLE_QA.md](references/ANTI_AI_STYLE_QA.md) antes de compilar. Revisa selección, interés, peso conjunto, legibilidad, fidelidad y coherencia. Si falla una relación, modifica el diseño; no añadas una frase exigiendo buena jerarquía.

Entrega al director el layout y sus decisiones, junto con los controles que deberá conservar la ejecución. [EXECUTION_BRIEF.md](references/EXECUTION_BRIEF.md) guía el traspaso y [Luces](../luces-camara-prompt/SKILL.md) compila cuando corresponde. Si el prompt admite una composición contraria a la elegida, falta un control espacial o gráfico. El copy de apoyo y los descartes no deben llegar al generador.

## Producción y revisión

El responsable aplica el protocolo común: dirección y prompt visibles, aprobación inicial salvo ejecución directa expresa, envío del prompt mostrado y verificación de la imagen. Las consultas internas no añaden otra aprobación ni convierten un encargo de arte en entrega de texto.

Tras producir, utiliza [crítica visual](../visual-quality-review/SKILL.md) para comparar el resultado con el diseño y sus fuentes. Corrige la causa concreta conservando lo que funciona y comprueba la nueva salida. Una revisión del prompt no valida el arte. Si no puedes ejecutar o inspeccionar, declara lo pendiente.

Al iterar, reemplaza la decisión responsable; no acumules refuerzos ni reglas por producto. Corrige el criterio general que explica el fallo y comprueba que sirva a las demás familias.

## Procedimiento de desarrollo

Para construir layout, tipografía y adaptaciones con contenido real aplica [GRAPHIC_CONSTRUCTION.md](references/GRAPHIC_CONSTRUCTION.md). Consulta solo el modo pertinente.

Para varias lenguas, escrituras mixtas o recorrido RTL aplica [MULTILINGUAL_RTL.md](references/MULTILINGUAL_RTL.md): literales fuente, dirección de bloques, jerarquía entre versiones, tipografía y verificación. No refleja automáticamente toda la pieza ni altera el orden lógico del texto para simular su lectura.
