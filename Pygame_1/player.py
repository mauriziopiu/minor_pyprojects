import pygame


class player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 10
        self.color = (0, 255, 0)
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
