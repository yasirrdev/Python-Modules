def garden_operations():
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    print("Testing ZeroDivisionError...")
    try:
        10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    print("Testing FileNotFoundError...")
    try:
        file = open("missing.txt")
        file.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    print("Testing KeyError...")
    try:
        plants = {"Rose": 4, "Tulip": 3}
        print(plants["missing_plant"])
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    print("Testing multiple errors together...")
    try:
        int("abc")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")


def test_error_types():
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
