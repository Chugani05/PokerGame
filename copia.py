from __future__ import annotations
from helpers import combinations
from cards import Card, Hand, Deck



class Dealer:
    def __init__(self, deck: list[str], player1: Player, player2: Player):
        self.deck = deck
        self.player1 = player1
        self.player2 = player2f

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

    
    def determine_best_hand(self) -> tuple[str | None, list[str]]:
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
                elif h1 < h2:
                    return (self.player2, hand2)
        return None


class Player:
    def __init__(self, name: str):
        self.name = name
        self.private_cards = []
        self.common_cards = []

    def __repr__(self) -> str:
        return self.name
    
    def recieve_priv_cards(self, cards: list[Card]):
        self.private_cards = cards
    
    def recieve_cmoon_cards(self, cards: list[Card]):
        self.common_cards = cards
        
    
    def best_hand(self):
        all_cards = self.common_cards + self.private_cards
        best_hand = None
        for hand in combinations(all_cards, n=5):
            hand = Hand(list(hand))
            if not best_hand or hand > best_hand:
                best_hand = hand
            elif best_hand == hand:
                for card1, card2 in zip(best_hand, hand):
                    if card1 < card2:
                        best_hand = hand
                        break 
                    elif card1 > card2:
                        break
        return best_hand


#------------------------------------------------------------------------------------

from __future__ import annotations
from roles import Dealer, Player
from cards import Card, Deck, Hand

class Game:
    @staticmethod
    def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
        p1, p2 = players
        dealer = Dealer(Deck(), p1, p2)
        p1.recieve_priv_cards(private_cards[0])
        p1.recieve_cmoon_cards(common_cards)
        p2.recieve_priv_cards(private_cards[1])
        p2.recieve_cmoon_cards(common_cards)
        print(p1.best_hand())
        print(p2.best_hand())
        
        result = dealer.determine_best_hand()
        
        if result is None:
            return None, p1.best_hand()
        
        winner, best_hand = result
        return winner, best_hand

'''dealer = Dealer(Deck(), *players)
        for player, priv_cards in zip(players, private_cards):
        player.receive_priv_cards(priv_cards)
        player.receive_cmoon_cards(common_cards)'''

'''p1, p2 = players
        dealer = Dealer(Deck(), p1, p2)
        p1.recieve_priv_cards(private_cards[0])
        p1.recieve_cmoon_cards(common_cards)
        p2.recieve_priv_cards(private_cards[1])
        p2.recieve_cmoon_cards(common_cards)
        print(p1.best_hand())
        print(p2.best_hand())
'''
