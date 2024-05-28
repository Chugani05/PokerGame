from helpers import combinations
from pruebita import Card, Hand, Player, Dealer

def best_hand(common_cards, private_cards):
    best_hand = None
    mixed_cards = private_cards + common_cards
    for hand1 in combinations(mixed_cards, n=5):
        hand = Hand(list(hand1))
        print(hand)
        if not best_hand or hand > best_hand:
            best_hand = hand
        elif best_hand == hand:
            for x, y in zip(best_hand, hand):
                if y > x:
                    best_hand = hand
                    break
                elif x > y:
                    break
    return best_hand


if __name__ == '__main__':

# [Card('3◆'), Card('3♣'), Card('A❤'), Card('K◆'), Card('Q♣')]
    print('ganadoras', best_hand([Card('Q♣'), Card('Q♠'), Card('9♠'), Card('4♣'), Card('4♠')], [Card('J♣'), Card('9❤')]))

# [9♠, 9❤, 4♣, 4♠, Q♣], 2, ('9', '4')
#  [Card('Q♣'), Card('Q♠'), Card('9❤'), Card('9♠'), Card('J♣')],