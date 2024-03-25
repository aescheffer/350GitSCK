from py_avataaars import PyAvataaar
import py_avataaars as pa
from ButtonClass import *
import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
class Av_Choice():
    #next_screen = Button(100,100, man_pic, 0.5)

    avatar = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,accessories_type=pa.AccessoriesType.PRESCRIPTION_02)
    avatar.render_png_file("AVATAR_DEF.png")
    man_pic = pygame.image.load('AVATAR_DEF.png').convert_alpha()
    man = Button(100,100, man_pic, 0.5)

    pink = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                         skin_color=pa.SkinColor.LIGHT,
                                hair_color=pa.HairColor.PASTEL_PINK,
                                top_type=pa.TopType.LONG_HAIR_CURVY,
                                mouth_type=pa.MouthType.SMILE,
                                eye_type=pa.EyesType.HEARTS,
                                eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL
                                )
    pink.render_png_file("AV_PINK.png")
    pink_girl_pic = pygame.image.load('AV_PINK.png').convert_alpha()
    pink_girl = Button(300,100, pink_girl_pic, 0.5)

    ed = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                       skin_color=pa.SkinColor.PALE,
                                hair_color=pa.HairColor.RED,
                                top_type=pa.TopType.SHORT_HAIR_DREADS_02,
                                mouth_type=pa.MouthType.TONGUE,
                                eye_type=pa.EyesType.WINK,
                                eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL
                                )
    ed.render_png_file("ED.png")
    ed_pic = pygame.image.load('ED.png').convert_alpha()
    ed_sheeran = Button(500,100, ed_pic, 0.5)

    ban = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                        skin_color=pa.SkinColor.BLACK,
                                hair_color=pa.HairColor.BLONDE,
                                top_type=pa.TopType.LONG_HAIR_FRO_BAND,
                                mouth_type=pa.MouthType.SCREAM_OPEN,
                                eye_type=pa.EyesType.HAPPY,
                                eyebrow_type=pa.EyebrowType.DEFAULT_NATURAL
                                )
    ban.render_png_file("BAND.png")
    band_pic = pygame.image.load('BAND.png').convert_alpha()
    band = Button(100,300, band_pic, 0.5)

    pat = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                        skin_color=pa.SkinColor.TANNED,
                                top_type=pa.TopType.EYE_PATCH,
                                mouth_type=pa.MouthType.CONCERNED,
                                eye_type=pa.EyesType.SIDE,
                                eyebrow_type=pa.EyebrowType.FLAT_NATURAL
                                )
    pat.render_png_file("PAT.png")
    patch_pic = pygame.image.load('PAT.png').convert_alpha()
    patch = Button(300,300, patch_pic, 0.5)

    sar = pa.PyAvataaar(style=pa.AvatarStyle.TRANSPARENT,
                        skin_color=pa.SkinColor.BROWN,
                                top_type=pa.TopType.HIJAB,
                                mouth_type=pa.MouthType.SMILE,
                                eye_type=pa.EyesType.HAPPY,
                                eyebrow_type=pa.EyebrowType.DEFAULT_NATURAL
                                )
    sar.render_png_file("SARAH.png")
    sarah_pic = pygame.image.load('SARAH.png').convert_alpha()
    sarah = Button(500,300, sarah_pic, 0.5)



#change the text on the screen after they choose
def change_words(text_object, new_words):
    text_object.change(new_words)
    screen.blit(text_object.get_text(), text_object.get_rect())


av = Av_Choice()
from TextboxClass import Textbox
txt = Textbox("What do you look like?", "Wow! You look great!", (380,67))

run = True
while run:
    screen.fill((202,228,241))
    screen.blit(txt.get_text(), txt.get_rect())
    #depending on character chosen, the usr_choice avatar will change
    if av.man.draw(screen):
        print('AVATAR CLICKED')
        usr_choice = av.man_pic
        av.man.move_and_remove([av.pink_girl, av.ed_sheeran, av.band, av.patch, av.sarah])
        change_words(txt, "Woah! Neat glasses!")
    if av.pink_girl.draw(screen):
        print('PINK!!!')
        usr_choice = av.pink_girl_pic
        av.pink_girl.move_and_remove([av.man, av.ed_sheeran, av.band, av.patch, av.sarah])
        change_words(txt, "Love your bright pink hair!")
    if av.ed_sheeran.draw(screen):
        print("ED SHEERAN!")
        usr_choice = av.ed_pic
        av.ed_sheeran.move_and_remove([av.man, av.pink_girl, av.band, av.patch, av.sarah])
        change_words(txt, "You look like Ed Sheeran!")
    if av.band.draw(screen):
        print("BAND")
        usr_choice = av.band_pic
        av.band.move_and_remove([av.man, av.pink_girl, av.ed_sheeran, av.patch, av.sarah])
        change_words(txt, "What a fun hairband!")
    if av.patch.draw(screen):
        print("PATCH")
        usr_choice = av.patch_pic
        av.patch.move_and_remove([av.man, av.pink_girl, av.ed_sheeran, av.band, av.sarah])
        change_words(txt, "Where'd your other eye go?!")
    if av.sarah.draw(screen):
        print("SARAH")
        usr_choice = av.sarah_pic
        av.sarah.move_and_remove([av.man, av.pink_girl, av.ed_sheeran, av.band, av.patch])
        change_words(txt, "You look like a Sarah!")
    #screen.blit(after.get_text(), after.get_rect())


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
