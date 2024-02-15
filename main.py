from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("800x800")
top.config(cursor='circle')
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

def explode_by_gob():
   goblet_yes.destroy()
   goblet_no.destroy()
   T.config(text="You're too young to put your name in the goblet!\n"
                 "You explode and the first-years use your head as a quaffle.")
   #restart.place(x=100,y=100)
   quit.place(x=100,y=200)

def dragon_choice():
   goblet_yes.destroy()
   goblet_no.destroy()
   hungarian.place(x=100,y=300)
   chinese.place(x=400,y=300)
   swedish.place(x=700,y=300)
   T.config(text="Too bad! You're the main character so you\n"
                 "don't get a choice! The first test is...\n"
                 "DRAGONS!!! Choose your dragon!")

def hungarian():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   # gilly.place(x=200,y=300)
   # shark.place(x=100,y=300)
   T.config(text="You were able to defeat the Hungarian Horntail and move on to the next round!\n"
                 "You must find a way to breathe underwater for an hour. What will you use?")
   gilly.place(x=200, y=300)
   shark.place(x=500, y=300)

def chinese():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   # bubble.place(x=200,y=300)
   # mystery.place(x=100,y=300)
   T.config(text="You defeated the Chinese Fireball! Moving on to the underwater challenge,\n"
                 "what will you use to breathe underwater for an hour?")
   bubble.place(x=200, y=300)
   mystery.place(x=500, y=300)

def swedish_death():
   hungarian.destroy()
   chinese.destroy()
   swedish.destroy()
   T.config(text="The Swedish Shortsnout died before your trial, and since your \n"
                 "lives were tied, your death was assigned to your cousin Vikram III.\n"
                 "Your memory will not live on.")

def ron_and_frenchie():
   return

def hermione():
   return

def cho():
   return

def bleach_death():
   return




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
mystery = Button(top, text="Mystery Potion", command=bleach_death)

#





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

