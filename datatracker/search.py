import json
import requests
from collections import defaultdict as dd
from types import SimpleNamespace


# Case insensitive string searchByName will accommodate incorrect casings of letters
# ex HaLo: reACH
class search:
    def __init__(self):
        self.__init__ = True

    def searchByName(game_data, search_term):
        results = []
        if search_term is not '':
            for game in game_data:
                if search_term.casefold() in game.name.casefold():
                    results.append(game)

            return results, len(results)
        else: return results, 0

    def searchByID(results, game_ID):  # search work
        idvResults = []

        for game in results:
            if game._id == game_ID:
                idvResults.append(game)
                break
            else:
                pass

        return idvResults
