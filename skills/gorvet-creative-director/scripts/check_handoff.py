"""Validate image-production handoffs; no network or image-model calls."""

import argparse
import hashlib
import json
from pathlib import Path
import sys


def digest(value):
    data = json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def fingerprints(job):
    execution = job.get("execution", {})
    if not isinstance(execution, dict):
        execution = {}
    direction = job.get("direction", {})
    scope = {"job_id": job.get("job_id"), "deliverable": job.get("deliverable"),
             "direction": direction}
    return {
        "direction": digest(scope),
        "proposal": digest({
            "scope": scope,
            "prompt": execution.get("prompt"),
            "reference_ids": execution.get("reference_ids"),
            "parameters": execution.get("parameters"),
        }),
    }


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def string_list(value):
    return isinstance(value, list) and all(nonempty(item) for item in value)


def validate(job, stage):
    """Return structural failures, never a claim of aesthetic quality."""
    errors = []
    if not isinstance(job, dict):
        return ["El registro debe ser un objeto JSON."]
    if job.get("schema_version") != "1.0":
        errors.append("Versión de contrato desconocida.")
    if not nonempty(job.get("job_id")):
        errors.append("Falta job_id.")
    if job.get("deliverable") not in ("image", "series"):
        errors.append("Este control es para imágenes; un encargo textual no autoriza generación.")
    direction = job.get("direction")
    if not isinstance(direction, dict):
        return errors + ["Falta la dirección resuelta."]
    for key in ("message", "concept", "medium", "composition"):
        if not nonempty(direction.get(key)):
            errors.append(f"Falta direction.{key}.")
    if not string_list(direction.get("image_text")):
        errors.append("direction.image_text debe ser una lista de literales, vacía si no hay copy.")
    sources = direction.get("references")
    source_ids = []
    if not isinstance(sources, list):
        errors.append("direction.references debe ser una lista.")
    else:
        for source in sources:
            if not isinstance(source, dict) or not all(nonempty(source.get(k)) for k in ("id", "role")):
                errors.append("Cada referencia necesita id y función.")
            else:
                source_ids.append(source["id"])
        if len(source_ids) != len(set(source_ids)):
            errors.append("Hay identificadores de referencia duplicados.")
    if stage not in ("generate", "deliver"):
        return errors + ["Etapa desconocida."]
    hashes = fingerprints(job)
    if stage == "deliver":
        output = job.get("output", {})
        review = job.get("review", {})
        if not isinstance(output, dict) or not isinstance(review, dict):
            return errors + ["Salida o revisión inválida."]
        if not nonempty(output.get("id")):
            errors.append("Falta la imagen producida.")
        if review.get("observed") is not True:
            errors.append("No hay inspección visual registrada.")
        if review.get("output_id") != output.get("id"):
            errors.append("La revisión corresponde a otra salida.")
        if review.get("direction_fingerprint") != hashes["direction"]:
            errors.append("La revisión no corresponde a la dirección vigente.")
        if review.get("verdict") != "pass":
            errors.append("La salida no tiene veredicto visual apto.")
        if not string_list(review.get("evidence")) or not review.get("evidence"):
            errors.append("Falta evidencia de la revisión visual.")
        return errors

    execution = job.get("execution")
    if not isinstance(execution, dict):
        return errors + ["Falta el encargo de ejecución."]
    prompt = execution.get("prompt")
    if not nonempty(prompt):
        errors.append("Falta el prompt de ejecución.")
    elif string_list(direction.get("image_text")):
        for literal in direction["image_text"]:
            if literal not in prompt:
                errors.append(f"Falta un literal seleccionado: {literal}")
    reference_ids = execution.get("reference_ids")
    if not string_list(reference_ids):
        errors.append("execution.reference_ids debe ser una lista.")
    elif len(reference_ids) != len(set(reference_ids)):
        errors.append("Hay referencias de ejecución duplicadas.")
    if not isinstance(execution.get("parameters"), dict):
        errors.append("execution.parameters debe ser un objeto.")
    auth = execution.get("authorization")
    if not isinstance(auth, dict):
        return errors + ["Falta autorización de ejecución."]
    mode = auth.get("mode")
    if mode not in ("approval", "direct"):
        errors.append("Modo de autorización desconocido.")
    if mode == "direct" and not nonempty(auth.get("direct_instruction")):
        errors.append("La ejecución directa necesita una instrucción expresa registrada.")
    visibility = execution.get("visibility", "shown")
    if visibility == "omit_on_request":
        if not nonempty(auth.get("visibility_instruction")):
            errors.append("Ocultar el encargo necesita una petición expresa registrada.")
    elif visibility == "shown":
        for actual, published in (("prompt", "published_prompt"),
                                  ("reference_ids", "published_reference_ids"),
                                  ("parameters", "published_parameters")):
            if execution.get(actual) != execution.get(published):
                errors.append(f"El valor enviado de {actual} no coincide con el mostrado.")
    else:
        errors.append("Modo de visibilidad desconocido.")
    attempt = execution.get("attempt")
    if type(attempt) is not int or not 1 <= attempt <= 3:
        errors.append("El límite estándar es una generación y dos correcciones.")
    elif attempt == 1:
        if mode == "approval" and auth.get("approved_fingerprint") != hashes["proposal"]:
            errors.append("Falta aprobación de la propuesta vigente.")
        if string_list(reference_ids) and set(reference_ids) != set(source_ids):
            errors.append("Las referencias adjuntas no coinciden con las de la dirección.")
    else:
        correction = execution.get("correction")
        if not isinstance(correction, dict):
            errors.append("Falta el diagnóstico y alcance de corrección.")
        else:
            if correction.get("restore_approved") is not True:
                errors.append("Una dirección nueva requiere una propuesta y autorización nuevas.")
            if correction.get("direction_fingerprint") != hashes["direction"]:
                errors.append("La corrección altera la dirección autorizada.")
            if not all(nonempty(correction.get(k)) for k in ("source_output_id", "diagnosis")):
                errors.append("Faltan imagen base o diagnóstico de corrección.")
            if mode == "approval" and auth.get("approved_direction_fingerprint") != hashes["direction"]:
                errors.append("No consta autorización de esta dirección para corregirla.")
            expected = set(source_ids)
            if nonempty(correction.get("source_output_id")):
                expected.add(correction["source_output_id"])
            if string_list(reference_ids) and set(reference_ids) != expected:
                errors.append("La corrección necesita sus fuentes y la salida base declarada.")
    return errors


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--stage", choices=("generate", "deliver"))
    parser.add_argument("--fingerprints", action="store_true")
    args = parser.parse_args()
    try:
        job = json.loads(args.path.read_text(encoding="utf-8-sig"))
        if args.fingerprints:
            if not isinstance(job, dict):
                raise ValueError("El registro debe ser un objeto.")
            print(json.dumps(fingerprints(job), ensure_ascii=False))
            return 0
        if not args.stage:
            parser.error("Indica --stage o --fingerprints.")
        errors = validate(job, args.stage)
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"allowed": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 1
    print(json.dumps({"allowed": not errors, "errors": errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
