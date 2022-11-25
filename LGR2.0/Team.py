from datetime import datetime
import pytz
import Game as G
import url_json


class Team:
    def __init__(self, team):
        self.team = team
        self.playing = False
        self.next_game = None
        self.game = self.get_next()
        self.playing = self.is_playing()

    def get_next(self):
        current_day = datetime.now(pytz.utc).strftime("%Y-%m-%d")
        url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={0}&startDate={1}".format(self.team, current_day)
        json = url_json.url_json(url)
        game_id = json["dates"][0]["games"][0]["gamePk"]
        home = json["dates"][0]["games"][0]["teams"]["home"]["team"]["id"] == 3
        game_state = int(json["dates"][0]["games"][0]["status"]["codedGameState"])
        if game_state < 5:
            if game_state > 2:
                self.playing = True
            date_time = json['dates'][0]["games"][0]["gameDate"]
            print(date_time)
            home = json['dates'][0]['games'][0]['teams']['home']
            away = json['dates'][0]['games'][0]['teams']['away']
            date = date_time.split('T')[0]
            time = date_time.split('T')[1]

            self.next_game = (self.timezone(date, time, -5), home, away)
            return G.Game(game_id, self)
        else:
            try:
                game_id = json["dates"][1]["games"][0]["gamePk"]
                date_time = json['dates'][1]["games"][0]["gameDate"]
                print(date_time)
                home = json['dates'][1]['games'][0]['teams']['home']
                away = json['dates'][1]['games'][0]['teams']['away']
                date = date_time.split('T')[0]
                time = date_time.split('T')[1]
                self.next_game = (self.timezone(date, time, -5), home, away)
                return G.Game(game_id, self)
            except:
                return 0

    def is_playing(self):
        self.get_next()
        return self.playing


def timezone(date, time, offset):
    day = date.split('-')[2]
    month = date.split('-')[1]
    hour = time.split(':')[0]
    min = time.split(':')[1]
    hour += offset
    if hour < 0:
        hour = 24 + hour
        day -= 1
        if day < 0:
            day = 30 + hour
            month -= 1
            if month < 0:
                month = 12 + month
    return hour, min, day, month
