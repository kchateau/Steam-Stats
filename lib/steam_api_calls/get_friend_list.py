from steam.webapi import WebAPI
from lib.steam_response_objects.friend import Friend
import os

list_of_friends = []

def get_friend_list(steamID):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('ISteamUser.GetFriendList', steamid=steamID)
    list_of_friends = make_friend_object_list(api_response["friendslist"]["friends"])
    return list_of_friends

def make_friend_object_list(api_response):
    friend_list = []
    for friend in api_response:
        curr_friend = Friend(friend['steamid'], friend['relationship'], friend["friend_since"])
        print(curr_friend.__dict__)
        friend_list.append(curr_friend)
    return friend_list