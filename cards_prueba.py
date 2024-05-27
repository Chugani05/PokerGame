from __future__ import annotations

import helpers


class Card:
    values = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }

    def __init__(self, card: str):
        self.suit = card[-1]
        self.pinta = card[0:-1]
        self.value = self.values[self.pinta] if self.pinta in self.values else int(self.pinta)

    def __gt__(self, other: Card) -> bool:
        return self.value > other.value

    def __eq__(self, other: Card) -> bool:
        return self.value == other.value

    def __repr__(self) -> str:
        return f'{self.pinta + self.suit}'


class Deck:
    SUITS = ('♠', '♣', '◆', '❤')
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        self.deck = []
        self.generate()
        self.shuffle_deck()

    def generate(self):
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(rank + suit))

    def shuffle_deck(self):
        helpers.shuffle(self.deck)


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

    def __init__(self, cards: list[str]):
        self.cards = cards
        self.cat = None
        self.cat_rank = None

    def evaluate_poker_hand():
        pass

    def card_value_to_str(self, value: int) -> str:
        return '23456789TJQKA'[value]

    def __contains__(self, card: str) -> bool:
        return card in self.cards
