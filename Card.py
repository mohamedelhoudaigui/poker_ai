class Card :
    def __init__(self, suite, number):
        self.suite = suite
        self.number = number

    def get_card(self):
        return (self.suite, self.number)

    def print_card(self):
            return f"{self.suite} {self.number}"
