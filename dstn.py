import requests as rq

class DSTNItem:
    def __init__(self, **kwargs):
        self.__json = kwargs.get("json", None)

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
        
    def get_string(self, language="vn"):
        dstn_string = []
        if language == "vn":
            dstn_string.append("==== Tiếng Việt ====\n")
            dstn_string.append(f"Mã sinh viên: {self.__masv}\n")
            dstn_string.append(f"Ngày sinh: {self.__ngaysinh}\n")
            dstn_string.append(f"Họ và tên: {self.__hoten}\n")
            dstn_string.append(f"Bậc: {self.__Bac}\n")
            dstn_string.append(f"Mã hệ: {self.__mahe}\n")
            dstn_string.append(f"Đợt năm: {self.__dotnam}\n")
            dstn_string.append(f"Loại tốt nghiệp: {self.__loaitotnghiep}\n")
            dstn_string.append(f"Số bằng: {self.__sobang}\n")
            dstn_string.append(f"Số vào sổ: {self.__sovaoso}\n")
            dstn_string.append(f"Ngày quyết định: {self.__ngayqd}\n")
            dstn_string.append(f"Tên bậc: {self.__tenbac}\n")
            dstn_string.append(f"Tên hệ: {self.__tenhe}\n")
            dstn_string.append(f"Tên ngành: {self.__tennganh}\n")
        
        if language == "en":
            dstn_string.append("==== English ====\n")
            dstn_string.append(f"Student ID: {self.__masv}\n")
            dstn_string.append(f"Birthday: {self.__ngaysinh}\n")
            dstn_string.append(f"Name: {self.__hoten}\n")
            dstn_string.append(f"Type: {self.__Bac}\n")
            dstn_string.append(f"Type code: {self.__mahe}\n")
            dstn_string.append(f"Year: {self.__dotnam}\n")
            dstn_string.append(f"Graduation rank: {self.__loaitotnghiep}\n")
            dstn_string.append(f"Degree ID: {self.__sobang}\n")
            dstn_string.append(f"Degree in book ID: {self.__sovaoso}\n")
            dstn_string.append(f"Issue date: {self.__ngayqd}\n")
            dstn_string.append(f"Type name: {self.__tenbac}\n")
            dstn_string.append(f"Type code name: {self.__tenhe}\n")
            dstn_string.append(f"Major name: {self.__tennganh}\n")
            
        return "".join(dstn_string)
        
    def __str__(self):
        return "".join([
            self.get_string(language="vn"),
            "\n",
            self.get_string(language="en"),
        ])

class DSTNRequest:
    def __init__(self, **kwargs):
        self.__base_url = kwargs.get("base_url", None)
        self.__rows = kwargs.get("rows", 10),
        self.__page = kwargs.get("page", 1),
        self.__sord = kwargs.get("sord", "desc"),
        self.__student_id = kwargs.get("student_id", None)
        self.__birthday = kwargs.get("birthday", None)
        
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
                print(f"Error code: {response.status_code}, logged to error.html")
        else:
            response_json = response.json()
            
            if response_json["total"] == 0:
                print("No records found. Please check informations again.")
            else:
                record_list = [DSTNItem(json=record) for record in response_json["rows"]]
                
                for record in record_list:
                    print(record)
                
