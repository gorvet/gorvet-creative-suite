"""Apply a bounded specialist contribution without mutating the input job."""

import argparse
import copy
import json
from pathlib import Path
import sys


OWNERS = {
    "gorvet-creative-director": {"brief", "direction.composition", "direction.gorvet", "direction.production_spec", "route"},
    "gorvet-creative-strategy": {"direction.message", "direction.concept", "direction.image_text",
                                 "direction.support_copy", "direction.omitted_content", "direction.content_decisions"},
    "image-art-direction": {"direction.medium", "direction.visual_proposition", "direction.scene",
                             "direction.visual_system", "direction.layout_blueprint"},
    "photography-direction": {"direction.capture"},
    "poster-promotional-design": {"direction.layout", "direction.typography"},
    "brand-reference-direction": {"direction.references", "direction.protected_attributes",
                                   "direction.reference_rules", "direction.identity"},
    "campaign-storytelling": {"direction.series"},
    "video-motion-direction": {"direction.motion"},
    "luces-camara-prompt": {"execution.prompt", "execution.reference_ids", "execution.parameters"},
    "prompt-optimization-qa": {"execution.prompt"},
    "visual-quality-review": {"review", "production_review"},
}


def apply_packet(job, packet):
    if not isinstance(job, dict) or not isinstance(packet, dict):
        raise ValueError("El encargo y la contribución deben ser objetos.")
    job_id = job.get("job_id")
    if not isinstance(job_id, str) or not job_id.strip() or packet.get("job_id") != job_id:
        raise ValueError("La contribución no corresponde al encargo.")
    revision = job.get("revision", 0)
    if type(revision) is not int or revision < 0 or type(packet.get("base_revision")) is not int:
        raise ValueError("La revisión debe ser un entero no negativo.")
    if packet["base_revision"] != revision:
        raise ValueError("La contribución parte de una versión obsoleta.")
    role = packet.get("role")
    if not isinstance(role, str) or role not in OWNERS:
        raise ValueError("Especialista desconocido.")
    updates = packet.get("updates")
    if not isinstance(updates, dict) or not updates:
        raise ValueError("No hay decisiones aportadas.")
    if not set(updates).issubset(OWNERS[role]):
        raise ValueError("El especialista intenta modificar decisiones ajenas.")
    locks = job.get("locked_fields", [])
    if not isinstance(locks, list) or any(not isinstance(x, str) or not x for x in locks):
        raise ValueError("Lista de campos protegidos inválida.")
    for path in updates:
        if any(path == lock or path.startswith(lock + ".") or lock.startswith(path + ".") for lock in locks):
            raise ValueError("La contribución modifica una decisión protegida.")
    if role == "prompt-optimization-qa":
        existing = job.get("execution", {})
        if not isinstance(existing, dict) or not isinstance(existing.get("prompt"), str) or not existing["prompt"].strip():
            raise ValueError("QA textual necesita un prompt existente; no crea otra dirección.")
    result = copy.deepcopy(job)
    for path, value in updates.items():
        parts = path.split(".")
        parent = result
        for part in parts[:-1]:
            if part not in parent:
                parent[part] = {}
            if not isinstance(parent[part], dict):
                raise ValueError("El registro contiene un grupo incompatible con la contribución.")
            parent = parent[part]
        parent[parts[-1]] = copy.deepcopy(value)
    trace = result.get("chain", [])
    if not isinstance(trace, list):
        raise ValueError("La cadena registrada debe ser una lista.")
    result["revision"] = revision + 1
    result["chain"] = trace + [{"role": role, "base_revision": revision,
                               "result_revision": revision + 1, "writes": sorted(updates)}]
    return result


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job", type=Path)
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    try:
        result = apply_packet(json.loads(args.job.read_text(encoding="utf-8-sig")),
                              json.loads(args.packet.read_text(encoding="utf-8-sig")))
    except (OSError, ValueError, TypeError) as exc:
        print(json.dumps({"allowed": False, "errors": [str(exc)]}, ensure_ascii=False))
        return 1
    print(json.dumps({"allowed": True, "job": result}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
