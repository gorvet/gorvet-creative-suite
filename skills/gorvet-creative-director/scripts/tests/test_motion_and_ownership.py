import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from test_check_handoff import gate, proposal, scorecard
from test_chain_and_scoring import chain, packet, scoring


def video():
    job = proposal()
    job.update(schema_version="1.2", deliverable="video")
    job["direction"]["motion"] = {
        "duration": 6,
        "shots": [
            {"id": "s1", "start": 0, "end": 3, "function": "Reconocer la forma",
             "action": "La forma gira y se detiene", "camera": "Fija",
             "transition": "Corte por forma", "continuity": "Termina frontal"},
            {"id": "s2", "start": 3, "end": 6, "function": "Leer la marca",
             "action": "ALFA aparece y permanece", "camera": "Fija",
             "transition": "Salida a negro", "continuity": "Recibe forma frontal"},
        ], "audio": {"mode": "sound", "spec": "Un golpe suave en el corte"},
        "delivery": {"aspect_ratio": "1:1", "format": "mp4"},
    }
    approve(job)
    return job


def approve(job):
    job["execution"]["authorization"]["approved_fingerprint"] = gate.fingerprints(job)["proposal"]


def delivered():
    job = video()
    playback = {"full_duration": True, "transitions_checked": True, "audio_checked": True}
    card = {"kind": "motion", "observed": True, "playback": copy.deepcopy(playback), "blockers": [],
            "criteria": {k: {"grade": 3, "evidence": ["Fixture: observado en 0–6 s."]}
                         for k in scoring.PROFILES["motion"]}}
    job["output"] = {"id": "render", "media_type": "video", "duration": 6}
    job["review"] = {"observed": True, "output_id": "render", "verdict": "pass",
                     "direction_fingerprint": gate.fingerprints(job)["direction"],
                     "evidence": ["Fixture: reproducción 0–6 s y corte 3 s."],
                     "playback": playback, "scorecard": card}
    return job


