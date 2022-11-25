from datetime import datetime
import url_json
import pytz


class Game:
    def __init__(self, code, team):
        self.code = code
        self.last_time = ""
        self.day = ""
        self.team = team
        self.update_comp_time()
        self.pp = False
        self.pk = False
        self.is_home = False
        self.linescore = None
        self.score = (0, 0)
        self.game_time = ""
        self.period = ""
        self.update_line()
        self.home = self.linescore["teams"]["home"]["team"]["name"]
        self.away = self.linescore["teams"]["away"]["team"]["name"]
        if self.home == "New York Rangers":
            self.is_home = True
        # print(self.home + self.away)

        # print(self.last_time + self.day)

    def game_update(self):
        # gets object of changes to game
        url = "https://statsapi.web.nhl.com/api/v1/game/{0}/feed/live/diffPatch?startTimecode={1}_{2}" \
            .format(self.team, self.day, self.last_time)
        current_game = url_json.url_json(url)
        #print(current_game)
        self.update_comp_time()

    def update_comp_time(self):
        day = datetime.now(pytz.utc)
        self.day = day.strftime("%Y%m%d")
        self.last_time = day.strftime("%H%M%S")
        #print("here")
        #print(self.last_time + self.day)

    def get_game_id(self):
        url = "https://statsapi.web.nhl.com/api/v1/schedule?teamId={0}".format(self.id)
        #print(url)
        current_game = url_json.url_json(url)
        self.id = current_game["dates"][0]["games"][0]["gamePk"]

    def get_score(self):
        self.update_line()
        return self.score

    def get_time(self):
        self.update_line()
        return self.game_time

    def power_play(self):
        self.game_update()
        return self.pp

    def update_line(self):
        url = "https://statsapi.web.nhl.com/api/v1/game/{}/linescore".format(self.code)
        self.linescore = url_json.url_json(url)
        self.score = (self.linescore["teams"]["home"]["goals"], self.linescore["teams"]["away"]["goals"])
        self.game_time = self.linescore["currentPeriodTimeRemaining"]
        self.period = self.linescore["currentPeriod"]
        if self.is_home:
            self.pp = bool(self.linescore['teams']['home']['powerPlay'])
            self.pk = bool(self.linescore['teams']['away']['powerPlay'])
        else:
            self.pp = bool(self.linescore['teams']['away']['powerPlay'])
            self.pk = bool(self.linescore['teams']['home']['powerPlay'])


    def __str__(self):
        print(f'{self.away} @ {self.home}')

