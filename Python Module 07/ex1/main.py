from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===")

    print("\nBuilding deck with different card types...")
    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Common", 5,
                               "Permanent: +1 mana per turn"))

    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    while True:
        card = deck.draw_card()
        if card is None:
            break
        card_type = card.__class__.__name__.replace('Card', '')
        print(f"\nDrew: {card.name} ({card_type})")
        print(f"Play result: {card.play({})}")

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
