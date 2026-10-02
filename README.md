# GORVET Creative Suite

GORVET Creative Suite es una colección de skills de **Gorvet Estudios** en el formato abierto [Agent Skills](https://agentskills.io/specification), para convertir ideas visuales en prompts de imagen claros, corregir fallos concretos en prompts existentes y dirigir el diseño de piezas promocionales estáticas. Está basada en el **Método G.O.R.V.E.T.** y reúne bibliotecas operativas para dirigir escenas, referencias, estilos, iluminación y composición.

Ayuda a resolver la falta de dirección en peticiones visuales, las instrucciones contradictorias y la pérdida de consistencia al ajustar un prompt.

## Skills incluidos

- **`luces-camara-prompt`**: desarrolla una dirección creativa y, después de que el usuario la apruebe, entrega el prompt en español e inglés. Incluye recursos para retrato, producto, publicidad, ilustración, interiores, retoque y restauración.
- **`image-prompt-qa`**: diagnostica el problema indicado por el usuario y corrige el prompt con el mínimo cambio necesario. Corrige identidad y selección de referencias, proporciones, producto, iluminación, composición, integración y repetición innecesaria. Conserva las convenciones de photobook cuando correspondan.
- **`poster-promotional-design`**: selecciona y jerarquiza el contenido de pósters, posts, stories, flyers y otras piezas promocionales estáticas. Define composición, tipografía y tratamiento visual, preservando los datos obligatorios y evitando decoración sin función. Incluye bibliotecas de criterio editorial, sistema visual, referencias comentadas, encargo de ejecución y revisión, además de cuatro esquemas visuales originales.

Cuando se invoca la suite, el asistente debe seleccionar el skill por el resultado solicitado: diseño de piezas con texto y layout, reparación de un prompt existente o dirección de escena y creación de prompts. No necesitas indicar el nombre interno para pedir un póster o un estado de WhatsApp. La selección depende de que la aplicación cargue las instrucciones actualizadas.

Los tres skills funcionan de forma independiente. `image-prompt-qa` se utiliza cuando se solicita una corrección; no es un paso obligatorio después de `luces-camara-prompt`.

Los skills de prompts trabajan con texto. `poster-promotional-design` procesa el brief y prepara un encargo de diseño antes de ejecutarlo, si el usuario pide un arte y el asistente dispone de una herramienta de imagen o diseño. La suite no incluye un generador propio.

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
    ├── image-prompt-qa/
    │   └── SKILL.md
    ├── luces-camara-prompt/
    │   ├── SKILL.md
    │   └── references/     # 28 bibliotecas operativas
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

Descarga el [paquete instalable de la última Release](https://github.com/gorvet/gorvet-creative-suite/releases/latest). El archivo `gorvet-creative-suite-1.4.0.zip` contiene el manifiesto, los tres skills completos, sus referencias, el README y la licencia. `SHA256SUMS.txt` permite comprobar su integridad.

El ZIP reúne toda la suite. Impórtalo directamente solo si la aplicación admite este formato de complemento. Para aplicaciones que instalan Agent Skills individuales, extrae el paquete y utiliza cada carpeta de `skills/`, siguiendo los pasos siguientes. No necesitas Git para descargarlo.

Para estudiar o modificar el producto, utiliza el repositorio. El paquete se genera desde el mismo código publicado.

## Instalación en una aplicación compatible con Agent Skills

1. Descarga y extrae el paquete de la Release.
2. Elige una o varias carpetas: `skills/luces-camara-prompt`, `skills/image-prompt-qa` y `skills/poster-promotional-design`. Pueden instalarse y utilizarse por separado.
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
$skillNames = @('luces-camara-prompt', 'image-prompt-qa', 'poster-promotional-design')
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

Con `image-prompt-qa`, proporciona el prompt original y describe exactamente qué salió mal. Adjunta las imágenes de referencia o del resultado cuando estén disponibles y el asistente pueda analizarlas.

Con `poster-promotional-design`, aporta el objetivo, el contenido y el formato de la pieza. El skill selecciona el contenido, resuelve jerarquía, layout y tipografía, y prepara un encargo para el generador. Si pides una imagen y hay una herramienta disponible, ejecuta ese encargo y revisa el resultado cuando pueda verlo. Cuando corresponda, entrega el arte y un texto complementario listo para publicar con la información necesaria que quedó fuera de la imagen. También puedes pedir solo copy, estructura, crítica o un prompt. Funciona por separado; sus referencias a `luces-camara-prompt` son apoyos opcionales.

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
Usa el skill image-prompt-qa. En este prompt, el rostro de la persona de referencia
parece pegado al cuerpo. Corrige únicamente su integración con la escena.
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
- **Quieres corregir un resultado:** aporta el prompt original, el fallo concreto y, si es posible, la imagen. Utiliza `image-prompt-qa` para corregirlo con cambios mínimos.
- **Utilizas referencias:** indica qué debe conservar cada una, como identidad, producto, pose o composición.
- **Quieres otro idioma:** solicítalo expresamente al pedir el prompt.
- **Necesitas reportar un problema:** abre una [Issue](https://github.com/gorvet/gorvet-creative-suite/issues) con la versión, el asistente utilizado y un ejemplo que no incluya datos privados.

La fidelidad de identidad, el texto dentro de la imagen y otros detalles dependen del generador utilizado. El skill prepara instrucciones y no garantiza un resultado visual idéntico entre plataformas.

## Generación del paquete

Para generar una distribución desde un commit confirmado, ejecuta `./scripts/build-release.ps1` en PowerShell. El ZIP y su suma SHA-256 se guardan en `dist/`, que está excluida de Git. El paquete incluye únicamente el manifiesto, README, licencia y skills del commit.

## Relación con el libro

GORVET Creative Suite es un complemento práctico del libro **“Luces, Cámara, ¡Prompt!”**. Aplica el Método G.O.R.V.E.T. mediante recursos operativos para trabajar con un asistente de IA. No es una edición del libro ni contiene su manuscrito o materiales editoriales fuente.

Puedes utilizar el skill sin comprar el libro. Para profundizar, consulta [Luces, Cámara, ¡Prompt! en Google Play Books](https://play.google.com/store/books/details?id=KcKTEQAAQBAJ) y los recursos de aprendizaje de [GoLab](https://golab.gorvet.com/).

## Autor y licencia

**Autor: Gorvet Estudios** · [gorvet.com](https://gorvet.com/)

Publicado bajo la [licencia MIT](LICENSE). Puedes usar, estudiar, modificar y distribuir el skill, incluso comercialmente, conservando el aviso de autoría y la licencia. La licencia se aplica al contenido de este repositorio; no incluye el libro ni sus materiales editoriales.
