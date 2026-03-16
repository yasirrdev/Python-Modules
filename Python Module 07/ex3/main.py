from ex3.GameEngine import GameEngine
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory


def main():
    print("=== DataDeck Game Engine ===")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("\nConfiguring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)
    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")
    hand_str = ", ".join(f"{c.name} ({c.cost})" for c in engine.hand)
    print(f"Hand: [{hand_str}]")

    print("\nTurn execution:")
    result = engine.simulate_turn()
    print(f"Strategy: {result['Strategy']}")
    print(f"Actions: {result['Actions']}")

    print("\nGame Report:")
    print(engine.get_engine_status())

    print("Abstract Factory + Strategy Pattern: ")
    print("Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
