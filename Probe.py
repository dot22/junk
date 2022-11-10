import random


class Card:
    card_suit = ('hearts', 'spades', 'clubs', 'diamonds')
    card_value = (
        'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',  'jack', 'queen', 'king', 'ace'
    )

    def __init__(self):
        self.suit = random.choice(Card.card_suit)
        self.value = random.choice(Card.card_value)
        self.meaning = (self.suit, self.value)

cards = [Card() for _ in range(4)]
print(cards[0].meaning)
