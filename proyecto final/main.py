from cast import RayCaster
import pygame



SIZE  = 500

screen = pygame.display.set_mode((2*SIZE, SIZE))
r = RayCaster(screen, SIZE)
#clock = pygame.time.Clock()
r.load_map('./assets/map2.txt')

running = True
while running:
    press = pygame.key.get_pressed()
    #glClear(GL_COLOR_BUFFER_BIT)
    
    #screen.fill(BLACK)
    r.render()

    #pygame.time.delay(30)
    #pygame.time.wait(30)

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                r.move('forward')
            if event.key == pygame.K_s:
                r.move('backward')
            if event.key == pygame.K_a:
                r.move('left')
            if event.key == pygame.K_d:
                r.move('right')

            if event.key == pygame.K_LEFT:
                r.rotate('left')
            if event.key == pygame.K_RIGHT:
                r.rotate('right')
            
    #clock.tick(60)
    pygame.display.flip()