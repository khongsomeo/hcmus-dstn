"""Exceptions for DSTN

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""


class HTTPException(Exception):
    """HttpException for DSTN

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, message=None, **kwargs):
        """Initialization

        Args:
            message (_str_): _message_

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(self, message)

        self.message = message
        self.response = kwargs.get("response", None)

    def __str__(self):
        """__str__ method

        Returns:
            _str_: _default string_

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        if self.message:
            return f"HTTPException: error {self.response.status_code} - {self.message}"
        return f"HTTPException: error {self.response.status_code}"


class NotFoundException(Exception):
    """NotFoundException for DSTN

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, *args):
        """Initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(*args)

        self.message = args[0] if args else None

    def __str__(self):
        """__str__ method

        Returns:
            _str_: _default string_

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        if self.message:
            return f"NotFoundException: {self.message}"
        return f"NotFoundException: default message"
