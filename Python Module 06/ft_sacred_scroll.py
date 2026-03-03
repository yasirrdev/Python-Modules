import alchemy


def main():
    print(f"Alchemy Module Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")

    try:
        fire = alchemy.create_fire()
        water = alchemy.create_water()
        earth = alchemy.create_earth()
        air = alchemy.create_air()

        print(f"Created elements: {fire}, {water}, {earth}, {air}")

    except AttributeError as e:
        print(f"Element creation failed: {e}")
    except Exception as e:
        print(f"An error occurred while creating elements: {e}")


if __name__ == "__main__":
    main()
