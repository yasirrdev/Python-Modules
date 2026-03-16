from ex4.TournamentCard import TournamentCard


class TournamentPlataform:

    def __init__(self):
        self.cards = {}
        self.matches = []
    
    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().split()[0] + '_001'
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if c