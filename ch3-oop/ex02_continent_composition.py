"""Bài 3.2: Composition giữa Continent và Country."""

from ex01_country_class import Country


class Continent:
    """Một châu lục chứa danh sách các quốc gia."""

    total_continents = 0

    def __init__(self, name: str, countries: list[Country] | None = None) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Tên châu lục phải là chuỗi không rỗng!")
        self.name = name
        self.countries: list[Country] = []
        if countries is not None:
            for country in countries:
                self.add_country(country)
        Continent.total_continents += 1

    def add_country(self, country: Country) -> None:
        if not isinstance(country, Country):
            raise TypeError("Phải thêm một đối tượng thuộc lớp Country!")
        self.countries.append(country)

    def total_population(self) -> int:
        return sum(country.population for country in self.countries)

    def total_area(self) -> float:
        return sum(country.area for country in self.countries)

    def get_largest_country(self) -> Country | None:
        return max(self.countries, key=lambda country: country.area, default=None)

    def __len__(self) -> int:
        return len(self.countries)

    def __str__(self) -> str:
        return "\n".join([self.name, *(str(country) for country in self.countries)])

    def __repr__(self) -> str:
        return f"Continent({self.name!r}, {self.countries!r})"


def main() -> None:
    canada = Country("Canada", 34482779, 9984670)
    usa = Country("United States of America", 313914040, 9826675)
    mexico = Country("Mexico", 112336538, 1943950)
    vietnam = Country("Vietnam", 98000000, 331212)

    north_america = Continent("North America", [canada, usa, mexico])
    asia = Continent("Asia")
    asia.add_country(vietnam)

    print(f"Total continents: {Continent.total_continents}")
    print(f"North America population: {north_america.total_population()}")
    print(f"North America area: {north_america.total_area()}")
    print(f"Largest country: {north_america.get_largest_country()}")
    print(f"Countries in Asia: {len(asia)}")
    print(north_america)


if __name__ == "__main__":
    main()
