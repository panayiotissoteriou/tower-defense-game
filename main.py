import enemies
from ui import draw_ui, get_clicked_button
from towers import *
from levels import LEVELS
import pygame
import towers

pygame.init()

# define screen dimensions
x1, y1 = 0, 0
x2, y2 = 1000, 750 #WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((x2, y2))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

current_level = LEVELS["default"]
path = current_level["path"]
build_spots = current_level["build_spots"]

# Create game objects once before the loop
# so their position changes persist between frames.
towers_built = [
    (towers.ArrowTower(), (150, 200)),
    (towers.ArtilleryTower(), (425, 400)),
    (towers.MagicTower(), (700, 600)),
]
enemies = [
    enemies.weakEnemy(),
    enemies.tankEnemy(),
    enemies.fastEnemy(),
]
for enemy in enemies:
    enemy.set_path(path)
money = 100

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = get_clicked_button(event.pos)
            if clicked is not None:
                print(f"Selected tower: {clicked}")

    # Clear the screen and draw the background and towers
    screen.fill((20, 20, 30))  # background color

    if path:
        pygame.draw.lines(screen, "gray82", False, path, 70)

    for spot in build_spots:
        rect = pygame.Rect(spot["x"] - spot["size"] // 2, spot["y"] - spot["size"] // 2, spot["size"], spot["size"])
        pygame.draw.rect(screen, (120, 120, 120), rect, 2)

    draw_ui(screen, money)

    # build towers
    for tower, position in towers_built:
        tower.update()
        tower.position = [position[0], position[1]]
        tower.draw_range(screen)
        tower.appear(screen, tower.colour, position, 25)
        tower.update_projectiles(screen)

    # draw enemies and move them
    for enemy in list(enemies):
        enemy.move()
        if enemy.health <= 0:
            enemies.remove(enemy)
            money += enemy.money_worth
            continue

        enemy.appear(screen, enemy.colour, enemy.position, 12)
        enemy.draw_health(screen)

    for tower, _ in towers_built:
        target = tower.acquire_target(enemies)
        tower.attack_enemy(target)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()