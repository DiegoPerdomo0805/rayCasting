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
        self.grid[20][20] = 1
        self.grid[20][21] = 1
        self.grid[21][21] = 1
        self.grid[21][20] = 1
        #self.grid[80][80] = 1
        #self.grid[80][81] = 1
        #self.grid[81][81] = 1
        #self.grid[81][80] = 1
        #for i in range(self.rows):
        #    for j in range(self.cols):
        #        if randint(0,6) == 6:
        #            self.grid[i][j] = 1
    
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

def get_neighbors(grid):
    neighbors = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            neighbors.append((i, j, grid[i][j]))
    return neighbors
