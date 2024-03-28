import pygame as pg
#making rectangular button class
#scale makes buttons bigger or smaller (customizable)
class Textbox():
    def __init__(self, words, afterword, spacing):
        self.words = words
        self.afterword = afterword
        self.spacing = spacing
        self.blue = (0,0,128)
        self.normal = ((202,228,241))
        self.font = pg.font.Font("freesansbold.ttf", 32)
        self.text = self.font.render(self.words, True, self.blue, self.normal)
        self.textSpot = self.text.get_rect()
        self.textSpot.center = spacing
        self.visible = True

    def change(self, new):
        self.text = self.font.render(new, True, self.blue, self.normal)

    def get_text(self):
        return self.text

    def get_rect(self):
        return self.textSpot

    def remove(self):
        self.visible = False



