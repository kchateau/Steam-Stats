from steam.webapi import WebAPI
from lib.steam_response_objects.game import Game
import os

list_of_games = []

def get_owned_games(steamID):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('IPlayerService.GetOwnedGames', steamid=steamID, include_appinfo=True, include_played_free_games=True, appids_filter=False, include_free_sub=False)
    list_of_games = make_owned_game_object_list(api_response["response"]["games"])
    return list_of_games

def make_owned_game_object_list(api_response):
    game_list = []
    for game in api_response:
        curr_game = Game(game['appid'], game['name'], game["playtime_forever"])
        game_list.append(curr_game)
    return game_list