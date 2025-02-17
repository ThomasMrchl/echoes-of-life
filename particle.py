import random
import math
import pygame
from settings import WIDTH, HEIGHT, NUM_PARTICLES, ATTRACTION_RADIUS, SPEED, COLORS, ATTRACTION_MATRIX

class Particle:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.vx = random.uniform(-SPEED /2, SPEED /2)
        self.vy = random.uniform(-SPEED /2, SPEED /2)
        self.color = random.choice(COLORS)
        self.color_index = COLORS.index(self.color)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= WIDTH:
            self.vx *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.vy *= -1

    def attract(self, particles):
        for particle in particles:
            if particle == self:
                continue

            distance = math.hypot(self.x - particle.x, self.y - particle.y)
            if distance < ATTRACTION_RADIUS:
                attraction_force = ATTRACTION_MATRIX[self.color_index][particle.color_index]
                self.vx += (particle.x - self.x) * attraction_force
                self.vy += (particle.y - self.y) * attraction_force
                if random.random() < 0.01:
                    # SOUND.play()
                    pass
