from __future__ import annotations

from prueba_cards import Card, Hand
from roles_prueba import Player


class Game:

    def __init__(self, players, common_cards, private_cards):
        self.players = players
        self.common_cards = common_cards
        self.private_cards = private_cards

    def get_winner(
        self, players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]
    ) -> tuple[Player | None, Hand]:
        best_hand = None
        winning_player = None
        winning_private_cards = None
        Player.common_cards = common_cards

        for player, private_hand in zip(players, private_cards):
            Player.private_cards = cards
            all_cards = common_cards + private_hand
            player_hand = Hand(all_cards)
            if best_hand is None or player_hand > best_hand[1]:
                best_hand = (player, player_hand)
                winning_player = player
                winning_private_cards = private_hand

        return winning_player, best_hand[1]
