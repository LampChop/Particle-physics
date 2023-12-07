from visualization import *
import math

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
        
        

def check_collision(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = math.sqrt(dx * dx + dy * dy)

    if distance < p1.r + p2.r and distance != 0:
        nx = dx / distance
        ny = dy / distance
        relative_velocity = [p2.vx - p1.vx, p2.vy - p1.vy]
        vel_along_normal = relative_velocity[0] * nx + relative_velocity[1] * ny

        if vel_along_normal > 0:
            # Частицы летят в разные стороны и все норм
            return

        e = 1  # коэффициент упругости

        j = -(1 + e) * vel_along_normal
        j /= 1 / p1.mass + 1 / p2.mass

        impulse = [j * nx, j * ny]

        p1.vx -= 1 / p1.mass * impulse[0]
        p1.vy -= 1 / p1.mass * impulse[1]
        p2.vx += 1 / p2.mass * impulse[0]
        p2.vy += 1 / p2.mass * impulse[1]

        # SРазъединяем частицы чтобы они не слиплись
        overlap = p1.r + p2.r - distance
        p1.x -= overlap / 2 * nx
        p1.y -= overlap / 2 * ny
        p2.x += overlap / 2 * nx
        p2.y += overlap / 2 * ny
