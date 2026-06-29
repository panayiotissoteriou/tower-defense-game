from abc import ABC, abstractmethod
import math
import pygame

class Tower(ABC):
    # self.position = position
    def __init__(self):
        self.damage = 5
        self.level = 1
        self.range = 50
        self.rate = 5
        self.position = [None, None]
        self.appearance = ""
        self.attack_symbol = ""
        self.colour = ""

    def get_build_position(self, ):
        # TODO: return the position where the tower is built
        pass

    def _get_range_points(self, steps=36):
        if self.position[0] is None or self.position[1] is None:
            return []

        center_x, center_y = self.position
        points = []
        for i in range(steps):
            angle = 2 * math.pi * i / steps
            x = center_x + self.range * math.cos(angle)
            y = center_y + self.range * math.sin(angle)
            points.append((x, y))
        return points

    def draw_range(self, screen, colour=(255, 255, 255), width=1, steps=36):
        points = self._get_range_points(steps=steps)
        if points:
            pygame.draw.lines(screen, colour, True, points, width)
            pygame.draw.lines(screen, (255, 255, 255, 80), True, points, 1)

    def attack_enemy(self, enemy_position_x, enemy_position_y):
        # TODO: if enemy within range, attack enemy with symbol
        pass

    @abstractmethod
    def appear(self, screen, colour, position, size=25):
        return pygame.draw.circle(screen, colour, position, size)

class ArrowTower(Tower):
    def __init__(self):
        super().__init__()
        self.colour = "darkgoldenrod1"
    
    def appear(self, screen, colour, position, size=25):
        return super().appear(screen, self.colour, position, size)

class ArtilleryTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage = self.damage + 10
        self.rate = self.rate / 2
        self.colour = "firebrick1"

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
        self.colour = "gray59"
