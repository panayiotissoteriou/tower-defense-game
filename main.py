import enemies
import towers
import pygame

pygame.init()

# define screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 30))  # background color

    # draw your towers, enemies, UI here
    pygame.draw.rect(screen, (0, 255, 0), (100, 100, 50, 50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()