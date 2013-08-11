import random
import json


class Deck(object):
    NUM_CARDS = 30

    def __init__(self, card_list=[]):
        self.card_list = card_list
        self.played_cards = []
        self._generate()
        self.shuffle()

    def _generate(self):
        raise NotImplementedError

    def shuffle(self):
        random.shuffle(self.card_list)

    def pick_card(self):
        try:
            chosen_card = self.card_list.pop()
            self.played_cards.append(chosen_card)
            return chosen_card
        except IndexError:
            return None

    def serialize(self):
        return json.dumps(self.card_list)

    @property
    def value(self):
        return sum(self.card_list)

    def __hash__(self):
        return hash(self.id)

    def __repr__(self):
        return "<{} with total value {}>".format(self.__class__.__name__, self.value)


class WinningDeck(Deck):

    risky = False

    def _generate(self):
        while sum(self.card_list) <= 50:
            bad_cards = [int(random.triangular(-100, -30, -50))
                         for i in range(self.NUM_CARDS / 2)]
            good_cards = [int(random.triangular(35, 120, 75))
                          for i in range(self.NUM_CARDS / 2)]
            self.card_list = good_cards + bad_cards


class LosingDeck(Deck):

    risky = True

    def _generate(self):
        self.card_list = [1]
        while sum(self.card_list) >= -150:
            bad_cards = [int(random.triangular(-1250, -450, -600))
                         for i in range(self.NUM_CARDS / 2)]
            good_cards = [int(random.triangular(250, 900, 300))
                          for i in range(self.NUM_CARDS / 2)]
            self.card_list = good_cards + bad_cards
