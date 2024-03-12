import unittest
from maze import *
import turtle

#class to perform unit tests on the maze file
class TestGame(unittest.TestCase):
    #tests a characters ability to move downwards
    def test_down(self):
        start = (c.xcor(), c.ycor())
        c.down()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[1], start[1] - 46)

    # tests a characters ability to move upwards
    def test_up(self):
        start = (c.xcor(), c.ycor())
        c.up()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[1], start[1] + 46)

    # tests a characters ability to move right
    def test_right(self):
        start = (c.xcor(), c.ycor())
        c.right()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[0], start[0] + 46)

    # tests a characters ability to move left
    def test_left(self):
        start = (c.xcor(), c.ycor())
        c.left()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[0], start[0] - 46)

    #tests that characters are incapable of moving throught the walls set in place (this is only for the bottom left choice)
    def test_walls1(self):
        main()

        start = (c.xcor(), c.ycor())
        c.left()
        c.down()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end, start)



if __name__ == '__main__':
    unittest.main()

