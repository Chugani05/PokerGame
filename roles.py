from __future__ import annotations
from helpers import combinations
from cards import Card, Hand, Deck



class Dealer:
    def __init__(self, deck: list[str], player1: Player, player2: Player):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2

    def deal_cards(self, num_cards: int) -> list:
        return [self.deck.pop(0) for _ in range(num_cards)]

    def revealcards(self) -> list[str]:
        community_cards = self.deal_cards(5)
        self.player1.recieve_cmoon_cards(community_cards)
        self.player2.recieve_cmoon_cards(community_cards)
        return community_cards

    def deal_private_cards(self):
        self.player1.recieve_priv_cards(self.deal_cards(2))
        self.player2.recieve_priv_cards(self.deal_cards(2))

    
    def best_hands(self) -> tuple[str, list[str]]:
        hand1 = self.player1.best_hand()
        hand2 = self.player2.best_hand()

        if hand1 > hand2:
            return (self.player1, hand1)
        elif hand1 < hand2:
            return (self.player2, hand2)
        elif hand1 == hand2:
            for h1, h2 in zip(hand1, hand2):
                if h1 > h2:
                    return (self.player1, hand1)
                elif h2 > h1:
                    return (self.player2, hand2)
        else:
            return (None, hand1)

    
    def decide_winner(self, player, community_cards):
        pass


class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards = []
        self.common_cards = []

    def __repr__(self) -> str:
        return f'{self.name}'
    
    def recieve_priv_cards(self, cards: list[Card]):
        self.private_cards = cards
    
    def recieve_cmoon_cards(self, cards: list[Card]):
        self.common_cards = cards
        
    
    def best_hand(self):
        mixed_cards = self.common_cards + self.private_cards
        best_hand = None
        for hand1 in combinations(mixed_cards, n=5):
            hand = Hand(list(hand1))
            if not best_hand or hand > best_hand:
                best_hand = hand
            elif best_hand == hand:
                for x, y in zip(best_hand, hand):
                    if y > x:
                        best_hand = hand
        return best_hand

