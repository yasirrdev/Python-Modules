import math


def parse_coordinates(coord_str: str) -> tuple:
    try:
        parts = coord_str.split(',')
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return x, y, z
    except ValueError:
        print(f"Invalid coordinate format:{coord_str}. Expected format: x,y,z")
        return None


def distance_from_origin(position: tuple) -> float:
    x, y, z = position
    return math.sqrt(x*x + y*y + z*z)


def main():
    print("=== Game Coordinate System ===")

    position = (10, 20, 5)
    print(f"Position created: {position}")

    dist = distance_from_origin(position)
    print(f"Distance between (0, 0, 0) and {position}: {dist:.2f}")

    coord_str = "3,4,0"

    print(f"Parsing coordinates: {coord_str}")
    parsed_position = parse_coordinates(coord_str)

    if parsed_position:
        print(f"Parsed position: {parsed_position}")
        dist_parsed = distance_from_origin(parsed_position)
        print(f"Distance between origin and {parsed_position}: {dist_parsed}")

    invalid_coord_str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_coord_str}\"")

    try:
        invalid_position = parse_coordinates(invalid_coord_str)
        if invalid_position is None:
            raise ValueError("Invalid coordinate format")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    if parsed_position:
        x, y, z = parsed_position
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
