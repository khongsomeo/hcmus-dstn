"""Test for DSTNItem

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

from typing import Dict
from unittest import TestCase
from src.dstn import DSTNItem
from .factory.student_factory import StudentFactory


class TestDSTNItem(TestCase):
    """Test DSTN Item

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Factory to generate a Student
    factory: StudentFactory

    # Informations of a Student, stored as a dict.
    json: Dict[str, str]

    def __init__(self, *args, **kwargs) -> None:
        """Initialization

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(*args, **kwargs)
        self.factory = StudentFactory()

    def setUp(self):
        self.json = self.factory.create_student()

    def test_default_language(self) -> None:
        """Test if the default language is `vn`

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json)

        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "vn")

    def test_set_language(self) -> None:
        """Test if we can successfully set a new language for DSTNItem

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json, language="en")

        self.assertTrue(hasattr(dstn_item, "info"))
        self.assertEqual(dstn_item.get_language(), "en")

    def test_item_size(self) -> None:
        """Test if the class holds enough items after initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json)

        self.assertEqual(len(dstn_item.get_info()), len(self.json) + 1)

    def test_same_fields(self) -> None:
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

    def test_not_loss_information_vn(self) -> None:
        """Test if the Vietnamese table generated (by using get_string)
        contain no information loss.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json, language="vn")

        # These fields from self.json should appears in the table.
        should_appear_fields = [
            "masv", "ngaysinh", "hoten", "Bac",
            "tenbac", "mahe", "tenhe", "dotnam",
            "tennganh", "loaitotnghiep", "sobang", "sovaoso", "ngayqd"
        ]

        for field in should_appear_fields:
            self.assertIn(self.json[field], str(dstn_item))

    def test_not_loss_information_en(self) -> None:
        """Test if the English table generated (by using get_string)
        contain no information loss.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        dstn_item = DSTNItem(json=self.json, language="en")

        # These fields from self.json should appears in the table.
        should_appear_fields = [
            "masv", "ngaysinh", "hotenAnh", "Bac",
            "tenbacAnh", "mahe", "tenheAnh", "dotnam",
            "tennganhAnh", "loaitotnghiepAnh", "sobang", "sovaoso", "ngayqd"
        ]

        for field in should_appear_fields:
            self.assertIn(self.json[field], str(dstn_item))
