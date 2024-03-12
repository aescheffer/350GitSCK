import turtle

#set up window to be used
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Maze Time!")
window.setup(700,700)

#class to hold information for each of the walls drawn in the maze
class Draw(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("darkgreen")
        self.penup()
        self.speed(0)

        #without this, the squares are too small and there are huge gaps in between each of them
        self.shapesize(2.3, 2.3, 0)

#class to hold and project the location of the character that is moved
class Character(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("brown")
        self.penup()
        self.speed(0)

    #checks if the coordinate that we want to move to is occupied by a wall in the walls list
    def up(self):
        if (self.xcor(), self.ycor() + 46) in walls:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 46)

    # checks if the coordinate that we want to move to is occupied by a wall in the walls list
    def down(self):
        if (self.xcor(), self.ycor() - 46) in walls:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 46)

    # checks if the coordinate that we want to move to is occupied by a wall in the walls list
    def left(self):
        if (self.xcor() - 46, self.ycor()) in walls:
            pass
        else:
            self.goto(self.xcor() - 46, self.ycor())

    # checks if the coordinate that we want to move to is occupied by a wall in the walls list
    def right(self):
        if (self.xcor() + 46, self.ycor()) in walls:
            pass
        else:
            self.goto(self.xcor() + 46, self.ycor())

#class to hold the location of which exit point/choice that the user makes in the maze
class Choice(turtle.Turtle):
    def __init__(self, x, y, char):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.letter = char

#this function sorts through the given maze and determines what spaces will be filled by which class based on
#what letter occupies the space
def create_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            position = maze[y][x]

            #starts from the very left portion of the screen as well as the very top
            #the window space being occupied is 598x598 pixels
            screenx = -276 + (x*46)
            screeny = 276 - (y*46)

            #walls
            if position == 'o':
                d.goto(screenx, screeny)
                d.stamp()
                walls.append((screenx, screeny))

            #character start
            if position == 'x':
                c.goto(screenx, screeny)

            #left path
            if position == 'l':
                choices.append(Choice(screenx, screeny, 'l'))

            #right path
            if position == 'r':
                choices.append(Choice(screenx, screeny, 'r'))

#global variables to make testing easier
d = Draw()
c = Character()
walls = []
choices = []

#main function where keybinds are set and the maze is created. This also checks for when the characters location
#is the same as one of the choices, which determines which button will be able to be pressed
def main():
    maze = ['ooooooooooooo',
            'ox     o    o',
            'o oooooo oooo',
            'o           o',
            'ooo o ooooo o',
            'o   o       o',
            'oooooo oo ooo',
            'o      o    o',
            'o oooooo o oo',
            'or       o oo',
            'ooo oooo o  o',
            'o   ol   oo o',
            'ooooooooooooo']

    create_maze(maze)

    turtle.listen()
    turtle.onkey(c.left, "a")
    turtle.onkey(c.right, "d")
    turtle.onkey(c.up, "w")
    turtle.onkey(c.down, "s")


    window.tracer(0)

    #while loop that updates the players location each time the user presses the button and exits once a choice has
    #been reached. When a choice has been reached, it also returns a letter indicating which path they chose
    while True:
        for choice in choices:
            if (c.xcor(), c.ycor()) == (choice.xcor(), choice.ycor()):
                turtle.bye()
                return choice.letter

        window.update()
