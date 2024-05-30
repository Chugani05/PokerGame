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

    def __init__(self, cards):
        self.cards = sorted(cards, key=Hand.get_card_value, reverse=True)
        self.cat, self.cat_rank = self.evaluate_poker_hand()

    def __contains__(self, card):
        return card in self.cards

    def is_flush(self):
        suits = [card.suit for card in self.cards]
        if len((suits)) == 1:
            return self.FLUSH, self.cards[0].pinta
        return None

    def is_straight(self):
        rank_order = '23456789TJQKA'
        rank_indices = sorted((rank_order.index(rank) for rank in [card.pinta for card in self.cards]))
        if len(rank_indices) == 5 and rank_indices[-1] - rank_indices[0] == 4:
            return self.STRAIGHT, self.cards[0].pinta
        if rank_indices == [0, 1, 2, 3, 12]:
            return self.STRAIGHT, '5'
        return None

    def is_straight_flush(self):
        if (flush := self.is_flush()) and (straight := self.is_straight()):
            return self.STRAIGHT_FLUSH, straight[1]
        return None

    def is_four_of_a_kind(self, rank_counts):
        for rank, count in rank_counts.items():
            if count == 4:
                return self.FOUR_OF_A_KIND, rank
        return None

    def is_full_house(self, rank_counts):
        three_of_a_kind = None
        pair = None
        for rank, count in rank_counts.items():
            if count == 3:
                three_of_a_kind = rank
            elif count == 2:
                pair = rank
        if three_of_a_kind and pair:
            return self.FULL_HOUSE, (three_of_a_kind, pair)
        return None

    def is_three_of_a_kind(self, rank_counts):
        for rank, count in rank_counts.items():
            if count == 3:
                return self.THREE_OF_A_KIND, rank
        return None

    def is_two_pair(self, rank_counts):
        pairs = []
        for rank, count in rank_counts.items():
            if count == 2:
                pairs.append(rank)
        if len(pairs) == 2:
            pairs.sort(key=Hand.get_card_numeric_value, reverse=True)
            return self.TWO_PAIR, tuple(pairs)
        return None

    def is_one_pair(self, rank_counts):
        for rank, count in rank_counts.items():
            if count == 2:
                return self.ONE_PAIR, rank
        return None

    def get_rank_counts(self, ranks):
        rank_counts = {}
        for rank in ranks:
            if rank in rank_counts:
                rank_counts[rank] += 1
            else:
                rank_counts[rank] = 1
        return rank_counts

    def evaluate_poker_hand(self):
        ranks = [card.pinta for card in self.cards]
        rank_counts = self.get_rank_counts(ranks)

        if match := self.is_straight_flush():
            return match
        elif match := self.is_four_of_a_kind(rank_counts):
            return match
        elif match := self.is_full_house(rank_counts):
            return match
        elif match := self.is_flush():
            return match
        elif match := self.is_straight():
            return match
        elif match := self.is_three_of_a_kind(rank_counts):
            return match
        elif match := self.is_two_pair(rank_counts):
            return match
        elif match := self.is_one_pair(rank_counts):
            return match
        else:
            return self.HIGH_CARD, self.cards[0].pinta

    def get_card_value(card):
        return Card.value

    def get_card_numeric_value(card):
        return Card.values[card]

    def __lt__(self, other):
        if self.cat != other.cat:
            return self.cat < other.cat
        else:
            if isinstance(self.cat_rank, tuple):
                for self_r, other_r in zip(self.cat_rank, other.cat_rank):
                    if Card.values[self_r] != Card.values[other_r]:
                        return Card.values[self_r] < Card.values[other_r]
                return False
            return Card.values[self.cat_rank] < Card.values[other.cat_rank]

    def __repr__(self):
        return f"Hand({self.cards}, Category: {self.cat}, Category Rank: {self.cat_rank})"
