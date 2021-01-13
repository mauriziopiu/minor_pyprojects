import unittest
import ball
import math


class MyTestCase(unittest.TestCase):

    # Bug 1
    # Concerns: Moving ball around
    # Expectation: ball.move needs to check for collision
    # Error: self.upperCollision() (L66 apparantly) emits TypeError: 'bool' object not callable
    # Solution: ball had attributes self.upperCollision as well as method self.upperCollision()

    # Bug 2
    # Concerns: Ball Constructor input
    # Expectation: Ball facing within SE, SW or NW
    # Error: Ball is constantly facing within NE
    # Problem: applied 2 times math.radians(), once in parameter and once within constructor
    # Solution: changed parameter to degree input

    # Movement Tests
    def test_ball_movement_facing30(self):
        b = ball.ball(250, 250, 30, 10)
        x_after_movement = 250 + 2
        y_after_movement = 250 - 4
        print("x before move: " + str(b.x))
        print("y before move: " + str(b.y))
        b.move()
        print("expected x: " + str(x_after_movement))
        print("expected y: " + str(y_after_movement))
        print("actual x: " + str(b.x))
        print("actual y: " + str(b.y))
        self.assertEqual(b.x, x_after_movement)
        self.assertEqual(b.y, y_after_movement)

    def test_ball_movement_facing120(self):
        b = ball.ball(250, 250, 120, 10)
        x_after_movement = 250 + 4
        y_after_movement = 250 + 2
        print("x before move: " + str(b.x))
        print("y before move: " + str(b.y))
        b.move()
        print("expected x: " + str(x_after_movement))
        print("expected y: " + str(y_after_movement))
        print("actual x: " + str(b.x))
        print("actual y: " + str(b.y))
        self.assertEqual(b.x, x_after_movement)
        self.assertEqual(b.y, y_after_movement)

    def test_ball_movement_facing210(self):
        b = ball.ball(250, 250, 210, 10)
        x_after_movement = 250 - 2
        y_after_movement = 250 + 4
        print("x before move: " + str(b.x))
        print("y before move: " + str(b.y))
        b.move()
        print("expected x: " + str(x_after_movement))
        print("expected y: " + str(y_after_movement))
        print("actual x: " + str(b.x))
        print("actual y: " + str(b.y))
        self.assertEqual(b.x, x_after_movement)
        self.assertEqual(b.y, y_after_movement)

    def test_ball_movement_facing300(self):
        b = ball.ball(250, 250, 300, 10)
        x_after_movement = 250 - 4
        y_after_movement = 250 - 2
        print("x before move: " + str(b.x))
        print("y before move: " + str(b.y))
        b.move()
        print("expected x: " + str(x_after_movement))
        print("expected y: " + str(y_after_movement))
        print("actual x: " + str(b.x))
        print("actual y: " + str(b.y))
        self.assertEqual(b.x, x_after_movement)
        self.assertEqual(b.y, y_after_movement)
