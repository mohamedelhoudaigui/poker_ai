class Hand:
    def __init__(self):
        self.hand = []

    def get_hand(self):
        return self.hand

    def print_hand(self):
        print(" | ".join(card.print_card() for card in self.hand))

    def add_card(self, card):
        self.hand.append(card)
