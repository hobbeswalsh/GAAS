import cPickle

STORAGE = "/tmp/games.pickle"
OUTCOMES = "/tmp/outcomes.pickle"


def get_all_games():
    try:
        return cPickle.load(open(STORAGE))
    except IOError:
        return {}


def get_game_by_uuid(uuid):
    all_games = get_all_games()
    return all_games.get(uuid)


def save_all_games(all_games):
    cPickle.dump(all_games, open(STORAGE, "w"))


def save_game(game):
    all_games = get_all_games()
    all_games[game.uuid] = game
    save_all_games(all_games)


def delete_game_by_uuid(uuid):
    try:
        all_games = get_all_games()
        all_games.pop(uuid)
        save_all_games(all_games)
        return True
    except KeyError:
        return False


def get_all_outcomes():
    try:
        return cPickle.load(open(OUTCOMES))
    except IOError:
        return []


def save_all_outcomes(outcomes):
    cPickle.dump(outcomes, open(OUTCOMES, "w"))


def save_game_outcome(adj):
    outcomes = get_all_outcomes()
    outcomes.append(adj)
    save_all_outcomes(outcomes)
