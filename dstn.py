import requests as rq
import termtables as tt


class DSTNItem:
    def __init__(self, **kwargs):
        self.__json = kwargs.get("json", None)
        self.__language = kwargs.get("language", "vn")

        if self.__json is not None:
            self.parse()

    def parse(self):
        self.__masv = self.__json["masv"]
        self.__ngaysinh = self.__json["ngaysinh"]
        self.__hoten = self.__json["hoten"]
        self.__hotenAnh = self.__json["hotenAnh"]
        self.__Bac = self.__json["Bac"]
        self.__mahe = self.__json["mahe"]
        self.__dotnam = self.__json["dotnam"]
        self.__loaitotnghiep = self.__json["loaitotnghiep"]
        self.__loaitotnghiepAnh = self.__json["loaitotnghiepAnh"]
        self.__sobang = self.__json["sobang"]
        self.__sovaoso = self.__json["sovaoso"]
        self.__ngayqd = self.__json["ngayqd"]
        self.__tenbac = self.__json["tenbac"]
        self.__tenbacAnh = self.__json["tenbacAnh"]
        self.__tenhe = self.__json["tenhe"]
        self.__tenheAnh = self.__json["tenheAnh"]
        self.__tennganh = self.__json["tennganh"]
        self.__tennganhAnh = self.__json["tennganhAnh"]

    def get_string(self):
        dstn_string = []
        if self.__language == "vn":
            dstn_string.append(["Mã sinh viên",  self.__masv])
            dstn_string.append(["Ngày sinh", self.__ngaysinh])
            dstn_string.append(["Họ và tên", self.__hoten])
            dstn_string.append(["Bậc", self.__Bac])
            dstn_string.append(["Tên bậc", self.__tenbac])
            dstn_string.append(["Mã hệ", self.__mahe])
            dstn_string.append(["Tên hệ", self.__tenhe])
            dstn_string.append(["Đợt năm", self.__dotnam])
            dstn_string.append(["Tên ngành", self.__tennganh])
            dstn_string.append(["Loại tốt nghiệp", self.__loaitotnghiep])
            dstn_string.append(["Số bằng", self.__sobang])
            dstn_string.append(["Số vào sổ", self.__sovaoso])
            dstn_string.append(["Ngày quyết định", self.__ngayqd])

        if self.__language == "en":
            dstn_string.append(["Student ID", self.__masv])
            dstn_string.append(["Birthday", self.__ngaysinh])
            dstn_string.append(["Name", self.__hotenAnh])
            dstn_string.append(["Type", self.__Bac])
            dstn_string.append(["Type name", self.__tenbacAnh])
            dstn_string.append(["Type code", self.__mahe])
            dstn_string.append(["Type code name", self.__tenheAnh])
            dstn_string.append(["Year", self.__dotnam])
            dstn_string.append(["Major name", self.__tennganhAnh])
            dstn_string.append(["Graduation rank", self.__loaitotnghiepAnh])
            dstn_string.append(["Degree ID", self.__sobang])
            dstn_string.append(["Degree in book ID", self.__sovaoso])
            dstn_string.append(["Issue date", self.__ngayqd])

        return tt.to_string(dstn_string, style=tt.styles.ascii_thin_double)

    def __str__(self):
        return self.get_string()


class DSTNRequest:
    def __init__(self, **kwargs):
        self.__base_url = kwargs.get("base_url", None)
        self.__rows = kwargs.get("rows", 10),
        self.__page = kwargs.get("page", 1),
        self.__sord = kwargs.get("sord", "desc"),
        self.__student_id = kwargs.get("student_id", None)
        self.__birthday = kwargs.get("birthday", None)
        self.__language = kwargs.get("language", None)

        self.__params = {
            "masv": self.__student_id,
            "ngaysinh": self.__birthday,
            "rows": self.__rows,
            "page": self.__page,
            "sord": self.__sord
        }

    def get(self):
        response = rq.get(
            url=self.__base_url,
            params=self.__params
        )

        if response.status_code != 200:
            with open("error.html", "w+") as f:
                print(response.content, file=f)
                print(
                    f"Error code: {response.status_code}, logged to error.html")
        else:
            response_json = response.json()

            if response_json["total"] == 0:
                print("No records found. Please check informations again.")
            else:
                record_list = [
                    DSTNItem(
                        json=record, language=self.__language)
                    for record in response_json["rows"]]

                for record in record_list:
                    print(record)
