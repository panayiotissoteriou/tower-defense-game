import enemies
from ui import draw_ui, get_clicked_button
from towers import *
from levels import LEVELS
import pygame
import towers

MAX_LIVES = 1

pygame.init()

# define screen dimensions
x1, y1 = 0, 0
x2, y2 = 1000, 750 #WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((x2, y2))
pygame.display.set_caption("Tower Defense")
clock = pygame.time.Clock()

current_level = LEVELS["default"]
path = current_level["path"]
build_spots = current_level.get("build_spots", [])
selected_tower_type = None
game_over = False


def get_clicked_build_spot(pos):
    for spot in build_spots:
        rect = pygame.Rect(
            spot["x"] - spot["size"] // 2,
            spot["y"] - spot["size"] // 2,
            spot["size"],
            spot["size"],
        )
        if rect.collidepoint(pos):
            return spot
    return None


def reset_level():
    global towers_built, enemy_group, money, lives, game_over
    towers_built = []
    enemy_group = [
        enemies.weakEnemy(),
        enemies.tankEnemy(),
        enemies.fastEnemy(),
    ]
    for index, enemy in enumerate(enemy_group):
        enemy.set_path(path)
        enemy.spawn_offset = index * enemy.spawn_gap
    money = 500
    lives = MAX_LIVES
    game_over = False


# Create game objects once before the loop
# so their position changes persist between frames.
towers_built = []
enemy_group = []
money = 500
lives = MAX_LIVES
reset_level()

# Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            reset_level()
            selected_tower_type = None
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            clicked = get_clicked_button(event.pos)
            if clicked is not None:
                selected_tower_type = clicked
                print(f"Selected tower: {clicked}")
            else:
                spot = get_clicked_build_spot(event.pos)
                if spot is not None and selected_tower_type is not None:
                    tower_class = {
                        "Arrow": towers.ArrowTower,
                        "Artillery": towers.ArtilleryTower,
                        "Magic": towers.MagicTower,
                        "Defender": towers.DefenderTower,
                    }.get(selected_tower_type)

                    if tower_class is not None:
                        new_tower = tower_class()
                        if money >= new_tower.price:
                            occupied = any(
                                tower.position[0] == spot["x"] and tower.position[1] == spot["y"]
                                for tower, _ in towers_built
                            )
                            if not occupied:
                                towers_built.append((new_tower, (spot["x"], spot["y"])))
                                money -= new_tower.price
                                print(f"Built {selected_tower_type} at {spot['x']}, {spot['y']}")
                            else:
                                print("Spot already occupied")
                        else:
                            print("Not enough money")

    # Clear the screen and draw the background and towers
    screen.fill((20, 20, 30))  # background color

    if path:
        pygame.draw.lines(screen, "gray82", False, path, 70)

    for spot in build_spots:
        rect = pygame.Rect(spot["x"] - spot["size"] // 2, spot["y"] - spot["size"] // 2, spot["size"], spot["size"])
        pygame.draw.rect(screen, (120, 120, 120), rect, 2)

    draw_ui(screen, money, selected_tower_type, lives)

    if game_over:
        overlay = pygame.Surface((x2, y2), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        screen.blit(overlay, (0, 0))

        font = pygame.font.Font(None, 72)
        text = font.render("GAME OVER", True, (255, 80, 80))
        text_rect = text.get_rect(center=(x2 // 2, y2 // 2))
        screen.blit(text, text_rect)

        small_font = pygame.font.Font(None, 32)
        restart_text = small_font.render("Press SPACE to restart", True, (255, 255, 255))
        restart_rect = restart_text.get_rect(center=(x2 // 2, y2 // 2 + 50))
        screen.blit(restart_text, restart_rect)

    # build towers
    for tower, position in towers_built:
        tower.update()
        tower.position = [position[0], position[1]]
        tower.draw_range(screen)
        tower.appear(screen, tower.colour, position, 25)
        tower.update_projectiles(screen)

    # draw enemies and move them
    for enemy in list(enemy_group):
        enemy.move()
        if enemy.health <= 0:
            enemy_group.remove(enemy)
            money += enemy.money_worth
            continue

        if enemy.path_index >= len(enemy.path):
            enemy_group.remove(enemy)
            lives -= 1
            if lives <= 0:
                game_over = True
            continue

        enemy.appear(screen, enemy.colour, enemy.position, 12)
        enemy.draw_health(screen)

    for tower, _ in towers_built:
        target = tower.acquire_target(enemy_group)
        tower.attack_enemy(target)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()