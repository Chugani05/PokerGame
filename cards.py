from __future__ import annotations
import random
import helpers

class Card:
    values = {'J' : 11, 'Q' : 12, 'K': 13, 'A' : 14}
    def __init__(self, card):
        self.suit = card[-1]
        self.pinta = card[0:-1]
        self.value = self.values[self.pinta] if self.pinta in self.values else int(self.pinta)

    def __gt__(self, other: Card) -> bool:
        return self.value > other.value
    
    def __eq__(self, other: Card) -> bool:
        return self.value == other.value
    
    def __str__(self):
        return f'{self.pinta + self.suit}'
    
    def __repr__(self) -> str:
        return f'{self.pinta + self.suit}'
    
class Deck:
    suits = ['♠', '♣', '◆', '❤']
    letters = ['J', 'Q', 'K', 'A']
    def __init__(self):
        self.deck = []
        self.generate()
        self.shuffle_deck()

    def generate(self):
        for suit in self.suits:
            for num in range(2, 11):
                self.deck.append(Card(str(num) + suit))
            for n in range(4):
                self.deck.append(Card(self.letters[n] + suit))
    
    def shuffle_deck (self):
        random.shuffle(self.deck)

class Hand:
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9

    def __init__(self, cards):
        self.cards = cards
        self.moves()

    def moves(self):
        return list(helpers.combinations(self.cards, n=5))
    
    def find_move(self):
        ... 
        
    