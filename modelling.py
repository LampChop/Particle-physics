from visualization import *
k = 9

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
        F = (-1 * k * (particle.q) * (obj.q)) / (r ** 2)
        particle.Fx += F * cos
        particle.Fy += F * sin

def move_object(particle, dt):
    ax = particle.Fx / abs(particle.q)
    ay = particle.Fy / abs(particle.q)
    particle.vx += ax * dt
    particle.vy += ay * dt
    particle.y += particle.vy * dt
    particle.x += particle.vx * dt

def recalculate_particles_positions(particles, dt):
    for particle in particles:
        calculate_force(particle, particles)
    for particle in particles:
        move_object(particle, dt)
