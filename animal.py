class Animal(object):
    def __init__(self,name,l0,l1,l2,l3,owner,upgradeCost,imageLink):
        self.name = name
        self.imageLink = imageLink
        self.l0 = l0
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3
        self.owner = owner
        self.currentLevel = 0
        self.upgradeCost = upgradeCost

    def upgrade(self):
        if self.currentLevel < 3:
            currentLevel += 1

    def getOwner(self):
        return self.owner

    def getUpgradeCost(self):
        return self.upgradeCost

    def setOwner(self,player):
        self.owner = player

    def getRentCost(self):
        if self.currentLevel == 0:
            return self.l0
        elif self.currentLevel == 1:
            return self.l1
        elif self.currentLevel == 2:
            return self.l2
        else:
            return self.l3

    def getName(self):
        return self.name
