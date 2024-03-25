import pygame
from sys import exit
import math
from pygame.locals import *
#from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        img = (pygame.image.load("img/wizard.png").convert_alpha())
        self.image = pygame.transform.scale(img, (60, 80))
        self.position = (100,100)
        self.hitbox = self.image.get_rect(center = self.position)
        self.velx = 0
        self.vely = 0
        self.speed = 5

    def keybinds(self):
        self.velx = 0
        self.vely = 0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.vely = -self.speed
        if keys[pygame.K_DOWN]:
            self.vely = self.speed
        if keys[pygame.K_RIGHT]:
            self.velx = self.speed
        if keys[pygame.K_LEFT]:
            self.velx = -self.speed

    def move(self):
        self.position += pygame.math.Vector2(self.velx, self.vely)
        self.hitbox.center = self.position

    def updatePos(self):
        self.keybinds()
        self.move()


def draw_grid():
    tile_size = 50
    for line in range(0,24):
        pygame.draw.line(screen, (255, 255, 255), (0, line*tile_size), (1200, line*tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line*tile_size, 0), (line*tile_size, 700))


class Room:
    def __init__(self, data):
        self.tileList = []

        #load images
        wall_img = pygame.image.load('img/roomWalls.jpg')

        rcount = 0
        for row in data:
            ccount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (50, 50))
                    imgrect = img.get_rect()
                    imgrect.x = ccount * 50
                    imgrect.y = rcount * 50
                    tile = (img, imgrect)
                    self.tileList.append(tile)
                ccount += 1
            rcount += 1

    def draw(self):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])

    def get_tileList(self):
        return self.tileList

if __name__ == '__main__':
    pygame.init()

    #create window
    screen = pygame.display.set_mode((1200,700))
    pygame.display.set_caption("Goblet of Python")
    clock = pygame.time.Clock()

    #load images
    background = pygame.transform.scale(pygame.image.load("img/brickwallBG.png").convert(), (1200,700))

    p = Player()
    allsprites = pygame.sprite.Group()
    allsprites.add(p)

    room_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Row 1
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 2
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 3
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 4
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 5
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 6
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 7
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 8
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 9
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 10
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 11
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 12
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],  # Row 13
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]   # Row 14
]

    room = Room(room_data)

    list = room.get_tileList()

    while True:
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        screen.blit(background, (0,0))
        screen.blit(p.image, p.hitbox)
        room.draw()

        #draw_grid()

        p.updatePos()
        pygame.draw.rect(screen, "blue", p.hitbox, width=1)

        pygame.display.update()
        clock.tick(60)

