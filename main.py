import random
from player import Player
from board import Board
from animal import Animal
import sqlite3 as lite
from dict_factory import dict_factory
from deck import Deck
from getInput import getPositiveIntegerInput,getGreaterThanInput

DATABASE = "cards.db"

def getCards():
    con = lite.connect(DATABASE)
    cur = con.cursor()
    cur.row_factory = dict_factory
    cur.execute("SELECT * FROM Cards")
    cards = cur.fetchall()
    return cards

def getAnimals():
    con = lite.connect(DATABASE)
    cur = con.cursor()
    cur.row_factory = dict_factory
    cur.execute("SELECT * FROM Animals")
    animals = cur.fetchall()
    return animals


def missAGo(currentPlayer):
    print("You landed on the miss a go space. Miss your next turn.")
    currentPlayer.setMissingTurn(True)

def drawCard(currentPlayer):
    deck.incrementPointer()
    print("You rolled a double so you draw a card")
    print(deck.getCurrentCardText())
    currentPlayer.setMoney(currentPlayer.getMoney()+deck.getCardMoneyValue())
    print("Your balance is now £",currentPlayer.getMoney())


def checkAnimal(currentPlayer,position):
    animal = board.getAnimal(position)
    if animal == []:
        return False
    else:
        print(f"You landed on the {animal.getName()} space")
        animalOwner = animal.getOwner()
        if animalOwner == "free":
            upgradeCost = animal.getUpgradeCost()
            if currentPlayer.getMoney()>upgradeCost:
                print("Would you like to buy the "+animal.getName()+"?")
                print("It costs £",upgradeCost)
                choice = input("")
                if choice == "yes":
                    animal.setOwner(currentPlayer)
                    currentPlayer.setMoney(currentPlayer.getMoney()-upgradeCost)
                    print("You bought the "+animal.getName())
                    print("Your balance is £",currentPlayer.getMoney())
            else:
                print("You don't have enough money to buy the",animal.getName())
        elif animalOwner == currentPlayer:
            print("You already own this animal so you can upgrade it.")
            print(f"Do you want to upgrade it for {animal.getUpgradeCost()}")
        else:
            cost = animal.getRentCost()
            animalOwner.setMoney(animalOwner.getMoney()+cost)
            currentPlayer.setMoney(currentPlayer.getMoney()-cost)
            print("Player",animalOwner.getID(),"already owns this.")
            print("You have to pay them £",cost)
            print("Your balance is £",currentPlayer.getMoney())
            print(f"Player {animalOwner.getID()}'s balance is £{animalOwner.getMoney()}")

def playTurn(currentPlayer):
    print("")
    input(f"Player {currentPlayer.getID()}'s turn.")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print("You rolled a",dice1,"and a",dice2)
    position = currentPlayer.getSquare() + dice1 + dice2
    if dice1 == dice2:
        drawCard(currentPlayer)
    if position > 25:
        position -= 25
        print("You passed the start so you get £500")
        currentPlayer.setMoney(500+currentPlayer.getMoney())
        print("Your balance is £",currentPlayer.getMoney())

    print("You landed on square",position)
    currentPlayer.moveToSquare(position)

    if position == 14:
        missAGo(currentPlayer)
    elif position == 0:
        print("You landed on the start space")
    else:
        checkAnimal(currentPlayer,position)

    return position

def mainGame():
    turnCounter = -1
    while True:
        turnCounter = (turnCounter + 1)%len(players)
        currentPlayer = players[turnCounter]
        if currentPlayer.getMissingTurn():
            currentPlayer.setMissingTurn(False)
            print("")
            print(f"Player {currentPlayer.getID()} misses their turn as they landed on the miss a go space")
        else:
            playTurn(currentPlayer)

if __name__ == "__main__":
    cards = getCards()
    deck = Deck(cards)
    animalsInformation = getAnimals()
    animals = []
    for a in animalsInformation:
        animals.append(Animal(a["name"],a["l0"],a["l1"],a["l2"],a["l3"],"free",a["upgradeCost"],a["imageLink"]))

    board = Board(animals)

    noPlayers = getGreaterThanInput("Enter the number of players",1)
    players = []
    for i in range(noPlayers):
        players.append(Player(i+1,0,2000))
    mainGame()
