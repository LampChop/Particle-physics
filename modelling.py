from visualization import *


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    # body.Fx =
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        r = max(r, body.R)  # FIXME: обработка аномалий при прохождении одного тела сквозь другое
        pass  # FIXME: Взаимодействие объектов


def move(particle, dt):
    particle.x += particle.vx * dt
    particle.y += particle.vy * dt
    if particle.x >= window_width - particle.r:
        particle.vx *= -1
    if particle.x <= particle.r:
        particle.vx *= -1
    if particle.y >= window_height - particle.r:
        particle.vy *= -1
    if particle.y <= particle.r:
        particle.vy *= -1
def collision(p1, p2): #Прописать столкновение. Столкнувшиеся частицы на один фрейм меняют цвет немного, было бы прикольно
    pass
