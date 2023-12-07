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
            nx = dx / distance
            ny = dy / distance
            relative_velocity = [other_particle.vx - self.vx, other_particle.vy - self.vy]
            vel_along_normal = relative_velocity[0] * nx + relative_velocity[1] * ny

            if vel_along_normal > 0:
                # Частицы летят в разные стороны и все норм
                return

            e = 1  # коэффициент упругости

            j = -(1 + e) * vel_along_normal
            j /= 1 / self.mass + 1 / other_particle.mass

            impulse = [j * nx, j * ny]

            self.vx -= 1 / self.mass * impulse[0]
            self.vy -= 1 / self.mass * impulse[1]
            other_particle.vx += 1 / other_particle.mass * impulse[0]
            other_particle.vy += 1 / other_particle.mass * impulse[1]

            # SРазъединяем частицы чтобы они не слиплись
            overlap = self.r + other_particle.r - distance
            self.x -= overlap / 2 * nx
            self.y -= overlap / 2 * ny
            other_particle.x += overlap / 2 * nx
            other_particle.y += overlap / 2 * ny
