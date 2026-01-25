class Plant:
    """A class representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height if height >= 0 else 0
        self.age = age if age >= 0 else 0

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_height(self):
        return self.height

    def set_height(self, value):
        self.height = value

    def get_age(self):
        return self.age

    def set_age(self, value):
        self.age = value

    def grow(self, cm: int) -> None:
        """Simulate the growth of the plant over a number of days."""
        if cm > 0:
            self.height += cm

    def age_one_day(self) -> None:
        """Simulate the aging of the plant by one day."""
        self.age += 1

    def get_info(self) -> str:
        """Return a string representation of the plant's information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


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
