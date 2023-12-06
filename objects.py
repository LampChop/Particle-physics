import pygame as pg
import math
class particle:
    x = 0
    y = 0
    vx = 0
    vy = 0
    r = 5
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
            (self.x, self.y),
            self.r
        )

    def check_collision(self, other_particle):
        dx = other_particle.x - self.x
        dy = other_particle.y - self.y
        distance = math.sqrt(dx * dx + dy * dy)

        if distance < self.r + other_particle.r:
            # Collision occurred
            # Perform velocity update based on laws of elastic collision
            nx = (other_particle.x - self.x) / distance
            ny = (other_particle.y - self.y) / distance
            dp = (self.vx - other_particle.vx) * nx + (self.vy - other_particle.vy) * ny
            self.vx -= dp * nx
            self.vy -= dp * ny
            other_particle.vx += dp * nx
            other_particle.vy += dp * ny
