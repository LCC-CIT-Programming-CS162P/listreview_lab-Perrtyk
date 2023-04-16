from time import sleep
import os
import random

import constants
import scoring
import scorecard
import playing
import time

# TODO: write main AFTER you have written and tested each function
def main():
    card = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1]]
    userTurn = False
    scorecard.resetScorecard(card)

    while any(constants.EMPTY in row for row in card):
        userTurn = True
        scorecard.updateScorecard(card)
        scorecard.displayScorecards(card)
        time.sleep(1)

        if userTurn:
            print('Game Message')
            time.sleep(1)
            playing.userPlay(card[0])
            scorecard.displayScorecards(card)
            userTurn = False
            playing.clear()

        if not userTurn:
            print('Game Message')
            time.sleep(1)
            playing.computerPlay(card[1])
            playing.clear()


    """
    -create a list of lists for the scorecard
    -set userTurn to false
    -call resetScorecard

    while there are still empty items in either scorecard
        swap players
        call updateScorecard
        call displayScorecard
        if it's the user's turn
            print a message and pause briefly
            call userPlay
        else
            print a message and pause breifly
            call computerPlay
        end if
     end while
     call updateScorecard
     call displayScorecard
     determine who won and display a message

    """


# this block is the same all of the time
# when the name of the file is main, call main
if __name__ == '__main__':
    main()
