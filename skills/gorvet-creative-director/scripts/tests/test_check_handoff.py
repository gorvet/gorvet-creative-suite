import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

module_path = Path(__file__).resolve().parents[1] / "check_handoff.py"
spec = importlib.util.spec_from_file_location("handoff", module_path)
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def scorecard(kind):
    profiles = {"concept": ("fit", "specificity", "interest", "clarity", "feasibility"),
                "visual": ("communication", "character", "structure", "typography", "fidelity", "craft")}
    return {"kind": kind, "observed": kind == "visual", "blockers": [],
            "criteria": {key: {"grade": 3, "evidence": ["Evidencia sintética para probar el contrato."]}
                         for key in profiles[kind]}}


def proposal():
    job = {
        "schema_version": "1.3", "job_id": "test", "deliverable": "image",
        "brief": {"status": "ready", "material_questions": [],
                  "content_items": [{"id": "name", "text": "ALFA", "protected_literals": ["ALFA"], "required_in_image": True}]},
        "direction": {"message": "Identidad", "concept": "Forma y contraste",
                      "medium": "Ilustración", "composition": "Sujeto a la izquierda",
                      "image_text": ["ALFA"], "references": [{"id": "source", "role": "identity"}],
                      "gorvet": {"G": "Identificación", "O": "Campo gráfico", "R": "Contraste y formas",
                                 "V": "Encuentro", "E": "Sujeto y literal", "T": "Geométrico"}},
        "preflight": scorecard("concept"),
        "execution": {"prompt": "ALFA abajo; sujeto a la izquierda.",
                      "reference_ids": ["source"], "parameters": {"transparent_background": False},
                      "attempt": 1, "authorization": {"mode": "approval"}},
    }
    job["direction"]["content_decisions"] = [{"id": "name", "destination": "image", "reason": "Identificar el sujeto", "literals": ["ALFA"]}]
    job["direction"]["production_spec"] = {
        "canvas": "Ilustración cuadrada.", "intent": "Identificar ALFA por el contraste de dos formas.",
        "composition": "Formas superpuestas a la izquierda y literal abajo a la derecha.",
        "treatment": "Formas planas azul y naranja sobre un campo claro uniforme.",
        "style_basis": {"origin": "proposal", "evidence": "El encargo pide contraste de formas", "reason": "La superposición hace visible el encuentro"},
        "elements": [
            {"id": "subject", "kind": "subject", "instruction": "Dos discos planos se superponen parcialmente", "placement": "Mitad izquierda", "scale": "Masa principal, dos tercios de la altura"},
            {"id": "name", "kind": "text", "literal": "ALFA", "instruction": "Sans serif de peso medio sobre el fondo, sin soporte gráfico", "placement": "Abajo a la derecha con margen exterior", "scale": "Una línea, menor que los discos"}],
        "graphic_devices": [], "constraints": ["Bordes nítidos y colores uniformes."]}
    job["direction"]["composition"] = job["direction"]["production_spec"]["composition"]
    finalize(job)
    return job


def finalize(job):
    execution = job["execution"]
    execution["prompt"] = gate.production_module.compile_prompt(job)
    for field in ("prompt", "reference_ids", "parameters"):
        execution["published_" + field] = copy.deepcopy(execution[field])
    checks = ("scope", "preservation", "coverage") if job.get("task_mode") == "edit" else ("selection", "design", "anti_ai", "coverage")
    job["production_review"] = {
        "direction_fingerprint": gate.fingerprints(job)["direction"],
        "prompt_fingerprint": gate.production_module.fingerprint(execution["prompt"]), "blockers": [],
        "checks": {k: {"status": "pass", "evidence": ["Fixture sintética: control de la versión vigente."]} for k in checks}}
    execution["authorization"]["approved_fingerprint"] = gate.fingerprints(job)["proposal"]
    execution["authorization"]["approved_direction_fingerprint"] = gate.fingerprints(job)["direction"]
    return job


