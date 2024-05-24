from __future__ import annotations

class Dealer:
    def __init__(self, deck: List[str], player1: Player, player2: Player):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2
    
    def reveal_cards(self) -> List[str]:
        community_cards = [self.deck.pop(0) for _ in range(5)]
        self.player1.set_common_cards(community_cards)
        self.player2.set_common_cards(community_cards)
        return community_cards

    def deal_private_cards(self):
        self.player1.set_private_cards([self.deck.pop(0) for _ in range(2)])
        self.player2.set_private_cards([self.deck.pop(0) for _ in range(2)])

    def best_hands(self) -> Tuple[str, List[str]]:
        hand1 = self.player1.best_hand()
        hand2 = self.player2.best_hand()
        
        if hand1 > hand2:
            return (self.player1.name, hand1)
        else:
            return (self.player2.name, hand2)

class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards: List[str] = []
        self.common_cards: List[str] = []

    def receive_private_cards(self, cards: List[str]):
        self.private_cards = cards

    def receive_community_cards(self, cards: List[str]):
        self.common_cards = cards

    def get_best_hand(self) -> List[str]:
        return sorted(self.private_cards + self.common_cards, reverse=True)[:5]
