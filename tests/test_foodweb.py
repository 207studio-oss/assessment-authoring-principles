import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "skills" / "checkyboard-authoring"
spec = importlib.util.spec_from_file_location("foodweb", ROOT / "scripts" / "foodweb.py")
foodweb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foodweb)


class FoodwebChecks(unittest.TestCase):
    def setUp(self):
        self.graph = json.loads((ROOT / "references" / "synthetic-foodweb.json").read_text(encoding="utf-8"))

    def test_complete_direct_loss_set(self):
        result = foodweb.analyze(self.graph, ["plant-a"])
        self.assertEqual(result["direct_food_loss"], ["herbivore-a", "herbivore-b"])
        self.assertNotIn("consumer-d", result["direct_food_loss"])

    def test_alternative_producer_path(self):
        result = foodweb.analyze(self.graph, ["plant-a"])
        self.assertEqual(result["supported_paths"]["predator-e"], ["plant-b", "larva-c", "consumer-d", "predator-e"])

    def test_indirect_loss_does_not_become_direct_loss(self):
        self.graph["edges"].remove(["larva-c", "consumer-d"])
        result = foodweb.analyze(self.graph, ["plant-a"])
        self.assertIn("consumer-d", result["no_remaining_producer_path"])
        self.assertNotIn("consumer-d", result["direct_food_loss"])

    def test_all_producers_removed(self):
        result = foodweb.analyze(self.graph, ["plant-a", "plant-b"])
        self.assertFalse(result["supported_paths"])
        self.assertEqual(len(result["no_remaining_producer_path"]), 5)

    def test_unknown_removed_node(self):
        with self.assertRaises(ValueError):
            foodweb.analyze(self.graph, ["unknown"])

    def test_producer_cannot_consume_another_node(self):
        self.graph["edges"].append(["larva-c", "plant-b"])
        with self.assertRaises(ValueError):
            foodweb.analyze(self.graph, ["plant-a"])


if __name__ == "__main__":
    unittest.main()
