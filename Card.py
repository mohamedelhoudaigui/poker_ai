
class Card :
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

    def print_card(self):
        return (self.suite, self.number)


