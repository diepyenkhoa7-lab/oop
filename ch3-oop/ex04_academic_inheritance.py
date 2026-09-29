"""Bài 3.4: Kế thừa, overriding và polymorphism trong trường đại học."""


class Member:
    """Thông tin nền tảng dùng chung cho thành viên trường."""

    def __init__(self, member_id: str, name: str, email: str) -> None:
        self.member_id = member_id
        self.name = name
        self.email = email

    def get_role(self) -> str:
        return "Thành viên chung"

    def get_details(self) -> str:
        return f"Mã: {self.member_id} | Họ tên: {self.name} | Email: {self.email}"

    def __str__(self) -> str:
        return self.get_details()

    def __repr__(self) -> str:
        return f"Member({self.member_id!r}, {self.name!r}, {self.email!r})"


class Student(Member):
    """Thành viên là sinh viên."""

    def __init__(
        self, member_id: str, name: str, email: str, major: str, gpa: float = 0.0
    ) -> None:
        super().__init__(member_id, name, email)
        self.major = major
        self.gpa = float(gpa)
        self.courses_taken: list[str] = []
        self.current_courses: list[str] = []

    def enroll_course(self, course_name: str) -> None:
        self.current_courses.append(course_name)

    def complete_course(self, course_name: str) -> None:
        if course_name in self.current_courses:
            self.current_courses.remove(course_name)
            self.courses_taken.append(course_name)

    def get_role(self) -> str:
        return "Sinh viên Đại học"

    def get_details(self) -> str:
        base_info = super().get_details()
        return (
            f"{base_info} | Ngành: {self.major} | GPA: {self.gpa} "
            f"| Đang học: {len(self.current_courses)} môn"
        )

    def __repr__(self) -> str:
        return (
            f"Student({self.member_id!r}, {self.name!r}, {self.email!r}, "
            f"{self.major!r}, {self.gpa!r})"
        )


class Faculty(Member):
    """Thành viên là giảng viên."""

    def __init__(
        self,
        member_id: str,
        name: str,
        email: str,
        department: str,
        academic_rank: str,
    ) -> None:
        super().__init__(member_id, name, email)
        self.department = department
        self.academic_rank = academic_rank
        self.teaching_courses: list[str] = []

    def assign_course(self, course_name: str) -> None:
        self.teaching_courses.append(course_name)

    def get_role(self) -> str:
        return "Giảng viên Khoa"

    def get_details(self) -> str:
        base_info = super().get_details()
        courses = ", ".join(self.teaching_courses) or "Chưa phân công"
        return (
            f"{base_info} | Học vị: {self.academic_rank} | Khoa: {self.department} "
            f"| Môn giảng dạy: {courses}"
        )

    def __repr__(self) -> str:
        return (
            f"Faculty({self.member_id!r}, {self.name!r}, {self.email!r}, "
            f"{self.department!r}, {self.academic_rank!r})"
        )


def main() -> None:
    s1 = Student("SV01", "Nguyen Van An", "an.nv@gdu.edu.vn", "Kỹ thuật phần mềm", 3.65)
    f1 = Faculty(
        "GV01", "TS. Tran Minh Quang", "quang.tm@gdu.edu.vn", "Khoa CNTT", "Tiến sĩ"
    )
    m1 = Member("MB01", "Le Thi Hoa", "hoa.lt@gdu.edu.vn")

    s1.enroll_course("Lập trình Python")
    s1.enroll_course("Cơ sở dữ liệu")
    s1.complete_course("Cơ sở dữ liệu")
    f1.assign_course("Lập trình Python")

    university_members = [s1, f1, m1]
    for member in university_members:
        print(f"{member.get_role()}: {member.get_details()}")

    print(f"isinstance(s1, Member): {isinstance(s1, Member)}")
    print(f"issubclass(Student, Member): {issubclass(Student, Member)}")
    print(f"Student MRO: {[cls.__name__ for cls in Student.mro()]}")


if __name__ == "__main__":
    main()
