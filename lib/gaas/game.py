import json
import random
from uuid import uuid4

from . import dal
from . import deck


class CardGame(object):

    def __init__(self):
        self.decks = [
            deck.WinningDeck(),
            deck.WinningDeck(),
            deck.LosingDeck(),
            deck.LosingDeck()]
        random.shuffle(self.decks)
        self.uuid = uuid4().hex

    def serialize(self):
        serialized = {}
        serialized["uuid"] = self.uuid
        for i in range(4):
            serialized["deck{}".format(i)] = self.decks[i].serialize()
        return json.dumps(serialized)

    def __hash__(self):
        return hash(self.uuid)

    def make_play(self, deck):
        chosen = self.decks[deck].pick_card()
        if chosen is None:
            self.decks.pop(deck)
            risky_remaining = [d for d in self.decks if d.risky]
            safe_remaining = [d for d in self.decks if not d.risky]
            if len(risky_remaining) > len(safe_remaining):
                adj = "risky"
            else:
                adj = "safe"
            dal.save_game_outcome(adj)
            deleted = dal.delete_game_by_uuid(self.uuid)
            if deleted:
                print "it was deleted!"
            else:
                print "it was not deleted!"
        return chosen