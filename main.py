import pygame
import numpy as np
import random as rnd
from visualization import *
from objects import *
from modelling import *

 #создаем массив сегментов
white = [255, 255, 255]
bunch = 100 # сколько частиц фигачим за раз
neutral = False
radii = [5, 7, 9]  # введите массы в нужном соотношении
charges = [-10, 10, 5]
x_velocities = y_velocities = [-3, 3]
mass_to_radius = scale_factor
particles = []


# particles.append(particle(400*scale_factor, 250*scale_factor, -10*scale_factor, 10*scale_factor, white, 5*scale_factor, 1, 0, 0))
def main():
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('particles')
    pygame.display.flip()
    running = True
    while running:

        for p in particles:
            p.draw(screen)
            move(p, 0.05)
            for other in particles:
                if p != other:
                    check_collision(p, other)

        pygame.display.update()
        screen.fill((0, 0, 0))

        for p in particles:
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    print(mouse_pos[0])
                    for i in range(bunch):  # сколько частиц фигачим за раз
                        r = rnd.choice(radii)*scale_factor
                        mass = rnd.choice(radii)
                        particles.append(
                            particle(mouse_pos[0]*scale_factor, mouse_pos[1]*scale_factor, rnd.choice(x_velocities)*scale_factor, rnd.choice(y_velocities)*scale_factor,
                                     r, mass, 0 if neutral else rnd.randrange(charges[0], charges[1], charges[2]), None, 0, 0))

        recalculate_particles_positions(particles, 0.05)




main()
