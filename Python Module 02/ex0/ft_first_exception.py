def check_temperature(temp_str: str) -> int:
    """Check if the temperature input is valid for plants."""
    try:
        temp = int(temp_str)
    except ValueError:
        raise ValueError(f"Invalid temperature value: '{temp_str}'")
    if temp > 40:
        raise ValueError(f"{temp}°C is too high for plants! (max 40°C)")
    if temp < 0:
        raise ValueError(f"{temp}°C is too low for plants! (min 0°C)")
    return temp


def test_temperature_input():
    """Test the temperature input function."""
    print("=== Garden Temperature Checker ===")

    tests = [
        "25",
        "abc",
        "100",
        "-50"
    ]
    for test in tests:
        print(f"Testing temperature: {test}")
        try:
            temp = check_temperature(test)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")

    print("All tests completed - program didn't crash!")
