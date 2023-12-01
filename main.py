import pygame
from visualization import *
from objects import *
from modelling import *
# def execution(delta):
#     """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
#     а также обновляя их положение на экране.
#     Цикличность выполнения зависит от значения глобальной переменной perform_execution.
#     При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
#     """
#     global model_time
#     global displayed_time
#     recalculate_positions([dr.obj for dr in space_objects], delta)
#     model_time += delta



#FIXME make open file

# def open_file():
#     """Открывает диалоговое окно выбора имени файла и вызывает
#     функцию считывания параметров системы небесных тел из данного файла.
#     Считанные объекты сохраняются в глобальный список space_objects
#     """
#     global space_objects
#     global browser
#     global model_time
#
#     model_time = 0.0
#     in_filename = "solar_system.txt"
#     space_objects = read_space_objects_data_from_file(in_filename)
#     max_distance = max([max(abs(obj.obj.x), abs(obj.obj.y)) for obj in space_objects])
#     calculate_scale_factor(max_distance)




# def init_ui(screen):
#     global browser
#     slider = thorpy.SliderX(100, (-10, 10), "Simulation speed")
#     slider.user_func = slider_reaction
#     button_stop = thorpy.make_button("Quit", func=stop_execution)
#     button_pause = thorpy.make_button("Pause", func=pause_execution)
#     button_play = thorpy.make_button("Play", func=start_execution)
#     timer = thorpy.OneLineText("Seconds passed")
#
#     button_load = thorpy.make_button(text="Load a file", func=open_file)
#
#     box = thorpy.Box(elements=[
#         slider,
#         button_pause,
#         button_stop,
#         button_play,
#         button_load,
#         timer])
#     reaction1 = thorpy.Reaction(reacts_to=thorpy.constants.THORPY_EVENT,
#                                 reac_func=slider_reaction,
#                                 event_args={"id": thorpy.constants.EVENT_SLIDE},
#                                 params={},
#                                 reac_name="slider reaction")
#     box.add_reaction(reaction1)
#
#     menu = thorpy.Menu(box)
#     for element in menu.get_population():
#         element.surface = screen
#
#     box.set_topleft((0, 0))
#     box.blit()
#     box.update()
#     return menu, box, timer
#FIXME make ui

particles = []
particles.append(particle(400, 250, -10, 10, (255, 255, 255)))
def main():
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('particles')
    pygame.display.flip()
    running = True
    while running:
        for p in particles:
            p.draw(screen)
            move(p, 0.05)
            print(p.x, p.y)
            pygame.display.update()
            screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
main()