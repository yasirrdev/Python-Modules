from ex3.CardFactory import CardFactory
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card


class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power=None) -> Card:
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None) -> Card:
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None) -> Card:
        return ArtifactCard("Mana Crystal", 2, "Common", 5,
                            "Permanent: +1 mana per turn")

    def get_supported_types(self) -> dict:
        return {
            'creatures': ['dragon', 'goblin'],
            'spells': ['fireball'],
            'artifacts': ['mana_ring']
        }

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        types = ['creature', 'spell', 'artifact']

        for i in range(size):
            card_type = types[i % 3]
            if card_type == 'creature':
                cards.append(self.create_creature())
            elif card_type == 'spell':
                cards.append(self.create_spell())
            else:
                cards.append(self.create_artifact())
        return {'deck': cards, 'size': len(cards)}
