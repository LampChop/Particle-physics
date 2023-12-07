import pygame as pg
from visualization import *
class particle:
    x = 0
    y = 0
    vx = 0
    vy = 0
    r = 500.
    mass = 1
    color = (255, 255, 255)
    def __init__(self, x, y, vx, vy, color, r, mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.mass = mass
    def draw(self, screen):
        pg.draw.circle(
            screen,
            self.color,
            (self.x/scale_factor, self.y/scale_factor),
            self.r/scale_factor
        )


