class Plant:
    """A class representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_height(self):
        return self._height

    def set_height(self, value):
        self._height = value if value >= 0 else 0

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value if value >= 0 else 0

    def grow(self, cm: int) -> None:
        """Simulate the growth of the plant over a number of days."""
        if cm > 0:
            self._height += cm

    def age_one_day(self) -> None:
        """Simulate the aging of the plant by one day."""
        self._age += 1

    def get_info(self) -> str:
        """Return a string representation of the plant's information."""
        return f"{self.name}: {self._height}cm, {self._age} days old"


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30)

    print(plant1.get_info())

    plant1.grow(-5)
    plant1._height = -10
    plant1._age = -3

    print(plant1.get_info())

    for _ in range(5):
        plant1.grow(3)
        plant1.age_one_day()

    print("\nAfter 5 days of growth:")
    print(plant1.get_info())
