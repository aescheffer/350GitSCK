import pygame
import unittest
from pygame.locals import *
from ButtonClass import Button
from LVL1and2 import *

class TestCases(unittest.TestCase):
    #test for player instance
    def testPlayer(self):
        sample_img = pygame.image.load('img/knight_left.png')
        player = Player(x=100,y=100,img=sample_img,scale=(40,80))
        assert(isinstance(player, Player))
        
    #test for enemy instance
    def testEnemy(self):
        enemy = Dragon(100,100)
        assert(isinstance(enemy,Dragon))
        
    #test for button instance
    def testButton(self):
        sample_img = pygame.image.load('img/restart_img.png')
        button = Button(100,100, sample_img)
        assert(isinstance(button, Button))

    #make sure program raises TypeError if parameter is wrong type
    def invalidPlayer(self):
        sample_img = pygame.image.load('img/knight_left.png')
        with self.assertRaises(TypeError):
            player = Player(x=100,y=100,img=sample_img,scale=0.5)
    
