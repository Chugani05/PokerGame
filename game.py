from __future__ import annotations
from roles import Dealer, Player
from cards import Card, Deck, Hand

class Game:

    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.dealer = Dealer()
        
    
    def get_winner(self, players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
       