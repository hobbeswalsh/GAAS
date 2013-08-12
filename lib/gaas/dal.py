
import mongoengine

from . import game

STORAGE = "/tmp/games.pickle"
OUTCOMES = "/tmp/outcomes.pickle"


def get_all_games():
    return game.CardGame.objects()

def get_game_by_uuid(uuid):
    return game.CardGame.objects(uuid=uuid).get()


def save_game(game):
    game.save()


def delete_game_by_uuid(uuid):
    g = get_game_by_uuid(uuid)
    g.delete()

# def get_all_outcomes():
#     try:
#         return cPickle.load(open(OUTCOMES))
#     except IOError:
#         return []


# def save_all_outcomes(outcomes):
#     cPickle.dump(outcomes, open(OUTCOMES, "w"))


# def save_game_outcome(adj):
#     outcomes = get_all_outcomes()
#     outcomes.append(adj)
#     save_all_outcomes(outcomes)


def connect_to_db():
    mongo_user = "restquest"
    mongo_pass = "thoundon"
    mongo_host = "ds037688.mongolab.com"
    mongo_port = 37688
    mongo_db = "rq_test"
    mongoengine.connect(
        mongo_db,
        host=mongo_host,
        port=mongo_port,
        username=mongo_user,
        password=mongo_pass)
