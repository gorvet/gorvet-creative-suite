# GORVET Creative Suite

GORVET Creative Suite es una colección de skills de **Gorvet Estudios** para convertir ideas visuales en prompts de imagen claros y corregir fallos concretos en prompts existentes. Está basada en el **Método G.O.R.V.E.T.** y reúne bibliotecas operativas para dirigir escenas, referencias, estilos, iluminación y composición.

Ayuda a resolver la falta de dirección en peticiones visuales, las instrucciones contradictorias y la pérdida de consistencia al ajustar un prompt.

## Skills incluidos

- **`luces-camara-prompt`**: desarrolla una dirección creativa y, después de que el usuario la apruebe, entrega el prompt en español e inglés. Incluye recursos para retrato, producto, publicidad, ilustración, interiores, retoque y restauración.
- **`image-prompt-qa`**: diagnostica el problema indicado por el usuario y corrige el prompt con el mínimo cambio necesario. Corrige identidad y selección de referencias, proporciones, producto, iluminación, composición, integración y repetición innecesaria. Conserva las convenciones de photobook cuando correspondan.

Ambos skills funcionan de forma independiente. `image-prompt-qa` se utiliza cuando se solicita una corrección; no es un paso obligatorio después de `luces-camara-prompt`.

Los skills trabajan con texto. La generación o edición de imágenes requiere una herramienta externa; no se ejecuta durante la preparación del prompt.

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
    └── luces-camara-prompt/
        ├── SKILL.md
        └── references/     # 28 bibliotecas operativas
```

`plugin.json` describe el complemento. Cada `SKILL.md` es el punto de entrada de su skill. La carpeta `references/` forma parte de la funcionalidad y debe conservarse completa.

## Requisitos

- Un asistente compatible con skills basados en archivos `SKILL.md`, como Codex.
- Acceso del asistente a las carpetas instaladas y a sus referencias.
- Git, si se descarga mediante clonación; también puede descargarse el repositorio desde GitHub.
- Una herramienta de imágenes, únicamente si se desea ejecutar el prompt obtenido.

Este paquete no requiere un servidor MCP, claves de API ni dependencias de ejecución propias. Los requisitos y el acceso a servicios del asistente utilizado se gestionan por separado.

## Descarga rápida

Descarga el [paquete instalable de la última Release](https://github.com/gorvet/gorvet-creative-suite/releases/latest). El archivo `gorvet-creative-suite-1.2.0.zip` contiene el manifiesto, los dos skills completos, sus referencias, el README y la licencia. `SHA256SUMS.txt` permite comprobar su integridad.

Utiliza este paquete para importar el complemento en una interfaz compatible con este formato. Si la interfaz requiere instalar cada skill por separado, extrae el ZIP y utiliza la carpeta correspondiente de `skills/`. No necesitas Git para esta descarga. El ZIP del complemento y el ZIP de código fuente que ofrece GitHub tienen finalidades distintas.

Para Codex, extrae el paquete y sigue la instalación manual indicada abajo. Para estudiar o modificar el producto, utiliza el repositorio. El paquete se genera desde el mismo código publicado.

## Instalación en Codex

1. Descarga o clona este repositorio y abre su carpeta.
2. Copia las carpetas completas `skills/luces-camara-prompt` y `skills/image-prompt-qa` al directorio de skills de Codex: `$CODEX_HOME/skills` si está configurado, o `~/.codex/skills` en caso contrario.
3. Abre una nueva sesión de Codex y comprueba que ambos skills estén disponibles.

En Windows, ejecuta lo siguiente desde la raíz del repositorio. El comando se detiene si ya existe cualquiera de los dos skills para evitar sobrescribir una instalación:

```powershell
$skillDirectory = if ($env:CODEX_HOME) {
    Join-Path $env:CODEX_HOME 'skills'
} else {
    Join-Path ([Environment]::GetFolderPath('UserProfile')) '.codex/skills'
}
$skillNames = @('luces-camara-prompt', 'image-prompt-qa')
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

En otros asistentes compatibles, instala las carpetas completas siguiendo las instrucciones del producto. La instalación manual anterior utiliza los skills directamente; no registra el manifiesto como complemento en una tienda.

## Uso

Invoca el skill por su nombre e indica tu objetivo visual, el uso de la imagen y cualquier referencia o restricción relevante.

Con `luces-camara-prompt`, primero recibirás una propuesta de escena, estilo, iluminación y composición. Solicita ajustes o apruébala para recibir el prompt final. Puedes pedir una entrega en un solo idioma o el desglose en la plantilla G.O.R.V.E.T.

Con `image-prompt-qa`, proporciona el prompt original y describe exactamente qué salió mal. Adjunta las imágenes de referencia o del resultado cuando estén disponibles y el asistente pueda analizarlas.

### Ejemplos

**Preparar una imagen de producto**

```text
Usa $luces-camara-prompt para preparar una fotografía publicitaria
de una taza de café artesanal sobre una mesa de madera.
Busco una sensación cálida y un formato vertical para redes sociales.
```

Después de revisar la propuesta:

```text
Apruebo la dirección creativa. Entrega el prompt final en español e inglés.
```

**Corregir un fallo concreto**

```text
Usa $image-prompt-qa. En este prompt, el rostro de la persona de referencia
parece pegado al cuerpo. Corrige únicamente su integración con la escena.
Prompt original: [pega aquí el prompt completo].
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
- **No recibes todavía el prompt final:** revisa y aprueba la propuesta de dirección creativa; la entrega ocurre en el segundo flujo.
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
