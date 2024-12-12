"""Defining structures so that a class is not too big.

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""


class GeneralType:
    """Generale class for a Type, which would have Vietnamese and English name.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialization

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        self.name_vn = kwargs.get("name_vn", None)
        self.name_en = kwargs.get("name_en", None)

    def get_name_vn(self) -> str:
        """Get type's name in Vietnamese

        Returns:
            str: type name, in Vietnamese
        """

        return self.name_vn

    def get_name_en(self) -> str:
        """Get type's name in English

        Returns:
            str: type name, in English
        """

        return self.name_en


class ProgramType(GeneralType):
    """Program Type - with additional `code` field.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(**kwargs)
        self.code = kwargs.get("code", None)

    def get_code(self):
        """Get the Program Code

        Returns:
            str : Program Code
        """

        return self.code


class MajorType(GeneralType):
    """Major Type

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """


class GraduationType(GeneralType):
    """Graduation Type

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """
