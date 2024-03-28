import pygame
from pygame.locals import *


pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width=750
screen_height=750

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Battle Voldemort")

#game variables
tile_size = 50
game_over = 0
level = 0
max_levels = 1

#images
sun_img = pygame.image.load('img/sunn.png')
background_img = pygame.image.load('img/skyy.png')

def reset_level(level):
    player.reset(100, screen_height-100)
    dementor_group.empty()
    dragon_group.empty()
    exit_group.empty()
    worlds = [world_data, world_data2]
    world = World(worlds[level])
    return world

class Player():
    def __init__(self,x,y):
        img = pygame.image.load('img/wizard.png')
        dead_image = pygame.image.load('img/ghost.png')
        self.image = pygame.transform.scale(img, (40,80))
        self.dead_image = pygame.transform.scale(dead_image, (40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True
    def update(self, game_over):

        dx = 0
        dy = 0

        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
            if key[pygame.K_RIGHT]:
                dx += 5

            #add gravity
            self.vel_y += 1
            if self.vel_y >10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            self.in_air = True
            for tile in world.tile_list:
                #check for coll in x
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground (jumping)
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    # check if above the ground (falling)
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            #check for collision with enemies
            if pygame.sprite.spritecollide(self, dementor_group, False):
                game_over = -1

            if pygame.sprite.spritecollide(self, dragon_group, False):
                game_over = -1

            #collision with cup
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1



            #update player cord.
            self.rect.x += dx
            self.rect.y += dy

        # if self.rect.bottom > screen_height:
        #     self.rect.bottom = screen_height
        #     dy = 0

        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
            else:
                gameOverImg = pygame.image.load('img/gameover.jpg')
                gameOverImg = pygame.transform.scale(gameOverImg,(300,300))
                screen.blit(gameOverImg, (225,300))


        # elif game_over == 1:
        #     winImg = pygame.image.load('img/youwin.jpg')
        #     winImg = pygame.transform.scale(winImg, (300, 300))
        #     screen.blit(winImg, (225, 250))

        #draw wizard
        screen.blit(self.image, self.rect)

        return game_over

    def reset(self,x,y):
        img = pygame.image.load('img/wizard.png')
        dead_image = pygame.image.load('img/ghost.png')
        self.image = pygame.transform.scale(img, (40, 80))
        self.dead_image = pygame.transform.scale(dead_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True


class World():
    def __init__(self,data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('img/dirt.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    dementor = Enemy(col_count * tile_size, row_count * tile_size)
                    dementor_group.add(dementor)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group.add(exit)
                if tile == 4:
                    dragon = Dragon(col_count * tile_size, row_count * tile_size)
                    dragon_group.add(dragon)
                if tile == 5:
                    egg = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    egg_group.add(egg)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/dementor.png')
        self.image = pygame.transform.scale(self.image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1

class Dragon(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/dragon.png')
        self.image = pygame.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 5
        self.move_counter = 0

    def update(self):
        self.checker = 1
        if self.checker == 1:
            self.rect.x += self.move_direction
            self.rect.y += self.move_direction
            self.move_counter += 1
        elif self.checker == -1:
            self.rect.x -= self.move_direction
            self.rect.y -= self.move_direction
            self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
            self.checker *= -1

class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/trophy.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size*1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Egg(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/egg.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size*1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

world_data = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,1,0,1,0,0,0,4,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

world_data2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,3,0,0],
    [1,0,0,0,0,0,0,2,0,0,0,0,1,0,0],
    [1,0,0,0,0,1,1,1,1,1,1,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,0,1,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,1,1,1,1,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,1,0,0,0,0,0,0,0,3,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


player = Player(100, screen_height - 400)

dementor_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
dragon_group = pygame.sprite.Group()
egg_group = pygame.sprite.Group()

worlds = [world_data, world_data2]
world = World(worlds[level])
#world2= World(world_data2)

run = True
while run:

    clock.tick(fps)
    screen.blit(background_img,(0,0))
    screen.blit(sun_img, (-500, -500))

    world.draw()

    if game_over == 0:
        dragon_group.update()
        dementor_group.update()



    dementor_group.draw(screen)
    dragon_group.draw(screen)
    exit_group.draw(screen)

    game_over = player.update(game_over)

    if game_over == 1:
        level += 1
        if level <= max_levels:
            worlds = []
            world = reset_level(level)
            game_over = 0
        else:
            winImg = pygame.image.load('img/youwin.jpg')
            winImg = pygame.transform.scale(winImg, (300, 300))
            screen.blit(winImg, (225, 250))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
