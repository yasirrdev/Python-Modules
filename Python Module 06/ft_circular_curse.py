from alchemy.grimoire import record_spell, validate_ingredients


def main():
    print("=== Circular Curse Mastery ===")

    print("\nTesting validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')

    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')

    print("\nCircular curse broken using deferred import technique!")


if __name__ == "__main__":
    main()
