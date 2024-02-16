from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("1000x700")
#top.config(cursor='circle')
top.title("Hammy Popper Demo")
text = 'Choose your character!'

def quit():
   top.destroy()

# def restart():
#    quit.forget()
#    restart.forget()
#    ron.place(x=300,y=300)
#    harry.place(x=200,y=300)
#    cedric.place(x=100,y=300)
#    T.config = 'Choose your character!'

#if you choose Ron as your character, instant death
def ron_death():
   ron.destroy()
   harry.destroy()
   cedric.destroy()
   T.config(text="bitch boy")
   #restart.place(x=100,y=100)
   quit.place(x=100,y=300)

#advance to goblet of fire if Cedric or Harry is chosen
def gob():
   ron.destroy()
   harry.destroy()
   cedric.destroy()
   goblet_yes.place(x=100,y=300)
   goblet_no.place(x=200,y=300)
   T.config(text="Will you place your name in the goblet of fire?")

#if choose YES for goblet of fire, die
def explode_by_gob():
   goblet_yes.destroy()
   goblet_no.destroy()
   T.config(text="You're too young to put your name in the goblet!\n"
                 "You explode and the first-years use your head as a quaffle.")
   #restart.place(x=100,y=100)
   quit.place(x=100,y=200)

#if choose NO for goblet of fire, choose dragon
def dragon_choice():
   goblet_yes.destroy()
   goblet_no.destroy()
   hungarian.place(x=100,y=300)
   chinese.place(x=400,y=300)
   swedish.place(x=700,y=300)
   T.config(text="Too bad! You're the main character so you\n"
                 "don't get a choice! The first test is...\n"
                 "DRAGONS!!! Choose your dragon!")

#if choose hungarian dragon, given choice between gilly weed and shark head for underwater challenge
def hungarian():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   T.config(text="You were able to defeat the Hungarian Horntail and move on to the next round!\n"
                 "You must find a way to breathe underwater for an hour. What will you use?")
   gilly.place(x=200, y=300)
   shark.place(x=500, y=300)

#if choose chinese dragon, given choice between o2 bubble or mystery potion
def chinese():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   T.config(text="You defeated the Chinese Fireball! Moving on to the underwater challenge,\n"
                 "what will you use to breathe underwater for an hour?")
   bubble.place(x=200, y=300)
   mystery.place(x=500, y=300)

#if choose swedish dragon, die
def swedish_death():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   T.config(text="The Swedish Shortsnout died before your trial, and since your \n"
                 "lives were tied, your death was assigned to your cousin Vikram III.\n"
                 "Your memory will not live on.")

#if choose mystery potion, die from bleach poisoning
def bleach_death():
   bubble.destroy()
   mystery.destroy()
   T.config(text="The mystery potion turns out to be bleach supplied by Draco Malfoy. You jump into the water with\n"
                 "full confidence but are never seen again. No one notices that there is one less contestant.")
   quit.place(x=200,y=300)

#if choose gilly weed, save Ron and French girl
def ron_and_frenchie():
   gilly.destroy()
   shark.destroy()
   T.config(text="Great choice! The Gilly Weed gave you flippers, making you fast enough to save\n"
                 "Ron Weasley and a sickly french child. You move on to the maze! Before you enter,\n"
                 "will you pick the left or right path?")
   left.place(x=200,y=300)
   right.place(x=500,y=300)

#if choose shark head spell, save hermione
def hermione():
   gilly.destroy()
   shark.destroy()
   T.config(text="The shark head spell gave you the confidence to rescue the brightest witch in your school:\n"
                 "Hermione Granger. She hints that \"the safe path doesn't always feel right.\" You have reached\n"
                 "the final challenge of the maze...which path will you choose?")
   left.place(x=200,y=300)
   right.place(x=500,y=300)

#if choose bubble spell, save cho
def cho():
   bubble.destroy()
   mystery.destroy()
   T.config(text="The bubble spell gave you the confidence to save the Ravenclaw, Cho! She gives you the advice that, when it\n "
            "comes to navigating the maze, \"take the high road.\" You misinterpret her advice and cheat by climbing over \n"
            "the hedges until you're caught by a soul-sucking dementor! What do you do?")
   patronus.place(x=200,y=300)
   dem_run.place(x=500,y=300)

#cast patronus charm on dementor
def patronus():
   patronus.destroy()
   dem_run.destroy()
   T.config(text="You summon your happiest memory and cast the Patronus charm. Out of your wand appears a massive translucent\n"
                 "slug that overpowers the dementor. The patronus also reveals the Tri Wizard Cup right in front of you, but\n"
                 "Viktor Krum has spotted it first and he raises his wand to attack you! What spell will you cast to\n"
                 "defend yourself?")
   expel.place(x=200,y=300)
   avis.place(x=500,y=300)

#run from the dementor
def dem_run():
   patronus.destroy()
   dem_run.destroy()
   T.config(text="Fueled by fear, you attempt to run from the dementor but onlly manage to fall a great height from\n"
                 "atop the hedges and break your neck, dying instantly. Too bad there's no spell to fix that!")
   quit.place(x=200,y=300)

