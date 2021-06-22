class Player(object):
    def __init__(self,playerID,square,money):
        self.id = playerID
        self.square = square
        self.money = money
        self.missingTurn = False

    def moveToSquare(self,square):
        self.square = square

    def getSquare(self):
        return self.square

    def setMoney(self,money):
        self.money = money

    def getMoney(self):
        return self.money

    def getID(self):
        return self.id

    def setMissingTurn(self,value):
        self.missingTurn = value

    def getMissingTurn(self):
        return self.missingTurn