class HandoffTests(unittest.TestCase):
    def test_approved_proposal_can_generate(self):
        self.assertEqual(gate.validate(proposal(), "generate"), [])

    def test_hidden_mutations_are_rejected(self):
        for field, value in (("prompt", "Texto oculto"), ("reference_ids", []),
                             ("parameters", {"transparent_background": True})):
            with self.subTest(field=field):
                job = proposal()
                job["execution"][field] = value
                self.assertTrue(gate.validate(job, "generate"))

    def test_stale_approval_after_visible_update_is_rejected(self):
        for field, value in (("prompt", "ALFA arriba"), ("parameters", {"size": "new"})):
            with self.subTest(field=field):
                job = proposal()
                job["execution"][field] = value
                job["execution"]["published_" + field] = copy.deepcopy(value)
                self.assertTrue(gate.validate(job, "generate"))

    def test_changed_direction_requires_new_approval(self):
        job = proposal()
        job["direction"]["composition"] = "Sujeto a la derecha"
        self.assertTrue(gate.validate(job, "generate"))

    def test_approval_is_scoped_to_the_job(self):
        job = proposal()
        job["job_id"] = "different-job"
        self.assertTrue(gate.validate(job, "generate"))

    def test_unknown_contract_version_is_rejected(self):
        job = proposal()
        job["schema_version"] = "2.0"
        self.assertTrue(gate.validate(job, "generate"))

    def test_unpublished_prompt_is_rejected(self):
        job = proposal()
        del job["execution"]["published_prompt"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_missing_selected_copy_is_rejected(self):
        job = proposal()
        job["direction"]["image_text"].append("BETA")
        job["execution"]["authorization"]["approved_fingerprint"] = gate.fingerprints(job)["proposal"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_unknown_or_missing_authorization_is_rejected(self):
        for auth in ({}, {"mode": "automatic"}, {"mode": "direct"}):
            job = proposal()
            job["execution"]["authorization"] = auth
            self.assertTrue(gate.validate(job, "generate"))

    def test_explicit_direct_instruction_can_generate(self):
        job = proposal()
        job["execution"]["authorization"] = {"mode": "direct", "direct_instruction": "Genera directamente."}
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_visibility_override_needs_explicit_instruction(self):
        job = proposal()
        job["execution"]["visibility"] = "omit_on_request"
        self.assertTrue(gate.validate(job, "generate"))
        job["execution"]["authorization"]["visibility_instruction"] = "No muestres el prompt."
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_prompt_only_request_does_not_authorize_image(self):
        job = proposal()
        job["deliverable"] = "prompt"
        self.assertTrue(gate.validate(job, "generate"))

    def test_local_correction_reuses_direction_authorization(self):
        job = proposal()
        execution = job["execution"]
        execution["attempt"] = 2
        execution["correction"] = {"restore_approved": True, "source_output_id": "generated-1",
                                   "diagnosis": "Restituir la colocación del sujeto.",
                                   "direction_fingerprint": gate.fingerprints(job)["direction"]}
        execution["reference_ids"].append("generated-1")
        execution["published_reference_ids"] = list(execution["reference_ids"])
        finalize(job)
        self.assertEqual(gate.validate(job, "generate"), [])
        job["direction"]["composition"] = "Otra composición"
        self.assertTrue(gate.validate(job, "generate"))

    def test_unsupported_fourth_attempt_is_rejected(self):
        job = proposal()
        job["execution"]["attempt"] = 4
        self.assertTrue(gate.validate(job, "generate"))

    def test_review_must_match_real_output_and_direction(self):
        job = proposal()
        job["output"] = {"id": "generated-1"}
        job["review"] = {"observed": True, "output_id": "generated-1", "verdict": "pass",
                         "direction_fingerprint": gate.fingerprints(job)["direction"],
                         "evidence": ["Se reconoce el sujeto y se lee ALFA en la zona prevista."],
                         "scorecard": scorecard("visual")}
        self.assertEqual(gate.validate(job, "deliver"), [])
        for field, value in (("observed", False), ("output_id", "other"), ("verdict", "revise"),
                             ("evidence", []), ("direction_fingerprint", "old")):
            with self.subTest(field=field):
                changed = copy.deepcopy(job)
                changed["review"][field] = value
                self.assertTrue(gate.validate(changed, "deliver"))

    def test_declared_pass_cannot_override_a_failed_scorecard(self):
        job = proposal()
        job["output"] = {"id": "generated-1"}
        job["review"] = {"observed": True, "output_id": "generated-1", "verdict": "pass",
                         "direction_fingerprint": gate.fingerprints(job)["direction"],
                         "evidence": ["El literal no coincide."], "scorecard": scorecard("visual")}
        job["review"]["scorecard"]["blockers"] = ["Literal incorrecto."]
        self.assertTrue(gate.validate(job, "deliver"))

    def test_generation_rejects_unresolved_preflight(self):
        job = proposal()
        job["preflight"]["criteria"]["clarity"]["grade"] = 2
        self.assertTrue(gate.validate(job, "generate"))

    def test_material_brief_question_blocks_production(self):
        job = proposal()
        job["brief"]["material_questions"] = ["Confirmar una condición material."]
        self.assertTrue(gate.validate(job, "generate"))

    def test_method_context_is_required_before_execution(self):
        job = proposal()
        del job["direction"]["gorvet"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_bounded_edit_uses_scope_without_inventing_a_new_concept(self):
        job = proposal()
        job["task_mode"] = "edit"
        job["preflight"] = {"kind": "edit_scope", "source_output_id": "source",
                            "target": "Literal", "mutation": "Restituir ALFA", "protected": ["Identidad", "Composición"],
                            "acceptance": "Texto correcto y resto conservado", "ready": True}
        finalize(job)
        self.assertEqual(gate.validate(job, "generate"), [])
        job["preflight"]["source_output_id"] = "unknown"
        self.assertTrue(gate.validate(job, "generate"))

    def test_malformed_inputs_fail_without_crashing(self):
        for value in (None, [], {}, {"direction": []}, {"direction": {"references": [None]}},
                      {"direction": {}, "execution": None}):
            with self.subTest(value=value):
                self.assertTrue(gate.validate(value, "generate"))

    def test_cli_returns_json_and_process_status(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            job = proposal()
            path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
            command = [sys.executable, str(module_path), str(path), "--stage", "generate"]
            allowed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(allowed.returncode, 0, allowed.stderr)
            self.assertTrue(json.loads(allowed.stdout)["allowed"])
            job["execution"]["published_prompt"] = "Another prompt"
            path.write_text(json.dumps(job), encoding="utf-8")
            blocked = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(blocked.returncode, 1)
            self.assertFalse(json.loads(blocked.stdout)["allowed"])

    def test_shipped_example_is_unapproved_and_not_modified_by_check(self):
        example = module_path.parents[1] / "examples" / "handoff.json"
        before = example.read_bytes()
        result = subprocess.run([sys.executable, str(module_path), str(example), "--stage", "generate"],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 1)
        self.assertFalse(json.loads(result.stdout)["allowed"])
        self.assertEqual(example.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
