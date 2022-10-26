#from cyglfw3 import *
#from OpenGL.GL import *
#
#glfw.Init()
#
#window = glfw.CreateWindow(640, 480, "Hello World", None, None)

import pygame
from OpenGL.GL import *



pygame.init()

screen = pygame.display.set_mode(
    (640, 480), 
    pygame.OPENGL | pygame.DOUBLEBUF
    )

x = 10
y = 40

glClearColor(0.0, 1.0, 0.0, 1.0)

#while True:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            pygame.quit()
#
#    pygame.display.update()
def pixel(x, y, color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(x, y, 10, 10)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

x = 0
speed = 1

def convert(color):
    return (color[0]/255, color[1]/255, color[2]/255)



running = True
while running:
    #clean the screen
    #glClearColor(0.1, 0.8, 0.0, 1.0)
    color = [255, 0, 0]
    color = convert(color)
    glClearColor(color[0], color[1], color[2], 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    #draw
    pixel(x, y, (0.0, 0.0, 1.0))

    x += speed

    if x > 640:
        speed = -1
    elif x < 0:
        speed = 1
    

    #screen.set_at((x, y), (255, 255, 255))
    #x += 1
    #y += 1

    #pygame.display.update()
    
    #flip the screen
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False