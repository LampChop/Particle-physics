from pygame import*

init()

size = (800, 600)

screen = display.set_mode(size)

ARIAL_50 = font.SysFont('arial', 50)

class Menu:
    """Класс меню."""

    def __init__(self):
        """Функция инициализации."""

        """self._option_surfaces -- список опций
           self._callbacks -- список клавиш, соответствующих некоторой опции, нажав на которую, эта опция откроется
           self._current_option_index -- индекс опции, на которой находится "курсор"
           
         """

        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0

    def append_option(self, option, callback):
        """Добавляет в список опций новую опцию, в список откликов -- соответствующую клавишу, нажав на которую, опция откроется"""

        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)

    def draw(self, surf, x, y, option_y_padding):
        """Рисует опции."""

        for i, option in enumerate (self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)

    def switch(self, direction):
        """Позволяет перескакивать с одной опции на другую."""

        global _current_option_index
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        """Открывает соответствующую опцию"""

        self._callbacks[self._current_option_index]()

