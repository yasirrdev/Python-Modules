class Plant:
    """A class representing a managed plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def height(self) -> int:
        return self._height

    @property
    def age(self) -> int:
        return self._age

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @height.setter
    def height(self, value: int) -> None:
        if value >= 0:
            self._height = value

    @age.setter
    def age(self, value: int) -> None:
        if value >= 0:
            self._age = value

    def grow(self, cm: int) -> None:
        if cm > 0:
            self._height += cm

    def age_one_day(self) -> None:
        self._age += 1

    def get_info(self) -> str:
        return f"{self._name}: {self._height}cm, {self._age} days old"


class Flower(Plant):
    """A class representing a flower in the garden."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color

    @property
    def color(self):
        return self._color

    def bloom(self) -> str:
        return f"The {self.color} {self.name} is blooming!"


class Tree(Plant):
    """A class representing a tree in the garden."""

    def __init__(
        self, name: str, height: int, age: int, trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    @property
    def trunk_diameter(self):
        return self._trunk_diameter

    def produce_shade(self) -> str:
        return (
            f"The {self.name} tree is providing shade with a trunk "
            f"diameter of {self.trunk_diameter}cm."
        )


class Vegetable(Plant):
    """A class representing a vegetable in the garden."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    @property
    def harvest_season(self):
        return self._harvest_season

    @property
    def nutritional_value(self):
        return self._nutritional_value


if __name__ == "__main__":
    flower1 = Flower("Rose", 30, 20, "Red")
    flower2 = Flower("Tulip", 25, 15, "Yellow")

    tree1 = Tree("Oak", 300, 365, 80)
    tree2 = Tree("Pine", 250, 300, 60)

    veg1 = Vegetable("Carrot", 20, 40, "Spring", "High in Vitamin A")
    veg2 = Vegetable("Tomato", 35, 50, "Summer", "Rich in antioxidants")

    plants = [flower1, flower2, tree1, tree2, veg1, veg2]

    print("=== Garden Plants ===")
    for plant in plants:
        plant.age_one_day()
        plant.grow(5)
    for plant in plants:
        print(plant.get_info())

    print("\n=== Special Actions ===")
    print(flower1.bloom())
    print(tree1.produce_shade())
    print(
        f"{veg1.name} is harvested in {veg1.harvest_season} and is "
        f"{veg1.nutritional_value}."
    )
