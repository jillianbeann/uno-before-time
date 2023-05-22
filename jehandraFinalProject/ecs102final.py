# /*  Uno
# ecs102final.py
# Jillian Handrahan
# Jill
# jehandra*/

# import what we need!
from graphics import *
from random import randrange


# GW
def setUpWin():
    windowGame = GraphWin("Uno Game", 800, 800)
    windowGame.setCoords(0, 0, 10, 10)

    return windowGame


def gameIntro(introBoard, textfile):
    # title the player name box
    highTitle = "Most Recent Players List"
    introText = Text(Point(8, 9.1), highTitle)
    introText.draw(introBoard)
    y = 8
    winNum=1

    # draw old players onto screen from text file
    # IFL
    winList=[]
    for line in textfile:
        numLabel=Text(Point(7.5,y+.08), winNum)
        numLabel.draw(introBoard)
        numPeriod=Text(Point(7.55, y+.08), ".")
        numPeriod.draw(introBoard)
        winList.append(line)
        winners = Text(Point(8, y), line)
        winners.draw(introBoard)
        y = y - .25
        winNum=winNum+1
    # outline to make it look nice
    outlineText = Rectangle(Point(7.2, 6.2), Point(8.8, 8.8))
    outlineText.draw(introBoard)

    # set up entry box
    nameBox = Entry(Point(4.4, 5.5), 10)
    nameBox.draw(introBoard)
    nameLabel = Text(Point(5, 5), "Enter your name in the box above")
    nameLabel.draw(introBoard)

    # fake button
    button = Rectangle(Point(5.1, 5.25), Point(6, 5.75))
    button.setFill("gray")
    button.draw(introBoard)
    buttonword = Text(Point(5.55, 5.5), "START")
    buttonword.draw(introBoard)

    # lay out the rules
    # OTXT
    ruleOutline = Rectangle(Point(1.2, 6.2), Point(2.8, 8.8))
    ruleOutline.draw(introBoard)
    rules = Text(Point(2, 9.1), "Game Rules")
    rules.draw(introBoard)
    turnRule = Text(Point(2, 8.15), "2 Turn Passes")
    turnRule.draw(introBoard)
    turnNumRule = Text(Point(2, 7.65), "10 Rounds")
    turnNumRule.draw(introBoard)
    winRule = Text(Point(2, 7.15), "Make it Through")
    winRuleTwo = Text(Point(2, 6.9), "all ten rounds")
    winRule.draw(introBoard)
    winRuleTwo.draw(introBoard)

    #IEB
    introBoard.getMouse()
    playername = nameBox.getText()
    # LOOD
    winList.insert(0, playername+"\n")
    winList.pop(5)

    # clear the screen after click
    nameBox.undraw()
    button.undraw()
    nameLabel.undraw()
    buttonword.undraw()

    # OFL
    userOutfile = open("players.txt", "w")
    for item in winList:
        # LOOD
        item = item.strip("\n")
        print(item, file=userOutfile)

    return winList


def startGame(gameBoard):
    # draw a line to divide your cards from the deck
    divideLine = Line(Point(0, 5), Point(10, 5))
    divideLine.setWidth(5)
    divideLine.draw(gameBoard)

    # add labels
    deckText = Text(Point(.5, 9.5), "Deck")
    deckText.setSize(30)
    deckText.draw(gameBoard)
    cardLabel = Text(Point(1, 4.5), "Your cards")
    cardLabel.setSize(30)
    cardLabel.draw(gameBoard)

    # pass turn button
    Passbutton = Rectangle(Point(4.5, 4.5), Point(5.5, 5))
    Passbutton.setFill("red")
    Passbutton.draw(gameBoard)
    buttontext = Text(Point(5, 4.75), "Pass turn")
    buttontext.draw(gameBoard)


