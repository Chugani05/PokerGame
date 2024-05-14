from __future__ import annotations

class Dealer:
    def __init__(self, deck, player1: Player, player2: Player):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2
    
    def reveal_cards(self) -> list:
        return [self.deck.pop(0) for _ in range(6)]

    def deal_cards(self):
        return [self.deck.pop(0) for _ in range(2)]
    
    def best_hands(self, hand1, hand2):
        ...

class Player:
    def __init__(self, name: str, private_cards, common_cards):
        self.name = name
        self.private_cards = private_cards
        self.common_cards = common_cards