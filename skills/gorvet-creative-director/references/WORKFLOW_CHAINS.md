# Cadenas de trabajo y retorno

Cada recorrido produce entradas concretas para el siguiente. El director puede omitir un trabajo que ya esté resuelto y documentado; no omite controles pendientes. Las consultas a identidad pueden adelantarse si sus restricciones condicionan la estrategia o el arte.

La entrada común es [recepción del brief](BRIEF_INTAKE.md): el director conversa con el usuario cuando falten datos materiales, conserva hechos y restricciones y entrega a estrategia un encargo utilizable. El brief del cliente, la orientación estratégica y la especificación de arte son entregables sucesivos; no tres versiones que puedan contradecirse.

## Pieza gráfica nueva

Brief → estrategia y selección editorial → identidad si hay fuentes → dirección de arte y esquema global → fotografía si el medio lo necesita y diseño gráfico con el texto real → integración y preflight de arte → compilación y comprobación del traspaso → propuesta y aprobación → producción → crítica visual.

Estrategia entrega la selección de imagen y apoyo, no una versión publicitaria de cada frase. Arte entrega una solución visible, no etiquetas de estilo. Fotografía y gráfica devuelven conflictos al mismo esquema; no trabajan con dos composiciones incompatibles. Compilación recibe la versión integrada, no todas las propuestas previas. Un fallo de selección vuelve a estrategia; un fallo tipográfico vuelve a gráfica; una instrucción ausente vuelve a compilación.

## Fotografía con intención ya definida

Brief y referencias → delimitación de identidad cuando corresponda → fotografía y preflight pertinente → compilación y comprobación del traspaso → propuesta y aprobación → producción → crítica visual.

Consulta estrategia o arte solo si falta el argumento o el tratamiento global. No es obligatorio añadir otra dirección de escena a un retrato o una captura ya definidos. Fotografía resuelve la captura y conserva intención, identidad y uso.

## Ilustración, imagen conceptual o visualización

Intención → estrategia si falta el argumento → arte → identidad o geometría de referencia si corresponde → integración y preflight → compilación y comprobación del traspaso → propuesta y aprobación → producción → crítica visual.

Fotografía no interviene por defecto. Diseño gráfico solo interviene si existe una decisión tipográfica o de comunicación gráfica que resolver. Un render conceptual no acredita planos, medidas ni mapas técnicos.

## Campaña, carrusel o serie

Objetivo → estrategia y concepto común → narrativa y función de piezas → identidad y constantes → sistema de arte → ejecución de cada pieza con los especialistas pertinentes → compilación por pieza → aprobación del conjunto acordado → producción y revisión individual → revisión de continuidad.

No se aleatoriza la jerarquía. Las variaciones responden a la función de cada pieza. Un cambio de formato obliga a revisar distribución y recortes; no a inventar otra campaña. El apoyo de publicación no se integra automáticamente en todas las imágenes.

## Edición acotada

Base aprobada y petición → contrato de intervención → especialista del defecto si hace falta → compilación de edición → propuesta visible según el protocolo → edición → comparación con la base y revisión del conjunto.

No se reabre estrategia. Si solo cambia una palabra, no se propone otra escena. Se identifican objetivo, cambio y contenido protegido según [EDIT_SCOPE.md](../../image-art-direction/references/EDIT_SCOPE.md). Tras un fallo de alcance se vuelve a la base aprobada; no se encadenan deformaciones de salidas fallidas.

## Revisión sin producción

Arte disponible y propósito → crítica visual → referencias o especialista pertinente si una duda afecta al juicio → veredicto y corrección recomendada.

No genera, no compila un prompt por defecto y no exige una nueva propuesta creativa para poder criticar.

## Depuración textual

Prompt existente y cambios solicitados → QA textual → versión consolidada.

No reinicia GORVET como ideación, no llama a fotografía para añadir técnica y no interpreta la presencia de un prompt como permiso para generar.

## Acabado determinista cuando importe la exactitud

Si el generador no conserva tipografía, marca o geometría necesarias, el director evalúa producir la base visual y completar el acabado mediante herramientas de maquetación disponibles. Diseño gráfico define el layout; el entorno de producción construye y renderiza; crítica visual verifica el resultado. No se declara ese acabado realizado si no existen herramientas ni un render inspeccionable.
