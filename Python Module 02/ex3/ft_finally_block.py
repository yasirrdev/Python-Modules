def water_plants(plant_list: list[str]) -> None:
    """"Water a list of plants, ensuring cleanup with a finally block."""
    print("Opening watering system...")
    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}...")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """"Test the watering system with a list of plants."""
    print("=== Garden Watering System ===")

    plants = ["Rose", "Tulip", None, "Daisy"]
    water_plants(plants)

    print("Watering system test completed!")
