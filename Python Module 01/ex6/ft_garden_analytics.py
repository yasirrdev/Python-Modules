class Plant:
    """A class representing a managed plant in the garden."""
    def __init__(self, name: str, height: int, age: int) -> None:
        self._name = name
        self._height = height if height >= 0 else 0
        self._age = age if age >= 0 else 0


class FloweringPlant(Plant):
    """A class representing a flowering plant in the garden."""
    def __init__(self, name: str, height: int, age: int,
                 flower_color: str) -> None:
        super().__init__(name, height, age)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    """A class representing a prize-winning flower in the garden."""
    def __init__(self, name: str, height: int, age: int,
                 flower_color: str, prize_level: str) -> None:
        super().__init__(name, height, age, flower_color)
        self.prize_level = prize_level


class Garden:
    def __init__(self, name: str) -> None:
        self.name = name
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        self.plants.append(plant)


class GardenManager:
    def __init__(self) -> None:
        self.gardens = []
        self.stats = self.GardenStats()

    def add_garden(self, garden: Garden) -> None:
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        manager = cls()
        garden1 = Garden("Rose Garden")
        garden2 = Garden("Tropical Garden")

        garden1.add_plant(PrizeFlower("Rose", 30, 60, "Red", "Gold"))
        garden1.add_plant(FloweringPlant("Tulip", 20, 45, "Yellow"))

        garden2.add_plant(FloweringPlant("Orchid", 25, 50, "Purple"))
        garden2.add_plant(PrizeFlower("Hibiscus", 40, 70, "Pink", "Silver"))

        manager.add_garden(garden1)
        manager.add_garden(garden2)
        return manager

    @staticmethod
    def format_height(height: int) -> str:
        """Format height in cm to a string with 'cm' suffix."""
        return f"{height} cm"

    class GardenStats:
        """A class to compute statistics about the gardens."""
    def average_height(self, plants: list) -> float:
        """Calculate the average height of the given plants."""
        if not plants:
            return 0.0
        return sum(plant._height for plant in plants) / len(plants)

    def count_plants(self, plants: list) -> int:
        """Count the number of plants in the given list."""
        return len(plants)

