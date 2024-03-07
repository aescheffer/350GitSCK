import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Maze Time!")
window.setup(700,700)


class Draw(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("darkgreen")
        self.penup()
        self.speed(0)
        self.shapesize(2.3, 2.3, 0)

class Character(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("brown")
        self.penup()
        self.speed(0)

    def up(self):
        if (self.xcor(), self.ycor() + 46) in walls:
            pass
        else:
            self.goto(self.xcor(), self.ycor() + 46)

    def down(self):
        if (self.xcor(), self.ycor() - 46) in walls:
            pass
        else:
            self.goto(self.xcor(), self.ycor() - 46)

    def left(self):
        if (self.xcor() - 46, self.ycor()) in walls:
            pass
        else:
            self.goto(self.xcor() - 46, self.ycor())

    def right(self):
        if (self.xcor() + 46, self.ycor()) in walls:
            pass
        else:
            self.goto(self.xcor() + 46, self.ycor())


class Choice(turtle.Turtle):
    def __init__(self, x, y, char):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.goto(x,y)
        self.letter = char

def create_maze(maze):
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            position = maze[y][x]

            screenx = -276 + (x*46)
            screeny = 276 - (y*46)

            if position == 'o':
                d.goto(screenx, screeny)
                d.stamp()
                walls.append((screenx, screeny))

            if position == 'x':
                c.goto(screenx, screeny)

            if position == 'l':
                choices.append(Choice(screenx, screeny, 'l'))

            if position == 'r':
                choices.append(Choice(screenx, screeny, 'r'))


d = Draw()
c = Character()
walls = []
choices = []

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

    while True:
        for choice in choices:
            if (c.xcor(), c.ycor()) == (choice.xcor(), choice.ycor()):
                turtle.bye()
                return choice.letter

        window.update()

#if __name__ == '__main__':
    #main()
