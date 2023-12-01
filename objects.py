import pygame as pg
class particle:
    x = 0
    y = 0
    vx = 0
    vy = 0
    color = (255, 255, 255)
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def draw(self, screen):
        pg.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            5
        )
