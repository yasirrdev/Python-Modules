from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlataform import TournamentPlataform


def main():
    print("=== DataDeck Tournament Platform ===")

    platform = TournamentPlataform()

    print("\nRegistering Tournament Cards...")
    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("Ice Wizard", 4, "Rare", 3, 4)

    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    print(f"{dragon.name} (ID: {dragon_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {dragon.rating}")
    print(f"- Record: {dragon.wins}-{dragon.losses}")

    print(f"\n{wizard.name} (ID: {wizard_id}):")
    print("- Interfaces: [Card, Combatable, Rankable]")
    print(f"- Rating: {wizard.rating}")
    print(f"- Record: {wizard.wins}-{wizard.losses}")

    print("\nCreating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")

    print("\nTournament Leaderboard:")
    for entry in platform.get_leaderboard():
        print(entry)

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
