from helpers import combinations
from pruebita import Card, Hand, Player, Dealer

def best_hand(common_cards, private_cards):
    best_hand = None
    mixed_cards = private_cards + common_cards
    for hand1 in combinations(mixed_cards, n=5):
        hand = Hand(list(hand1))
        if not best_hand or hand > best_hand:
            best_hand = hand
        elif best_hand == hand:
            for x, y in zip(best_hand, hand):
                if y > x:
                    best_hand = hand
    return best_hand


if __name__ == '__main__':

# [Card('3◆'), Card('3♣'), Card('A❤'), Card('K◆'), Card('Q♣')]
    print(best_hand([Card('10◆'), Card('9◆'), Card('8♠'), Card('6❤'), Card('5♠')], [Card('8♣'), Card('3❤')]))