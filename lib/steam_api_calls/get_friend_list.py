from steam.webapi import WebAPI
from lib.steam_response_objects.friend_user import FriendUser
from lib.steam_api_calls.get_player_summaries import get_player_summaries, get_player_summaries_multiple_ids
import os

list_of_friends = []
list_of_friend_ids = []


def get_friend_list(steamID):
    api = WebAPI(os.environ.get("STEAM_KEY"))
    api_response = api.call('ISteamUser.GetFriendList', steamid=steamID)
    list_of_friends = make_friend_object_list(api_response["friendslist"]["friends"])
    comma_separated_ids = []

    for friend in list_of_friends:
        comma_separated_ids.append(friend.steam_id)

    comma_separated_string = ','.join(map(str, comma_separated_ids)) 
    list_of_friend_users = get_player_summaries_multiple_ids(comma_separated_string)

    for friend in list_of_friends:
        for user in list_of_friend_users:
            if friend.steam_id == user.steam_id:
                friend.display_name = user.display_name
                friend.state = user.state

    list_of_friends.sort(key=lambda r: r.friend_since)

    return list_of_friends

def make_friend_object_list(api_response):
    friend_list = []
    for friend in api_response:
        curr_friend = FriendUser(friend['steamid'], friend['relationship'], friend["friend_since"])
        friend_list.append(curr_friend)
    return friend_list