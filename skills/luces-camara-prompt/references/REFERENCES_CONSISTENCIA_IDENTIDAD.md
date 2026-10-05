# CONSISTENCIA DE IDENTIDAD Y COHERENCIA VISUAL

## Consistencia
Mantener elementos esenciales aunque cambien:
- pose;
- entorno;
- expresión.

Tipos:
- rostro/personaje;
- estilo visual;
- identidad emocional.

## Coherencia
Las imágenes no solo deben parecerse: deben comunicar el mismo universo.

## Rostro
- conservar bloque descriptivo base;
- no cambiar sinónimos de rasgos esenciales entre versiones;
- usar `same face`, `same proportions`, `consistent appearance` cuando aporte.

## Anclas
Repetir aproximadamente tres anclas clave:
- identidad;
- estilo/luz;
- paleta/encuadre.

## Auto-referencia progresiva
1. crear imagen base;
2. usarla como referencia siguiente;
3. cambiar solo pose/acción o una capa;
4. repetir.

## Cantidad de referencias
Orientación del libro:
- una vista 3/4 bien iluminada y fondo neutro puede bastar;
- frontal + 3/4/lateral puede mejorar posiciones;
- más referencias aumentan peso e influencia.

## Contexto residual
El libro recomienda:
- mantener un mismo chat cuando se quiere conservar una pauta;
- iniciar un contexto nuevo cuando se quiere cambiar radicalmente modelo o estilo;
- reiniciar con prompt base + imagen cuando la consistencia se degrade.

## Errores
- cambiar descriptores clave → deriva;
- varios estilos → mezcla;
- cambiar luz/paleta → ruptura;
- demasiadas referencias → competencia;
- emociones contradictorias dentro de una misma escena → expresión incoherente.

En una serie narrativa, la emoción puede evolucionar con la historia mientras se conservan identidad y continuidad visual. Las anclas se repiten entre prompts autónomos; no se reformulan varias veces dentro del mismo prompt.

## Plantillas
Guardar prompts exitosos como bases de series o campañas.

Para fijar un entorno de serie, aplicar «Fondos de series» en `WORKFLOWS_OPTIMIZACION_PROMPT.md`: definir anclas espaciales concretas o una referencia del escenario, en vez de duplicar su descripción con una orden genérica de mantenerlo igual.
