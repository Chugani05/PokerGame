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

    def __init__(self, cards: List[str]):
        self.cards = cards
        self.cat = None
        self.cat_rank = None
        self.evaluate_hand()

    def evaluate_hand(self):
        all_combinations = list(combinations(self.cards, 5))
        best_hand_rank = 0
        best_hand = None

        for combination in all_combinations:
            rank, hand, cat_rank = self.rank_hand(combination)
            if rank > best_hand_rank:
                best_hand_rank = rank
                best_hand = hand
                self.cat = rank
                self.cat_rank = cat_rank

    def rank_hand(self, hand: Tuple[str]) -> Tuple[int, List[str], Union[str, Tuple[str, str]]]:
        values = sorted(['--23456789TJQKA'.index(card[0]) for card in hand], reverse=True)
        suits = [card[1] for card in hand]
        value_counts = Counter(values)
        suit_counts = Counter(suits)

        is_flush = len(suit_counts) == 1
        is_straight = len(value_counts) == 5 and values[0] - values[4] == 4
        counts = value_counts.most_common()

        if is_straight and is_flush:
            return (Hand.STRAIGHT_FLUSH, hand, self.card_value_to_str(values[0]))
        elif counts[0][1] == 4:
            return (Hand.FOUR_OF_A_KIND, hand, self.card_value_to_str(counts[0][0]))
        elif counts[0][1] == 3 and counts[1][1] == 2:
            return (Hand.FULL_HOUSE, hand, (self.card_value_to_str(counts[0][0]), self.card_value_to_str(counts[1][0])))
        elif is_flush:
            return (Hand.FLUSH, hand, self.card_value_to_str(values[0]))
        elif is_straight:
            return (Hand.STRAIGHT, hand, self.card_value_to_str(values[0]))
        elif counts[0][1] == 3:
            return (Hand.THREE_OF_A_KIND, hand, self.card_value_to_str(counts[0][0]))
        elif counts[0][1] == 2 and counts[1][1] == 2:
            high_pair = max(counts[0][0], counts[1][0])
            low_pair = min(counts[0][0], counts[1][0])
            return (Hand.TWO_PAIR, hand, (self.card_value_to_str(high_pair), self.card_value_to_str(low_pair)))
        elif counts[0][1] == 2:
            return (Hand.ONE_PAIR, hand, self.card_value_to_str(counts[0][0]))
        else:
            return (Hand.HIGH_CARD, hand, self.card_value_to_str(values[0]))

    def card_value_to_str(self, value: int) -> str:
        return '--23456789TJQKA'[value]

    def __contains__(self, card: str) -> bool:
        return card in self.cards
        
    
