import pygame
from pygame.locals import *
from ButtonClass import Button

# dragon_group = pygame.sprite.Group()
# mermaid_group = pygame.sprite.Group()
# bad_group = pygame.sprite.Group()


#dictates how the Dragon enemy moves--will end game if player and dragon collide
class Dragon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        #initializes dragon image and location
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/dragon.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 5
        self.move_counter = 0

    #updates dragon position
    def update(self):
        self.checker = 1
        if self.checker == 1:
            self.rect.x += self.move_direction
            self.rect.y += self.move_direction
            self.move_counter += 1

        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
            self.checker *= -1
        #boundary rectangle to show player where they cannot go
        #pygame.draw.rect(screen, "white", self.rect, width=1)


#first enemy group that will cause game over for player2
class Mermaids1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/mermaid.png')
        self.image = pygame.transform.scale(self.image, (30,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 5
        self.count = 0
    #updates position so mermaids don't stay in the same place
    def update(self):
        self.rect.y -= self.dir
        self.count += 1
        if self.count > 20:
            self.dir *= -1
            self.count = -20


#second group of enemy mermaids
class Mermaids2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/mermaid.png')
        self.image = pygame.transform.scale(self.image, (30,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 2
        self.count = 0

    def update(self):
        self.rect.y -= self.dir
        self.count += 1
        if self.count > 25:
            self.dir *= -1
            self.count = -25

#third group of enemy mermaids. rules the same as previous two
class Mermaids3(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/mermaid.png')
        self.image = pygame.transform.scale(self.image, (30,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dir = 1
        self.count = 0

    def update(self):
        self.rect.x -= self.dir
        self.count += 1
        if self.count > 50:
            self.dir *= -1
            self.count = -50
        #pygame.draw.rect(screen, "white", self.rect, width=1)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y, image, dimensions, vert_or_horiz):
        pygame.sprite.Sprite.__init__(self)
        self.vert_or_horiz = vert_or_horiz
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, dimensions)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    #make the bad guys move around left and right
    def update(self):
        #if the object is called with 'horiz', enemy will move horizontally (range 30)
        if self.vert_or_horiz == 'horiz':
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 30:
                self.move_direction *= -1
                self.move_counter *= -1
        #enemy will move vertically (range 30)
        elif self.vert_or_horiz == 'vert':
            self.rect.y += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 30:
                self.move_direction *= -1
                self.move_counter *= -1
        #enemy will move vertically with a range of 150
        else:
            self.rect.y += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 150:
                self.move_direction *= -1
                self.move_counter *= -1

