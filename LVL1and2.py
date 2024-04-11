import pygame
from pygame.locals import *

#first level character is a wizard
class Player():
    def __init__(self,x,y):
        self.reset(x,y)

    #method to allow player to move around and have consequences for collisions with
    #world and enemies
    def update(self, game_over):
        #variables to record change in x and y coordinates
        dx = 0
        dy = 0

        #if the player has not died or won...
        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE] or key[pygame.K_w]) and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if (key[pygame.K_SPACE] == False) or (key[pygame.K_w] == False):
                self.jumped = False
            if (key[pygame.K_LEFT] or key[pygame.K_a]):
                dx -= 5
                left = pygame.image.load('img/knight_left.png')
                self.image = pygame.transform.scale(left, (40, 80))
            if (key[pygame.K_RIGHT] or key[pygame.K_d]):
                dx += 5
                right = pygame.image.load('img/knighty.png')
                self.image = pygame.transform.scale(right, (40, 80))

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

            if pygame.sprite.spritecollide(self, dragon_group, False):
                game_over = -1

            #collision with cup
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1



            #update player cord.
            self.rect.x += dx
            self.rect.y += dy

        #if the player dies, change image to ghost and stop the game
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        #draw wizard
        screen.blit(self.image, self.rect)

        return game_over

    #reset character position and image if restart button is pressed
    def reset(self,x,y):
        img = pygame.image.load('img/knighty.png')
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


#first level world creation class
class World():
    def __init__(self,data):
        self.tile_list = []

        #load images
        dirt_img = pygame.image.load('img/stone.jpg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                #based on the tile number, place a certain image/enemy into that location on the board
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size,tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group.add(exit)
                if tile == 4:
                    dragon = Dragon(col_count * tile_size, row_count * tile_size)
                    dragon_group.add(dragon)
                col_count += 1
            row_count += 1

    #draw the world onto the screen
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0],tile[1])



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
        elif self.checker == -1:
            self.rect.x -= self.move_direction
            self.rect.y -= self.move_direction
            self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
            self.checker *= -1
        #boundary rectangle to show player where they cannot go
        pygame.draw.rect(screen, "white", self.rect, width=1)

#if the player reaches the trophy image, the world will change and they will exit to the next level
class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/trophy.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size*1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



'''NEW MAP CLASSES FOR LEVEL 2'''



#second level player image and rules for movement
class Player2():
    def __init__(self, x, y):
        self.reset(x,y)

    def update(self, game_over):
        #changes in x and y position depending on player input (keys pressed)
        dx = 0
        dy = 0

        if game_over == 0:
            #get pressed keys
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                dx -= 5
                right = pygame.image.load('img/scuba_right.png')
                self.img = pygame.transform.scale(right, (60, 70))
            if key[pygame.K_RIGHT]:
                dx += 5
                left = pygame.image.load('img/scuba_man.png')
                self.img = pygame.transform.scale(left, (60, 70))
            if key[pygame.K_SPACE] and self.jump == False:
                self.vely = -10
                self.jump = True
            if key[pygame.K_SPACE] == False:
                self.jump = False

            #make gravity
            self.vely += 1
            if self.vely > 3:
                self.vely = 3
            dy += self.vely

            #checking for collision
            for tile in world2.tileList:
                #x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if jumping
                    if self.vely < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vely = 0
                    #falling
                    elif self.vely >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vely = 0

            #check mermaid collision
            if pygame.sprite.spritecollide(self, mermaid_group, False):
                game_over = -1

            #check collision with second mermaid enemy group
            if pygame.sprite.spritecollide(self, exit_group2, False):
                game_over = 1

            #add x and y position changes to ending character location
            self.rect.x += dx
            self.rect.y += dy
            #pygame.draw.rect(screen, "white", self.rect, width=1)

        #if the game is over, change character image to ghost and stop the game
        elif game_over == -1:
            self.img = self.deadimg
            if self.rect.y > 100:
                self.rect.y -= 3

        #draw player onto the screen
        screen.blit(self.img, self.rect)
        return game_over

    #resets character position when restart button is pressed by user
    def reset(self, x, y):
        img = pygame.image.load('img/wizard.png')
        self.deadimg = pygame.transform.scale(pygame.image.load('img/ghost.png'), (40,70))
        self.img = pygame.transform.scale(img, (40, 70))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vely = 0
        self.jump = False
        self.width = self.img.get_width()
        self.height = self.img.get_height()



