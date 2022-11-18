import pygame
from OpenGL.GL import *
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
SKY = (255, 0, 0)
GROUND = (200, 200, 100)

walls = {
    "1": pygame.image.load("assets/wall1.png"),
    "2": pygame.image.load("assets/wall2.png"),
}

#sprite1 = pygame.image.load("assets/sprite1.png")
#sprite2 = pygame.image.load("assets/sprite2.png")
#sprite2 = pygame.image.load("sprite2.png")
#sprite3 = pygame.image.load("sprite3.png")
#sprite4 = pygame.image.load("sprite4.png")

#enemies = [
#    {
#        'x': 100,
#        'y': 100,
#        'sprite': sprite1
#        #'speed': 1,
#        #'direction': 'right'
#    }, 
#    {
#        'x': 200,
#        'y': 200,
#        'sprite': sprite1
#    }
#]


class RayCaster(object):
    def __init__(self, screen):
        pygame.init()
        self.screen = pygame.display.set_mode(screen)
        _, _, self.width, self.height = screen.get_rect()
        self.blocksize = 50
        self.map = []
        self.player = {
            'x': 100,
            'y': 100,
            'angle': 0,
            'fov': math.pi / 3
        }
        #self.zbuffer = [-float('inf') for z in range(0, self.width, 2)]
        #self.clear()

    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                self.point(x, y, BLACK)

    def point(self, x, y, c = WHITE):
        self.screen.set_at((x, y), c)

    def block(self, x, y, c = WHITE):
        for i in range(x, x + self.blocksize):
            for j in range(y, y + self.blocksize):
                self.point(i, j, c)
        #pygame.draw.rect(self.screen, c, (x, y, self.blocksize, self.blocksize), 1)

    def load_map(self, path):
        with open(path) as f:
            self.map = [line.strip() for line in f]

    def draw_map(self):
        for x in range(len(self.map)):
            for y in range(self.map[x].__len__()):
                wall = self.map[x][y]
                self.block(y * self.blocksize, x * self.blocksize, walls[wall])
                #if self.map[y // self.blocksize][x // self.blocksize] == ' ':
                #    self.block(x, y, BLACK)
        #for i, line in enumerate(self.map):
        #    for j, c in enumerate(line):
        #        if c == '1':
        #            self.block(j * self.blocksize, i * self.blocksize)

    #def draw_sprite(self, sprite):
    #    sprite_a = math.atan2((sprite['y'] - self.player['y']), (sprite['x'] - self.player['x']))
#
    #    sprite_size = int((500 / d) * 40)#el 40 es un valor que se puede cambiar para cambiar el tamaño de los sprites
#
    #    sprite_x = int(500 + (sprite_a - self.player['angle']) * 500 / self.player['fov'] + sprite_size / 2)
    #    sprite_y = int(500/2 - sprite_size / 2)
    #    
    #    d = ((self.player[x] - sprite[x]) ** 2 + (self.player[y] - sprite[y]) ** 2) ** 0.5
    #    
    #    
    #    
    #    for x in range(sprite_x, sprite_x + sprite_size):
    #        for y in range(sprite_y, sprite_y + sprite_size):
    #            tx = int((x - sprite_x ) * 128/sprite_size)  #sprite['x'] + x - sprite_x
    #            ty = int((y - sprite_y)  * 128/sprite_size)   #sprite['y'] - player.y + sprite_size / 2
    #            c = sprite['sprite'].get_at((tx, ty))
    #            if c != TRANSPARENT:
    #                self.point(x, y, c)
    #            #self.point(x, y, sprite)
    #    #height = min(600, max(0, 600 / y))
    #    #top = 300 - height // 2
    #    #bottom = 300 + height // 2
    #    #for i in range(top, bottom):
    #    #    self.point(x, i, sprite)

    def draw_player(self):
        self.block(self.player['x'], self.player['y'], WHITE)

    

    def cast_ray(self, a):
        d = 0
        while True:
            x = self.player['x'] + d * math.cos(a)
            y = self.player['y'] + d * math.sin(a)
            i = int(y // self.blocksize)
            j = int(x // self.blocksize)
            if self.map[i][j] != ' ':
                hitx = x - j * self.blocksize
                hity = y - i * self.blocksize
                maxhit = self.blocksize * math.sqrt(2)
                if hitx > hity:
                    offset = maxhit - hitx
                else:
                    offset = maxhit - hity
                return d + offset, self.map[i][j]
            self.point(x, y)
            d += 1

    def drawStake(self, x, h, c):
        for y in range(h):
            self.point(x, y, c)
    
    def move(self, direction, speed=7):
        if direction == 'forward':
            self.player['x'] += int(speed * math.cos(self.player['angle']))
            self.player['y'] += int(speed * math.sin(self.player['angle']))
        elif direction == 'backward':
            self.player['x'] -= int(speed * math.cos(self.player['angle']))
            self.player['y'] -= int(speed * math.sin(self.player['angle']))
        elif direction == 'right':
            self.player['angle'] += 0.1
        elif direction == 'left':
            self.player['angle'] -= 0.1
        
    #def cast_ray(self, x, y, angle):
    #    for i in range(1000):
    #        dx = math.cos(angle) * i
    #        dy = math.sin(angle) * i
    #        ix = i|nt(x + dx)
    #        iy = int(y + dy)
    #        try:
    #            if self.map[iy // self.blocksize][ix // self.blocksize] == '1':
    #                return i
    #        except IndexError:
    #            return i
    #    return i

    #def render(self, player):
    #    self.screen.fill(BLACK)
    #    self.draw_map()
    #    for enemy in enemies:
    #        self.screen.blit(sprite1, (enemy['x'], enemy['y']))
    #    self.screen.blit(player.surf, (player.x, player.y))
    #    pygame.display.flip()
#
    #    for i in range(0, self.width, 2):
    #        angle = player.angle - player.fov / 2 + (i / self.width) * player.fov
    #        #distance = self.cast_ray(player.x, player.y, angle)
    #        d, c, tx = self.cast_ray(player.x, player.y, angle)
    #        self.draw_stripe(i, distance)
    #    
    #    for enemy in enemies:
    #        self.draw_sprite(enemy)



#pygame.init()
screen = (800, 600)
r = RayCaster(screen)
#clock = pygame.time.Clock()
r.load_map('map.txt')

running = True
while running:
    
    screen.fill(BLACK)
    r.draw_map()
    pygame.display.flip()
    #clock.tick(60)