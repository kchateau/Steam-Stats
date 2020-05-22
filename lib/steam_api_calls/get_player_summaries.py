from steam.webapi import WebAPI
from lib.steam_response_objects.steam_user import SteamUser
import os


def get_player_summaries(steamID):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('ISteamUser.GetPlayerSummaries', steamids=steamID)
    queried_user = api_response["response"]["players"][0]

    user = SteamUser(queried_user['personaname'], queried_user['steamid'], queried_user["profileurl"], queried_user["avatarfull"], queried_user["profilestate"])
    return user

def get_player_summaries_multiple_ids(steamIDList):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('ISteamUser.GetPlayerSummaries', steamids=steamIDList)
    list_of_users = api_response["response"]["players"]
    user_object_list = []

    for user in list_of_users:
        curr_user = SteamUser(user['personaname'], user['steamid'], user["profileurl"], user["avatarfull"], user["profilestate"])
        user_object_list.append(curr_user)
    
    return user_object_list