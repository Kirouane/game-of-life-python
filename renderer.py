class Renderer:

    def render(self, grid):
        for line in grid.grid:
            for cell in line:
                if (cell.value == True):
                    print('██', end='')
                else:
                    print('  ', end='')
                
            print('')
