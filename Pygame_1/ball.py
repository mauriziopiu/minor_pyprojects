import pygame
import math


class ball(object):
    # (x, y) = (350, 250)
    # facing must be between [0, 360)
    def __init__(self, x, y, facing, size):
        self.x = x
        self.y = y
        self.facing = math.radians(facing)
        self.vel = 5
        self.size = size
        self.width = 2 * self.size
        self.color = (255, 0, 0)

    def leftCollision(self):
        return self.x <= self.vel

    def rightCollision(self):
        return self.x + self.width + self.vel >= 500

    def upperCollision(self):
        return self.y <= self.vel

    def lowerCollision(self):
        return self.y + self.width + self.vel >= 500

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.size, self.size)

    def move(self):
        # [0, 90) degrees (OK like that)
        if math.radians(0) <= self.facing < math.radians(90):
            section = math.radians(0)
            self.x += int(self.vel * math.sin(self.facing-section))
            self.y -= int(self.vel * math.cos(self.facing-section))
            if self.leftCollision():
                pass
            elif self.upperCollision():
                pass
        # [90, 180) degrees
        elif math.radians(90) <= self.facing < math.radians(180):
            section = math.radians(90)
            self.x += int(self.vel * math.cos(self.facing - section))
            self.y += int(self.vel * math.sin(self.facing - section))
            if self.rightCollision():
                pass
            elif self.upperCollision():
                pass
        # [180, 270) degrees
        elif math.radians(180) <= self.facing < math.radians(270):
            section = math.radians(180)
            self.x -= int(self.vel * math.sin(self.facing - section))
            self.y += int(self.vel * math.cos(self.facing - section))
            if self.leftCollision():
                pass
            elif self.lowerCollision():
                pass
        # [270, 360) degrees
        elif math.radians(270) <= self.facing <= math.radians(359):
            section = math.radians(270)
            self.x -= int(self.vel * math.cos(self.facing - section))
            self.y -= int(self.vel * math.sin(self.facing - section))
            if self.rightCollision():
                pass
            elif self.upperCollision():
                pass


"""
    def move(self):
        # North West
        if self.facing == "NW":
            self.x -= self.vel
            self.y -= self.vel
            if self.leftCollision():
                self.facing = "NE"
            elif self.upperCollision():
                self.facing = "SW"
        # North East
        elif self.facing == "NE":
            self.x += self.vel
            self.y -= self.vel
            if self.rightCollision():
                self.facing = "NW"
            elif self.upperCollision():
                self.facing = "SE"
        # South West
        elif self.facing == "SW":
            self.x -= self.vel
            self.y += self.vel
            if self.leftCollision():
                self.facing = "SE"
            elif self.lowerCollision():
                self.facing = "NW"
        # South East
        elif self.facing == "SE":
            self.x += self.vel
            self.y += self.vel
            if self.rightCollision():
                self.facing = "SW"
            elif self.upperCollision():
                self.facing = "NE"
"""
