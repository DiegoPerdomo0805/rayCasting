from copy import deepcopy
from random import randint

class GameOfLife:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = self.create_grid()
        self.configure_cells()
    
    def create_grid(self):
        return [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    
    def configure_cells(self):
        #self.grid[9][10] = 1
        ##self.grid[10+0][10+0] = 1
        ##self.grid[10+0][10+1] = 1
        ##self.grid[10+1][10+0] = 1
        #self.grid[10+1][10+1] = 1
        #self.grid[80][80] = 1
        #self.grid[80][81] = 1
        #self.grid[81][81] = 1
        #self.grid[81][80] = 1
        for i in range(self.rows):
            for j in range(self.cols):
                if randint(0,6) == 6:
                    self.grid[i][j] = 1
    
    #def get_neighbours(self, row, col):
        #neighbours = 0

        #for i in range(row-1, row+1):
         #   for j in range(col-1, col+1):
          #      if i == 0 and j == 0:
           #         continue
            #    if i >= 0 and i < self.rows and j >= 0 and j < self.cols:
             #       #if i != row or j != col:
              #      if self.grid[i][j] == 1:
               #         neighbours += 1
                        #print(neighbours)
                    #neighbours.append(self.grid[i][j])
        #print(neighbours if neighbours > 0)
        #if neighbours > 0:
         #   print(neighbours)
        #return neighbours

    def get_grid(self):
        return self.grid

    def get_old_grid(self):
        return deepcopy(self.grid)

def get_neighbours(row, col, grid):
    neighbors = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if i == row and j == col:
                continue
            elif i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]):
                if grid[i][j] == 1:
                    #print('i: ', i, 'j: ', j)
                    neighbors += 1
    return neighbors