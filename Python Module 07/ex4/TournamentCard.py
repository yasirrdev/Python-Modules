from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity)
        self.power = attack
        self.health = health
        self.wins = 0
        self.losses = 0
        self.rating = 1200

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Tournament'
        return info

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed'
        }

    def attack(self, target) -> dict:
        return {
            'attacker': self.name,
            'target': target,
            'damage': self.power,
            'combat_type': 'tournament'
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            'defender': self.name,
            'damage_taken': incoming_damage,
            'still_alive': self.health > incoming_damage
        }

    def get_combat_stats(self) -> dict:
        return {'name': self.name, 'power': self.power, 'health': self.health}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'wins': self.wins,
            'losses': self.losses
        }

    def get_tournament_stats(self) -> dict:
        return {
            'name': self.name,
            'rating': self.rating,
            'record': f"{self.wins}-{self.losses}"
        }
