class Evolution:

    def getNbLiveCells(self, cells):
        nb = 0
        for cell in cells:
            if cell.value == True:
                nb = nb + 1
        
        return nb

    def next (self, grid):
        deadCells = []
        livingCells = [] 

        for line in grid.grid:
            for cell in line:
                cellLen = self.getNbLiveCells(cell.neighborCells)
                if (cellLen < 2):
                    deadCells.append(cell)
                elif (cellLen > 3):
                    deadCells.append(cell)
                elif (cellLen == 3):
                    livingCells.append(cell)

        for cell in deadCells:
            cell.value = False
        
        for cell in livingCells:
            cell.value = True            