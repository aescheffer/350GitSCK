import unittest
from maze import *
import turtle

class TestGame(unittest.TestCase):
    def test_down(self):
        start = (c.xcor(), c.ycor())
        c.down()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[1], start[1] - 46)

    def test_up(self):
        start = (c.xcor(), c.ycor())
        c.up()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[1], start[1] + 46)

    def test_right(self):
        start = (c.xcor(), c.ycor())
        c.right()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[0], start[0] + 46)

    def test_left(self):
        start = (c.xcor(), c.ycor())
        c.left()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end[0], start[0] - 46)

    def test_walls1(self):
        main()

        start = (c.xcor(), c.ycor())
        c.left()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end, start)

    def test_walls2(self):
        main()

        start = (c.xcor(), c.ycor())
        c.down()
        end = (c.xcor(), c.ycor())

        self.assertEqual(end, start)




if __name__ == '__main__':
    unittest.main()

