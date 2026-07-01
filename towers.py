import math
import pygame


class Tower:
    def __init__(self):
        self.damage = 5
        self.level = 1
        self.range = 100
        self.rate = 5
        self.position = [None, None]
        self.appearance = ""
        self.attack_symbol = ""
        self.colour = ""
        self.price = 50
        self.range_coordinates = []
        self.cooldown = 0
        self.target = None

    def get_build_position(self):
        return None

    def _get_range_points(self, radius, steps=36):
        if self.position[0] is None or self.position[1] is None:
            return []

        center_x, center_y = self.position
        points = []
        for i in range(steps):
            angle = 2 * math.pi * i / steps
            points.append((center_x + radius * math.cos(angle), 
                           center_y + radius * math.sin(angle)))

        self.range_coordinates = points
        return self.range_coordinates

    def draw_range(self, screen, colour=(255, 255, 255), width=1, steps=36):
        points = self._get_range_points(self.range, steps=steps)
        if points:
            pygame.draw.lines(screen, colour, True, points, width)

    def in_range(self, enemy_position):
        if self.position[0] is None or self.position[1] is None:
            return False

        tower_x, tower_y = self.position
        enemy_x, enemy_y = enemy_position
        distance = math.hypot(enemy_x - tower_x, enemy_y - tower_y)
        return distance <= self.range

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1

    def acquire_target(self, enemies):
        if self.target is not None:
            if self.target.health > 0 and self.in_range(self.target.position):
                return self.target
            self.target = None

        for enemy in enemies:
            if enemy.health > 0 and self.in_range(enemy.position):
                self.target = enemy
                return enemy

        self.target = None
        return None

    def attack_enemy(self, enemy):
        if enemy is None or enemy.health <= 0:
            return False

        if self.cooldown > 0:
            return False

        if self.in_range(enemy.position):
            enemy.lose_health(self.damage)
            self.cooldown = max(1, int(60 / max(1, self.rate)))
            return True
        return False

    def appear(self, screen, colour=None, position=None, size=25):
        if colour is None:
            colour = self.colour
        if position is None:
            position = self.position
        return pygame.draw.circle(screen, colour, position, size)


class ArrowTower(Tower):
    def __init__(self):
        super().__init__()
        self.colour = "darkgoldenrod1"


class ArtilleryTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage += 20
        self.rate /= 2
        self.colour = "dodgerblue4"


class MagicTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage += 15
        self.range += 5
        self.colour = "darkorchid"


class DefenderTower(Tower):
    def __init__(self):
        super().__init__()
        self.health = 50
        self.colour = "darkorange4"
