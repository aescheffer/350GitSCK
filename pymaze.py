import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 750
screen_height = 750

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Trying my best')

tile_size = 50
game_over = 0


#load images
#have to be drawn in order, otherwise the later stuff will be on top of earlier stuff and you wont see it
# sun_img = pygame.image.load('img/sunn.png')
# sun_img = pygame.transform.scale(sun_img, (160, 120))
bg_img = pygame.image.load('img/foggy_night.png')
bg_img = pygame.transform.scale(bg_img, (750,750))

class Player():
    def __init__(self, x, y):
        img = pygame.image.load('img/wizard.png')
        self.image = pygame.transform.scale(img, (40,80))
        dead_image = pygame.image.load('img/ghost.png')
        self.dead_image = pygame.transform.scale(dead_image, (40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        #y velocity
        self.vel_y = 0
        self.jumped = False

    def update(self, game_over):
        #calculate new player position
        #check collision at new position
        #adjust player position

        if game_over == 0:
            #dx and dy represent the change in the x and y variables (start and end position)
            dx = 0
            dy = 0


            #get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            #set jumped back to false
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_LEFT]:
                dx -= 5
            if key[pygame.K_RIGHT]:
                dx += 5

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground (player is jumping)
                    if self.vel_y < 0:
                        #player will move until he bumps his head
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    elif self.vel_y >= 0:
                        #player will move until he falls
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
            #check for collision with enemies
            if pygame.sprite.spritecollide(self, bad_group, False):
                game_over = -1
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

            #update player coordinates
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


        elif game_over == 1:
            winImg = pygame.image.load('img/youwin.jpg')
            winImg = pygame.transform.scale(winImg, (300, 300))
            screen.blit(winImg, (225, 250))



        #draw player onto screen
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255,255,255), self.rect, 2)

        return game_over


class World():
    def __init__(self, data):
        self.tile_list = []
        #load images
        dirt_img = pygame.image.load('img/hedges.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                #create dirt
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    bad = Enemy(col_count * tile_size, row_count * tile_size, 'img/viktorkrum.png', (80,90), 'horiz')
                    bad_group.add(bad)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group.add(exit)
                if tile == 4:
                    bad = Enemy(col_count * tile_size, row_count * tile_size, 'img/vines.png', (50, 70), 'vert')
                    bad_group.add(bad)

                if tile == 5:
                    bad = Enemy(col_count * tile_size, row_count * tile_size, 'img/spider.png', (50, 70), 'vertigo')
                    bad_group.add(bad)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            #takes picture and puts it in the location of rect coordinates
            screen.blit(tile[0], tile[1])
            #outlines all images -- helpful for logic
            #pygame.draw.rect(screen, (255,255,255), tile[1], 2)


class Enemy(pygame.sprite.Sprite):
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
        if self.vert_or_horiz == 'horiz':
            self.rect.x += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 30:
                self.move_direction *= -1
                self.move_counter *= -1
        elif self.vert_or_horiz == 'vert':
            self.rect.y += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 30:
                self.move_direction *= -1
                self.move_counter *= -1
        else:
            self.rect.y += self.move_direction
            self.move_counter += 1
            if abs(self.move_counter) > 150:
                self.move_direction *= -1
                self.move_counter *= -1

class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/trophy.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size*1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y





world_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 4, 4, 4, 4, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 5, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 1, 0, 2, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


player = Player(100, screen_height - 130)
bad_group = pygame.sprite.Group()

exit_group = pygame.sprite.Group()

world = World(world_data)

run = True
while run:
    clock.tick(fps)
    #fills top right of screen hence 0,0
    screen.blit(bg_img, (0,0))
    #screen.blit(sun_img, (100,100))

    world.draw()

    if game_over == 0:
        bad_group.update()

    bad_group.draw(screen)
    exit_group.draw(screen)

    game_over = player.update(game_over)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #tells pygame to update display window with all instructions earlier in run loop
    pygame.display.update()

pygame.quit()
