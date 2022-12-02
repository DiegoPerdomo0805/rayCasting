import pygame
from OpenGL.GL import *
import random
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT_1 = (0, 0, 0, 0)
TRANSPARENT_2 = (255, 255, 255, 255)
SKY = (255, 0, 0)
Khorne = (153, 0, 0)
Nurgle = (0, 153, 0)
Slaanesh = (0, 0, 153)
Tzeentch = (153, 153, 0)

walls = {
    "1": pygame.image.load("./assets/Giygas.jpg"),
    "2": pygame.image.load("./assets/daemons-of-slaanesh.png"),
    "3": pygame.image.load("./assets/nurgle.jpg"),
    #"2": pygame.image.load("assets/wall2.png"),
}

demons = [
    {
        "x": 100,
        "y": 200,
        "texture": pygame.image.load("./assets/Afrit.png")
    },
    {
        "x": 200,
        "y": 200,
        "texture": pygame.image.load("./assets/Afrit.png")
    },
    {
        "x": 300,
        "y": 200,
        "texture": pygame.image.load("./assets/Afrit.png")
    },
    {
        "x": 400,
        "y": 200,
        "texture": pygame.image.load("./assets/Afrit.png")
    },
]




class RayCaster(object):
    def __init__(self, screen, size):
        pygame.init()
        self.size = size
        self.screen = screen#pygame.display.set_mode(screen)
        _, _, self.width, self.height = screen.get_rect()
        self.blocksize = size // 10
        self.map = []
        self.player = {
            'x': 100,
            'y': 100,
            'angle': math.pi / 3,
            'fov': math.pi / 3
        }
        self.zbuffer = [-float('inf') for z in range(self.width)]
        self.clear()
        #self.zbuffer = [-float('inf') for z in range(0, self.width, 2)]
        #self.clear()

    def clear(self):
        for x in range(self.width):
            for y in range(self.height):
                self.point(x, y, BLACK)

    def point(self, x, y, c = WHITE):
        #print(x, y, c)
        #self.screen.set_at((x, y), c)
        self.screen.set_at((x, y), c)

    def draw_rectangle(self, x, y, texture):
        for i in range(x, x + self.blocksize+1):
            for j in range(y, y + self.blocksize+1):
                #self.point(i, j, texture)
                tx = (i - x) * 256 // self.blocksize
                ty = (j - y) * 256 // self.blocksize
                c = texture.get_at((tx, ty))
                self.point(i, j, c)

    def load_map(self, filename):
        with open(filename) as f:
            for line in f.readlines():
                self.map.append(list(line))


    def draw_stake(self, x, height, texture, texx = 0):
        #print("draw_stake")
        #print(x, height, texture, offset)
        start = int(self.height // 2 - height // 2)
        end   = int(self.height // 2 + height // 2)
        for y in range(start, end):
            #print(x, y)
            ty = (y - start) * 256 // height
            ty = int(ty)
            #print(ty)
            c = texture.get_at((texx, ty))
            self.point(x, y, c)


    def draw_enemy(self, enemy):
        ex = enemy['x'] - self.player['x']
        ey = enemy['y'] - self.player['y']
        #print(ex, ey)
        angle = math.atan2(ey, ex) - self.player['angle']

        dist = (ex * ex + ey * ey)**0.5

        e_size = (self.size // dist) * 100

        x = self.size + (self.size // 2 - e_size // 2) + (angle - self.player['angle'])*self.size / self.player['fov']
        y = self.height // 2 - e_size // 2

        x, y, e_size = int(x), int(y), int(e_size)

        for i in range(x, x + e_size):
            for j in range(y, y + e_size):
                if i < 0 or i >= self.width or j < 0 or j >= self.height:
                    continue
                tx = (i - x) * 256 // e_size
                ty = (j - y) * 256 // e_size
                c = enemy['texture'].get_at((tx, ty))
                if c != TRANSPARENT_1 and c != TRANSPARENT_2:
                    self.point(i, j, c)
                #self.point(i, j, c)
        #print(angle)
        #if angle < -math.pi:
        #    angle += 2 * math.pi
        #if angle > math.pi:
        #    angle -= 2 * math.pi
        ##print(angle)
        #if angle > -self.player['fov'] / 2 and angle < self.player['fov'] / 2:
        #    dist = (ex * ex + ey * ey)**0.5
        #    #print(dist)
        #    if dist < self.zbuffer[int(self.width // 2 + angle * self.width // self.player['fov'])]:
                

    

    def cast_ray(self, a):
        d  = 0
        while True:
            x = self.player['x'] + d * math.cos(a)
            y = self.player['y'] + d * math.sin(a)
            #print(x, y)
            #print(self.map[int(y // self.blocksize)][int(x // self.blocksize)])
            if self.map[int(y // self.blocksize)][int(x // self.blocksize)] != ' ':
                hitx = x - int(x // self.blocksize) * self.blocksize
                hity = y - int(y // self.blocksize) * self.blocksize
                maxhit = max(hitx, hity)
                texx = int(256 * (maxhit - hitx) if hitx > hity else 256 * (maxhit - hity))
                return d, self.map[int(y // self.blocksize)][int(x // self.blocksize)], texx
            d += 1

    def render(self):
        self.clear()
        #print(self.map)
        #print(self.size)

        #print(self.map[0][10])
        for x in range(0, self.size, self.blocksize):
            for y in range(0, self.size, self.blocksize):
                #print(self.map)
                #print(x, y)
                #print((x//self.blocksize)-1, (y// self.blocksize)-1)
                if self.map[(x//self.blocksize)][(y// self.blocksize)] != ' ':
                    #print("draw_rectangle", self.map[(x//self.blocksize)-1][(y// self.blocksize)-1])
                    #self.draw_rectangle(x, y, walls[self.map[y // self.blocksize][x // self.blocksize]])
                    #print(x, y, self.map[(x//self.blocksize)][(y// self.blocksize)])
                    self.draw_rectangle(x, y, walls[self.map[(x//self.blocksize)][(y// self.blocksize)]])
                    #self.draw_rectangle(x, y, walls[self.map[y // self.blocksize][x // self.blocksize]])
        self.point(self.player['x'], self.player['y'], WHITE)

        for e in range(1, self.size):
            a = self.player['angle'] - self.player['fov'] / 2 + self.player['fov'] * e / self.size
            d, c, texx = self.cast_ray(a)
            #print(d, m)
            x_v = self.size + e
            h = self.blocksize * self.size / d
            #print(x_v, h)
            self.draw_stake(x_v, h, walls[c], texx)


        #for demon in demons:
        #    self.draw_enemy(demon)


    def move(self, dir):
        if dir == 'right':
            print(int(10 * math.cos(self.player['angle'])))
            self.player['x'] += int(10 * math.cos(self.player['angle']))
        elif dir == 'forward':
            self.player['y'] += int(10 * math.sin(self.player['angle']))
        elif dir == 'left':
            self.player['x'] -= int(10 * math.cos(self.player['angle']))
        elif dir == 'backward':
            self.player['y'] -= int(10 * math.sin(self.player['angle']))


    def rotate(self, dir):
        if dir == 'left':
            self.player['angle'] -= math.pi / 180 * 10
        elif dir == 'right':
            self.player['angle'] += math.pi / 180 * 10
        #print('---------------------------------------------------------------------------------')
        #pygame.display.flip()

    





#pygame.init()

