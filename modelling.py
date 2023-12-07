from visualization import *
import math
k = 9

def move(particle, dt):
    ax = particle.Fx / particle.q
    ay = particle.Fy / particle.q
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
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    distance = math.sqrt(dx * dx + dy * dy)

    if distance < p1.r + p2.r and distance != 0:
        print('collision happened')
        for i in range(3):
            p1.color[i] = 0
            p2.color[i] = 0
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

        # Разъединяем частицы чтобы они не слиплись
        overlap = p1.r + p2.r - distance
        p1.x -= overlap / 2 * nx
        p1.y -= overlap / 2 * ny
        p2.x += overlap / 2 * nx
        p2.y += overlap / 2 * ny

def calculate_force(particle, particles):
    particle.Fx = particle.Fy = 0
    for obj in particles:
        if particle == obj:
            continue
        r = ((particle.x - obj.x) ** 2 + (particle.y - obj.y) ** 2) ** 0.5 + 0.5
        dx = obj.x - particle.x
        dy = obj.y - particle.y
        sin = dy / r
        cos = dx / r
        F = (k * (particle.q) * (obj.q)) / (r ** 2)
        particle.Fx += F * cos
        particle.Fy += F * sin

  

def recalculate_particles_positions(particles, dt):
    for particle in particles:
        calculate_force(particle, particles)
    for particle in particles:
        move(particle, dt)
