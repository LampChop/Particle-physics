from visualization import *
import pygame as pg
import numpy as np
class particle:
    """Класс частицы."""

    def __init__(self, x, y, vx, vy, r, mass, q, color, Fx, Fy):
        """Функция инициализации."""

        """Принимает на вход координаты частицы, проекции ее скорости на
        оси x и y, ее радиус, массу, заряд, цвет и проекции сил на оси x и y.
        Если заряд частицы больше нуля, ее цвет красный, меньше нуля -- синий,
        равен нулю -- белый.

        """

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.q = q
        red = [220, 20, 60]
        blue = [70, 130, 180]
        white = [255, 255, 255]

        if color is None:
            if q > 0:
                self.color = red
            if q < 0:
                self.color = blue
            if q == 0:
                self.color = white
        else:
            self.color = color
        self.r = r
        self.mass = mass
        self.Fx = Fx
        self.Fy = Fy

    def draw(self, screen):
        """Рисует частицу."""

        pg.draw.circle(
            screen,
            (self.color[0], self.color[1], self.color[2]),  # Теперь цвет это кортеж, который мы можем изменять
            (self.x / scale_factor, self.y / scale_factor),
            self.r / scale_factor
        )


