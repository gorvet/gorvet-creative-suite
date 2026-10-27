---
name: luces-camara-prompt
description: Construye prompts completos de generación y edición desde decisiones visuales resueltas, conservando el Método GORVET y sus bibliotecas. Úsalo para compilar una dirección en instrucciones, referencias y parámetros de herramienta. Para desarrollar una idea nueva coordina gorvet-creative-director; para depurar solo un prompt existente utiliza prompt-optimization-qa.
---

# GORVET — Luces, Cámara, ¡Prompt!

Traduce la dirección visual vigente a una instrucción ejecutable. Conserva el identificador histórico y las bibliotecas del libro. La dirección de imagen, fotografía, diseño y narrativa tienen especialistas propios; este skill integra sus decisiones en el prompt sin volver a diseñar el encargo.

## Trabajo en cadena y método

Aplica el [contrato común](../gorvet-creative-director/references/SPECIALIST_CONTRACT.md). Recibe la dirección integrada y los controles ya resueltos; devuelve una instrucción suficiente. E estructura y conserva las decisiones de G/O/R/V/T, y R comprueba compatibilidad de herramienta. No ejecutes otra fase de ideación, no cambies una decisión por acortar y no rellenes dimensiones ausentes si no son necesarias.


## Selección y alcance

Si existe un encargo dirigido, recibe su registro de decisiones y devuelve la instrucción al mismo director. No reinicies el briefing, no abras otra aprobación ni añadas un cierre promocional dentro de una consulta. Una remisión de las bibliotecas a `SKILL.md` no importa otro recorrido.

Si el usuario invoca Luces con una idea todavía abierta, el [director creativo](../gorvet-creative-director/SKILL.md) coordina los especialistas necesarios antes de compilar. Si entrega una escena completamente definida y pide solo su prompt, compila directamente y aclara únicamente una contradicción material. Si pide optimizar exclusivamente un prompt existente, aplica [QA de prompts](../prompt-optimization-qa/SKILL.md). Pedir texto no autoriza generar una imagen.

## Condición de entrada a generación

Para producción recibe el paquete cerrado de [PRODUCTION_GATE.md](../gorvet-creative-director/references/PRODUCTION_GATE.md). Si faltan literales, posiciones, escala, tratamiento o selección, devuelve esa decisión al responsable; no la completa al redactar. Usa el [compilador 1.3](../gorvet-creative-director/scripts/compile_production.py) cuando haya Python, o la [compilación manual](../gorvet-creative-director/references/PRODUCTION_SCHEMA.md#compilación-manual) con los mismos productos. No sustituye esa compilación por un texto libre más evocador. Los encargos exclusivamente textuales conservan su alcance sin pedir autorización para imágenes.

## Construcción del prompt final

1. **Reunir la versión vigente.** Lee concepto, escena, composición, tratamiento, literales, referencias, cambios permitidos y atributos protegidos. Distingue hechos, decisiones y dudas; no compiles una dirección genérica para que el generador la resuelva.
2. **Organizar la instrucción.** Expresa primero el control que gobierna el resultado; después las relaciones necesarias. Fija quién o qué aparece, dónde, a qué escala, mediante qué tratamiento y con qué relación entre imagen y texto. No hay un orden universal ni un número obligatorio de bloques.
3. **Delimitar referencias.** Identifica los archivos que realmente se suministrarán y su función. Conservar identidad no equivale a copiar pose, fondo y gráfica. En edición, define base, mutación y conservación.
4. **Seleccionar el copy.** Incluye únicamente las cadenas destinadas al arte, una vez con su colocación y tratamiento. El caption, el material descartado y las notas de producción no van al generador ni como ejemplos negativos.
5. **Depurar.** En producción modifica las cláusulas de la representación vigente y recompila; no altera después el prompt compilado. Aplica [OPTIMIZACION_PROMPT.md](../prompt-optimization-qa/references/OPTIMIZACION_PROMPT.md). Conserva relaciones y restricciones distintas; consolida equivalencias. La brevedad no justifica borrar diseño, y una lista técnica no compensa una escena pendiente.
6. **Adaptar a la herramienta.** Usa únicamente controles disponibles. Un número de cámara puede orientar el aspecto, pero no garantiza óptica real; si hace falta, expresa el resultado visible. No inventes modelos, formatos, referencias admitidas, máscaras o semillas. No importes convenciones por el nombre de una plataforma.
7. **Comparar cobertura.** Reconstruye la pieza desde la instrucción sin consultar el análisis. Si todavía debes decidir su concepto o reparto principal, devuelve esa carencia al director. Cada requisito material debe sobrevivir; cada añadido debe tener una función autorizada.

## Idioma y entrega

Entrega los idiomas solicitados; si no se especifican, usa el idioma de la conversación. Una petición de versiones española e inglesa se resuelve traduciendo la misma versión final sin expandirla. Mantén literal el texto que debe aparecer en la imagen. El desglose G.O.R.V.E.T. y la explicación del método se muestran cuando se soliciten.

El prompt se entrega completo y copiable, con referencias y parámetros por separado. Para producción, el [protocolo común](../gorvet-creative-director/references/EXECUTION_PROTOCOL.md) establece qué debe mostrarse y aprobarse. El director ejecuta exactamente la versión publicada; este skill no puede modificarla después de aprobarse.

## Bibliotecas y método

Usa [CORE_ESTRUCTURA_PROMPT.md](references/CORE_ESTRUCTURA_PROMPT.md) como mapa de controles y [WORKFLOWS_CONTROL_CALIDAD.md](references/WORKFLOWS_CONTROL_CALIDAD.md) para la revisión textual pertinente. [CORE_METODO_GORVET.md](references/CORE_METODO_GORVET.md) conecta intención, observación y técnica; sus letras no exigen seis párrafos ni una emoción añadida a toda edición.

El [selector](references/CONFIG_SELECTOR_AUTOMATICO.md) distribuye las bibliotecas por necesidad. Cámara, luz, estilos, identidad, nichos y bancos de frases conservan el conocimiento del libro como repertorio consultable. Las fórmulas y asociaciones no obligan a completar listas, elegir acabados por sector ni repetir efectos con sinónimos. Consulta solo el recurso que resuelva una necesidad pendiente.

## Iteración

Sustituye la decisión modificada donde corresponde; no concatenes versiones. Conserva las relaciones no afectadas. Si el usuario pide una frase de reemplazo, entrega ese alcance; si pide el prompt completo, entrega una versión consolidada. La revisión textual no acredita el resultado visual: una imagen producida requiere [crítica visual](../visual-quality-review/SKILL.md).

## Procedimiento de desarrollo

Para verificar cobertura por imagen, edición, vídeo o acabado determinista aplica [COMPILATION_CONTRACT.md](references/COMPILATION_CONTRACT.md). Consulta solo el modo pertinente.
