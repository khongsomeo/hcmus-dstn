"""DSTN Classes

Author(s):
    - Quan H. Tran <quan@trhgquan.xyz>
    - Xuong L. Tran <xuong@trhgquan.xyz>
    - Me A. Doge <domyeukemphancam@trhgquan.xyz>
"""

from abc import abstractmethod
from .exception import NotFoundException, HTTPException
import requests as rq
import termtables as tt

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

        self.__json = kwargs.get("json", None)
        self.__language = kwargs.get("language", "vn")

        if self.__json is not None:
            self.parse()

    def parse(self):
        """Parsing a JSON result to class property.

        Author(s):
            - Quan H. Tran <quan@trhgquan.xyz>
            - Me A. Doge <domyeukemphancam@trhgquan.xyz>
        """

        self.__masv = self.__json["masv"]
        self.__ngaysinh = self.__json["ngaysinh"]
        self.__hoten = self.__json["hoten"]
        self.__hoten_anh = self.__json["hotenAnh"]
        self.__bac = self.__json["Bac"]
        self.__mahe = self.__json["mahe"]
        self.__dotnam = self.__json["dotnam"]
        self.__loaitotnghiep = self.__json["loaitotnghiep"]
        self.__loaitotnghiep_anh = self.__json["loaitotnghiepAnh"]
        self.__sobang = self.__json["sobang"]
        self.__sovaoso = self.__json["sovaoso"]
        self.__ngayqd = self.__json["ngayqd"]
        self.__tenbac = self.__json["tenbac"]
        self.__tenbac_anh = self.__json["tenbacAnh"]
        self.__tenhe = self.__json["tenhe"]
        self.__tenhe_anh = self.__json["tenheAnh"]
        self.__tennganh = self.__json["tennganh"]
        self.__tennganh_anh = self.__json["tennganhAnh"]

    def get_string(self):
        """Parsing class property to formatted (tabular) UI

        Returns:
            _str_: _the tabular string_

        Author(s):
            - Quan H. Tran <quan@trhgquan.xyz>
        """

        dstn_string = []
        if self.__language == "vn":
            dstn_string.append(["Mã sinh viên",  self.__masv])
            dstn_string.append(["Ngày sinh", self.__ngaysinh])
            dstn_string.append(["Họ và tên", self.__hoten])
            dstn_string.append(["Bậc", self.__bac])
            dstn_string.append(["Tên bậc", self.__tenbac])
            dstn_string.append(["Mã hệ", self.__mahe])
            dstn_string.append(["Tên hệ", self.__tenhe])
            dstn_string.append(["Đợt năm", self.__dotnam])
            dstn_string.append(["Tên ngành", self.__tennganh])
            dstn_string.append(["Loại tốt nghiệp", self.__loaitotnghiep])
            dstn_string.append(["Số bằng", self.__sobang])
            dstn_string.append(["Số vào sổ", self.__sovaoso])
            dstn_string.append(["Ngày quyết định", self.__ngayqd])

        elif self.__language == "en":
            dstn_string.append(["Student ID", self.__masv])
            dstn_string.append(["Birthday", self.__ngaysinh])
            dstn_string.append(["Name", self.__hoten_anh])
            dstn_string.append(["Type", self.__bac])
            dstn_string.append(["Type name", self.__tenbac_anh])
            dstn_string.append(["Type code", self.__mahe])
            dstn_string.append(["Type code name", self.__tenhe_anh])
            dstn_string.append(["Year", self.__dotnam])
            dstn_string.append(["Major name", self.__tennganh_anh])
            dstn_string.append(["Graduation rank", self.__loaitotnghiep_anh])
            dstn_string.append(["Degree ID", self.__sobang])
            dstn_string.append(["Degree in book ID", self.__sovaoso])
            dstn_string.append(["Issue date", self.__ngayqd])

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
        pass


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
        except NotFoundException as e:
            print(e)

        # Error while playing with HTTP
        except HTTPException as e:
            print(e)

            response = e.response

            with open(SINGLE_LOG, "w+") as f:
                print(response.content, file=f)

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
            except NotFoundException as e:
                print(f"{name} - Status: INVALID")

            # Error while playing with HTTP
            except HTTPException as e:
                print(e)

                response = e.response

                with open(MULTIPLE_LOG, "w+") as f:
                    print(response.content, file=f)

            else:
                print(f"{name} - Status: VALID")
