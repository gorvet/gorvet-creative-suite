"""Compile resolved decisions, never a raw brief, into a generation prompt."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and all(nonempty(x) for x in value)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False,
                                     separators=(",", ":"), allow_nan=False).encode("utf-8")).hexdigest()


def resolved(value, label):
    if not nonempty(value):
        raise ValueError(f"Falta una decisión ejecutable: {label}.")
    if re.search(r"(?:textos?|literales?)\s+(?:establecidos|acordados|anteriores)|según\s+(?:la\s+)?propuesta|como\s+se\s+(?:indicó|acordó)", value, re.I):
        raise ValueError(f"{label} depende de contexto que el generador no recibe.")
    return value.strip()


def editorial(job):
    brief, direction = job.get("brief"), job.get("direction")
    if not isinstance(brief, dict) or not isinstance(direction, dict):
        raise ValueError("Faltan brief o dirección.")
    items, decisions = brief.get("content_items"), direction.get("content_decisions")
    if not isinstance(items, list) or not isinstance(decisions, list):
        raise ValueError("Faltan inventario de contenido y selección editorial.")
    sources, selected = {}, []
    for item in items:
        if not isinstance(item, dict) or not nonempty(item.get("id")) or not nonempty(item.get("text")):
            raise ValueError("Cada dato necesita id y texto fuente.")
        identifier = item["id"]
        if identifier in sources or not strings(item.get("protected_literals", [])) or type(item.get("required_in_image", False)) is not bool:
            raise ValueError("Dato duplicado o protección de contenido inválida.")
        sources[identifier] = item
    seen = set()
    for decision in decisions:
        if not isinstance(decision, dict) or not nonempty(decision.get("id")):
            raise ValueError("Decisión editorial inválida.")
        identifier = decision["id"]
        if identifier not in sources or identifier in seen or not nonempty(decision.get("reason")):
            raise ValueError("La selección tiene datos ajenos, repetidos o sin criterio.")
        seen.add(identifier)
        destination, literals = decision.get("destination"), decision.get("literals")
        if destination not in ("image", "support", "omit") or not strings(literals):
            raise ValueError("Destino editorial o literales inválidos.")
        item = sources[identifier]
        if item.get("required_in_image") is True and destination != "image":
            raise ValueError("Se ha descartado un texto exigido en la imagen.")
        if destination == "image":
            if not literals:
                raise ValueError("Una decisión de texto visible necesita sus literales exactos.")
            selected.extend(literals)
            rendered = "\n".join(literals)
        else:
            if literals:
                raise ValueError("Un apoyo o descarte no puede añadir texto al generador.")
            rendered = decision.get("copy", "") if destination == "support" else ""
            if destination == "support" and (not nonempty(rendered) or not nonempty(decision.get("support_destination"))):
                raise ValueError("El apoyo necesita copy y un destino real.")
        if destination != "omit" and any(x not in rendered for x in item.get("protected_literals", [])):
            raise ValueError("La selección altera un literal protegido de la fuente.")
    if seen != set(sources):
        raise ValueError("Queda contenido sin decidir; no se compila el brief por exhaustividad.")
    if not strings(direction.get("image_text")) or selected != direction["image_text"] or len(selected) != len(set(selected)):
        raise ValueError("Los literales visibles no corresponden a la selección editorial vigente.")
    return selected


def compile_prompt(job):
    if not isinstance(job, dict) or job.get("schema_version") != "1.3":
        raise ValueError("La producción actual requiere contrato 1.3.")
    direction = job.get("direction")
    if not isinstance(direction, dict):
        raise ValueError("Falta la dirección integrada.")
    if job.get("task_mode", "create") == "edit":
        scope = job.get("preflight")
        if not isinstance(scope, dict) or scope.get("kind") != "edit_scope" or scope.get("ready") is not True:
            raise ValueError("La edición necesita un alcance resuelto.")
        protected = scope.get("protected")
        if not strings(protected) or not protected:
            raise ValueError("Falta la protección de la edición.")
        lines = ["Edita la base " + resolved(scope.get("source_output_id"), "base") + ".",
                 "Objetivo: " + resolved(scope.get("target"), "objetivo"),
                 "Intervención: " + resolved(scope.get("mutation"), "mutación"),
                 "Conserva: " + "; ".join(protected),
                 "Aceptación: " + resolved(scope.get("acceptance"), "aceptación")]
        if not strings(direction.get("image_text")):
            raise ValueError("Faltan los literales de edición, vacíos si no hay texto.")
        lines += ["Literal protegido: " + json.dumps(x, ensure_ascii=False) for x in direction["image_text"]]
    elif job.get("task_mode", "create") == "create":
        selected = editorial(job)
        spec = direction.get("production_spec")
        if not isinstance(spec, dict):
            raise ValueError("Falta la representación concreta de la pieza final.")
        if spec.get("composition") != direction.get("composition"):
            raise ValueError("La composición integrada y la que se enviará al generador no coinciden.")
        lines = [resolved(spec.get(key), key) for key in ("canvas", "intent", "composition", "treatment")]
        basis = spec.get("style_basis")
        if (not isinstance(basis, dict) or basis.get("origin") not in ("user", "reference", "proposal")
                or not nonempty(basis.get("evidence")) or not nonempty(basis.get("reason"))):
            raise ValueError("Falta procedencia y criterio de la dirección estética.")
        elements, text_values, ids, graphic_ids = spec.get("elements"), [], set(), []
        if not isinstance(elements, list) or not elements:
            raise ValueError("Faltan los elementos y sus relaciones visuales.")
        for element in elements:
            if not isinstance(element, dict) or not nonempty(element.get("id")) or element["id"] in ids:
                raise ValueError("Los elementos necesitan identificadores únicos.")
            ids.add(element["id"])
            kind = element.get("kind")
            if kind not in ("subject", "background", "text", "graphic"):
                raise ValueError("Tipo de elemento visual desconocido.")
            instruction = resolved(element.get("instruction"), "instrucción de elemento")
            placement = resolved(element.get("placement"), "posición y relaciones")
            scale = resolved(element.get("scale"), "escala y prioridad")
            if kind == "text":
                literal = element.get("literal")
                if not nonempty(literal):
                    raise ValueError("Falta el literal del bloque tipográfico.")
                text_values.append(literal)
                lines.append("Texto exacto " + json.dumps(literal, ensure_ascii=False) + ": " + instruction + "; " + placement + "; " + scale)
            else:
                if "literal" in element:
                    raise ValueError("Solo un bloque de texto puede introducir un literal.")
                if kind == "graphic":
                    graphic_ids.append(element["id"])
                lines.append(instruction + "; " + placement + "; " + scale)
        if text_values != selected:
            raise ValueError("El diseño debe situar cada literal seleccionado, sin añadir otros.")
        devices = spec.get("graphic_devices")
        if not strings(devices) or devices != graphic_ids:
            raise ValueError("Los recursos gráficos deben corresponder a los elementos gráficos descritos, vacíos si no se necesitan.")
        lines.append(("Recursos gráficos externos limitados a los elementos gráficos descritos. " if devices else "Sin recursos gráficos externos. ") +
                     "No añadir adornos, soportes de texto ni iconos distintos de los descritos.")
        constraints = spec.get("constraints")
        if not strings(constraints):
            raise ValueError("Faltan los controles de ejecución; pueden ser una lista vacía.")
        lines.extend(resolved(x, "control de ejecución") for x in constraints)
        lines.append("El texto visible externo se limita a los literales indicados; no añadir titulares ni mensajes."
                     if selected else "Sin texto externo a la escena; no añadir titulares ni mensajes.")
        if job.get("deliverable") == "video":
            motion = direction.get("motion")
            if not isinstance(motion, dict):
                raise ValueError("Falta el plan temporal.")
            lines.append("Plan temporal resuelto: " + json.dumps(motion, ensure_ascii=False, sort_keys=True))
    else:
        raise ValueError("Modo de producción desconocido.")
    sources = direction.get("references")
    if not isinstance(sources, list):
        raise ValueError("Falta la lista de fuentes, vacía si no hay referencias.")
    for source in sources:
        if not isinstance(source, dict) or not nonempty(source.get("id")) or not nonempty(source.get("role")):
            raise ValueError("Cada fuente necesita id y función.")
        lines.append("Referencia " + source["id"] + ": " + resolved(source["role"], "función de referencia"))
    protected = direction.get("protected_attributes", [])
    if not strings(protected):
        raise ValueError("Los atributos protegidos necesitan controles textuales explícitos.")
    lines.extend(resolved(x, "atributo protegido") for x in protected)
    execution = job.get("execution", {})
    if not isinstance(execution, dict):
        raise ValueError("Ejecución inválida.")
    attempt = execution.get("attempt", 1)
    if type(attempt) is not int or not 1 <= attempt <= 3:
        raise ValueError("Intento de ejecución inválido.")
    if attempt > 1:
        correction = execution.get("correction")
        if not isinstance(correction, dict) or correction.get("restore_approved") is not True:
            raise ValueError("Falta el alcance de corrección.")
        lines = ["Corrige únicamente el defecto de la base " + resolved(correction.get("source_output_id"), "base de corrección") +
                 ": " + resolved(correction.get("diagnosis"), "corrección visible") +
                 ". Conserva el resto de la dirección siguiente."] + lines
    return "\n\n".join(dict.fromkeys(lines))


def validate_review(job, prompt, direction_fingerprint):
    review = job.get("production_review")
    if not isinstance(review, dict):
        return ["Falta la revisión del paquete antes de generar."]
    errors = []
    if review.get("direction_fingerprint") != direction_fingerprint or review.get("prompt_fingerprint") != fingerprint(prompt):
        errors.append("La revisión previa corresponde a otras decisiones o a otro prompt.")
    if review.get("blockers") != []:
        errors.append("La revisión previa tiene bloqueos o no los ha comprobado.")
    expected = {"selection", "design", "anti_ai", "coverage"} if job.get("task_mode", "create") == "create" else {"scope", "preservation", "coverage"}
    checks = review.get("checks")
    if not isinstance(checks, dict) or set(checks) != expected:
        return errors + ["Faltan etapas del control previo."]
    for key in expected:
        check = checks[key]
        if (not isinstance(check, dict) or check.get("status") != "pass"
                or not strings(check.get("evidence")) or not check["evidence"]):
            errors.append(f"Etapa pendiente o sin evidencia: {key}.")
    return errors


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        job = json.loads(args.path.read_text(encoding="utf-8-sig"))
        prompt = compile_prompt(job)
        print(json.dumps({"compiled": True, "prompt": prompt, "prompt_fingerprint": fingerprint(prompt)}, ensure_ascii=False))
        return 0
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"compiled": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
