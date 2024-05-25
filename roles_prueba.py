from __future__ import annotations

from cards_prueba import Hand

import helpers


class Dealer:
    def __init__(self, deck: list[str], player1: Player, player2: Player):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2

    def reveal_community_cards(self) -> list[str]:
        community_cards = [self.deck.pop(0) for _ in range(5)]
        Player.receive_common_cards(community_cards)
        return community_cards

    def deal_private_cards(self):
        self.player1.receive_private_cards([self.deck.pop(0) for _ in range(2)])
        self.player2.receive_private_cards([self.deck.pop(0) for _ in range(2)])

    def best_hand(self) -> tuple[str, list[str]]:
        hand1 = self.player1.get_best_hand()
        hand2 = self.player2.get_best_hand()

        if hand1 > hand2:
            return (self.player1.name, hand1)
        else:
            return (self.player2.name, hand2)


class Player:
    common_cards = []

    def __init__(self, name: str):
        self.name = name
        self.private_cards = []

    def receive_private_cards(self, cards: list[str]):
        self.private_cards = cards

    @classmethod
    def receive_common_cards(cls, cards: list[str]):
        cls.common_cards = cards

    def get_best_hand(self) -> list[str]:
        return sorted(self.private_cards + self.common_cards, reverse=True)[:5]

    def get_best_combination(self):
        all_cards = self.private_cards + self.common_cards
        best_hand = None
        best_rank = None

        for combination in helpers.combinations(all_cards, 5):
            rank = Hand.evaluate_poker_hand(combination)
            if best_rank is None or rank > best_rank:
                best_hand = combination
                best_rank = rank

        return best_hand
