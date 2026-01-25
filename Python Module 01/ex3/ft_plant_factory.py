class Plant:
    """A class representing a plant in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return a string representation of the plant's information."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


if __name__ == "__main__":

    plant_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    ]

    plants = []

    for name, height, age in plant_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        # Append sirve para meter la planta en la lista
        print(f"Created: {plant.get_info()}")

    print(f"\nTotal plants created: {len(plants)}")
