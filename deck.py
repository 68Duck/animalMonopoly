class Deck(object):
    def __init__(self,cards):
        self.cards = cards
        self.pointer = 0
    def incrementPointer(self):
        self.pointer = (self.pointer + 1)%len(self.cards)
    def getCurrentCardText(self):
        return self.cards[self.pointer]["displayText"]
    def getCardMoneyValue(self):
        return self.cards[self.pointer]["moneyValue"]
