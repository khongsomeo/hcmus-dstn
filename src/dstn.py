"""DSTN Classes

Author(s):
    - Quan H. Tran <quan@trhgquan.xyz>
    - Xuong L. Tran <xuong@trhgquan.xyz>
    - Me A. Doge <domyeukemphancam@trhgquan.xyz>
"""

from abc import abstractmethod
import requests as rq
import termtables as tt
from .exception import NotFoundException, HTTPException

# Position to save logs
SINGLE_LOG = "error_single.html"
MULTIPLE_LOG = "error_multiple.html"


class DSTNItem:
    """Parse a JSON DSTN to beautified - table format.

    Author
        - Quan H. Tran <quan@trhgquan.xyz>
        - Xuong L. Tran <xuong@trhgquan.xyz>
        - Me A. Doge <domyeukemphancam@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialization

        Author(s):
            - Quan H. Tran <quan@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        self.info = {
            "language": kwargs.get("language", "vn")
        }

        json_data = kwargs.get("json", None)

        if json_data is not None:
            for key, value in json_data.items():
                self.info[key] = value

    def get_string(self):
        """Parsing class property to formatted (tabular) UI

        Returns:
            _str_: _the tabular string_

        Author(s):
            - Quan H. Tran <quan@trhgquan.xyz>
        """

        dstn_string = []
        if self.info["language"] == "vn":
            dstn_string.append(["Mã sinh viên",  self.info["masv"]])
            dstn_string.append(["Ngày sinh", self.info["ngaysinh"]])
            dstn_string.append(["Họ và tên", self.info["hoten"]])
            dstn_string.append(["Bậc", self.info["Bac"]])
            dstn_string.append(["Tên bậc", self.info["tenbac"]])
            dstn_string.append(["Mã hệ", self.info["mahe"]])
            dstn_string.append(["Tên hệ", self.info["tenhe"]])
            dstn_string.append(["Đợt năm", self.info["dotnam"]])
            dstn_string.append(["Tên ngành", self.info["tennganh"]])
            dstn_string.append(["Loại tốt nghiệp", self.info["loaitotnghiep"]])
            dstn_string.append(["Số bằng", self.info["sobang"]])
            dstn_string.append(["Số vào sổ", self.info["sovaoso"]])
            dstn_string.append(["Ngày quyết định", self.info["ngayqd"]])

        elif self.info["language"] == "en":
            dstn_string.append(["Student ID", self.info["masv"]])
            dstn_string.append(["Birthday", self.info["ngaysinh"]])
            dstn_string.append(["Name", self.info["hotenAnh"]])
            dstn_string.append(["Type", self.info["Bac"]])
            dstn_string.append(["Type name", self.info["tenbacAnh"]])
            dstn_string.append(["Type code", self.info["mahe"]])
            dstn_string.append(["Type code name", self.info["tenheAnh"]])
            dstn_string.append(["Year", self.info["dotnam"]])
            dstn_string.append(["Major name", self.info["tennganhAnh"]])
            dstn_string.append(
                ["Graduation rank", self.info["loaitotnghiepAnh"]])
            dstn_string.append(["Degree ID", self.info["sobang"]])
            dstn_string.append(["Degree in book ID", self.info["sovaoso"]])
            dstn_string.append(["Issue date", self.info["ngayqd"]])

        return tt.to_string(dstn_string, style=tt.styles.ascii_thin_double)

    def __str__(self):
        return self.get_string()


class DSTNRequest:
    """Abstract request class

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
        - Me A. Doge <domyeukemphancam@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialize

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        # Base API URL
        self.api_url = kwargs.get("api_url", None)

        # Result parameters
        self.results = kwargs.get("results", None)

        # Headers for the request.
        self.headers = kwargs.get("headers", None)

        # Query parameter
        self.params = {
            "rows": self.results["rows"],
            "page": self.results["page"],
            "sord": self.results["sord"],
        }

    def get(self):
        """Sending a GET request

        Returns:
            Response: response data.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        response = rq.get(
            url=self.api_url,
            params=self.params,
            headers=self.headers,
        )

        # HTTP error (invalid requests, missing parameters, etc.)
        if response.status_code != 200:
            raise HTTPException(response=response)

        response_json = response.json()

        # No result (fake degree, wrong name, etc.)
        if response_json["total"] == 0:
            raise NotFoundException("No results found")

        return response_json

    @abstractmethod
    def process(self):
        """Processing data (abstract method)

        Author:
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """


class DSTNSingleRequest(DSTNRequest):
    """Processing a single user check

    Author(s):
        - Quan H. Tran <quan@trhgquan.xyz>
        - Xuong L. Tran <xuong@trhgquan.xyz>
        - Me A. Doge <domyeukemphancam@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialization

        Author(s):
            - Quan H. Tran <quan@trhgquan.xyz>
            - Xuong L. Tran <xuong@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        super().__init__(**kwargs)

        self.__language = kwargs.get("language", None)

        # Update masv and sobang to parameters
        self.params["masv"] = kwargs.get("student_name", None)
        self.params["sobang"] = kwargs.get("degree_id", None)

    def process(self):
        """Processing to get the result.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        try:
            response_json = self.get()

        # No records found
        except NotFoundException as notfound_error_handler:
            print(notfound_error_handler)

        # Error while playing with HTTP
        except HTTPException as http_error_handler:
            print(http_error_handler)

            response = http_error_handler.response

            with open(SINGLE_LOG, "w+", encoding="utf8") as log_handler:
                print(response.content, file=log_handler)

        else:
            record_list = [
                DSTNItem(
                    json=record, language=self.__language)
                for record in response_json["rows"]]

            for record in record_list:
                print(record)


class DSTNListRequest(DSTNRequest):
    """Processing a list of users

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    def __init__(self, **kwargs):
        """Initialization

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        super().__init__(**kwargs)
        self.__student_list = kwargs.get("student_list", None)

    def process(self):
        """Processing to get the result.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        for name, degree_id in self.__student_list:
            self.params["masv"] = name
            self.params["sobang"] = degree_id

            try:
                _ = self.get()

            # No records found
            except NotFoundException:
                print(f"{name} - Status: INVALID")

            # Error while playing with HTTP
            except HTTPException as http_error_handler:
                print(http_error_handler)

                response = http_error_handler.response

                with open(MULTIPLE_LOG, "w+", encoding="utf8") as multiple_log_handler:
                    print(response.content, file=multiple_log_handler)

            else:
                print(f"{name} - Status: VALID")
