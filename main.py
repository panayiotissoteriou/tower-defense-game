import enemies
from towers import *
import pygame
import towers

pygame.init()

# define screen dimensions
x1, y1 = 0, 0
x2, y2 = 1000, 750 #WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((x2, y2))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

# Create game objects once before the loop
# so their position changes persist between frames.
towers_built = [
    (towers.ArrowTower(), (100, 200)),
    (towers.ArtilleryTower(), (300, 400)),
    (towers.MagicTower(), (500, 500)),
]
enemies = [
    enemies.weakEnemy(),]

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen and draw the background and towers
    screen.fill((20, 20, 30))  # background color
    pygame.draw.line(screen, "gray82", (x1, y1), (x2, y2), 80)

    for tower, position in towers_built:
        tower.draw_range(screen, tower.colour, 1, 36)
        tower.appear(screen, tower.colour, position, 25)

        

    for enemy in enemies:
        enemy.move(enemy.move_by_x, enemy.move_by_y)
        if enemy.health <= 0:
            enemies.remove(enemy)
            pass #or break
        else:
            enemy.appear(screen, enemy.colour, enemy.position, 12)
    
    

    pygame.display.flip()
    clock.tick(60)

pygame.quit()