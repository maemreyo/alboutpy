from deck import Deck


class Hand(Deck):
    def __init__(self, label):
        self.deck = []
        self.label = label
        self.win_count = 0

    def __str__(self):
        return self.label + ': ' + ' '.join([str(card) for card in self.deck])

    def get_label(self):
        return self.label

    def get_win_count(self):
        return self.win_count

    def round_winner(self):
        self.win_count = self.win_count + 1
