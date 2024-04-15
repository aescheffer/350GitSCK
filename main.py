import pygame
from pygame.locals import *
from ButtonClass import Button

from enemy import *
from world import *
from player import *
from ButtonClass import *


def main():
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

    # images to load in...
    #player images
    img1 = pygame.image.load('img/knighty.png')
    scale1 = (40,80)
    img2 = pygame.image.load('img/scuba_man.png')
    scale2 = (40,70)
    img3 = pygame.image.load('img/wizard.png')
    scale3 = (40,70)


    #background images for all levels
    background_img1 = pygame.image.load('img/arena3.jpg')
    background_img2 = pygame.transform.scale(pygame.image.load('img/underwaterBG.jpg'), (750, 750))
    background_img3 = pygame.transform.scale(pygame.image.load('img/foggy_night.png'), (750, 750))
    #restart button image
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

    #Initializing all the exit and enemy groups
    exit_group = pygame.sprite.Group()
    dragon_group = pygame.sprite.Group()
    exit_group2 = pygame.sprite.Group()
    mermaid_group = pygame.sprite.Group()
    bad_group = pygame.sprite.Group()
    exit_group3 = pygame.sprite.Group()

    #setting up the worlds
    world = World(LVL1,exit_group,dragon_group)
    world2 = World2(LVL2, exit_group2, mermaid_group)
    world3 = World3(LVL3, exit_group3, bad_group)

    #setting up the characters
    player = Player(100, screen_height - 400, img1, scale1, world,dragon_group,exit_group)

    player2 = Player(50, 600, img2, scale2, world2, mermaid_group, exit_group2)

    player3 = Player(100, screen_height - 130, img3, scale3, world3, bad_group, exit_group3)

    # exit_group = pygame.sprite.Group()
    # exit_group2 = pygame.sprite.Group()
    # dragon_group = pygame.sprite.Group()

    #worlds = [LVL1, LVL2, LVL3]
    # world = World(LVL1)

    # mermaid_group = pygame.sprite.Group()
    # world2= World2(LVL2)


    # bad_group = pygame.sprite.Group()
    # exit_group3 = pygame.sprite.Group()
    # world3 = World3(LVL3)


    start = Start()
    # restart_img = pygame.image.load('img/restart_img.png')
    restart_button = Button(100, 100, restart_img)


    run = True
    while run:
        clock.tick(fps)

        #checks if level is starting screen
        if level == -1:
            #loads in initial greeting and background image
            mono = pygame.image.load('img/monoLVL1.png')
            screen.blit(background_img1, (0, 0))
            screen.blit(mono, (35,190))
            game_over = start.update(game_over)
            if game_over == 1:
                level += 1
                game_over = 0

        if level == -2:
            #loads in initial greeting and background image
            mono = pygame.image.load('img/monoLVL2.png')
            screen.blit(background_img1, (0, 0))
            screen.blit(mono, (35,190))
            game_over = start.update(game_over)
            if game_over == 1:
                level = 1
                game_over = 0
        if level == -3:
            #loads in initial greeting and background image
            mono = pygame.image.load('img/monoLVL3.png')
            screen.blit(background_img1, (0, 0))
            screen.blit(mono, (35,190))
            game_over = start.update(game_over)
            if game_over == 1:
                level = 2
                game_over = 0

        #checks if level is lvl1
        elif level == 0:
            #load in lvl1 pictures and world
            screen.blit(background_img1, (0, 0))
            world.draw()

            #if the game is still going--player has not won or died
            if game_over == 0:
                dragon_group.update()

            dragon_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update1(game_over)

            #if the player wins, update the level, if on level 3, print winning message
            if game_over == 1:
                level = -2
                if level <= max_levels:
                    game_over = 0

            #if player dies, end game, reset player positions, and give them restart option
            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200, img1, scale1)
                    game_over = 0

        #checks if level is the second level
        elif level == 1:
            #loads in lvl2 world and pictures
            screen.blit(background_img2, (0, 0))
            world2.draw()

            #if player has not died or won... update object positions
            if game_over == 0:
                mermaid_group.update()

            mermaid_group.draw(screen)
            exit_group2.draw(screen)

            game_over = player2.update2(game_over)

            #if player wins, move on to next level
            if game_over == 1:
                level = -3
                game_over = 0

            #if player dies, end game, reset player positions and give them restart option
            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200, img1, scale1)
                    player2.reset(50, 600, img2, scale2)
                    game_over = 0

        #if third and final level...
        elif level == 2:
            #draw in lvl 3 pictures and world
            screen.blit(background_img3, (0, 0))
            world3.draw()

            #if player has not died or won, update object positions
            if game_over == 0:
                bad_group.update()

            bad_group.draw(screen)
            exit_group3.draw(screen)

            game_over = player3.update3(game_over)

            #if player dies, end game, reset player positions and give them restart option
            if game_over == -1:
                if restart_button.draw(screen):
                    level = -1
                    player.reset(100, screen_height - 200, img1, scale1)
                    player2.reset(50, 600, img2, scale2)
                    player3.reset(100, screen_height - 130, img3, scale3)
                    game_over = 0


        #execute all events while game is running, if X is clicked on screen, close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #update the display screen
        pygame.display.update()

    #close window and game
    pygame.quit()

if __name__ == '__main__':
    main()