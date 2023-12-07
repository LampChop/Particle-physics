import pygame as pg
from visualization import *
class particle:
    x = 0
    y = 0
    vx = 0
    vy = 0
    r = 500
    mass = 1
    color = [255, 255, 255]
    def __init__(self, x, y, vx, vy, r, mass, q, Fx, Fy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.q = q
        red = [220, 20, 60]
        blue = [70, 130, 180]
        if q > 0:
            self.color = red
        else:
            self.color = blue
        self.r = r
        self.mass = mass
        self.Fx = Fx
        self.Fy = Fy
    def __init__(self, x, y, vx, vy, r, mass, q, Fx, Fy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.q = q
        self.color = color
        self.r = r
        self.mass = mass
        self.Fx = Fx
        self.Fy = Fy
    def draw(self, screen):
        pg.draw.circle(
            screen,
            (self.color[0], self.color[1], self.color[2]), #Теперь цвет это кортеж, который мы можем изменять
            (self.x/scale_factor, self.y/scale_factor),
            self.r/scale_factor
        )

