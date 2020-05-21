class Game:
    app_id = ""
    name = ""
    playtime = ""

    def __init__(self, app_id, name, playtime):
        self.app_id = app_id
        self.name = name
        self.playtime = self.playtime_to_hours(playtime)

    def playtime_to_hours(self, playtime):
        return round((playtime/60), 1)


    

     