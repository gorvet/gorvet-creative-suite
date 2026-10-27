import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_check_handoff import gate, proposal, finalize


compiler = gate.production_module


class ProductionPacketTests(unittest.TestCase):
    def test_self_contained_compilation_has_every_selected_literal_and_no_raw_brief(self):
        job = proposal()
        job["brief"]["content_items"].extend([
            {"id": "support", "text": "Dato operativo complementario"},
            {"id": "internal", "text": "Nota privada del equipo"}])
        job["direction"]["content_decisions"].extend([
            {"id": "support", "destination": "support", "reason": "Consulta posterior", "literals": [],
             "copy": "Información para el mensaje acompañante", "support_destination": "Mensaje separado acordado"},
            {"id": "internal", "destination": "omit", "reason": "No comunica al destinatario", "literals": []}])
        finalize(job)
        prompt = job["execution"]["prompt"]
        self.assertIn('"ALFA"', prompt)
        self.assertIn("Mitad izquierda", prompt)
        self.assertNotIn("Dato operativo", prompt)
        self.assertNotIn("mensaje acompañante", prompt)
        self.assertNotIn("Nota privada", prompt)
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_unclassified_content_blocks_compilation(self):
        job = proposal()
        job["brief"]["content_items"].append({"id": "pending", "text": "Dato aún sin seleccionar"})
        self.assertTrue(gate.validate(job, "generate"))

    def test_all_content_may_be_retained_when_review_finds_it_necessary(self):
        # No quota of words or omissions: selection is a design judgment.
        self.assertEqual(gate.validate(proposal(), "generate"), [])

    def test_required_copy_cannot_move_out_of_image(self):
        job = proposal()
        job["direction"]["content_decisions"][0].update(destination="omit", literals=[])
        job["direction"]["image_text"] = []
        self.assertTrue(gate.validate(job, "generate"))

    def test_protected_fact_cannot_be_silently_normalized(self):
        job = proposal()
        job["direction"]["content_decisions"][0]["literals"] = ["ALPHA"]
        job["direction"]["image_text"] = ["ALPHA"]
        job["direction"]["production_spec"]["elements"][1]["literal"] = "ALPHA"
        self.assertTrue(gate.validate(job, "generate"))

    def test_support_requires_actual_destination(self):
        job = proposal()
        job["brief"]["content_items"].append({"id": "more", "text": "Detalle"})
        job["direction"]["content_decisions"].append({"id": "more", "destination": "support", "reason": "Consultar después",
                                                     "literals": [], "copy": "Detalle adicional"})
        self.assertTrue(gate.validate(job, "generate"))

    def test_unknown_duplicate_or_unmapped_literal_blocks(self):
        for mutation in ("source", "duplicate", "extra_literal", "missing_literal"):
            job = proposal()
            if mutation == "source":
                job["direction"]["content_decisions"][0]["id"] = "unknown"
            elif mutation == "duplicate":
                job["direction"]["content_decisions"].append(copy.deepcopy(job["direction"]["content_decisions"][0]))
            elif mutation == "extra_literal":
                job["direction"]["production_spec"]["elements"].append({"id": "extra", "kind": "text", "literal": "PROMESA INVENTADA",
                                                                       "instruction": "Sans serif", "placement": "Arriba", "scale": "Grande"})
            else:
                job["direction"]["production_spec"]["elements"].pop()
            with self.subTest(mutation=mutation):
                self.assertTrue(gate.validate(job, "generate"))

    def test_each_element_needs_explicit_placement_scale_and_instruction(self):
        for key in ("instruction", "placement", "scale"):
            job = proposal()
            del job["direction"]["production_spec"]["elements"][0][key]
            self.assertTrue(gate.validate(job, "generate"))

    def test_vague_prompt_cannot_replace_resolved_design_even_with_approval(self):
        job = proposal()
        execution = job["execution"]
        execution["prompt"] = execution["published_prompt"] = "ALFA. Composición editorial de gran personalidad, buena jerarquía. Utilizar exactamente los textos establecidos en la propuesta."
        execution["authorization"]["approved_fingerprint"] = gate.fingerprints(job)["proposal"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_context_dependent_clause_cannot_become_a_design_block(self):
        job = proposal()
        job["direction"]["production_spec"]["elements"][1]["instruction"] = "Utilizar los textos establecidos en la propuesta"
        with self.assertRaises(ValueError):
            compiler.compile_prompt(job)

    def test_protected_attributes_survive_compilation(self):
        job = proposal()
        job["direction"]["protected_attributes"] = ["Conserva la geometría exacta del sujeto de source."]
        finalize(job)
        self.assertIn(job["direction"]["protected_attributes"][0], job["execution"]["prompt"])
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_graphic_devices_cannot_be_unresolved_or_inconsistent(self):
        job = proposal()
        job["direction"]["production_spec"]["graphic_devices"] = ["Marco que no se ha diseñado"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_conflicting_integrated_composition_blocks_compilation(self):
        job = proposal()
        job["direction"]["composition"] = "Sujeto a la derecha"
        self.assertTrue(gate.validate(job, "generate"))

    def test_appearance_has_basis_and_graphic_devices_are_explicit(self):
        for field in ("style_basis", "graphic_devices", "constraints"):
            job = proposal()
            del job["direction"]["production_spec"][field]
            self.assertTrue(gate.validate(job, "generate"))
        job = proposal()
        job["direction"]["production_spec"]["style_basis"]["origin"] = "automatic_category_default"
        self.assertTrue(gate.validate(job, "generate"))

    def test_expressive_styles_are_allowed_when_designed(self):
        job = proposal()
        spec = job["direction"]["production_spec"]
        spec["treatment"] = "Tinta impresa con textura visible y contraste irregular deliberado."
        spec["style_basis"] = {"origin": "user", "evidence": "Petición explícita de lenguaje impreso", "reason": "El gesto material es parte del encargo"}
        spec["elements"].append({"id": "accent", "kind": "graphic", "instruction": "Una pincelada azul corta, sin envolver el literal",
                                  "placement": "Bajo ALFA", "scale": "Más estrecha que el literal"})
        spec["graphic_devices"] = ["accent"]
        finalize(job)
        self.assertIn("Una pincelada azul", job["execution"]["prompt"])
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_missing_pending_or_empty_review_stage_blocks(self):
        for mutation in ("missing", "pending", "no_evidence", "blocker"):
            job = proposal()
            review = job["production_review"]
            if mutation == "missing":
                del review["checks"]["anti_ai"]
            elif mutation == "pending":
                review["checks"]["design"]["status"] = "revise"
            elif mutation == "no_evidence":
                review["checks"]["coverage"]["evidence"] = []
            else:
                review["blockers"] = ["Selección aún pendiente"]
            self.assertTrue(gate.validate(job, "generate"))

    def test_style_change_needs_new_review_even_after_recompiling_and_approving(self):
        job = proposal()
        job["direction"]["production_spec"]["treatment"] = "Otro tratamiento concreto"
        execution = job["execution"]
        execution["prompt"] = execution["published_prompt"] = compiler.compile_prompt(job)
        execution["authorization"]["approved_fingerprint"] = gate.fingerprints(job)["proposal"]
        self.assertTrue(gate.validate(job, "generate"))

    def test_old_contract_does_not_bypass_new_gates(self):
        for version in ("1.1", "1.2"):
            job = proposal()
            job["schema_version"] = version
            job.pop("production_review")
            job["direction"].pop("production_spec")
            self.assertTrue(gate.validate(job, "generate"))

    def test_textless_work_does_not_invent_copy_or_force_editorial_content(self):
        job = proposal()
        job["brief"]["content_items"] = []
        job["direction"].update(image_text=[], content_decisions=[])
        job["direction"]["production_spec"]["elements"].pop()
        finalize(job)
        self.assertIn("Sin texto externo", job["execution"]["prompt"])
        self.assertEqual(gate.validate(job, "generate"), [])

    def test_compiler_cli_is_read_only_and_rejects_incomplete_work(self):
        script = Path(__file__).resolve().parents[1] / "compile_production.py"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            for job, expected in ((proposal(), 0), ({"schema_version": "1.3"}, 1)):
                path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
                before = path.read_bytes()
                result = subprocess.run([sys.executable, str(script), str(path)], capture_output=True, text=True, encoding="utf-8")
                self.assertEqual(result.returncode, expected, result.stderr)
                self.assertEqual(json.loads(result.stdout)["compiled"], expected == 0)
                self.assertEqual(path.read_bytes(), before)

    def test_malformed_editorial_and_design_data_fail_without_crashing(self):
        for group, field, value in (("brief", "content_items", [None]), ("direction", "content_decisions", [None]),
                                    ("direction", "production_spec", [])):
            job = proposal()
            job[group][field] = value
            self.assertTrue(gate.validate(job, "generate"))


if __name__ == "__main__":
    unittest.main()
