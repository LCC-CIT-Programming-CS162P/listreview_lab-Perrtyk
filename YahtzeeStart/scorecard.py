"""
    This module contains all of the functions related to working with the scorecard
"""

import constants
from playing import clear

# TODO: write resetScorecard and updateScorecard
def resetScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    sets each of the individual values for the user and the computer to the constant empty.
    The subtotal, bonus and total should be set to 0.
    It does not return a value but the scorecard is altered by the function
    """
    new_scorecard = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1],
                 [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, -1]]
    scorecard.clear()
    scorecard.extend(new_scorecard)


def updateScorecard(scorecard):
    """ takes the 2-d list that represents the scorecard as it's parameter and
    calculates the subtotal, bonus and total for both the user and the computer.
    It does not return a value but the scorecard is altered by the function
    """
    if len(scorecard) <= constants.BONUS:
        return  # scorecard does not have enough elements to calculate bonus

    if len(scorecard[0]) <= constants.USER:
        return  # user column does not have enough elements to calculate bonus

    # calculate subtotal for user and computer
    user_subtotal = 0
    comp_subtotal = 0
    for row in scorecard[constants.ONES:constants.SIXES + 1]:
        user_subtotal += row[constants.USER]
        comp_subtotal += row[constants.COMPUTER]

    # check if user and computer qualify for bonus
    if user_subtotal >= constants.BONUS:
        scorecard[constants.BONUS][constants.USER] = constants.BONUS
    if comp_subtotal >= constants.BONUS:
        scorecard[constants.BONUS][constants.COMPUTER] = constants.BONUS

    if len(scorecard) <= constants.TOTAL:
        return  # scorecard does not have enough elements to calculate total

    if len(scorecard[0]) <= constants.TOTAL:
        return  # total column does not have enough elements to calculate total

    # calculate bonus for user and computer
    user_bonus = 0
    comp_bonus = 0
    if scorecard[constants.BONUS][constants.USER] == constants.BONUS:
        user_bonus = constants.BONUS_POINTS
    if scorecard[constants.BONUS][constants.COMPUTER] == constants.BONUS:
        comp_bonus = constants.BONUS_POINTS

    # calculate total for user and computer
    user_total = user_subtotal + user_bonus
    comp_total = comp_subtotal + comp_bonus
    for row in scorecard[constants.THREE_OF_A_KIND:constants.CHANCE + 1]:
        user_total += row[constants.USER]
        comp_total += row[constants.COMPUTER]

    # update scores in scorecard
    scorecard[constants.SUBTOTAL][constants.USER] = user_subtotal
    scorecard[constants.SUBTOTAL][constants.COMPUTER] = comp_subtotal
    scorecard[constants.BONUS][constants.USER] = user_bonus
    scorecard[constants.BONUS][constants.COMPUTER] = comp_bonus
    scorecard[constants.TOTAL][constants.USER] = user_total
    scorecard[constants.TOTAL][constants.COMPUTER] = comp_total





def formatCell(value):
    return "" if value < 0 else str(value)


def displayScorecards(scorecard):
    labels = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
              "3 of a Kind", "4 of a Kind", "Full House", "Small Straight", "Large Straight",
              "Chance", "Yahtzee", "Sub Total", "Bonus", "Total Score"]
    lineFormat = "| {3:2s} {0:<15s}|{1:>8s}|{2:>8s}|"
    border = '-' * 39
    uScorecard = scorecard[constants.USER]
    cScorecard = scorecard[constants.COMPUTER]

    #clear()
    print(border)
    print(lineFormat.format("", "  You   ", "Computer", ""))
    print(border)

    for i in range(constants.ONES, constants.SIXES + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.SUBTOTAL], formatCell(uScorecard[constants.SUBTOTAL]), formatCell(cScorecard[constants.SUBTOTAL]), ""))
    print(border)
    print(lineFormat.format(labels[constants.BONUS], formatCell(uScorecard[constants.BONUS]), formatCell(cScorecard[constants.BONUS]), ""))
    print(border)

    for i in range(constants.THREE_OF_A_KIND, constants.YAHTZEE + 1):
        print(lineFormat.format(labels[i], formatCell(uScorecard[i]), formatCell(cScorecard[i]), str(i)))

    print(border)
    print(lineFormat.format(labels[constants.TOTAL], formatCell(uScorecard[constants.TOTAL]), formatCell(cScorecard[constants.TOTAL]), ""))
    print(border)



