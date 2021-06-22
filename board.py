class Board(object):
    def __init__(self,animals):
        self.animals = animals
        self.initBoard()

    def initBoard(self):
        self.board = []
        self.board.append([])
        for i in range(12):
            self.board.append(self.animals[i])
        self.board.append([])
        for i in range(13,24,1):
            self.board.append(self.animals[i])

    def getAnimal(self,square):
        return self.board[square-1]
