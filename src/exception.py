"""Exceptions for DSTN

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

from typing import Optional, Any


class HTTPException(Exception):
    """HttpException for DSTN

    For errors related to HTTP Requests.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Extra message to return in exception
    message: str

    # Response from the request
    response: Any

    def __init__(self, message: Optional[str] = None, **kwargs):
        """Initialization

        Args:
            message (str): message to inform user.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(self, message)

        self.message = message
        self.response = kwargs.get("response", None)

    def __str__(self) -> str:
        """__str__ method

        Returns:
            str: _default string_

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        if self.message:
            return f"HTTPException: error {self.response.status_code} - {self.message}"
        return f"HTTPException: error {self.response.status_code}"


class NotFoundException(Exception):
    """NotFoundException for DSTN

    For errors related to invalid informations.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Extra message to return in exception
    message: str

    def __init__(self, *args) -> None:
        """Initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(*args)

        self.message = args[0] if args else None

    def __str__(self) -> str:
        """__str__ method

        Returns:
            str: _default string_

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        if self.message:
            return f"NotFoundException: {self.message}"
        return "NotFoundException: default message"
