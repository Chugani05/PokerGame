from __future__ import annotations
import roles

class Game:

    def __init__(self, players, common_cards, private_cards):
        self.players = players
        self.common_cards = common_cards
        self.private_cards = private_cards

    def get_winner( players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
        ...