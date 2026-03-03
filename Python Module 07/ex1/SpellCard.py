from ex0.Card import Card


class SpellCard(Card):

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:

        effects = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Restore {self.cost} health',
            'buff': 'Apply buff effect',
            'debuff': 'Apply debuff effect'
        }
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effects.get(self.effect_type, self.effect_type)
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'targets': targets,
            'effect': self.effect_type,
            'spell_resolved': True
        }
