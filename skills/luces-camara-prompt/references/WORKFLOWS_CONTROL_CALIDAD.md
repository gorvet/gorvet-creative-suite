# CONTROL DE CALIDAD

## Regla de optimización obligatoria
Antes de entregar cualquier prompt final, hacer una pasada de compresión semántica.

El conocimiento interno puede ser extenso; la salida no debe volcar toda la biblioteca. Seleccionar únicamente los elementos que cambian de forma material el resultado visual.

### Longitud
- Prompt normal: 1 párrafo compacto.
- Prompt realmente complejo: máximo 2 párrafos.
- No crear 3, 4 o más párrafos para reiterar la misma escena.
- Si una instrucción puede decirse con menos palabras sin perder control visual, usar la versión más corta.

### Deduplicación
Cada función visual debe expresarse una sola vez.

No repetir con sinónimos equivalentes:
- realismo;
- calidad;
- nitidez;
- estilo;
- iluminación;
- profundidad de campo;
- composición;
- atmósfera;
- relación de aspecto.

Ejemplo de redundancia a evitar:
`photorealistic, ultra-realistic, hyperrealistic, realistic photography, realistic textures`.
Elegir solo el descriptor o combinación mínima que aporte control real.

### Técnica mínima suficiente
Por defecto usar como máximo:
- 1 estilo dominante;
- 1 cámara o look de captura, solo si aporta;
- 1 lente, solo si aporta;
- 1 instrucción de profundidad/enfoque;
- 1 esquema principal de iluminación;
- 1 composición/encuadre principal;
- 1 atmósfera o emoción dominante;
- materialidad y microdetalle solo cuando sean relevantes.

No añadir especificaciones técnicas para “sonar profesional”.

### Relación de aspecto
- Mencionarla exactamente UNA vez.
- Colocarla al final del prompt.
- Omitirla si el usuario no la necesita o si no aporta al uso previsto.
- Nunca repetirla en narrativa, bloque técnico y cierre.

### Español / inglés
La versión inglesa debe conservar la misma densidad informativa que la española. No expandirla con listas de sinónimos o especificaciones nuevas.

## Técnico
- sujeto/objeto claro;
- escala lógica;
- plano correcto;
- perspectiva coherente;
- luz con dirección;
- profundidad adecuada;
- materialidad creíble;
- sin instrucciones contradictorias.

## Emocional
- la emoción se percibe;
- gesto, color y luz coinciden;
- el mensaje funciona sin explicación.

## Estratégico
- sirve para el uso;
- ratio adecuado cuando proceda;
- espacio para copy si procede;
- producto/marca con jerarquía correcta;
- estilo correcto para el nicho.

## Referencias
- propósito explícito;
- atributos a conservar claros;
- atributos que deben cambiar controlados por texto;
- sin mezcla accidental entre identidad, pose y estilo.

## Estilo
- uno dominante;
- matices compatibles;
- sin adjetivos vacíos;
- sin redundancia.

## Mini-brief
El prompt final debe ser interpretable por un fotógrafo, director de arte, diseñador o artista 3D sin explicación adicional, pero no debe parecer un briefing inflado.

## Revisión del resultado
Tres filtros del libro:
1. técnico;
2. emocional;
3. estratégico.

Evaluar por lo que funciona/comunica, no solo por “me gusta/no me gusta”.
