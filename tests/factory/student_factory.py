"""A Factory to generate Student instance.

Author(s):
    - Xuong L. Tran <xuong@trhgquan.xyz>
"""

import datetime
import string
import random
from typing import Dict, Optional
from faker import Faker
from .type.student_type import ProgramType, GraduationType, MajorType


class StudentFactory:
    """Factory to generate student for a test.

    Author(s):
        - Xuong L. Tran <xuong@trhgquan.xyz>
    """

    # Faker instance to generate fake data
    fake: Faker

    # Available programs
    program_type: Dict[str, ProgramType]

    # Available majors
    major: Dict[str, MajorType]

    # Available graduation type
    graduation_type: Dict[str, GraduationType]

    def __init__(self):
        """Intialize the class.

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        # Create a new Faker instance
        self.fake = Faker()

        # Available program types of a student.
        self.program_type = {
            "CQ": ProgramType(name_vn="Chính quy", name_en="Full-time", code=0),
            "CLC": ProgramType(name_vn="Chất lượng cao", name_en="High-quality", code=7),
            "TT": ProgramType(name_vn="Tiên tiến", name_en="Advanced Program", code=5),
            "VP": ProgramType(name_vn="Việt Pháp", name_en="Vietnamese-France", code=6)
        }

        # Available majors of a student.
        self.major = {
            "CNTT": MajorType(name_vn="Công nghệ thông tin", name_en="Information Technology"),
            "HTTT": MajorType(name_vn="Hệ thống thông tin", name_en="Information Systems"),
            "KHMT": MajorType(name_vn="Khoa học máy tính", name_en="Computer Science"),
            "CNPM": MajorType(name_vn="Công nghệ phần mềm", name_en="Software Engineering"),
        }

        # Available graduation type of a student.
        self.graduation_type = {
            "XS": GraduationType(name_vn="Xuất sắc", name_en="Excellent"),
            "G": GraduationType(name_vn="Giỏi", name_en="Very good"),
            "KH": GraduationType(name_vn="Khá", name_en="Good"),
            "TBK": GraduationType(name_vn="Trung bình khá", name_en="Average good"),
            "TB": GraduationType(name_vn="Trung bình", name_en="Average")
        }

    def get_mssv(self, class_of: int, program: Optional[str] = "CQ") -> str:
        """Create Student ID from a class (of year) and program.

        The format should be
            `[CLASS - 2 digits]12[PROGRAM - 1 digit][RANDOM - 3 digits]`

        Args:
            class_of (int): the class (year) that student is in (enrolled)
            program (str, optional): The program of that student. Defaults to "CQ".

        Returns:
            str: a student's ID

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        prefix = class_of % 100
        program_code = self.program_type[program].get_code()
        generated = random.randint(0, 999)

        return f"{prefix}12{program_code}{generated}"

    @staticmethod
    def generate_sovaoso() -> str:
        """Generate Record ID of a student (in the graduation records)

        Returns:
            str: generated Record ID

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        text_str = "".join(random.choices(string.ascii_uppercase, k=4))
        num_str = random.randint(0000, 9999)

        return f"{text_str}/{num_str}"

    @staticmethod
    def generate_sobang() -> str:
        """Generate degree ID of a student.

        This function would return the Degree ID in the following format
            `SOBANG/12345678`

        Returns:
            str: generated Degree ID

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        random_id = "".join(random.choices(string.digits, k=8))

        return f"SOBANG/{random_id}"

    def create_student(self) -> Dict[str, str]:
        """Generate a fake student.
        Note that the return is a dict - which is automatically parse from response.json.

        Returns:
            Dict[str, str]: a student's full information

        Author(s):
            - Xuong L. Tran <xuong@trhgquan.xyz>
        """

        # Generate fake infos
        hoten = self.fake.name()
        ngaysinh = self.fake.date_of_birth(minimum_age=22, maximum_age=35)
        mahe = random.choice(list(self.program_type.keys()))
        manganh = random.choice(list(self.major.keys()))
        khoa = ngaysinh + datetime.timedelta(days=365 * 18)
        loaitn = random.choice(list(self.graduation_type.keys()))
        ngaytotnghiep = khoa + datetime.timedelta(days=365 * 4)

        # Wrapping informations into a dict.
        student = {
            "masv": self.get_mssv(khoa.year, mahe),
            "ngaysinh": ngaysinh.strftime("%d/%m/%Y"),
            "hoten": hoten,
            "hotenAnh": hoten,
            "Bac": "DH",
            "tenbac": "Đại học",
            "tenbacAnh": "Bachelor of Science",
            "mahe": mahe,
            "tenhe": self.program_type[mahe].get_name_vn(),
            "tenheAnh": self.program_type[mahe].get_name_en(),
            "dotnam": str(ngaytotnghiep.year),
            "tennganh": self.major[manganh].get_name_vn(),
            "tennganhAnh": self.major[manganh].get_name_en(),
            "loaitotnghiep": self.graduation_type[loaitn].get_name_vn(),
            "loaitotnghiepAnh": self.graduation_type[loaitn].get_name_en(),
            "sobang": StudentFactory.generate_sobang(),
            "sovaoso": StudentFactory.generate_sovaoso(),
            "ngayqd": ngaytotnghiep.strftime('%d/%m/%Y'),
        }

        return student
