from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck:

    def __init__(self):
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.deck:
            if card.name == card_name:
                self.deck.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.deck)

    def draw_card(self) -> Card:
        if self.deck:
            return self.deck.pop(0)
        return None

    def get_deck_stats(self) -> dict:
        creatures = sum(1 for c in self.deck if isinstance(c, CreatureCard))
        spells = sum(1 for c in self.deck if isinstance(c, SpellCard))
        artifacts = sum(1 for c in self.deck if isinstance(c, ArtifactCard))
        total = len(self.deck)
        avg = sum(c.cost for c in self.deck) / total if total > 0 else 0
        return {
            'total_cards': total,
            'creatures': creatures,
            'spells': spells,
            'artifacts': artifacts,
            'avg_cost': round(avg, 1)
        }
