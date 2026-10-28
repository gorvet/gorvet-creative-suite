# Diseño multilingüe y bidireccional

## Activar por necesidad

Aplica este procedimiento cuando una pieza contenga varios idiomas, distintos sistemas de escritura o lectura de derecha a izquierda. No añade traducciones ni una versión árabe a un encargo que no las pide. Gráfica posee la construcción y lectura; concepto/contenido conserva los literales y su selección; identidad protege el logotipo; crítica inspecciona la salida.

## Preparar el contenido

Identifica idioma, variante regional, escritura y literal de cada bloque. Distingue texto aportado, traducción solicitada y transliteración. No inventes una traducción para rellenar un hueco ni sustituyas grafías de nombres o caracteres parecidos por su apariencia. Si falta una traducción esencial, devuelve esa necesidad al director. Una revisión de composición no acredita corrección lingüística en un idioma que no se puede revisar con fiabilidad.

Conserva una fuente textual en orden lógico para cada literal. No inviertas manualmente cadenas para simular RTL ni uses texto reflejado. En escritura árabe, el recorrido del texto principal es RTL, mientras los números y segmentos latinos pueden conservar recorrido LTR; la pieza debe resolver ambos. [W3C: requisitos de composición árabe y persa](https://www.w3.org/International/alreq/#h_textdirection).

## Construir la jerarquía

Decide idioma principal, peso de las versiones, orden de lectura y relaciones entre bloques. No exige tamaños idénticos: busca jerarquía y peso óptico comparables según la función. Un texto traducido puede ocupar otra extensión; recompón cortes y espacios antes de reducirlo hasta volverlo ilegible. Mantén precio, unidad, condición y llamada asociados en cada idioma.

En una pieza predominantemente RTL, prueba recorrido, agrupación y anclajes desde ese contexto. No reflejes automáticamente fotografía, marcas, símbolos, números ni todos los elementos del layout. La adaptación responde a la lectura y al significado, no a una transformación horizontal de la imagen entera.

## Tipografía y mezcla de escrituras

Selecciona fuentes con cobertura y formas correctas para el contenido real. En árabe/persa comprueba enlaces de letras, marcas y colocación de signos; evita aplicar espaciado entre letras como si fuera texto latino si rompe su construcción. Prueba interlineado, ascendentes, descendentes y signos en el render, no solo en el nombre de la fuente. El documento de [requisitos de composición árabe y persa del W3C](https://www.w3.org/International/alreq/) delimita esas necesidades; no extrapoles todas sus reglas a hebreo u otros sistemas.

Comprueba los fragmentos mixtos: números, moneda, fechas, paréntesis, nombres latinos, URL y teléfonos. Si una herramienta de maquetación admite dirección por bloque y aislamiento de fragmentos, usa esos controles y verifica el render. No introduzcas caracteres invisibles en literales aprobados como arreglo genérico. Cuando el soporte solo permita texto plano y necesite controles Unicode, documenta el cambio y verifica su efecto; los aisladores evitan ciertas interferencias entre segmentos. [W3C: controles Unicode de bidireccionalidad](https://www.w3.org/International/questions/qa-bidi-unicode-controls).

## Traspaso a producción

Entrega a compilación cada literal con idioma, dirección del bloque, posición, tratamiento y relación con sus equivalentes. No le envíes traducciones descartadas ni una cadena visualmente invertida. Si el generador no conserva las formas y el orden, la corrección debe preservar el texto fuente y el layout; usa acabado determinista solo si está disponible. Una simulación de caligrafía ilegible no cumple una petición de texto real.

## Revisión y retorno

Inspecciona el tamaño de uso y amplía los textos: integridad de palabras, orden de lectura, cortes, conexiones, signos, números, condiciones y coexistencia de versiones. Compara con los literales fuente, no con una transcripción inventada de la salida. Para vídeo/motion, prueba también permanencia y recorrido temporal con dirección audiovisual.

Un error de traducción vuelve a contenido; un error de distribución o formas, a gráfica; una inversión o pérdida introducida en el prompt, a compilación; un incumplimiento de la salida, a corrección de ejecución. Si no puede verificarse una escritura o detalle esencial, registra ese límite y no declares validado el texto. No crea un segundo flujo de aprobación.
