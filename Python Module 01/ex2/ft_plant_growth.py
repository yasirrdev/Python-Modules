class Plant:
    """A class representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.weekly_growth = 0

    def get_info(self) -> str:
        """Return a string representation of the plant's information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, cm: int) -> None:
        """Simulate the growth of the plant over a number of days."""
        self.height += cm
        self.weekly_growth += cm

    def age_one_day(self) -> None:
        """Simulate the aging of the plant by one day."""
        self.age += 1

    def reset_weekly_growth(self) -> None:
        """Reset the weekly growth counter."""
        self.weekly_growth = 0

    def get_weekly_growth(self) -> int:
        """Return the total growth over the week."""
        return self.weekly_growth


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)

    plants = [plant1, plant2, plant3]

    print("=== Day 1 ===")
    for plant in plants:
        print(plant.get_info())

    for _ in range(6):
        for plant in plants:
            plant.grow(2)
            plant.age_one_day()

    print("\n=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        print(f"Growth this week: +{plant.get_weekly_growth()}cm\n")
        plant.reset_weekly_growth()
