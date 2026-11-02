import importlib.util
import json
from pathlib import Path
import tempfile
import unittest


class GenerateIndexTest(unittest.TestCase):
    def test_explicit_empty_clears_and_omitted_fields_inherit(self):
        spec = importlib.util.spec_from_file_location(
            "generate_index", Path(__file__).with_name("generate-index.py"))
        generator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(generator)
        with tempfile.TemporaryDirectory() as root:
            skills = Path(root, "skills")
            skills.mkdir()
            Path(skills, "sample.md").write_text(
                '---\nname: sample\nrequires: []\noutputs: []\n'
                'description:\nicon: ""\n---\nBody\n', encoding="utf-8")
            index = Path(root, "index.json")
            index.write_text(json.dumps({"skills": [{
                "name": "sample", "requires": ["old"], "outputs": ["old"],
                "description": "old", "icon": "old", "category": "utility",
                "downloads": 8, "rating": 4.5,
            }]}), encoding="utf-8")
            generator.SKILLS_DIR = str(skills)
            generator.INDEX_PATH = str(index)
            generator.main()
            result = json.loads(index.read_text(encoding="utf-8"))["skills"][0]
            self.assertEqual(result["requires"], [])
            self.assertEqual(result["outputs"], [])
            self.assertEqual(result["description"], "")
            self.assertEqual(result["icon"], "")
            self.assertEqual(result["category"], "utility")
            self.assertEqual(result["downloads"], 8)
            self.assertEqual(result["rating"], 4.5)


if __name__ == "__main__":
    unittest.main()