#second level world creation
class World2():
    def __init__(self, data):
        self.tileList = []

        #load image
        wall_img = pygame.image.load('img/underwaterWalls.jpg')

        rcount = 0
        for row in data:
            ccount = 0
            for tile in row:
                #places images in certain positions depending on numbers on the world board
                if tile == 1:
                    img = pygame.transform.scale(wall_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = ccount * tile_size
                    img_rect.y = rcount * tile_size
                    self.tileList.append((img, img_rect))
                if tile == 2:
                    mermaid = Mermaids1(ccount * tile_size, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 3:
                    mermaid = Mermaids2(ccount * tile_size, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 4:
                    mermaid = Mermaids3(ccount * tile_size+10, rcount * tile_size)
                    mermaid_group.add(mermaid)
                if tile == 5:
                    egg = Exit(ccount * tile_size, rcount * tile_size - (tile_size // 2))
                    exit_group2.add(egg)


                ccount += 1
            rcount += 1

    #draws world on screen
    def draw(self):
        for tile in self.tileList:
            screen.blit(tile[0], tile[1])

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





'''NEW MAP CLASSES FOR LEVEL 3'''



#third player corresponding to the third and final level of the game
class Player3():
    def __init__(self, x, y):
        self.reset(x,y)

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
            for tile in world3.tile_list:
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
            if pygame.sprite.spritecollide(self, exit_group3, False):
                game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        #if game is over/enemy collides with player, player image becomes ghost and game stops
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
            else:
                #place game over image on screen
                gameOverImg = pygame.image.load('img/gameover.jpg')
                gameOverImg = pygame.transform.scale(gameOverImg,(300,300))
                screen.blit(gameOverImg, (225,300))

        #if player3 reaches final trophy, display final winning image
        elif game_over == 1:
            winImg = pygame.image.load('img/youwin.jpg')
            winImg = pygame.transform.scale(winImg, (300, 300))
            screen.blit(winImg, (225, 250))



        #draw player onto screen
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255,255,255), self.rect, 2)

        return game_over

    #reset player3 position when restart button is pushed by user
    def reset(self, x, y):
        img = pygame.image.load('img/wizard.png')
        self.image = pygame.transform.scale(img, (40,80))
        dead_image = pygame.image.load('img/ghost.png')
        self.dead_image = pygame.transform.scale(dead_image, (40,80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False

#third and final world creation
class World3():
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
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/viktorkrum.png', (80,90), 'horiz')
                    bad_group.add(bad)
                if tile == 3:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size//2))
                    exit_group3.add(exit)
                if tile == 4:
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/vines.png', (50, 70), 'vert')
                    bad_group.add(bad)

                if tile == 5:
                    bad = Enemy2(col_count * tile_size, row_count * tile_size, 'img/spider.png', (50, 70), 'vertigo')
                    bad_group.add(bad)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            #takes picture and puts it in the location of rect coordinates
            screen.blit(tile[0], tile[1])
            #outlines all images -- helpful for logic
            #pygame.draw.rect(screen, (255,255,255), tile[1], 2)

#enemy class to create all enemies in level 3
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




#first screen the user sees--gives instructions on what to expect
#when space bar is pressed, user starts first level
#when restart is called, this class will allow user to return to opening screen
class Start:
    def __init__(self):
        pass

    #updates game over variable depending on if space bar is pressed by user
    def update(self, game_over):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_over = 1

        return game_over










if __name__ == '__main__':
    #initialize pygame
    pygame.init()

    clock = pygame.time.Clock()
    fps = 60

    #set screen dimensions
    screen_width = 750
    screen_height = 750

    #initialize main screen and caption
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Goblet of Python")

    # game variables
    tile_size = 50
    game_over = 0
    level = -1
    max_levels = 2

    # images to load in
    background_img1 = pygame.image.load('img/arena3.jpg')
    background_img2 = pygame.transform.scale(pygame.image.load('img/underwaterBG.jpg'), (750, 750))
    background_img3 = pygame.transform.scale(pygame.image.load('img/foggy_night.png'), (750, 750))
    restart_img = pygame.image.load('img/restart_img.png')


    #level creation in the form of 2d arrays, numbers represent what is placed in that position on screen
    LVL1 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    #world 2
    LVL2 = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 4, 0, 1],
        [1, 0, 3, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 4, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 5, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    #world 3
    LVL3 = [
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

    #first level player
    player = Player(100, screen_height - 400)


    exit_group = pygame.sprite.Group()
    exit_group2 = pygame.sprite.Group()
    dragon_group = pygame.sprite.Group()
    egg_group = pygame.sprite.Group()

    worlds = [LVL1, LVL2, LVL3]
    world = World(LVL1)

    mermaid_group = pygame.sprite.Group()
    world2= World2(LVL2)
    character = Player2(50, 600)

    bad_group = pygame.sprite.Group()
    exit_group3 = pygame.sprite.Group()
    world3 = World3(LVL3)
    player3 = Player3(100, screen_height - 130)

    start = Start()
    # restart_img = pygame.image.load('img/restart_img.png')
    from ButtonClass import Button
    restart_button = Button(100, 100, restart_img)


    run = True
    while run:
        clock.tick(fps)

        if level == -1:
            mono = pygame.image.load('img/mono2.png')
            screen.blit(background_img1, (0, 0))
            screen.blit(mono, (35,190))
            game_over = start.update(game_over)
            if game_over == 1:
                level += 1
                game_over = 0

        elif level == 0:
            screen.blit(background_img1, (0, 0))

            world.draw()

            if game_over == 0:
                dragon_group.update()

            dragon_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update(game_over)

            if game_over == 1:
                level += 1
                if level <= max_levels:
                    #worlds = []
                    #world = reset_level(level)
                    game_over = 0
                else:
                    winImg = pygame.image.load('img/youwin.jpg')
                    winImg = pygame.transform.scale(winImg, (300, 300))
                    screen.blit(winImg, (225, 250))

            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200)
                    game_over = 0

        elif level == 1:
            screen.blit(background_img2, (0, 0))

            world2.draw()

            if game_over == 0:
                mermaid_group.update()

            mermaid_group.draw(screen)
            exit_group2.draw(screen)

            game_over = character.update(game_over)

            if game_over == 1:
                level += 1
                game_over = 0

            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200)
                    character.reset(50, 600)
                    game_over = 0

        elif level == 2:
            screen.blit(background_img3, (0, 0))

            world3.draw()

            if game_over == 0:
                bad_group.update()

            bad_group.draw(screen)
            exit_group3.draw(screen)

            game_over = player3.update(game_over)

            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200)
                    character.reset(50, 600)
                    player3.reset(100, screen_height - 130)
                    game_over = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
