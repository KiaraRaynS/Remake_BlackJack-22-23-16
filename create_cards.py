

class Card:

    def __init__(self):
        import random
        self.suits = ['♠', '♥', '♣', '♦']
        self.suit = random.choice(self.suits)
        value = random.randint(0, 10)
        if value > 1:
            self.value = random.randint(2, 9)
        elif value == 10:
            self.value = random.choice('J', 'Q', 'K')
        else:
            self.value = 'A'
        self.card_value = [self.suit, self.value]

    def __repr__(self):
        return str(self.card_value)
