import pygame
#making rectangular button class
#scale makes buttons bigger or smaller (customizable)
class Button():
    def __init__(self, x, y, image, scale=0.5):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self, surface):
        action = False
        #get mouse position
        if self.visible:
            pos = pygame.mouse.get_pos()
            #check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
            #this sets button back to clicked = False so that it can be clicked multiple times
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            #draw button on screen
            surface.blit(self.image, (self.rect.x, self.rect.y))

        return action



