import pygame
import numpy as np
import random as rnd
from visualization import *
from particle import *
from fields import *
from modelling import *
from menu import *
from gui import *

bunch = 1 # сколько частиц появляется за раз
neutral = False
radii = [10, 8]  # распределение масс
charges = [-1, 1]
charges_positive = list(filter(lambda x: x > 0, charges))
charges_negative = list(filter(lambda x: x < 0, charges))
x_velocities = y_velocities = 5*np.array([-2, -1, 0, 1, 2])
particles = []
count = 0
m_field = magnetic_field(0)
e_field = electric_field(0)

button_friction = button(screen, 50 + window_width - ui_width, 50, 140, 70, grey, 28, "Friction on", "Friction off" )
slider1knob = pygame.Rect(20, -15, 20, 70)
slider_friction = slider(screen, 50 + window_width - ui_width, 165, 150, 40, grey, dark_grey, 28, "Friction", slider1knob)
slider2knob = pygame.Rect(65, -15, 20, 70)
slider_force = slider(screen, 50 + window_width - ui_width, 260, 150, 40, grey, dark_grey, 28, "Electric force", slider2knob)
slider3knob = pygame.Rect(65, -15, 20, 70)
slider_electric_field = slider(screen, 50 + window_width - ui_width, 355, 150, 40, grey, dark_grey, 28, "Electric field", slider3knob)
slider4knob = pygame.Rect(65, -15, 20, 70)
slider_magnetic_field = slider(screen, 50 + window_width - ui_width, 450, 150, 40, grey, dark_grey, 28, "Magnetic field", slider4knob)
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
                starting = False
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

    mouse_down = False
    while game_1:
        pygame.display.update()
        make_gui(screen, [button_friction], [slider_friction, slider_force, slider_electric_field, slider_magnetic_field])
        for p in particles:
            p.draw(screen)
            move(p, 0.05)
            for other in particles:
                if p != other:
                    check_collision(p, other)
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
            if event.type == pygame.MOUSEBUTTONDOWN or event.type == MOUSEMOTION:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_down = True
                    if event.pos[0] < window_width - ui_width:

                        if event.button == 1 or event.button == 2 or event.button == 3:
                            mouse_pos = event.pos
                            for i in range(bunch):  # сколько частиц фигачим за раз
                                mass = rnd.choice(radii)
                                r = mass*scale_factor
                                if event.button == 1:
                                    charge = rnd.choice(charges_positive)
                                if event.button == 2:
                                    charge = 0
                                if event.button == 3:
                                    charge = rnd.choice(charges_negative)
                                particles.append(
                                    particle(mouse_pos[0]*scale_factor, mouse_pos[1]*scale_factor, rnd.choice(x_velocities)*scale_factor, rnd.choice(y_velocities)*scale_factor,
                                             r, mass, 0 if neutral else charge, None, 0, 0))  # создаем частицу и кладем в массив
                if mouse_down:
                    if button_friction.is_clicked(event.pos):
                        model_constants.friction_on = not model_constants.friction_on
                        if model_constants.friction_on:
                            print("friction is on!")
                        else:
                            print("friction is off!")

                    if slider_friction.is_clicked(event.pos):
                        model_constants.friction = 0.001 * slider_friction.value + 0.0001

                    if slider_force.is_clicked(event.pos):
                        model_constants.k = 400 * scale_factor * slider_force.value

                    if slider_electric_field.is_clicked(event.pos):
                        slider_electric_field.value = int((slider_electric_field.value * 10) + 0.5) / 10
                        slider_electric_field.knob_rect.topleft = (slider_electric_field.value * slider_electric_field.width - 10,
                        slider_electric_field.knob_rect.topleft[1])
                        e_field.field_value = (slider_electric_field.value - 0.5) * 40
                        e_field.orient = np.sign(e_field.field_value)

                    if slider_magnetic_field.is_clicked(event.pos):
                        slider_magnetic_field.value = int((slider_magnetic_field.value * 10) + 0.5) / 10
                        slider_magnetic_field.knob_rect.topleft = (
                            slider_magnetic_field.value * slider_magnetic_field.width - 10,
                            slider_magnetic_field.knob_rect.topleft[1])
                        m_field.field_value = (slider_magnetic_field.value - 0.5) * 40
                        m_field.orient = np.sign(m_field.field_value)

            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False


        recalculate_particles_positions(particles, m_field, e_field, 0.001)
        e_field.draw(screen)
        m_field.draw(screen)
        '''При выборе Мяу перекидывает в дисплей с картинкой Шлепы'''

    while cat:
        screen.blit(background_image_1, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:  # логическое переобозначение, дабы вернуться в меню при нажатии на пробел
                if event.key == K_SPACE:
                    starting = True
                    authors = False
                    cat = False

    '''При выборе авторы перекидывает в дисплей с фоткой авторов, то есть нас'''

    while authors:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.blit(background_image_2, (0, 0))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:  # логическое переобозначение, дабы вернуться в меню при нажатии на пробел
                if event.key == K_SPACE:
                    starting = True
                    authors = False

pygame.quit()
