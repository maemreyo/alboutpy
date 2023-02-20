import random

from card import Card


# Define a deck and its methods
class Deck:
    def __init__(self):
        self.deck = []
        for suit in range(4):
            for rank in range(13):
                self.deck.append(Card(suit, rank))
        self.shuffle()

    def __len__(self):
        return len(self.deck)

    def add_card(self, card):
        self.deck.append(card)

    def pop_card(self):
        return self.deck.pop()

    def shuffle(self):
        random.shuffle(self.deck)
