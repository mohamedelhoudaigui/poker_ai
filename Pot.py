class Pot:
    def __init__(self):
        self.pot_size = 0

    def add_to_pot(self, amount):
        self.pot_size += amount

    def empty_pot(self):
        self.pot_size = 0

    def get_pot_size(self):
        return self.pot_size

    def print_pot_size(self):
        print(f'pot size is {self.pot_size}')