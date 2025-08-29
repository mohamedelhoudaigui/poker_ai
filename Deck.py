from Card import Card
from Hand import Hand
import random

class Deck:

    def __init__(self):
        self.cards = []
        ranks = '23456789TJQKA'
        suits = '♠♥♦♣'
        for suit in suits :
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            print(card.get_card())

    def get_r_card(self):
        if self.cards:
            random_card = random.choice(self.cards)
            self.cards.remove(random_card)
            return random_card
        else:
            return None

    def get_size(self):
        return len(self.cards)

    def shuffle_deck(self):
        random.shuffle(self.cards)
