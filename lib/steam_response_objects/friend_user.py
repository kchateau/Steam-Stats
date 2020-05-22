import datetime

class FriendUser:
    display_name = ""
    steam_id = ""
    relationship = ""
    friend_since = None
    state = ""

    def __init__(self, steam_id, relationship, friend_since):
        self.steam_id = steam_id
        self.relationship = relationship
        self.friend_since = self.convert_friend_since(friend_since)

    def convert_friend_since(self, friend_since):
        return datetime.datetime.utcfromtimestamp(friend_since)

    def add_display_name(self, display_name):
        self.display_name = display_name
        return

    def add_state(self, state):
        self.state = get_state(state)
        return

    def get_state(self, stateNum):
        if stateNum == 0:
            return "Offline"
        elif stateNum == 1:
            return "Online"
        elif stateNum == 2:
            return "Busy"
        elif stateNum == 3:
            return "Away"
        elif stateNum == 4:
            return "Snooze"
        elif stateNum == 5:
            return "Looking to Trade"
        elif stateNum == 6:
            return "Looking to Play"
        else:
            return "Unknown"


    

     