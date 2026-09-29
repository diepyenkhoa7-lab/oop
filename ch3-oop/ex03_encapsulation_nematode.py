"""Bài 3.3: Encapsulation và validation cho C. elegans."""


class Nematode:
    """Mô hình một cá thể giun tròn với trạng thái private có kiểm tra."""

    VALID_GENDERS = {"hermaphrodite", "male"}

    def __init__(self, body_length: float, gender: str, age: int) -> None:
        self.__validate_body_length(body_length)
        if not isinstance(gender, str):
            raise ValueError(
                "Giới tính không hợp lệ (chỉ chấp nhận 'hermaphrodite' hoặc 'male')!"
            )
        normalized_gender = gender.lower()
        if normalized_gender not in self.VALID_GENDERS:
            raise ValueError(
                "Giới tính không hợp lệ (chỉ chấp nhận 'hermaphrodite' hoặc 'male')!"
            )
        self.__validate_age(age)
        self.__body_length = body_length
        self.__gender = normalized_gender
        self.__age = age

    @staticmethod
    def __validate_body_length(length: float) -> None:
        if not isinstance(length, (int, float)) or isinstance(length, bool) or length <= 0:
            raise ValueError("Chiều dài cơ thể phải là số thực dương!")

    @staticmethod
    def __validate_age(age: int) -> None:
        if not isinstance(age, int) or isinstance(age, bool) or age < 0:
            raise ValueError("Tuổi cá thể phải là số nguyên không âm!")

    def get_body_length(self) -> float:
        return self.__body_length

    def get_gender(self) -> str:
        return self.__gender

    def get_age(self) -> int:
        return self.__age

    def set_body_length(self, new_length: float) -> None:
        self.__validate_body_length(new_length)
        self.__body_length = new_length

    def set_age(self, new_age: int) -> None:
        self.__validate_age(new_age)
        if new_age < self.__age:
            raise ValueError("Tuổi mới không thể nhỏ hơn tuổi hiện tại!")
        self.__age = new_age

    def grow(self, days: int, length_growth: float) -> None:
        self.__validate_age(days)
        if not isinstance(length_growth, (int, float)) or isinstance(length_growth, bool):
            raise ValueError("Mức tăng chiều dài phải là số không âm!")
        if length_growth < 0:
            raise ValueError("Mức tăng chiều dài phải là số không âm!")
        self.set_age(self.__age + days)
        self.set_body_length(self.__body_length + length_growth)

    def __str__(self) -> str:
        return (
            f"Nematode(Length: {self.__body_length}mm, Gender: {self.__gender}, "
            f"Age: {self.__age} days)"
        )

    def __repr__(self) -> str:
        return f"Nematode({self.__body_length!r}, {self.__gender!r}, {self.__age})"


def main() -> None:
    n1 = Nematode(1.05, "hermaphrodite", 3)
    print(n1)
    try:
        print(n1.__body_length)
    except AttributeError as error:
        print(f"Private attribute access: {error}")
    print(f"Name-mangled value: {n1._Nematode__body_length}")
    n1.grow(2, 0.15)
    print(n1)
    print(repr(n1))


if __name__ == "__main__":
    main()
