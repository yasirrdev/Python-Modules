from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets

    def execute_turn(self, hand: list[Card], battlefield: list[Card]) -> dict:
        cards_played = []
        mana_used = 0
        damage = 0
        for card in hand:
            if card.cost <= 3:
                cards_played.append(card.name)
                mana_used += card.cost
                damage += card.cost
        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': ['Enemy Player'],
            'damage_dealt': damage
        }
