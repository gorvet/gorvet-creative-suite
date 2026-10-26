"""Check the evidence structure and calculation of a GORVET scorecard."""

import argparse
import json
from pathlib import Path
import sys


PROFILES = {
    "concept": {"fit": 25, "specificity": 20, "interest": 20, "clarity": 20, "feasibility": 15},
    "visual": {"communication": 20, "character": 20, "structure": 20,
               "typography": 15, "fidelity": 15, "craft": 10},
}
OPTIONAL = {"concept": set(), "visual": {"typography", "fidelity"}}


def evidence_list(value):
    return isinstance(value, list) and bool(value) and all(
        isinstance(item, str) and item.strip() for item in value)


def evaluate(card):
    if not isinstance(card, dict):
        return {"valid": False, "index": None, "verdict": "unverified", "errors": ["Falta la rúbrica."]}
    kind = card.get("kind")
    if not isinstance(kind, str) or kind not in PROFILES:
        return {"valid": False, "index": None, "verdict": "unverified", "errors": ["Rúbrica desconocida."]}
    errors, weak = [], []
    criteria = card.get("criteria")
    if not isinstance(criteria, dict):
        criteria = {}
        errors.append("criteria debe ser un objeto.")
    if set(criteria) != set(PROFILES[kind]):
        errors.append("La rúbrica debe contener exactamente los criterios de su perfil.")
    blockers = card.get("blockers")
    if not isinstance(blockers, list) or any(not isinstance(x, str) or not x.strip() for x in blockers):
        blockers = []
        errors.append("blockers debe ser una lista de hallazgos materiales.")
    if kind == "visual" and card.get("observed") is not True:
        errors.append("No se puntúa una imagen que no se ha observado.")
    points, weights = 0, 0
    for key, weight in PROFILES[kind].items():
        criterion = criteria.get(key)
        if not isinstance(criterion, dict):
            errors.append(f"Falta el criterio {key}.")
            continue
        applicable = criterion.get("applicable", True)
        if type(applicable) is not bool:
            errors.append(f"Aplicabilidad inválida en {key}.")
            continue
        if not applicable:
            reason = criterion.get("reason")
            if key not in OPTIONAL[kind] or not isinstance(reason, str) or not reason.strip():
                errors.append(f"No aplicable injustificado en {key}.")
            if "grade" in criterion:
                errors.append(f"Un criterio no aplicable no recibe nota: {key}.")
            continue
        grade = criterion.get("grade")
        if type(grade) is not int or not 0 <= grade <= 4:
            errors.append(f"La nota de {key} debe ser un entero entre 0 y 4.")
            continue
        if not evidence_list(criterion.get("evidence")):
            errors.append(f"Falta evidencia en {key}.")
        points += grade * weight
        weights += weight
        if grade < 3:
            weak.append(key)
    index = round(25 * points / weights) if weights and not errors else None
    verdict = "unverified" if errors else ("revise" if weak or blockers else "pass")
    return {"valid": not errors, "index": index, "verdict": verdict,
            "weak": weak, "blockers": blockers, "errors": errors}


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    try:
        result = evaluate(json.loads(args.path.read_text(encoding="utf-8-sig")))
    except (OSError, ValueError, TypeError) as exc:
        result = {"valid": False, "verdict": "unverified", "errors": [str(exc)]}
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
