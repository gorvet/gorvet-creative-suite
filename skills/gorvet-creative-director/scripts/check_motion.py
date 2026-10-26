"""Check a temporal plan and recorded playback scope; does not inspect media."""

import argparse
import json
import math
from pathlib import Path
import sys


def text(value):
    return isinstance(value, str) and bool(value.strip())


def number(value):
    return type(value) in (int, float) and math.isfinite(value)


def validate_motion(job, stage):
    errors = []
    if not isinstance(job, dict) or stage not in ("generate", "deliver"):
        return ["Registro o etapa audiovisual inválidos."]
    direction = job.get("direction", {})
    motion = direction.get("motion") if isinstance(direction, dict) else None
    if not isinstance(motion, dict):
        return ["Falta direction.motion."]
    duration = motion.get("duration")
    if not number(duration) or duration <= 0:
        errors.append("La duración debe ser positiva y finita.")
    shots = motion.get("shots")
    if not isinstance(shots, list) or not shots:
        errors.append("Falta el plan de planos.")
        shots = []
    ids, cursor = set(), 0
    for shot in shots:
        if not isinstance(shot, dict):
            errors.append("Cada plano debe ser un objeto.")
            continue
        identifier = shot.get("id")
        if not text(identifier) or identifier in ids:
            errors.append("Los planos necesitan identificadores únicos.")
        else:
            ids.add(identifier)
        for field in ("function", "action", "camera", "transition", "continuity"):
            if not text(shot.get(field)):
                errors.append(f"Falta {field} en un plano.")
        start, end = shot.get("start"), shot.get("end")
        if not number(start) or not number(end) or start < 0 or end <= start:
            errors.append("Intervalo temporal inválido.")
        else:
            if not math.isclose(start, cursor, abs_tol=1e-6, rel_tol=0):
                errors.append("El montaje tiene huecos, solapes o planos desordenados.")
            cursor = end
    if number(duration) and not math.isclose(cursor, duration, abs_tol=1e-6, rel_tol=0):
        errors.append("El plan no cubre la duración total.")
    audio = motion.get("audio")
    if not isinstance(audio, dict) or audio.get("mode") not in ("silent", "sound") or not text(audio.get("spec")):
        errors.append("Falta la decisión explícita de audio y su especificación.")
    delivery = motion.get("delivery")
    if not isinstance(delivery, dict) or not all(text(delivery.get(k)) for k in ("aspect_ratio", "format")):
        errors.append("Faltan proporción y formato de entrega.")
    if stage == "deliver":
        output, review = job.get("output"), job.get("review")
        if not isinstance(output, dict) or output.get("media_type") != "video":
            errors.append("Un storyboard o fotograma no acredita una salida de vídeo.")
        elif not number(output.get("duration")) or not number(duration) or not math.isclose(output["duration"], duration, abs_tol=0.05, rel_tol=0):
            errors.append("La duración observada no corresponde al plan.")
        playback = review.get("playback") if isinstance(review, dict) else None
        if not isinstance(playback, dict) or playback.get("full_duration") is not True or playback.get("transitions_checked") is not True:
            errors.append("Falta reproducción completa y revisión de transiciones.")
        if isinstance(audio, dict) and audio.get("mode") == "sound":
            if not isinstance(playback, dict) or playback.get("audio_checked") is not True:
                errors.append("Falta revisión del audio solicitado.")
        card = review.get("scorecard") if isinstance(review, dict) else None
        criteria = card.get("criteria") if isinstance(card, dict) else None
        audio_grade = criteria.get("audio") if isinstance(criteria, dict) else None
        if isinstance(audio, dict) and audio.get("mode") == "sound" and isinstance(audio_grade, dict) and audio_grade.get("applicable") is False:
            errors.append("El audio solicitado no puede declararse no aplicable.")
    return errors


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--stage", choices=("generate", "deliver"), required=True)
    args = parser.parse_args()
    try:
        errors = validate_motion(json.loads(args.path.read_text(encoding="utf-8-sig")), args.stage)
    except (OSError, ValueError, TypeError) as exc:
        errors = [str(exc)]
    print(json.dumps({"allowed": not errors, "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
