import pygame
import numpy as np
import random as rnd
from visualization import *
from objects import *
from modelling import *
from menu import *

white = [255, 255, 255]
bunch = 1 # сколько частиц фигачим за раз
neutral = False
radii = [10, 8]  # введите массы в нужном соотношении
charges = [-1, 2, 2]
x_velocities = y_velocities = [-1, 1]
mass_to_radius = scale_factor
particles = []
count = 0
background_image_1 = pygame.image.load('шлепа.jpg')
background_image_2 = pygame.image.load('authors.jpg')

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('particles')
pygame.display.flip()
running = True
starting = True
game_1 = True
game_3 = True
authors = True
cat = True

field = magnet_field(0, 0)
e_field = E_field(0, 0)

menu = Menu()
menu.append_option('Начать', lambda: print('Si'))
menu.append_option('Мяу', lambda: print('Гав'))
menu.append_option('Авторы', lambda: print('НБМ'))
menu.append_option('Выход', quit)
while running:
    while starting:
        screen.fill((0, 0, 0))

        menu.draw(screen, 100, 100, 75)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
            elif e.type == KEYDOWN:
                if e.key == K_w:
                    menu.switch(-1)
                    count += 1
                if e.key == K_s:
                    menu.switch(1)
                    count -= 1
                elif e.key == K_SPACE:
                    if count == 0:
                        game_1 = True
                        starting = False
                    elif count == -1:
                        cat = True
                        game_1 = False
                        starting = False
                    elif count == -2:
                        authors = True
                        game_1 = False
                        cat = False
                        starting = False
                    menu.select()

        display.flip()

    while game_1:

        pygame.display.update()
        screen.fill((0, 0, 0))

        for p in particles:
            p.draw(screen)
            move(p, 0.05)
            for other in particles:
                if p != other:
                    check_collision(p, other)

        for p in particles:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    starting = True
                    game_1 = False
                    authors = False
                    cat = False
                if event.key == K_q:
                    field.orient = 1
                    field.tesla = 10
                if event.key == K_e:
                    field.orient = -1
                    field.tesla = 10
                if event.key == K_d:
                    field.orient = 0
                    field.tesla = 0
                if event.key == K_c:
                    e_field.orient = 1
                    e_field.e = 10
                if event.key == K_z:
                    e_field.orient = -1
                    e_field.e = 10
                if event.key == K_a:
                    e_field.orient = 0
                    e_field.e = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = event.pos
                    for i in range(bunch):  # сколько частиц фигачим за раз
                        mass = rnd.choice(radii)
                        r = mass*scale_factor
                        if mass > 9:
                            charge = mass
                        else:
                            charge = -mass
                        particles.append(
                            particle(mouse_pos[0]*scale_factor, mouse_pos[1]*scale_factor, rnd.choice(x_velocities)*scale_factor, rnd.choice(y_velocities)*scale_factor,
                                     r, mass, 0 if neutral else charge, None, 0, 0))
        recalculate_particles_positions(particles, field, e_field, 0.001)
        field.draw(screen)
        e_field.draw(screen)

    while cat:
        screen.blit(background_image_1, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    starting = True
                    authors = False
                    cat = False


    while authors:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(background_image_2, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    starting = True
                    authors = False

pygame.quit()
