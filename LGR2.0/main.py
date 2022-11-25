from time import sleep
from os import system
import Team as T


def play_game(team, game):
    game.get_score()
    if game.home == "New York Rangers":
        nyr_score = game.score[0]
    else:
        nyr_score = game.score[1]

    last_nyr_score = nyr_score
    while team.playing and game.game_time != "Final":
        game.get_score()
        # defines rangers as team for score check
        if game.home == "New York Rangers":
            nyr_score = game.score[0]
            other_score = game.score[1]
            if nyr_score != last_nyr_score:
                goal(game.pp, game.pk)
                last_nyr_score = nyr_score
        game.power_play()
        print("Period: {0} Time: {1}\n".format(game.period, game.game_time))
        print("{0}: {1} \n{2}: {3}\n".format(game.home, game.score[0], game.away, game.score[1]))
        print('Power Play:', game.pp)
        print('Penalty Kill:', game.pk)

    if game.game_time == 'Final':
        if game.home == "New York Rangers" and game.score[0]>game.score[1]:
            print('Rangers Win!')
        elif game.away == "New York Rangers" and game.score[0]<game.score[1]:
            print('Rangers Win!')



        sleep(10)

def goal(pp, pk):
    """Will Contain Code To Execute Goal Routine"""
    if pp:
        print("IT'S A POWERPLAY GOAL!!")
    elif pk:
        print("IT'S A SHORTHANDED GOAL!!")
    else:
        print("GOAL!!!!!")

    system(("osascript -e 'set volume output volume 100'"))
    system("afplay horn.wav")
    sleep(1)

def main():
    rangers = T.Team("3")
    rangers.get_next()
    current_game = rangers.game
    while True:
        if rangers.playing:
            play_game(rangers, current_game)
        else:
            print(f"next game: {rangers.next_game[1]} @ {rangers.next_game[2]} on {rangers.next_game[0][3]}-"
                  f"{rangers.next_game[0][2]} at {rangers.next_game[0][0]}:{rangers.next_game[0][1]}")





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
