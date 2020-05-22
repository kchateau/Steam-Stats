import datetime

class Friend:
    steam_id = ""
    relationship = ""
    friend_since = ""

    def __init__(self, steam_id, relationship, friend_since):
        self.steam_id = steam_id
        self.relationship = relationship
        self.friend_since = self.convert_friend_since(friend_since)

    def convert_friend_since(self, friend_since):
        return datetime.datetime.utcfromtimestamp(friend_since).strftime('%m-%d-%Y')


    

     