import pygame
from particle import Particle
from settings import WIDTH, HEIGHT, NUM_PARTICLES, BACKGROUND_COLOR

pygame.init()
pygame.mixer.init()

#window creation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echoes of Life")
clock = pygame.time.Clock()

particles = [Particle() for _ in range(NUM_PARTICLES)]

going = True
while going:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False

    for particle in particles:
        particle.attract(particles)
        particle.move()

        # print(f"Particle position: x={particle.x}, y={particle.y}")
        pygame.draw.circle(screen, particle.color, (particle.x, particle.y), 2)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


