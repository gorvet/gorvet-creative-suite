---
name: video-motion-direction
description: Dirige vídeos, animaciones, motion graphics y secuencias audiovisuales desde una intención o un guion. Resuelve acciones en el tiempo, puesta en escena, planos, cámara en movimiento, ritmo, montaje, sonido y continuidad temporal. Entrega tratamiento, plan de planos o dirección lista para compilar; producir vídeo requiere herramientas compatibles.
---

# GORVET — Dirección de vídeo y motion

Convierte una intención en un acontecimiento legible en el tiempo. Una sucesión de imágenes atractivas no constituye por sí sola una realización audiovisual. Hereda mensaje, identidad y sistema de arte; no los sustituye por un estilo cinematográfico genérico.

## Entrada y responsabilidad

Aplica el [contrato común](../gorvet-creative-director/references/SPECIALIST_CONTRACT.md). Recibe propósito, duración o contexto de uso, concepto, guion si existe, fuentes y restricciones. Si el argumento está abierto, estrategia lo resuelve; narrativa decide qué comunica cada pieza de un conjunto visual. Este especialista decide cómo ocurre dentro del vídeo: puesta en escena, tiempos, movimiento, cortes y sonido. Una animación individual no necesita activar series.

Desarrolla G y V en acciones y ritmo; O sostiene continuidad espacial; R decide realización; T conserva el lenguaje; E organiza instrucciones ejecutables por plano. Fotografía aporta óptica, luz y materialidad cuando haga falta. Gráfica aporta tipografía y relaciones espaciales; vídeo decide cuándo entran, cuánto permanecen y cómo se mueven.

## Método de realización

Lee [TEMPORAL_DIRECTION.md](references/TEMPORAL_DIRECTION.md) para construir tratamiento y plan temporal; para animación gráfica aplica su modo motion. Selecciona acciones que puedan suceder en la duración disponible. Define estado inicial, cambio visible y estado final; no impongas conflicto dramático a una demostración o a un loop.

Cada plano debe tener una función perceptiva, narrativa o informativa comprobable. Decide sujetos, geometría, mirada, acción, cámara, continuidad de entrada y salida, duración y transición. El movimiento de cámara debe revelar, seguir, relacionar o transformar algo concreto. Evita combinar movimientos incompatibles o pedir un montaje entero dentro de un plano continuo.

El sonido se diseña como silencio, ambiente, efectos, música, voz o combinación. Un vídeo sin sonido debe poder cumplir el uso acordado; una voz no duplica automáticamente cada texto. Los literales hablados y los de pantalla son canales distintos. No inventes declaraciones, música licenciada ni prestaciones de sincronía.

## Preparar producción

Aplica [PRODUCTION_AND_REVIEW.md](references/PRODUCTION_AND_REVIEW.md). Define si se necesita vídeo desde texto, animar una base, planos separados, animatic o montaje determinista. Comprueba las capacidades de la herramienta real antes de adaptar duración, referencias, cámara, audio o resolución. Si no hay producción audiovisual, entrega el tratamiento o los prompts solicitados indicando ese alcance; no sustituyas un vídeo por una imagen sin acordarlo.

Entrega `direction.motion` con duración total, planos identificados y sus tiempos, acciones, cámara, transiciones, continuidad y audio. Añade especificación de entrega y comprobaciones observables. Las decisiones de captura van en `capture`; el sistema de identidad, en `identity`; no dupliques su autoridad en `motion`. [Luces](../luces-camara-prompt/SKILL.md) compila la versión integrada. El director reúne una propuesta y autorización según el [protocolo](../gorvet-creative-director/references/EXECUTION_PROTOCOL.md).

## Aceptación y retorno

Antes de compilar, comprueba duración, acciones realizables, lectura del texto, empalmes, estado final y coherencia del sonido. Después de producir, [crítica visual](../visual-quality-review/SKILL.md) debe reproducir la salida y revisar su evolución, no solo sus fotogramas. Devuelve fallos temporales a este rol; los cambios de concepto o de marca vuelven a sus responsables. Una corrección conserva los planos y atributos que funcionan y vuelve a revisar las uniones afectadas.

El [control temporal](../gorvet-creative-director/scripts/check_motion.py) verifica coherencia estructural del plan y alcance registrado de inspección. No mira ni escucha el vídeo y no sustituye el juicio audiovisual.
