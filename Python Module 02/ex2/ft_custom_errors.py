class GardenError(Exception):
    """Base class for exceptions in the garden module."""
    pass


class PlantError(GardenError):
    """Exception raised for errors related to plants."""
    pass


class WaterError(GardenError):
    """Exception raised for errors related to watering."""
    pass


def check_plant():
    raise PlantError("The tomato plant is wilting!")


def check_watering():
    raise WaterError("Not enough water in the tank!")


def test_custom_errors():
    """"Test custom garden error classes."""
    print("=== Custom Garden Errors Demo ===")

    print("Testing PlantError...")

    try:
        check_plant()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("Testing WaterError...")

    try:
        check_watering()
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("Testing all garden errors...")
    for test in [check_plant, check_watering]:
        try:
            test()
        except GardenError as e:
            print(f"Caught GardenError: {e}")

    print("All custom error types work correctly!")
