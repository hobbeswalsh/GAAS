import json
import random

from flask import request

from . import app
from .. import deck
from .. import game
from .. import dal


def create_routes():
    @app.route("/api/v1/deck/new")
    def create_new_deck():
        choices = [deck.WinningDeck, deck.LosingDeck]
        return random.choice(choices)().serialize()

    @app.route("/api/v1/winningdeck/new")
    def create_new_winning_deck():
        return deck.WinningDeck().serialize()

    @app.route("/api/v1/losingdeckdeck/new")
    def create_new_losing_deck():
        return deck.LosingDeck().serialize()

    @app.route("/api/v1/game/new")
    def create_new_game():
        g = game.CardGame()
        dal.save_game(g)
        return g.serialize()

    @app.route("/api/v1/game/<uuid>")
    def get_game_by_uuid(uuid):
        game = dal.get_game_by_uuid(uuid)
        if game:
            return game.serialize()
        return json.dumps(None)

    @app.route("/api/v1/game/<uuid>/play", methods=["POST"])
    def make_a_play(uuid):
        game = dal.get_game_by_uuid(uuid)
        print game
        deck = int(request.values.get("deckNum"))
        chosen_card = game.make_play(deck)
        dal.save_game(game)
        return json.dumps(chosen_card)

    @app.route("/api/v1/game/<uuid>", methods=["DELETE"])
    def delete_game(uuid):
        success = dal.delete_game_by_uuid(uuid)
        if success:
            message = "Game {} deleted.".format(uuid)
        else:
            message = "Game {} not found.".format(uuid)
        return json.dumps({
            "success": success,
            "message": message})
