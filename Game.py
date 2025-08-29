from Hand import Hand
from Deck import Deck
from Pot import Pot

class Game:
    def __init__(self):
        self.deck = Deck()
        self.pot = Pot()

        self.hand1 = Hand()
        self.hand2 = Hand()

        for _ in range (0, 3):
            rand_card1 = self.deck.get_r_card()
            rand_card2 = self.deck.get_r_card()
            self.hand1.add_card(rand_card1)
            self.hand2.add_card(rand_card2)

        self.com_cards = []

    def print_hands(self):
        self.hand1.print_hand()
        self.hand2.print_hand()

    def print_pot(self):
        self.pot.print_pot_size()

    def populate_com_cards(self, n):
        for i in range (n):
            self.com_cards.append(self.deck.get_r_card())

    def print_com_cards(self):
        print(" | ".join(card.print_card() for card in self.com_cards))
