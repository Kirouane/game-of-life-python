from grid import Grid
from renderer import Renderer
from animation import Animation

grid = Grid(60, Renderer(), Animation(100))
grid.alive(30, 30).alive(31, 30).alive(32, 30).alive(33, 31).alive(30, 31).alive(31, 31).alive(31, 33).alive(33, 33)
#grid.alive(20, 20).alive(20, 21).alive(20, 22).alive(20, 23).alive(20, 24)
grid.animate()