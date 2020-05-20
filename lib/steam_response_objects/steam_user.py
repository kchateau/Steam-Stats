class SteamUser:
    display_name = ""
    steam_id = ""
    profile_url = ""
    avatar = ""
    state = ""

    def __init__(self, display_name, steam_id, profile_url, avatar, state):
        self.display_name = display_name
        self.steam_id = steam_id
        self.profile_url = profile_url
        self.avatar = avatar
        self.state = self.get_state(state)

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

    

     