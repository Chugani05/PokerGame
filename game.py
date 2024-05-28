from __future__ import annotations
from roles import Dealer, Player
from cards import Card, Deck, Hand

class Game:
    @staticmethod
    def get_winner(players: list[Player], common_cards: list[Card], private_cards: list[list[Card]]) -> tuple[Player | None, Hand]:
        p1 = players[0]
        p2 = players[1]
        dealer = Dealer(Deck(), p1, p2)
        p1.recieve_priv_cards(private_cards[0])
        p1.recieve_cmoon_cards(common_cards)
        p2.recieve_priv_cards(private_cards[1])
        p2.recieve_cmoon_cards(common_cards)
        print(p1.best_hand())
        print(p2.best_hand())
        result = dealer.best_hands()
        
        if result is None:
            return None, p1.best_hand()
        
        winner, best_hand = result
        return winner, best_hand

        
      


'''dealer = Dealer(Deck(), players[0], players[1])
        for player, priv_cards in zip(players, private_cards):
            player.recieve_priv_cards(priv_cards)
            player.recieve_cmoon_cards(common_cards)
            print(player.name)
        winner, best_hand = dealer.best_hands()
        return winner, best_hand'''

