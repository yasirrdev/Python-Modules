from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int, mana_pool: int):
        super().__init__(name, cost, rarity)
        self.power = attack
        self.health = health
        self.mana_pool = mana_pool

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Elite'
        return info

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite card deployed with combat and magic abilities'
        }

    def attack(self, target: Card) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.power,
            'combat_type': 'melee'
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = incoming_damage - 2
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': self.health > taken
        }

    def get_combat_stats(self) -> dict:
        return {
            'name': self.name,
            'power': self.power,
            'health': self.health
        }

    def cast_spell(self, spell_name: str, targets: list[Card]) -> dict:
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': len(targets) + 2
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {'channeled': amount, 'total_mana': self.mana_pool}

    def get_magic_stats(self) -> dict:
        return {'name': self.name, 'mana_pool': self.mana_pool}
