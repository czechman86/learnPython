# Blackjack

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

userHand = []
compHand = []

playAgain = True

def initialDraw():
    userHand.append(cards[random.randint(0, 12)])
    userHand.append(cards[random.randint(0, 12)])

    compHand.append(cards[random.randint(0, 12)])
    compHand.append(cards[random.randint(0, 12)])

def scoreInformer():
    print(f"You have drawn: {userHand}, with a total of {sum(userHand)}")
    print(f"The computer has drawn {compHand[0]}")

def aceCheck(userList):
    listTracker = 0
    if sum(userList) > 21:
        for num in userList:
            if num == 11:
                userList[listTracker] = 1
            listTracker += 1

def hitComp():
    while sum(compHand) < 17:
        compHand.append(cards[random.randint(0, 12)])
        if sum(compHand) >= 17:
            aceCheck(compHand)
        continue
    return sum(compHand)

def hitMe():
    while sum(userHand) < 21:
        hitMeOption = input("Would you like to draw another card? 'y' or 'n' ").lower()
        if hitMeOption == "y":
            userHand.append(cards[random.randint(0, 12)])
            aceCheck(userHand)
            scoreInformer()
            continue
        else:
            return sum(userHand)

def scoreCompare():
    if sum(userHand) > 21 and sum(compHand) > 21:
        print("Both Over")
    elif sum(userHand) <= 21 and sum(compHand) > 21:
        print("Congrats! You win!")
    elif sum(userHand) > 21 and sum(compHand) <= 21:
        print("Sorry, you lose")
    elif sum(userHand) > sum(compHand):
        print("Congrats! You Win!")
    elif sum(userHand) < sum(compHand):
        print("You lose.")
    else:
        print("Draw Game")

def finalResults():
    print(f"Your hand consisted of: {userHand} with a total of {sum(userHand)}")
    print(f"The computer hand consisted of: {compHand} with a total of {sum(compHand)}")

def playAnotherGame():
    goAgain = input("Do you want to play again? 'y' or 'n'? ")
    if goAgain == "y":
        userHand.clear()
        compHand.clear()
        return True
    else:
        return False


def blackjack(handOfUser, handOfComp, playAgainBoll):
    while playAgainBoll:

        initialDraw()

        scoreInformer()

        hitComp()

        hitMe()

        scoreCompare()

        finalResults()

        playAgainBoll = playAnotherGame()


blackjack(userHand, compHand, playAgain)