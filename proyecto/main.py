#from cyglfw3 import *
#from OpenGL.GL import *
#
#glfw.Init()
#
#window = glfw.CreateWindow(640, 480, "Hello World", None, None)

import pygame
from OpenGL.GL import *
from random import randint
from GOL import GameOfLife, get_neighbours
import time



#Una célula tiene 8 vecinos. Para nosotros, una célula es un pixel, los vecinos son los 8 píxeles alrededor. 
#La célula puede estar viva (pintada de blanco, digamos) o muerta (pintada de negro). Pueden usar otros colores, pero esta es la idea.
#Cada "turno" va a ser un frame para nosotros. Pueden hacer un delay entre cada frame para poder mejor visualizar su animación.
#La resolución queda a su discreción, pero les recomiendo trabajar en una resolución muy baja, de como 100x100, y cuando terminen hacer algunas pruebas a resoluciones altas. 



WIDTH = 20#640
HEIGHT = 20#480
SCALE = 10


pygame.init()

screen = pygame.display.set_mode(
    (WIDTH*SCALE, HEIGHT*SCALE), 
    pygame.OPENGL | pygame.DOUBLEBUF
    )

x = 0
y = 0

glClearColor(1.0, 1.0, 1.0, 1.0)

#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#
#    pygame.display.update()
def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x*SCALE, y*SCALE, 1*SCALE, 1*SCALE)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)
    #if color == (1.0, 1.0, 1.0):
        #pygame.display.flip()
    


x = 0
speed = 1

def convert(color):
    return (color[0]/255, color[1]/255, color[2]/255)

#pixeles = []
#
#for t in range(250):
#    (i, j) = (randint(0, WIDTH), randint(0, HEIGHT))
#    pixeles.append((i, j, convert((randint(55, 255), randint(55, 255), randint(55, 255)))))


#for (i, j) in pixeles:



#GRID = [[]]
#for i in range(WIDTH):
#    for j in range(HEIGHT):
#        if randint(0,3) == 3:
#            GRID.append([i, j, (1.0, 1.0, 1.0)])
#        else:
#            GRID.append([i, j, (0.0, 0.0, 0.0)])
#        #GRID[i].append((i, j, (1.0, 1.0, 1.0)))


g = GameOfLife(WIDTH, HEIGHT)
#GameOfLife.get_neighbours
#print(g.get_grid())
GRID = g.get_grid()

#print(GRID)


#print(GRID)
running = True
while running:
#game of life
    color = [0, 0, 0]
    color = convert(color)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    FUTURE_GRID = g.get_old_grid()

    #determinar el futuro estado del gird y las células
    for i in range(WIDTH):
        for j in range(HEIGHT):
            temp = get_neighbours(i, j, GRID)
            if GRID[i][j] == 1:
                #color = [255, 255, 255]
                #time.sleep(0.5)
                #print("viva ->  ", temp, "  ", i, "  ", j)
                if temp < 2:
                    FUTURE_GRID[i][j] = 0
                elif temp > 3:
                    FUTURE_GRID[i][j] = 0
                else:
                    FUTURE_GRID[i][j] = 1
            else:
                #time.sleep(0.5)
                #print("muerta ->  ", temp, "  ", i, "  ", j)
                if temp == 3:
                    FUTURE_GRID[i][j] = 1
                else:
                    FUTURE_GRID[i][j] = 0
                color = [0, 0, 0]

    time.sleep(1)
    #Pintar el estado inicial del grid
    for i in range(WIDTH):
        for j in range(HEIGHT):
            #neighbours =g.get_neighbours(i, j)
            if GRID[i][j] == 1:
                color = [255, 255, 255]
            else:
                color = [0, 0, 0]
            color = convert(color)
            pixel(i, j, color)

    GRID = FUTURE_GRID
    #flip the screen
    pygame.display.flip()
    #Cambiar el estado del grid al futuro estado
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #running = False


#print(check_neighbors(0, 0))