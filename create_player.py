from create_cards import Card


class Person():

    def __init__(self):
        self.hand = []
        self.hand_value = 0
        self.card_values = []
        self.max_hand_value = 21

    def draw_card(self):
        new_card = Card()
        card_value = new_card.card_value
        # Check if card in hand
        while card_value in self.hand:
            new_card = Card()
        print(new_card)