#take left path in the maze
def left():
   left.destroy()
   right.destroy()
   T.config(text="You head down the left path and before you know it, you've found the cup! And so has Cedric! You grab it\n"
                 "together and are transported to...a cemetery? And the dark wizard Voldemort is here too?!?! What\n"
                 "ever will you do???")
   fight.place(x=200,y=300)
   vol_run.place(x=500,y=300)

#duel Voldemort --> Win
def fight_voldy():
   fight.destroy()
   vol_run.destroy()
   T.config(text="Using Cedric as a human shield, you \"dodge\" Voldemort's cast of the death curse. You ultimately\n"
                 "defeat the dark wizard and return to Hogwarts as the champion of the Tri Wizard Tournament!!!\n"
                 "THE END")

#run away from Voldemort in the cemetery
def run_voldy():
   fight.destroy()
   vol_run.destroy()
   T.config(text="You run as fast as you can in the opposite direction of the dark lord. Because you didn't check where\n"
                 "you were headed, you fall into an open grave. Cedric reaches down to help you out, but is killed by\n"
                 "Voldemort, falling on top of you and leaving you to suffocate in darkness under the corpse of your friend.\n"
                 "THE END")

#right path in the maze
def right():
   left.destroy()
   right.destroy()
   T.config(text="You walk down the right path and spot the Tri Wizard Cup! As you approach the cup, you suddenly \n"
                 "lock eyes with a bewitched Viktor Krum! You both race toward the cup and you have time to cast \n"
                 "one spell. Unfortunately, you only remember two...which do you pick?")
   expel.place(x=200,y=300)
   avis.place(x=500,y=300)

#defence from Viktor Krum
def avis():
   expel.destroy()
   avis.destroy()
   T.config(text="You cast the Avis spell, summoning a small flock of birds. Viktor is unfazed and the birds take more\n"
                 "interest in the berries growing from the hedges than coming to your aid. Viktor body slams you into the\n"
                 "ground where vines engulf your body and drag you deeper into the maze. You die cold and utterly alone.")
   quit.place(x=200,y=300)

#defence from Viktor Krum
def expelliarmus():
   expel.destroy()
   avis.destroy()
   T.config(text="You cast Expelliarmus, unarming Viktor of his wand. As you clutch one handle of the cup, you notice\n"
                 "that Cedric Diggory has grasped the other at the same time. Together, you are transported to a\n"
                 "cemetery where Voldemort himself has been waiting! What will you do???")
   run_voldy.place(x=200,y=300)
   fight_voldy.place(x=500,y=300)

#Label changes depending on where you are in the game
T = Label(top, text=text)
T.place(x=200,y=200)

#restart and quit buttons
#restart = Button(top, text="Restart", command=restart)
quit = Button(top, text="Quit", command=top.destroy)

#character choice: Ron (death), Harry, or Cedric
ron = Button(top, text ="Ron", command = ron_death)
ron.place(x=300,y=300)
harry = Button(top, text="Harry", command = gob)
harry.place(x=200,y=300)
cedric = Button(top, text="Cedric", command = gob)
cedric.place(x=100,y=300)

#goblet of fire yes or no
goblet_yes = Button(top, text="Yes", command = explode_by_gob)
goblet_no = Button(top, text="No", command = dragon_choice)

#Choose your dragon!
hungarian = Button(top, text="Hungarian Horntail", command = hungarian)
chinese = Button(top, text="Chinese Fireball", command = chinese)
swedish = Button(top, text="Swedish Shortsnout", command=swedish_death)

# #Water challenge
gilly = Button(top, text="Gilly Weed", command = ron_and_frenchie)
shark = Button(top, text="Shark Head Spell", command= hermione)
#
bubble = Button(top, text="Oxygen Bubble Spell", command=cho)
mystery = Button(top, text="Mystery Potion from your Slytherin \"friends\"", command=bleach_death)

#Maze options
left = Button(top, text="Left", command=left)
right = Button(top, text="Right", command=right)

expel = Button(top,text="Expelliarmus",command=expelliarmus)
avis = Button(top,text="Avis",command=avis)

patronus = Button(top,text="Patronus Charm",command=patronus)
dem_run = Button(top,text="Run for your life!",command=dem_run)

#Final choice
fight = Button(top,text="Duel Voldemort",command=fight_voldy)
vol_run = Button(top,text="RUN!!!",command=run_voldy)





top.mainloop()



#
# import tkinter
# from tkinter import *
#
# window = tkinter.Tk()
# # set window size using geometry funct --> in pixels
# window.geometry("350x200")
#
# # to rename the title of the window
# window.title("GUI")
#
# # pack is used to show the object in the window
# #label = tkinter.Label(window, text = "Hello World!", font=("Arial Bold", 5git 0)).pack()
#
# #create button --> grid function sets button position
# #bg = background color, fg = foreground color
# # bt = Button(window,text="Enter", bg="blue",fg="red")
# # bt.grid(column=1,row=0)
# #test on line 18!!!
# #test on line 19
#
#
# #makes button that will make program stop running
# #bd is border width pixels
# btn = Button(window, activeforeground=red, text="Destroy", bd="15", command = window.destroy)
# btn.pack(side="bottom")
#
# #this makes the window appear
# window.mainloop()
#