class MotionTests(unittest.TestCase):
    def test_video_uses_shared_approval_and_delivery_gates(self):
        self.assertEqual(gate.validate(video(), "generate"), [])
        self.assertEqual(gate.validate(delivered(), "deliver"), [])

    def test_timing_gap_overlap_reordering_and_invalid_numbers(self):
        for value in (-1, 1, 4, True, float("nan"), "3"):
            job = video()
            job["direction"]["motion"]["shots"][1]["start"] = value
            approve(job) if not isinstance(value, float) else None
            self.assertTrue(gate.motion_module.validate_motion(job, "generate"))

    def test_missing_plan_fields_and_duplicate_ids(self):
        for field in ("action", "camera", "function", "continuity", "transition", "id"):
            job = video()
            del job["direction"]["motion"]["shots"][0][field]
            self.assertTrue(gate.motion_module.validate_motion(job, "generate"))
        job = video()
        job["direction"]["motion"]["shots"][1]["id"] = "s1"
        self.assertTrue(gate.motion_module.validate_motion(job, "generate"))

    def test_missing_or_wrong_duration_audio_delivery(self):
        for field, value in (("duration", 8), ("duration", False), ("shots", []),
                             ("audio", {}), ("delivery", {})):
            job = video()
            job["direction"]["motion"][field] = value
            self.assertTrue(gate.motion_module.validate_motion(job, "generate"))

    def test_changed_timeline_invalidates_approval(self):
        job = video()
        job["direction"]["motion"]["shots"][0]["action"] = "Otra acción"
        self.assertTrue(gate.validate(job, "generate"))

    def test_video_requires_new_contract(self):
        job = video()
        job["schema_version"] = "1.1"
        self.assertTrue(gate.validate(job, "generate"))

    def test_image_score_cannot_validate_video(self):
        job = delivered()
        job["review"]["scorecard"] = scorecard("visual")
        self.assertTrue(gate.validate(job, "deliver"))

    def test_partial_playback_and_unheard_audio_cannot_pass(self):
        for field in ("full_duration", "transitions_checked", "audio_checked"):
            for scope in ("review", "scorecard"):
                job = delivered()
                target = job["review"] if scope == "review" else job["review"]["scorecard"]
                target["playback"][field] = False
                self.assertTrue(gate.validate(job, "deliver"))

    def test_sound_cannot_be_marked_not_applicable(self):
        job = delivered()
        job["review"]["scorecard"]["criteria"]["audio"] = {
            "applicable": False, "reason": "No se escuchó"}
        self.assertTrue(gate.validate(job, "deliver"))

    def test_silent_video_does_not_require_audio_review(self):
        job = delivered()
        job["direction"]["motion"]["audio"] = {"mode": "silent", "spec": "Entrega sin pista sonora"}
        job["review"]["direction_fingerprint"] = gate.fingerprints(job)["direction"]
        job["review"]["playback"]["audio_checked"] = False
        job["review"]["scorecard"]["playback"]["audio_checked"] = False
        job["review"]["scorecard"]["criteria"]["audio"] = {
            "applicable": False, "reason": "Entrega silenciosa acordada"}
        self.assertEqual(gate.validate(job, "deliver"), [])

    def test_still_or_wrong_duration_is_not_a_video_delivery(self):
        for field, value in (("media_type", "image"), ("duration", 3), ("duration", True)):
            job = delivered()
            job["output"][field] = value
            self.assertTrue(gate.validate(job, "deliver"))

    def test_motion_cli_rejects_invalid_plan(self):
        script = Path(__file__).resolve().parents[1] / "check_motion.py"
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "job.json"
            path.write_text(json.dumps({}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(script), str(path), "--stage", "generate"],
                                    capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(result.returncode, 1)
            self.assertFalse(json.loads(result.stdout)["allowed"])

    def test_all_roles_chain_without_erasing_prior_decisions(self):
        job = {"job_id": "all-roles", "revision": 0}
        contributions = [
            ("gorvet-creative-director", {"brief": {"purpose": "Diseño"}}),
            ("gorvet-creative-strategy", {"direction.concept": "Forma reconocible"}),
            ("brand-reference-direction", {"direction.identity": {"symbol": "Maestro"}}),
            ("campaign-storytelling", {"direction.series": {"pieces": ["a", "b"]}}),
            ("image-art-direction", {"direction.visual_system": {"color": "Rojo"}}),
            ("photography-direction", {"direction.capture": {"light": "Lateral"}}),
            ("poster-promotional-design", {"direction.typography": {"weight": "Bold"}}),
            ("video-motion-direction", {"direction.motion": video()["direction"]["motion"]}),
            ("luces-camara-prompt", {"execution.prompt": "ALFA en reposo final"}),
            ("prompt-optimization-qa", {"execution.prompt": "ALFA permanece al final"}),
            ("visual-quality-review", {"review": {"verdict": "revise"}}),
        ]
        for role, updates in contributions:
            job = chain.apply_packet(job, packet(job, role, updates))
        self.assertEqual(job["revision"], 11)
        self.assertEqual(job["direction"]["identity"]["symbol"], "Maestro")
        self.assertEqual(job["direction"]["concept"], "Forma reconocible")
        self.assertEqual(job["direction"]["motion"]["duration"], 6)
        self.assertEqual(job["direction"]["capture"]["light"], "Lateral")

    def test_every_role_rejects_foreign_owned_fields(self):
        job = {"job_id": "ownership"}
        exclusive = {field: role for role, fields in chain.OWNERS.items()
                     for field in fields if field != "execution.prompt"}
        for role, own in chain.OWNERS.items():
            for field in exclusive:
                if field in own:
                    continue
                with self.subTest(role=role, field=field), self.assertRaises(ValueError):
                    chain.apply_packet(job, packet(job, role, {field: "Fuera de alcance"}))


if __name__ == "__main__":
    unittest.main()
