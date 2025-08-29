from Hand import Hand

class Player:
    def __init__(self, hand, ships):
        self.ships = ships
        self.hand = hand

    def check(self):
        pass

    def bet(self, amount):
        if self.ships < amount:
            raise ValueError("Insufficient ships to place the bet.")
        self.ships -= amount
        return amount

    def call(self, amount):
        if self.ships < amount:
            raise ValueError("Insufficient ships to call.")
        self.ships -= amount
        return amount

    def raise(self, amount):
        if self.ships < amount:
            raise ValueError("Insufficient ships to raise.")
        self.ships -= amount
        return amount

    def fold(self):
        return

    def add_ships(self, amount):
        self.ships += amount