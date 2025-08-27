import random

class Deck:
    def __init__(self):
        self.cards = []
        ranks = '23456789TJQKA'
        suits = '♠♥♦♣'
        for suit in suits :
            for rank in ranks:
                self.cards.append(Card(suit, rank))


