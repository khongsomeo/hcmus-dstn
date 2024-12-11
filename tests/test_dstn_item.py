from unittest import TestCase
import json
import os
from src.dstn import DSTNItem

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEST_JSON = os.path.join(THIS_DIR, "data/sample.json")


class TestDSTNItem(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open(TEST_JSON, "r+", encoding="utf8") as json_data_file:
            self.json = json.load(json_data_file)

    def test_default_language(self):
        dstn_item = DSTNItem(json=self.json)
        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "vn")

    def test_set_language(self):
        dstn_item = DSTNItem(json=self.json, language="en")
        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "en")

    def test_item_size(self):
        dstn_item = DSTNItem(json=self.json, language="en")
        self.assertEqual(len(dstn_item.get_info()), len(self.json) + 1)

    def test_same_fields(self):
        dstn_item = DSTNItem(json=self.json)

        ignored_fields = ["language"]

        current_info = dstn_item.get_info()

        for field, value in current_info.items():
            if field not in ignored_fields:
                self.assertEqual(value, self.json[field])
