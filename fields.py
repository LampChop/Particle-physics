import numpy as np
import pygame as pg
class magnetic_field:
    """Класс магнитного поля."""

    def __init__(self, magnetic_field_value):
        """Функция инициализации."""

        """Принимает на вход значение индукции магнитного поля.

        """

        self.field_value = magnetic_field_value
        self.orient = np.sign(magnetic_field_value)

    def draw(self, screen):
        """Рисует направление вектора магнитной индукции."""

        if self.orient == 1:
            pg.draw.line(screen, (255, 255, 255), [(400 - 5), (300 - 5)], [(400 + 5), (300 + 5)], 3)
            pg.draw.line(screen, (255, 255, 255), [(400 - 5), (300 + 5)], [(400 + 5), (300 - 5)], 3)
            pg.draw.circle(
                screen,
                (255, 255, 255),
                (400, 300), 10, 1
            )
        elif self.orient == -1:
            pg.draw.circle(
                screen,
                (255, 255, 255),
                (400, 300), 10, 1
            )
            pg.draw.circle(
                screen,
                (255, 255, 255),
                (400, 300), 3,
            )
        elif self.orient == 0:
            pass


class electric_field:
    """Класс электрического поля."""

    def __init__(self, electric_field_value):
        """Функция инициализации."""

        """Принимает на вход значение напряженности электрического поля.

        """

        self.field_value = electric_field_value
        self.orient = np.sign(electric_field_value)

    def draw(self, screen):
        """Рисует направление вектора напряженности электрического поля."""

        if self.orient == -1:
            pg.draw.line(screen, (255, 255, 255), [50, 50], [100, 50], 5)
            pg.draw.line(screen, (255, 255, 255), [50, 50], [60, 60], 5)
            pg.draw.line(screen, (255, 255, 255), [50, 50], [60, 40], 5)
        elif self.orient == 1:
            pg.draw.line(screen, (255, 255, 255), [50, 50], [100, 50], 5)
            pg.draw.line(screen, (255, 255, 255), [100, 50], [90, 60], 5)
            pg.draw.line(screen, (255, 255, 255), [100, 50], [90, 40], 5)
        elif self.orient == 0:
            pass
