from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
from alchemy.transmutation.advanced import philosophers_stone, elixir_of_life


def main():
    print("=== Pathway Debate Mastery ===")

    print("\nAbsolute imports (from alchemy.transmutation.basic):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")

    print("\nRelative imports (from .basic, ..potions):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


if __name__ == "__main__":
    main()
