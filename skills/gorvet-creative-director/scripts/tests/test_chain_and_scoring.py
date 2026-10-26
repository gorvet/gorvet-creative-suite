import copy
import importlib.util
from pathlib import Path
import unittest


def load(name):
    path = Path(__file__).resolve().parents[1] / (name + ".py")
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


chain = load("chain_handoff")
scoring = load("score_review")


def card(kind="visual", grade=3):
    return {"kind": kind, "observed": kind == "visual", "blockers": [],
            "criteria": {key: {"grade": grade, "evidence": ["Evidencia sintética del control."]}
                         for key in scoring.PROFILES[kind]}}


def packet(job, role, updates):
    return {"job_id": job["job_id"], "base_revision": job.get("revision", 0),
            "role": role, "updates": updates}


class ChainTests(unittest.TestCase):
    def test_sequential_contributions_preserve_other_work(self):
        original = {"job_id": "chain", "revision": 0, "direction": {}}
        job = original
        stages = [
            ("gorvet-creative-strategy", {"direction.message": "Mensaje", "direction.concept": "Concepto"}),
            ("image-art-direction", {"direction.medium": "Fotografía", "direction.scene": "Acción acordada"}),
            ("photography-direction", {"direction.capture": {"light": "Lateral"}}),
            ("poster-promotional-design", {"direction.typography": {"alignment": "left"}}),
            ("luces-camara-prompt", {"execution.prompt": "Instrucción consolidada"}),
            ("prompt-optimization-qa", {"execution.prompt": "Instrucción depurada"}),
        ]
        for role, updates in stages:
            job = chain.apply_packet(job, packet(job, role, updates))
        self.assertEqual(original, {"job_id": "chain", "revision": 0, "direction": {}})
        self.assertEqual(job["revision"], 6)
        self.assertEqual(job["direction"]["message"], "Mensaje")
        self.assertEqual(job["direction"]["capture"]["light"], "Lateral")
        self.assertEqual(job["execution"]["prompt"], "Instrucción depurada")
        self.assertEqual([x["role"] for x in job["chain"]], [x[0] for x in stages])

    def test_photography_cannot_redefine_strategy(self):
        job = {"job_id": "chain", "direction": {"message": "Original"}}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "photography-direction", {"direction.message": "Otro"}))
        self.assertEqual(job["direction"]["message"], "Original")

    def test_graphic_design_cannot_change_medium(self):
        job = {"job_id": "chain"}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "poster-promotional-design", {"direction.medium": "Otro"}))

    def test_art_cannot_add_copy(self):
        job = {"job_id": "chain"}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "image-art-direction", {"direction.image_text": ["Nuevo"]}))

    def test_stale_or_foreign_contribution_is_rejected(self):
        job = {"job_id": "chain", "revision": 3}
        for change in ({"base_revision": 2}, {"job_id": "other"}):
            data = packet(job, "photography-direction", {"direction.capture": {}})
            data.update(change)
            with self.assertRaises(ValueError):
                chain.apply_packet(job, data)

    def test_locked_decisions_cannot_be_rewritten_by_child(self):
        job = {"job_id": "chain", "locked_fields": ["direction"]}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "photography-direction", {"direction.capture": {}}))

    def test_text_qa_does_not_create_a_prompt(self):
        job = {"job_id": "chain"}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "prompt-optimization-qa", {"execution.prompt": "Inventado"}))

    def test_visual_qa_cannot_rewrite_the_art(self):
        job = {"job_id": "chain"}
        with self.assertRaises(ValueError):
            chain.apply_packet(job, packet(job, "visual-quality-review", {"direction.scene": "Otra"}))


class ScoringTests(unittest.TestCase):
    def test_ready_anchors_give_index_75(self):
        result = scoring.evaluate(card())
        self.assertEqual(result["index"], 75)
        self.assertEqual(result["verdict"], "pass")

    def test_high_average_cannot_hide_a_weak_criterion(self):
        data = card(grade=4)
        data["criteria"]["typography"]["grade"] = 2
        result = scoring.evaluate(data)
        self.assertGreater(result["index"], 85)
        self.assertEqual(result["verdict"], "revise")

    def test_blocker_overrides_a_maximum_index(self):
        data = card(grade=4)
        data["blockers"] = ["Un dato obligatorio es falso."]
        result = scoring.evaluate(data)
        self.assertEqual(result["index"], 100)
        self.assertEqual(result["verdict"], "revise")

    def test_unobserved_visual_cannot_be_scored(self):
        data = card()
        data["observed"] = False
        result = scoring.evaluate(data)
        self.assertIsNone(result["index"])
        self.assertEqual(result["verdict"], "unverified")

    def test_unjustified_or_required_criterion_cannot_be_omitted(self):
        for key, reason in (("typography", ""), ("communication", "No quiero evaluarlo")):
            data = card()
            data["criteria"][key] = {"applicable": False, "reason": reason}
            self.assertFalse(scoring.evaluate(data)["valid"])

    def test_optional_criterion_reweights_without_penalty(self):
        data = card()
        data["criteria"]["typography"] = {"applicable": False, "reason": "Imagen sin texto"}
        result = scoring.evaluate(data)
        self.assertEqual(result["index"], 75)
        self.assertEqual(result["verdict"], "pass")

    def test_decimal_boolean_and_missing_evidence_are_invalid(self):
        for grade in (3.5, True, 5, -1):
            data = card()
            data["criteria"]["structure"]["grade"] = grade
            self.assertFalse(scoring.evaluate(data)["valid"])
        data = card()
        data["criteria"]["structure"]["evidence"] = []
        self.assertFalse(scoring.evaluate(data)["valid"])

    def test_concept_does_not_claim_observing_an_image(self):
        data = card("concept")
        data["observed"] = False
        self.assertEqual(scoring.evaluate(data)["verdict"], "pass")

    def test_unknown_or_missing_criteria_are_invalid(self):
        data = card()
        del data["criteria"]["craft"]
        self.assertFalse(scoring.evaluate(data)["valid"])
        data = card()
        data["criteria"]["invisible"] = copy.deepcopy(data["criteria"]["craft"])
        self.assertFalse(scoring.evaluate(data)["valid"])

    def test_malformed_scorecards_are_not_approved(self):
        for data in (None, [], {}, {"kind": []}, {"kind": "visual", "criteria": []}):
            with self.subTest(data=data):
                self.assertFalse(scoring.evaluate(data)["valid"])


if __name__ == "__main__":
    unittest.main()
