class Cell:

    def __init__(self, i, j) :
        self.i = i
        self.j = j
        self.value = False
        self.neighborCells = []
        
    def addNeighbor(self, cell):
        if (cell != None):
            self.neighborCells.append(cell)
    
    def __str__(self):
        return str(self.i) + str(self.j)
