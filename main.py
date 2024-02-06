import tkinter
from tkinter import *

window = tkinter.Tk()
# set window size using geometry funct --> in pixels
window.geometry("350x200")

# to rename the title of the window
window.title("GUI")

# pack is used to show the object in the window
#label = tkinter.Label(window, text = "Hello World!", font=("Arial Bold", 5git 0)).pack()

#create button --> grid function sets button position
#bg = background color, fg = foreground color
# bt = Button(window,text="Enter", bg="blue",fg="red")
# bt.grid(column=1,row=0)
#test on line 18!!!
#test on line 19

#add button click event DOESNT WORK
# def clicked(l1):
#    l1.configure(text="Button was clicked!!")
# bt=Button(window,text="enter",command=clicked)

#makes button that will make program stop running
#bd is border width pixels
btn = Button(window, text="Destroy", bd="15", command = window.destroy)
btn.pack(side="bottom")

#this makes the window appear
window.mainloop()


