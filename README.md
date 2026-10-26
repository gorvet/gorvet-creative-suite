# GORVET Creative Director

GORVET Creative Director es un complemento de **Juank de Gorvet** en el formato abierto [Agent Skills](https://agentskills.io/specification), para convertir ideas visuales en prompts de imagen claros, corregir fallos concretos en prompts existentes y dirigir el diseño de piezas promocionales estáticas. Está basado en el **Método G.O.R.V.E.T.** y reúne bibliotecas operativas para dirigir escenas, referencias, estilos, iluminación y composición.

Ayuda a resolver la falta de dirección en peticiones visuales, las instrucciones contradictorias y la pérdida de consistencia al ajustar un prompt.

## Skills incluidos

- **`luces-camara-prompt`**: desarrolla una dirección creativa y, después de que el usuario la apruebe, entrega el prompt en español e inglés. Incluye recursos para retrato, producto, publicidad, ilustración, interiores, retoque y restauración.
- **`prompt-optimization-qa`**: depura la redacción de prompts, especialmente los de Luces, Cámara, ¡Prompt! Elimina redundancia, expansión innecesaria y contradicciones sin perder decisiones, restricciones ni textos literales. No incluye convenciones de Storyface.
- **`poster-promotional-design`**: actúa como director de arte publicitario de pósters, posts, stories, flyers y otras piezas estáticas. Selecciona una de tres bibliotecas de dirección: productos, personas o promociones. Comparte reglas de contenido, concepto, jerarquía, composición, traspaso al generador y revisión del arte, además de cuatro esquemas visuales originales.

Cuando se invoca la suite, el asistente debe seleccionar el skill por el resultado solicitado: diseño de piezas con texto y layout, optimización de un prompt existente o dirección de escena y creación de prompts. No necesitas indicar el nombre interno para pedir un póster o un estado de WhatsApp. La selección depende de que la aplicación cargue las instrucciones actualizadas.

Los tres skills funcionan de forma independiente. Luces consulta las reglas de optimización al redactar; el skill `prompt-optimization-qa` atiende revisiones explícitas de prompts existentes, sin una segunda fase creativa. El QA de posts pertenece a `poster-promotional-design` y revisa comunicación y fidelidad, además de la redacción. Storyface queda fuera de este paquete; sus reglas pueden aportarse como un contrato externo cuando se soliciten.

Los skills de prompts trabajan con texto. `poster-promotional-design` dirige y ejecuta el arte cuando se solicita una imagen y hay una herramienta disponible. Puede entregar o mostrar el encargo completo cuando se pida, sin añadir una aprobación obligatoria al proceso. La suite no incluye un generador propio.

## Método G.O.R.V.E.T.

El Método G.O.R.V.E.T. organiza el proceso de transformar una idea en una escena y construir un prompt con intención, claridad y estilo:

- **G — Guion visual:** definir la historia o el instante que se quiere contar.
- **O — Observación del entorno:** situar la escena mediante lugar, momento y atmósfera.
- **R — Recursos técnicos:** elegir cámara, lente, luz, estilo y tratamiento visual según la intención.
- **V — Valor emocional:** expresar la emoción mediante señales visuales concretas.
- **E — Estructura narrativa:** organizar el prompt en frases cortas y jerarquizadas; cada oración añade algo nuevo al plano.
- **T — Tono:** mantener un lenguaje visual coherente con el propósito de la imagen.

Puede utilizarse como briefing visual antes de redactar y como guía para identificar qué revisar cuando el resultado falla. La historia, la técnica y la emoción se integran en la escena; no requieren seis párrafos en el prompt final.

## Estructura

```text
gorvet-creative-suite/
├── .gitignore
├── LICENSE
├── README.md
├── plugin.json
├── scripts/                # Generación del paquete desde un commit
└── skills/
    ├── prompt-optimization-qa/
    │   ├── SKILL.md
    │   └── references/     # Optimización compartida del prompt
    ├── luces-camara-prompt/
    │   ├── SKILL.md
    │   └── references/     # Bibliotecas operativas
    └── poster-promotional-design/
        ├── SKILL.md
        ├── assets/         # Esquemas visuales originales
        └── references/     # Edición, diseño, referentes, ejecución y revisión
```

Cada carpeta de `skills/` es una unidad independiente en formato Agent Skills: contiene un `SKILL.md` con metadatos YAML e instrucciones Markdown, además de sus recursos cuando corresponda. La carpeta `references/` forma parte de la funcionalidad y debe conservarse completa.

`plugin.json` aporta metadatos de empaquetado para interfaces que admitan ese manifiesto. No forma parte del formato básico Agent Skills ni es necesario para instalar las carpetas de skills directamente.

## Requisitos

- Una aplicación o agente que implemente el estándar Agent Skills y pueda cargar `SKILL.md` junto con sus recursos.
- Acceso del asistente a las carpetas instaladas y a sus referencias. Para analizar imágenes adjuntas, también necesita capacidad de visión.
- Git, si se descarga mediante clonación; también puede descargarse el repositorio desde GitHub.
- Una herramienta de imagen o diseño, si se desea ejecutar un prompt o producir el arte solicitado mediante `poster-promotional-design`.

Los skills no dependen de un proveedor o modelo concreto y no requieren un servidor MCP, claves de API ni código ejecutable propio. La aplicación anfitriona gestiona la carga de instrucciones, las referencias y el acceso al modelo; la calidad de seguimiento depende de ese modelo. El script de distribución del repositorio solo sirve para preparar las Releases.

## Descarga rápida

Descarga el [paquete instalable de la última Release](https://github.com/gorvet/gorvet-creative-suite/releases/latest). El archivo `gorvet-creative-suite-1.7.0.zip` contiene el manifiesto, los tres skills completos, sus referencias, el icono, el README y la licencia. `SHA256SUMS.txt` permite comprobar su integridad. El identificador técnico `gorvet-creative-suite` se conserva para mantener la continuidad de las instalaciones; el nombre visible es GORVET Creative Director.

El ZIP reúne toda la suite. Impórtalo directamente solo si la aplicación admite este formato de complemento. Para aplicaciones que instalan Agent Skills individuales, extrae el paquete y utiliza cada carpeta de `skills/`, siguiendo los pasos siguientes. No necesitas Git para descargarlo.

Para estudiar o modificar el producto, utiliza el repositorio. El paquete se genera desde el mismo código publicado.

## Instalación en una aplicación compatible con Agent Skills

1. Descarga y extrae el paquete de la Release.
2. Elige una o varias carpetas: `skills/luces-camara-prompt`, `skills/prompt-optimization-qa` y `skills/poster-promotional-design`. Pueden instalarse y utilizarse por separado.
3. Utiliza el mecanismo de instalación de la aplicación: copiar al directorio de skills, importar una carpeta o subir un ZIP individual, según indique su documentación.
4. Conserva `SKILL.md` en la raíz de cada carpeta de skill y todas sus referencias junto a él. Si la aplicación exige un ZIP individual, empaqueta esa unidad completa con la estructura de archivo que la aplicación indique; el ZIP de toda la suite no equivale a un skill individual.
5. Actualiza la lista de skills o abre una nueva sesión, según la aplicación, y comprueba que reconozca el nombre instalado.

El estándar define cómo se organiza un skill; cada aplicación decide dónde instalarlo, cómo activarlo y qué empaquetado acepta. No existe una ruta de instalación ni una sintaxis de invocación universal. Un chat que únicamente permite adjuntar documentos no necesariamente implementa Agent Skills.

### Ejemplo de instalación manual en Codex

1. Descarga o clona este repositorio y abre su carpeta.
2. Copia las carpetas completas de los skills elegidos al directorio de skills de Codex: `$CODEX_HOME/skills` si está configurado, o `~/.codex/skills` en caso contrario.
3. Abre una nueva sesión de Codex y comprueba que los skills estén disponibles.

En Windows, ejecuta lo siguiente desde la raíz del repositorio. El comando se detiene si ya existe cualquiera de los skills para evitar sobrescribir una instalación:

```powershell
$skillDirectory = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex/skills'
}
$skillNames = @('luces-camara-prompt', 'prompt-optimization-qa', 'poster-promotional-design')
foreach ($skillName in $skillNames) {
    if (Test-Path -LiteralPath (Join-Path $skillDirectory $skillName)) {
        throw "El skill $skillName ya está instalado. Revisa la instalación antes de actualizarlo."
    }
}
New-Item -ItemType Directory -Path $skillDirectory -Force | Out-Null
foreach ($skillName in $skillNames) {
    Copy-Item -LiteralPath (Join-Path 'skills' $skillName) -Destination $skillDirectory -Recurse
}
```

Este ejemplo es específico de Codex. En otras aplicaciones, utiliza su ubicación y mecanismo de instalación. Copiar las carpetas de skills no registra `plugin.json` como complemento en una tienda.

## Uso

Activa el skill mediante el selector, comando o mecanismo de tu aplicación e indica tu objetivo visual, el uso de la imagen y cualquier referencia o restricción relevante. También puedes pedirlo por su nombre cuando la aplicación permita activación mediante lenguaje natural. La sintaxis `$nombre-del-skill` que admite Codex no es un requisito del estándar.

Con `luces-camara-prompt`, primero recibirás una propuesta de escena, estilo, iluminación y composición. Solicita ajustes o apruébala para recibir el prompt final. Puedes pedir una entrega en un solo idioma o el desglose en la plantilla G.O.R.V.E.T.

Con `prompt-optimization-qa`, proporciona el prompt original y el objetivo de depuración: eliminar repetición, reducir expansión o resolver contradicciones sin cambiar la dirección visual.

Con `poster-promotional-design`, aporta el objetivo, el contenido, el formato y las referencias disponibles. El skill selecciona la dirección de productos, personas o promociones por lo que se anuncia y su función, no por recibir una foto o un texto. Esa biblioteca gobierna el protagonismo, el argumento y el tratamiento; las reglas comunes resuelven selección, jerarquía, composición y ejecución. Pregunta por datos materiales que no pueda resolver con fidelidad. Si pides el arte, lo ejecuta y revisa lo que pueda observar. Si pides ver el prompt o aprobar previamente la propuesta, respeta esa forma de trabajo. También puedes solicitar solo copy, estructura o crítica. Funciona de forma independiente y no asigna una plantilla por producto o sector.

### Ejemplos

**Preparar una imagen de producto**

```text
Usa el skill luces-camara-prompt para preparar una fotografía publicitaria
de una taza de café artesanal sobre una mesa de madera.
Busco una sensación cálida y un formato vertical para redes sociales.
```

Después de revisar la propuesta:

```text
Apruebo la dirección creativa. Entrega el prompt final en español e inglés.
```

**Corregir un fallo concreto**

```text
Usa el skill prompt-optimization-qa. Este prompt repite la iluminación y el estilo.
Depúralo sin perder las decisiones visuales ni las restricciones.
Prompt original: [pega aquí el prompt completo].
```

**Dirigir una pieza promocional**

Ejemplo ficticio:

```text
Usa el skill poster-promotional-design para un póster vertical de un taller
de fotografía. Texto obligatorio: «Luz de ventana», «18 de noviembre, 10:00»,
«Estudio Norte». Público: principiantes. Quiero una composición tipográfica
con una fotografía de apoyo. No añadas precios ni datos de inscripción.
Entrega el contenido jerarquizado y la estructura del layout.
```

## Demostración breve

Este ejemplo ilustra el flujo de conversación; no procede de las páginas del libro.

**1. Idea del usuario**

> Quiero una fotografía vertical de café artesanal que transmita una mañana tranquila.

**2. Propuesta de dirección creativa**

> Una taza de cerámica sobre una mesa de madera junto a una ventana. Estilo fotográfico natural, luz suave de mañana, vapor tenue y encuadre cercano con espacio alrededor de la taza.

**3. Aprobación del usuario**

> Apruebo la propuesta. Entrega el prompt final.

**4. Ejemplo de prompt en español**

> Fotografía vertical de una taza de cerámica con café artesanal sobre una mesa de madera junto a una ventana. Un hilo tenue de vapor asciende sobre el café. Luz suave de mañana desde un lateral, sombras delicadas y colores cálidos contenidos. Encuadre cercano, taza como sujeto principal y fondo ligeramente desenfocado. La escena transmite calma y una pausa cotidiana. Relación de aspecto 4:5.

**Ejemplo de prompt en inglés**

> Vertical photograph of a ceramic cup filled with artisan coffee on a wooden table beside a window. A faint wisp of steam rises from the coffee. Soft morning light from one side, gentle shadows, and restrained warm colors. Close framing with the cup as the main subject and a slightly blurred background. The scene conveys calm and an everyday moment of rest. Aspect ratio 4:5.

La entrega del skill también incluye la mención al Método GORVET, el enlace a GoLab y las opciones de continuación. Para obtener una imagen, utiliza el prompt en tu generador.

## Ayuda rápida

- **El skill no aparece:** comprueba que la carpeta instalada contiene directamente `SKILL.md` y abre una nueva sesión del asistente.
- **En `luces-camara-prompt`, no recibes todavía el prompt final:** revisa y aprueba la propuesta de dirección creativa; la entrega ocurre en el segundo flujo.
- **Quieres depurar un prompt:** aporta el texto original y qué debe conservarse. Utiliza `prompt-optimization-qa` para optimizarlo; para revisar un post o su arte, utiliza `poster-promotional-design`.
- **Utilizas referencias:** indica qué debe conservar cada una, como identidad, producto, pose o composición.
- **Quieres otro idioma:** solicítalo expresamente al pedir el prompt.
- **Necesitas reportar un problema:** abre una [Issue](https://github.com/gorvet/gorvet-creative-suite/issues) con la versión, el asistente utilizado y un ejemplo que no incluya datos privados.

La fidelidad de identidad, el texto dentro de la imagen y otros detalles dependen del generador utilizado. El skill prepara instrucciones y no garantiza un resultado visual idéntico entre plataformas.

## Generación del paquete

Para generar una distribución desde un commit confirmado, ejecuta `./scripts/build-release.ps1` en PowerShell. El ZIP y su suma SHA-256 se guardan en `dist/`, que está excluida de Git. El paquete incluye el manifiesto, README, licencia y skills del commit, además de los recursos de `assets/` cuando exista esa carpeta.

La publicación está automatizada mediante `.github/workflows/release.yml`. Un push normal actualiza el código. Al subir una etiqueta con formato `vMAYOR.MENOR.PARCHE`, GitHub Actions comprueba que coincida con `plugin.json`, ejecuta el script existente, verifica el ZIP y su checksum y crea una Release con ambos archivos y notas generadas desde GitHub. Utiliza el token integrado de Actions; no requiere un secreto adicional.

Para publicar una versión nueva:

1. Actualiza `version` en `plugin.json` y el nombre del ZIP documentado en este README.
2. Haz commit y push de los cambios.
3. Crea y sube la etiqueta de esa versión. Por ejemplo, para `1.7.0`:

```powershell
git tag v1.7.0
git push origin v1.7.0
```

Comprueba la ejecución en la pestaña Actions y descarga los archivos de la Release resultante. Las etiquetas deben ser nuevas: el workflow no sobrescribe releases existentes. Si la etiqueta no coincide con el manifiesto o falla la verificación del paquete, la ejecución termina sin publicar.

También puedes iniciar `Publish plugin release` desde Actions mediante `Run workflow`, indicando una etiqueta existente. Esta vía empaqueta el commit de esa etiqueta y aplica las mismas comprobaciones; permite iniciar una publicación que no haya arrancado con el push.

## Relación con el libro

GORVET Creative Director es un complemento práctico del libro **“Luces, Cámara, ¡Prompt!”**. Aplica el Método G.O.R.V.E.T. mediante recursos operativos para trabajar con un asistente de IA. No es una edición del libro ni contiene su manuscrito o materiales editoriales fuente.

Puedes utilizar el skill sin comprar el libro. Para profundizar, consulta [Luces, Cámara, ¡Prompt! en Google Play Books](https://play.google.com/store/books/details?id=KcKTEQAAQBAJ) y los recursos de aprendizaje de [GoLab](https://golab.gorvet.com/).

## Autor y licencia

**Autor y desarrollador: Juank de Gorvet** · [gorvet.com](https://gorvet.com/)

El manifiesto declara la autoría en `author.name`, el desarrollador en `extensions.com.openai.interface.developerName` y la web en `homepage` y `websiteURL`. En el directorio de ChatGPT, el nombre público del desarrollador depende de la identidad verificada seleccionada al publicar, según la [documentación de publicación de OpenAI](https://developers.openai.com/plugins/deploy/submission). Esa identidad de la ficha se administra en ChatGPT y no se sustituye únicamente cambiando el JSON del paquete.

El logo y el icono se incluyen en `assets/icon.png`. Los campos `logo`, `logoDark`, `composerIcon` y `composerIconDark` apuntan a ese mismo archivo para conservar la identidad gráfica en ambos temas, sin depender de una imagen externa.

Publicado bajo la [licencia MIT](LICENSE). Puedes usar, estudiar, modificar y distribuir el skill, incluso comercialmente, conservando el aviso de autoría y la licencia. La licencia se aplica al contenido de este repositorio; no incluye el libro ni sus materiales editoriales.
