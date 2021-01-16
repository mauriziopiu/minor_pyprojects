import pygame
import math

EMPTY = math.radians(0)
QUARTER = math.radians(90)
MID = math.radians(180)
TREQUARTER = math.radians(270)
FULL = math.radians(360)


class ball(object):
    # (x, y) = (350, 250)
    # facing must be between [0, 360)
    def __init__(self, x, y, vel, facing, size):
        self.x = x
        self.y = y
        self.facing = math.radians(facing)
        self.vel = vel
        self.vel_x = 0
        self.vel_y = 0
        self.size = size
        self.width = 2 * self.size
        self.color = (255, 0, 0)
        self.determineInitVelocity()

    def determineInitVelocity(self):
        self.vel_x = self.vel * math.sin(self.facing)
        self.vel_y = (-1) * self.vel * math.cos(self.facing)

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size, self.size)

    def hasXCollision(self):
        return self.x < self.vel or self.x > 500 - self.width - self.vel

    def hasYCollision(self):
        return self.y < self.vel or self.y > 500 - self.width - self.vel

    def handleCollision(self):
        # Vertical Wall Collision
        if self.hasXCollision():
            self.vel_x *= (-1)
        # Horizontal Wall Collision
        elif self.hasYCollision():
            self.vel_y *= (-1)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        if self.hasXCollision() or self.hasYCollision():
            self.handleCollision()

