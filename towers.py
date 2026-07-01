from abc import ABC, abstractmethod
import math
import pygame


class Tower(ABC):
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

    def get_build_position(self):
        pass

    def _get_range_points(self, radius, steps=36):
        if self.position[0] is None or self.position[1] is None:
            return []

        center_x, center_y = self.position
        points = []
        for i in range(steps):
            angle = 2 * math.pi * i / steps
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            points.append((x, y))

        self.range_coordinates = points
        return self.range_coordinates

    def draw_range(self, screen, colour=(255, 255, 255), width=1, steps=36):
        points = self._get_range_points(self.range, steps=steps)
        if points:
            pygame.draw.lines(screen, colour, True, points, width)
            pygame.draw.lines(screen, (255, 255, 255, 80), True, points, 1)

    def in_range(self, enemy_position):
        if self.position[0] is None or self.position[1] is None:
            return False

        tower_x, tower_y = self.position
        enemy_x, enemy_y = enemy_position
        distance = math.hypot(enemy_x - tower_x, enemy_y - tower_y)
        return distance <= self.range

    def attack_enemy(self, enemy):
        if self.in_range(enemy.position):
            enemy.lose_health(self.damage)
            return True
        return False

    def appear(self, screen, colour, position, size=25):
        return pygame.draw.circle(screen, colour, position, size)

class ArrowTower(Tower):
    def __init__(self):
        super().__init__()
        self.colour = "darkgoldenrod1"
        self.range_coordinates = self._get_range_points(self.range_coordinates, steps=36)
    
    def appear(self, screen, colour, position, size=25):
        return super().appear(screen, self.colour, position, size)
    
    def get_range_coordinates(self):
        return super()._get_range_points(self, self.range, steps=36)

class ArtilleryTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage = self.damage + 10
        self.rate = self.rate / 2
        self.colour = "dodgerblue4"

    def appear(self, screen, colour, position, size=25):
        return super().appear(screen, self.colour, position, size)


class MagicTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage = self.damage + 5
        self.range = self.range + 5
        self.colour = "darkorchid"

    def appear(self, screen, colour, position, size=25):
        return super().appear(screen, self.colour, position, size)

class DefenderTower(Tower):
    # builds a wall
    def __init__(self):
        super().__init__()
        self.health = 50
        self.colour = "darkorange4"
