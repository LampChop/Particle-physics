import pygame
from visualization import *

left_rect = pygame.Rect(0, 0, window_width - ui_width, window_height)
right_rect = pygame.Rect(window_width - ui_width, 0, window_width, window_height)
grey = (200, 200, 200)
light_grey = (220, 220, 220)
dark_grey = (170, 170, 170)
black_text = (20, 20, 20)


class button:
    def __init__(self, screen, x, y, width, height, color, fontsize, text1, text2):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.font = pygame.font.Font(None, fontsize)
        self.text1 = self.font.render(text1, True, black_text)
        self.text2 = self.font.render(text2, True, black_text)
        self.pushed = False

    def show(self, screen):
        pygame.draw.rect(screen, self.color if not self.pushed else (self.color[0] - 30, self.color[1] - 30, self.color[2] - 30), pygame.Rect(self.x, self.y, self.width, self.y))
        screen.blit(self.text1 if not self.pushed else self.text2, (self.x + 10, self.y + 10))

    def is_clicked(self, event_pos):
        x_true = self.x + self.width >= event_pos[0] >= self.x
        y_true = self.y + self.height >= event_pos[1] >= self.y
        if(x_true and y_true):
            self.pushed = not self.pushed
        return x_true and y_true


class slider:
    def __init__(self, screen, x, y, width, height, color, knob_color, fontsize, text, knob_rect):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.knob_color = knob_color
        self.font = pygame.font.Font(None, fontsize)
        self.text = self.font.render(text, True, black_text)
        self.knob_rect = knob_rect  # Ползунок
        self.value = knob_rect.topleft[0]

    def show(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.knob_color, pygame.Rect(self.knob_rect.topleft[0] + self.x, self.knob_rect.topleft[1] + self.y, self.knob_rect.width, self.knob_rect.height))
        screen.blit(self.text, (self.x + 10, self.y - self.knob_rect.height/2))

    def is_clicked(self, event_pos):
        x_true = self.x + self.width >= event_pos[0] >= self.x
        y_true = self.y + self.knob_rect.topleft[1] + self.knob_rect.height >= event_pos[1] >= self.y + self.knob_rect.topleft[1]
        if x_true and y_true:
            self.value = (event_pos[0] - self.x)/self.width
            self.knob_rect.topleft = (event_pos[0] - self.x - 10, self.knob_rect.topleft[1])
        return x_true and y_true


def make_gui(screen, buttons, sliders):
    screen.fill((0, 0, 0), rect=left_rect)
    screen.fill((240, 240, 240), rect=right_rect)

    for button in buttons:
        button.show(screen)
    for slider in sliders:
        slider.show(screen)

    slider_font = pygame.font.Font(None, 36)
    slider_text = slider_font.render("Slider", True, black_text)
    screen.blit(slider_text, (115, 210))