def cardPicker():
    # RND
    cardColorchooser = randrange(0, 6)
    if cardColorchooser == 0:
        cardFill = "light blue"
    elif cardColorchooser == 1:
        cardFill = "pink"
    elif cardColorchooser == 2:
        cardFill = "red"
    elif cardColorchooser == 3:
        cardFill = "light green"
    elif cardColorchooser == 4:
        cardFill = "purple"
    elif cardColorchooser == 5:
        cardFill = "orange"

    # RND
    cardNumberChooser = randrange(0, 6)
    if cardNumberChooser == 0:
        cardNum = "1"
    elif cardNumberChooser == 1:
        cardNum = "2"
    elif cardNumberChooser == 2:
        cardNum = "3"
    elif cardNumberChooser == 3:
        cardNum = "4"
    elif cardNumberChooser == 4:
        cardNum = "5"
    elif cardNumberChooser == 5:
        cardNum = "6"
    return cardNum, cardFill


# CLOD
class Uno:

    def __init__(self, color, number, window):
        self.color = color
        self.number = number
        self.window = window

    def startCards(self, xOne, yOne, xTwo, yTwo):
        # make the shapes of the cards
        cardOne = Rectangle(Point(xOne, yOne), Point(xTwo, yTwo))
        cardOne.setFill(self.color)
        cardOne.draw(self.window)

        # add the number on the card
        cardNumText = Text(Point(xOne + .5, yTwo - 1), self.number)
        cardNumText.setSize(35)
        cardNumText.draw(self.window)

    def deck(self):
        # card + color
        deck = Rectangle(Point(4, 6), Point(6, 9))
        deck.setFill(self.color)
        deck.draw(self.window)

        # card number
        deckNum = Text(Point(4.5, 8), self.number)
        deckNum.setSize(35)
        deckNum.draw(self.window)

    def playGame(self, cardColorList, cardNumberList, deckCol, deckNum):
        # algorithm to check which card was selected
        clickCheck = False
        turnsPassed = False
        while clickCheck == False:
            # tell the user to select a card
            selectText=Text(Point(5,5.5), "Select a Card")
            selectText.draw(self.window)
            # IMS
            clickPoint = self.window.getMouse()
            selectText.undraw()
            xVal = clickPoint.getX()
            yVal = clickPoint.getY()
            # check if card 1
            if 1 < xVal < 3 and 1 < yVal < 4:
                selectionColor = cardColorList[0]
                selectionNumber = cardNumberList[0]
                if selectionColor==deckCol:
                    dChangeCol=selectionColor
                    dChangeNum=selectionNumber
                    clickCheck=True
                elif selectionNumber==deckNum:
                    dChangeCol=selectionColor
                    dChangeNum= selectionNumber
                    clickCheck=True
            # check if card 2
            elif 4 < xVal < 6 and 1 < yVal < 4:
                selectionColor = cardColorList[1]
                selectionNumber = cardNumberList[1]
                if selectionColor==deckCol:
                    dChangeCol = selectionColor
                    dChangeNum = selectionNumber
                    clickCheck = True
                elif selectionNumber == deckNum:
                    dChangeCol = selectionColor
                    dChangeNum = selectionNumber
                    clickCheck = True
            # check if card 3
            elif 7 < xVal < 9 and 1 < yVal < 4:
                selectionColor = cardColorList[2]
                selectionNumber = cardNumberList[2]
                if selectionColor==deckCol:
                    dChangeCol = selectionColor
                    dChangeNum = selectionNumber
                    clickCheck = True
                elif selectionNumber == deckNum:
                    dChangeCol = selectionColor
                    dChangeNum = selectionNumber
                    clickCheck = True
                else:
                    clickCheck = False
            # check if its pass turn button
            elif 4.5 < xVal < 5.5 and 4.5 < yVal < 5:
                dChangeCol=deckCol
                dChangeNum=deckNum
                turnsPassed = True
                clickCheck = True
            else:
                clickCheck = False

        return dChangeNum, dChangeCol, turnsPassed


############ End of Uno Class ############

