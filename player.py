
import pygame
from pygame.locals import *
from ButtonClass import Button

# dragon_group = pygame.sprite.Group()
# mermaid_group = pygame.sprite.Group()
# bad_group = pygame.sprite.Group()
# exit_group = pygame.sprite.Group()
# exit_group2 = pygame.sprite.Group()
# exit_group3 = pygame.sprite.Group()
screen = pygame.display.set_mode((750, 750))

#Player class, there are three objects each representing the player at the three levels
class Player():
    def __init__(self,x,y,img,scale,world,dragon_group,exit_group):
        self.reset(x,y,img,scale)
        self.world = world
        self.dragon_group = dragon_group
        self.exit_group = exit_group

    #method to allow player to move around and have consequences for collisions with
    #world and enemies
    def update1(self, game_over):
        #variables to record change in x and y coordinates
        dx = 0
        dy = 0

        #if the player has not died or won...
        if game_over == 0:
            #get keypresses
            key = pygame.key.get_pressed()
            #space bar used to jump--temporarily changes y-pos of player, can only be pressed once before gravity
            if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) and self.jumped == False and self.in_air == False:
                self.vel_y = -15
                self.jumped = True
            if (key[pygame.K_SPACE] == False) or (key[pygame.K_w] == False) or (key[pygame.K_UP] == False):
                self.jumped = False
            #image to move left and right changes so player avatar is facing the right way
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
            for tile in self.world.tile_list:
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
            if pygame.sprite.spritecollide(self, self.dragon_group, False):
                game_over = -1

            #collision with cup
            if pygame.sprite.spritecollide(self, self.exit_group, False):
                game_over = 1

            #update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        #if the player dies, change image to ghost that floats upward and stop the game
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5

        #draw wizard for each update based on changes in x and y
        screen.blit(self.image, self.rect)

        return game_over

    #player move rules for level 2 (player can jump infinitely upward but slowly to simulate
    #water environment
    def update2(self, game_over):
        #changes in x and y position depending on player input (keys pressed)
        dx = 0
        dy = 0

        if game_over == 0:
            #get pressed keys
            key = pygame.key.get_pressed()
            #player avatar image changes to face where the user is directing them with arrow keys
            if (key[pygame.K_LEFT] or key[pygame.K_a]):
                dx -= 5
                right = pygame.image.load('img/scuba_right.png')
                self.image = pygame.transform.scale(right, (40, 70))
            if (key[pygame.K_RIGHT] or key[pygame.K_d]):
                dx += 5
                left = pygame.image.load('img/scuba_man.png')
                self.image = pygame.transform.scale(left, (40, 70))
            #player can jump infititely vertical
            if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) and self.jumped == False:
                self.vel_y = -10
                self.jumped = True
            if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) == False:
                self.jumped = False

            #make gravity (heavier for lvl 2)
            self.vel_y += 1
            if self.vel_y > 3:
                self.vel_y = 3
            dy += self.vel_y

            #checking for collision
            for tile in self.world.tileList:
                #x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0

            #check mermaid collision
            if pygame.sprite.spritecollide(self, self.dragon_group, False):
                game_over = -1

            #check collision with second mermaid enemy group
            if pygame.sprite.spritecollide(self, self.exit_group, False):
                game_over = 1

            #add x and y position changes to ending player location
            self.rect.x += dx
            self.rect.y += dy
            #pygame.draw.rect(screen, "white", self.rect, width=1)

        #if the game is over, change player image to ghost and stop the game
        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 100:
                self.rect.y -= 3

        #draw player onto the screen
        screen.blit(self.image, self.rect)

        return game_over

    #rules for level 3 player movement
    def update3(self, game_over):
        #calculate new player position
        #check collision at new position
        #adjust player position

        if game_over == 0:
            #dx and dy represent the change in the x and y variables (start and end position)
            dx = 0
            dy = 0

            #get keypresses
            key = pygame.key.get_pressed()
            if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) and self.jumped == False:
                self.vel_y = -15
                self.jumped = True
            #set jumped back to false
            if (key[pygame.K_SPACE] or key[pygame.K_w] or key[pygame.K_UP]) == False:
                self.jumped = False
            if (key[pygame.K_LEFT] or key[pygame.K_a]):
                dx -= 5
            if (key[pygame.K_RIGHT] or key[pygame.K_d]):
                dx += 5

            #add gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            #check for collision
            for tile in self.world.tile_list:
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
            if pygame.sprite.spritecollide(self, self.dragon_group, False):
                game_over = -1
            #if player wins and collides with object of exit class, game is finished
            if pygame.sprite.spritecollide(self, self.exit_group, False):
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


    #reset player position, image, and scale if restart button is pressed
    #applicable for players at all 3 levels
    def reset(self,x,y, img, scale):
        dead_image = pygame.image.load('img/ghost.png')
        self.image = pygame.transform.scale(img, scale)
        self.dead_image = pygame.transform.scale(dead_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.in_air = True

