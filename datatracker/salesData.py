class salesData(object):
    def __init__(self, game_data):
        self.game_data = game_data

    def salesPer_Global(game_data, yearMin, yearMax):
        platforms = salesData._findUniquePlatforms(game_data)
        platforms_dict = salesData._createPlatformDict(platforms)
        globalSalesRAW = salesData._salesGlobal(game_data, platforms_dict, yearMin, yearMax)
        globalSales = salesData._dictionaryCleaner(globalSalesRAW)
        return globalSales

    def _salesGlobal(game_data, platforms_dict, yearMin, yearMax):
        for game in game_data:
            if type(game.year) != type(None):
                if yearMin <= game.year <= yearMax:
                    platforms_dict[f"{game.platform}"] += game.globalSales
            else:
                pass
        return platforms_dict

    def _findUniquePlatforms(game_data):
        platforms = {game.platform for game in game_data}
        return platforms

    def _createPlatformDict(platforms):  # ReturnsDict
        platforms_dict = {}
        for platform in platforms:
            platforms_dict[f'{platform}'] = 0
        return platforms_dict

    def _dictionaryCleaner(dictionary):
        nullEntries = []
        for entry in dictionary:
            if (dictionary[entry] == 0
                    or dictionary[entry] == type(None)):
                nullEntries.append(entry)

        for entry in nullEntries:
            del dictionary[entry]

        return dictionary