def dealCards():
    # deal three cards
    xStart = 1
    yStart = 1
    xEnd = 3
    yEnd = 4
    # keep track of which cards are drawn
    cardsListNum = []
    cardsListCol = []
    for i in range(3):
        unoNumber, unoColor = cardPicker()
        # generate randomly, your cards
        card = Uno(unoColor, unoNumber, gameWin)
        card.startCards(xStart, yStart, xEnd, yEnd)
        xStart = xStart + 3
        xEnd = xEnd + 3
        cardsListNum.append(unoNumber)
        cardsListCol.append(unoColor)
    return card, cardsListNum, cardsListCol

def winSequence():
    winText = Text(Point(5, 9.5), "YOU WIN")
    winText.setFace("courier")
    winText.setSize(30)
    winText.setFill("green")
    winText.draw(gameWin)

def loseSequence():
    loseText = Text(Point(5, 9.5), "YOU LOSE")
    loseText.setFace("courier")
    loseText.setSize(30)
    loseText.setFill("red")
    loseText.draw(gameWin)

# run ten turns of the game
def tenTurns(playcard, lisNum, lisCol, deckColorStart, deckNumberStart):
    x = 10
    passedTurns = 0
    compPassTurn = 0
    while x > 0:

        # your turn
        newDeckNum, newDeckCol, passedTurnsBool = playcard.playGame(lisCol, lisNum, deckColorStart, deckNumberStart)

        newDeckCard = Uno(newDeckCol, newDeckNum, gameWin)
        newDeckCard.deck()

        continueGame = Text(Point(5, 5.5), "Click the mouse to continue")
        continueGame.draw(gameWin)
        gameWin.getMouse()
        continueGame.undraw()

        # computers turn
        # simulate the computer putting the correct cards down
        compNumber, compColor = cardPicker()
        whatWillItPick = randrange(0, 11)
        if 0 <= whatWillItPick <= 3:
            compNumber = newDeckNum
            deckColorStart=compColor
            deckNumberStart=compNumber
        if 4 <= whatWillItPick <= 7:
            compColor = newDeckCol
            deckColorStart=compColor
            deckNumberStart=compNumber
        if 8 <= whatWillItPick <= 10:
            deckColorStart=newDeckCol
            deckNumberStart=newDeckNum
            compPassTurn = compPassTurn + 1
            compPassText = Text(Point(5, 5.5), "The computer passed its turn")
            compPassText.draw(gameWin)
            gameWin.getMouse()
            compPassText.undraw()
            # if computer passes too many turns you win
            if compPassTurn > 1:
                winSequence()
                continueGame.setText("click to quit")
                continueGame.draw(gameWin)
                # close window with mouse click
                gameWin.getMouse()
                gameWin.close()

        compTurn = Uno(compColor, compNumber, gameWin)
        compTurn.deck()
        x = x - 1
        # if you pass too many turns
        if passedTurnsBool == True:
            passedTurns = passedTurns + 1
            if passedTurns > 2:
                loseSequence()
                continueGame.setText("click to quit")
                continueGame.draw(gameWin)
                # close window with mouse click
                gameWin.getMouse()
                gameWin.close()
    # if you make it through ten turns:
    while x==0:
        winSequence()
        continueGame.setText("click to quit")
        continueGame.draw(gameWin)
        # close window with mouse click
        gameWin.getMouse()
        gameWin.close()


if __name__ == "__main__":
    gameWin = setUpWin()

    winFile = open("players.txt", "r")
    winnerList=gameIntro(gameWin, winFile)

    startGame(gameWin)

    # FNC (cardPicker)
    deckNumber, deckColor = cardPicker()
    # randomly generate starting deck
    deckCard = Uno(deckColor, deckNumber, gameWin)
    deckCard.deck()

    # deal the cards
    card, listNumber, listColor = dealCards()

    # play ten turns
    tenTurns(card,listNumber,listColor, deckColor, deckNumber)
