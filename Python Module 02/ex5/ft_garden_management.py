class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}

    def add_plant(self, name, water_level, sunlight_hours):
        if not name:
            raise PlantError("Plant name cannot be empty.")
        plant = {
            "name": name,
            "water_level": water_level,
            "sunlight_hours": sunlight_hours
        }
        self.plants[name] = plant
        print(f"Added plant: {name}")

    def water_plants(self):
        print("Opening watering system")
        try:
            if not self.plants:
                raise WaterError("No plants to water.")
            for plant in self.plants.values():
                print(f"Watering plant: {plant['name']}")
        finally:
            print("Closing watering system")

    def check_plant_health(self, name):
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in the garden.")

        water = self.plants[name]['water_level']
        sunlight = self.plants[name]['sunlight_hours']

        if water < 1 or water > 10:
            raise PlantError(f"'{name}' has invalid water level:{water}")
        if sunlight < 2 or sunlight > 12:
            raise PlantError(f"'{name}' has invalid sunlight hours:{sunlight}")

        print(f"Plant '{name}' is healthy!")


def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
        manager.add_plant("lettuce", 15, 6)
        manager.add_plant("", 4, 5)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    try:
        manager.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("Checking plant health...")
    try:
        manager.check_plant_health("tomato")
        manager.check_plant_health("lettuce")
    except PlantError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")
