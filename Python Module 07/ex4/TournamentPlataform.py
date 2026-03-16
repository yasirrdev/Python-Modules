from ex4.TournamentCard import TournamentCard


class TournamentPlataform:

    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self.matches = []

    def register_card(self, card: TournamentCard) -> str:
        card_id = card.name.lower().split()[0] + '_001'
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        if card1.power >= card2.power:
            winner, loser = card1, card2
            winner_id, loser_id = card1_id, card2_id

        else:
            winner, loser = card2, card1
            winner_id, loser_id = card2_id, card1_id

        self.matches.append({'winner': winner_id, 'loser': loser_id})

        winner.update_wins(1)
        loser.update_losses(1)

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.rating,
            'loser_rating': loser.rating
        }

    def get_rating(self, item) -> int:
        return item[1].rating

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.items(),
                              key=self.get_rating, reverse=True)
        leaderboard = []

        for i, (card_id, card) in enumerate(sorted_cards):
            leaderboard.append(
                f"{i + 1}. {card.name} - Rating: "
                f"{card.rating} ({card.wins}-{card.losses})"
            )

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total = len(self.cards)
        ratings = sum(c.rating for c in self.cards.values())
        avg = ratings / total if total else 0

        return {
            'total_cards': total,
            'matches_played': len(self.matches),
            'avg_rating': avg,
            'plataform_status': 'active'
        }
