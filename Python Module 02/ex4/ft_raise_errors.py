def check_plant_health(plant_name, water_level, sunlight_hours):
    """Check the health of a plant based on given parameters."""
    if not plant_name:
        raise ValueError("Plant name cannot be empty.")
    if water_level < 1:
        raise ValueError("Water level must be at least 1.")
    if water_level > 10:
        raise ValueError("Water level cannot exceed 10.")
    if sunlight_hours < 2:
        raise ValueError("Sunlight hours must be at least 2.")
    if sunlight_hours > 12:
        raise ValueError("Sunlight hours cannot exceed 12.")
    return f"{plant_name} is healthy !"


def test_plant_checks():
    """Test the plant health checking function."""
    print("=== Garden Plant Health Checker ===")

    print("Testing with valid parameters:")
    try:
        result = check_plant_health("Rose", 5, 6)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing with empty plant name:")
    try:
        result = check_plant_health("", 5, 6)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing with bad water level:")
    try:
        result = check_plant_health("Tulip", 0, 6)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("Testing bad sunlight hours:")
    try:
        result = check_plant_health("Daisy", 5, 1)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed.")
