import enemies
from towers import *
import pygame
import towers

pygame.init()


# define screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Game loop
running = True

while running:
    # create a list to store towers built and draw them in the game loop
    towers_built = [(towers.ArrowTower(), (100, 200)), (towers.ArtilleryTower(), (300, 400)), (towers.MagicTower(), (500, 500))]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 30))  # background color
    pygame.draw.line(screen, "gray82", (0, 0), (WIDTH, HEIGHT),  80)

    # draw your towers, enemies, UI here
    if len(towers_built) == 0:
        towers_built = []
    elif len(towers_built) > 0:
        for tower, position in towers_built:
            tower.appear(screen, tower.colour, position, 25)

    # create enemies and draw them in the game loop
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()