from cell import Cell
from evolution import Evolution
class Grid:
    
    def __init__(self, dim, renderer, animation):
        self.dim = dim
        self.renderer = renderer
        self.animation = animation
        self.evolution = Evolution()
        self.grid = [ [ None for y in range(dim) ] for x in range(dim) ]
        for i in range(dim):
            for j in range(dim):
                self.grid[i][j] = Cell(i, j)

        for i in range(dim):
            for j in range(dim):
                cell = self.grid[i][j]
                
                cell.addNeighbor(self.grid[i-1][j] if i-1 >=0 else None)
                cell.addNeighbor(self.grid[i+1][j] if i+1 < dim else None)
                cell.addNeighbor(self.grid[i][j-1] if j-1 >=0 else None)
                cell.addNeighbor(self.grid[i][j+1] if j+1 < dim else None)
                cell.addNeighbor(self.grid[i-1][j-1] if i-1 >=0 and j-1 >=0 else None)
                cell.addNeighbor(self.grid[i-1][j+1] if i-1 >=0 and j+1 < dim else None)
                cell.addNeighbor(self.grid[i+1][j-1] if i+1 < dim and j-1 >=0 else None)
                cell.addNeighbor(self.grid[i+1][j+1] if i+1 < dim and j+1 < dim else None)
                

    def alive(self, i, j):
        self.grid[i][j].value = True
        return self

    def render(self):
        self.renderer.render(self)

    def animate(self):
        self.animation.animate(self)

    def next(self):
        self.evolution.next(self)
