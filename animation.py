import os
import time

class Animation:
    
    def __init__(self, iterations):
        self.iterations = iterations


    def animate(self, grid):
        for i in range(self.iterations):
            time.sleep(0.01)
            os.system("clear")
            grid.render()
            grid.next()
