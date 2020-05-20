from steam.webapi import WebAPI
from lib.steam_response_objects.steam_user import SteamUser
import os

def get_player_summaries(steamID):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('ISteamUser.GetPlayerSummaries', steamids=steamID)
    queried_user = api_response["response"]["players"][0]

    user = SteamUser(queried_user['personaname'], queried_user['steamid'], queried_user["profileurl"], queried_user["avatarfull"], queried_user["profilestate"])
    return user