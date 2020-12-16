from types import SimpleNamespace

from collections import Counter as ct
import collections as col


# names , titles = platformData.copiesPerPlatform(gameData)

class platformData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def copiesPer_Dict(game_data):  # Calls multiple functions to return one dictionary
        numberOfPlatforms = platformData._findUniquePlatforms(game_data, 2013, 2021)
        platforms = platformData._titlesPer(game_data)
        topPlatforms = platformData._top_Platforms(platforms, numberOfPlatforms)  # Sorts the data by top platform descending order
        return topPlatforms  # Returns Dict


    # Counts the number of publishers    
    def _titlesPer(json_data):
        platforms = ct(k.platform for k in json_data if k.platform)
        return platforms

    def _findUniquePlatforms(json_data, yearMin, yearMax):
        # finds unique publishers taking advantage of the set data structure
        # Constructor
        platform_set = set((""))
        platformdict = {}

        for platform in json_data:
            if type(platform.year) != type(None) and platform.platform != type(None) and platform != type(None):
                if yearMin <= platform.year <= yearMax:
                    platform_set.add(platform.platform)

                else:
                    pass
            else:
                pass

        unique_platforms = len(platform_set)
        return unique_platforms

    def _top_Platforms(platforms, top):
        top_platforms = set((""))
        top_platforms = dict(ct(platforms).most_common(top))
        return top_platforms

