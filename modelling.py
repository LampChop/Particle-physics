from typing import Any

from visualization import *
import math
class physical_constants:
    def __init__(self, k, friction, friction_on, e):
        self.k = k
        self.friction = friction
        self.friction_on = friction_on
        self.e = e


model_constants = physical_constants(100 * scale_factor, 0.0001, True, 0.95)
re = 10 * scale_factor  # радиус, на котором отталкивание переходит в притяжение
D = 3 * scale_factor ** 3  # величина атомарной силы
a = 1 / scale_factor  # чем больше, тем близкодейственнее
segments_division = 1
segments = [[j for j in range(segments_division)] for i in range(segments_division)]
segment_width = window_width/segments_division*scale_factor
segment_height = window_height/segments_division*scale_factor

def calculate_segment(p):
    i = int(p.x/segment_width)
    j = int(p.y/segment_height)
    return [i, j]
def adjacent_segments(p1, p2):
    s1 = calculate_segment(p1)
    s2 = calculate_segment(p2)
    return(abs(s1[0] - s2[0]) < 2 and abs(s1[1] - s2[1]) < 2)
def move(particle, dt):
    """Рассчитывает движение частицы, проверяет столкновение частицы со стенами, корректирует движение после столкновения."""

    # print(calculate_segment(particle))
    ax = particle.Fx / particle.mass
    ay = particle.Fy / particle.mass
    particle.vx += ax * dt
    particle.vy += ay * dt
    particle.y += particle.vy * dt
    particle.x += particle.vx * dt
    if particle.x >= window_width*scale_factor - particle.r:
        particle.vx *= -1
        particle.x -= 2*(particle.x - window_width*scale_factor + particle.r)
    if particle.x <= particle.r:
        particle.vx *= -1
        particle.x += 2*(-particle.x + particle.r)
    if particle.y >= window_height*scale_factor - particle.r:
        particle.vy *= -1
        particle.y -= 2 * (particle.y - window_height * scale_factor + particle.r)
    if particle.y <= particle.r:
        particle.vy *= -1
        particle.y += 2*(particle.r - particle.y)
    # for i in range(3):
    #     if particle.color[i] < 255:
    #         particle.color[i] += 1

def check_collision(p1, p2):
    """Проверяет столкновение частиц друг с другом, корректирует их движение после столкновения."""

    #print(adjacent_segments(p1, p2))
    if(adjacent_segments(p1, p2)):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < p1.r + p2.r and distance != 0:
            print('collision happened')
            # for i in range(3):
            #     p1.color[i] = 0
            #     p2.color[i] = 0
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

            # Разъединяем частицы чтобы они не слиплись, массивные частицы более инертны
            m1 = p1.mass
            m2 = p2.mass
            k1 = m2/(m1 + m2)
            k2 = m1/(m1 + m2)
            overlap = p1.r + p2.r - distance
            p1.x -= overlap * k1 * nx
            p1.y -= overlap * k1 * ny
            p2.x += overlap * k2 * nx
            p2.y += overlap * k2 * ny


def calculate_force(particle, particles):
    """Рассчитывает проекции на оси x и y силы, действующей на тело со стороны других тел."""

    particle.Fx = particle.Fy = 0

    for obj in particles:
        if particle != obj and obj.q != 0 and adjacent_segments(particle, obj):
            r = ((particle.x - obj.x) ** 2 + (particle.y - obj.y) ** 2) ** 0.5 + scale_factor/2
            dx = obj.x - particle.x
            dy = obj.y - particle.y
            sin = dy / r
            cos = dx / r
            F = scale_factor**3 * (-1 * k * particle.q * obj.q) / (r ** 2)
            F_atom = 2 * D * (1 - np.exp(-a * (r - re))) * a * np.exp(-a * (r - re))
            if F_atom > 0:
                F += F_atom
            particle.Fx += F * cos
            particle.Fy += F * sin

def calculate_magnet_force(body, field):
    """Рассчитывает проекии на оси x и y силы со стороны магнитного поля, действующую на тело."""

    body.Fx += body.q*(body.vy/scale_factor)*(field.tesla*field.orient)
    body.Fy -= body.q*(body.vx/scale_factor)*(field.tesla*field.orient)

def calculate_e_force(body, e_field):
    """Рассчитывает силу со стороны электрического поля, действующую на тело."""

    body.Fx += body.q * e_field.orient * e_field.e

def recalculate_particles_positions(particles, field, e_field, dt):
    """Делает так, чтобы силы, действующие на тело, влияли на его движение."""

    for particle in particles:
        calculate_force(particle, particles)
        calculate_magnet_force(particle, field)
        calculate_e_force(particle, e_field)
    for particle in particles:
        move(particle, dt)

