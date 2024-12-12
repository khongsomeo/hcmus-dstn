"""Test for DSTN Item

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

from unittest import TestCase
from src.dstn import DSTNItem
from .factory.student_factory import StudentFactory


class TestDSTNItem(TestCase):
    """Test DSTN Item

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, *args, **kwargs):
        """Initialization

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(*args, **kwargs)
        self.factory = StudentFactory()

    def setUp(self):
        self.json = self.factory.create_student()

    def test_default_language(self):
        """Test if the default language is `vn`

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json)

        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "vn")

    def test_set_language(self):
        """Test if we can successfully set a new language for DSTNItem

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json, language="en")

        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "en")

    def test_item_size(self):
        """Test if the class holds enough items after initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json)

        self.assertEqual(len(dstn_item.get_info()), len(self.json) + 1)

    def test_same_fields(self):
        """Test if there are no information loss occurs during intialization.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json)

        ignored_fields = ["language"]
        current_info = dstn_item.get_info()

        for field, value in current_info.items():
            if field not in ignored_fields:
                self.assertEqual(value, self.json[field])
