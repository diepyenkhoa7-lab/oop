"""Bài 3.1: Mô hình quốc gia bằng lớp Country."""


class Country:
    """Lưu thông tin và cung cấp phép tính cơ bản cho một quốc gia."""

    def __init__(self, name: str, population: int, area: float) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên quốc gia phải là chuỗi không rỗng!")
        if not isinstance(population, int) or population < 0:
            raise ValueError("Dân số phải là số nguyên không âm!")
        if not isinstance(area, (int, float)) or isinstance(area, bool) or area <= 0:
            raise ValueError("Diện tích phải là số dương!")
        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other: "Country") -> bool:
        if not isinstance(other, Country):
            raise TypeError("Đối tượng so sánh phải thuộc lớp Country!")
        return self.area > other.area

    def population_density(self) -> float:
        return self.population / self.area

    def __str__(self) -> str:
        return (
            f"{self.name} has a population of {self.population} "
            f"and is {self.area} square km."
        )

    def __repr__(self) -> str:
        return f"Country({self.name!r}, {self.population}, {self.area!r})"


def main() -> None:
    canada = Country("Canada", 34482779, 9984670)
    usa = Country("United States of America", 313914040, 9826675)
    vietnam = Country("Vietnam", 98000000, 331212)

    print(canada)
    print(usa)
    print(f"Canada density: {canada.population_density():.2f} people/km2")
    print(f"Vietnam density: {vietnam.population_density():.2f} people/km2")
    print(f"Canada larger than USA: {canada.is_larger(usa)}")
    print(f"Vietnam larger than Canada: {vietnam.is_larger(canada)}")
    countries = [canada, usa, vietnam]
    print(countries)  # List dùng repr() cho từng phần tử.


if __name__ == "__main__":
    main()
