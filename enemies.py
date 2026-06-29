from abc import ABC, abstractmethod
import pygame

class Enemy(ABC):
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.position = [5,5]
        self.x_or_y = "x"
        self.move_by_x = 2
        self.move_by_y = 1.5
        self.appearance = ""

    def lose_health(self, hit):
        # hit is a damage from a tower
        self.health -= hit

    def attack_defender():
        #not sure if needed, or if func in defender is needed
        pass
    
    @abstractmethod
    def move(self, move_by_x, move_by_y):
        # TODO: introduce some randomness, and somehow to always be going in the correct direction
        self.position = [self.position[0] + move_by_x, self.position[1] + move_by_y]
        return self.position

    @abstractmethod
    def appear(self, screen, colour, position, size=12):
        return pygame.draw.circle(screen, colour, position, size)

class weakEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.appearance = "w|w"
        self.colour = "red"
        self.points = 3

    def move(self, move_by_x, move_by_y):
        return super().move(move_by_x, move_by_y)

    def appear(self, screen, colour, position, size=12):
        return super().appear(screen, self.colour, position, size)


class TankEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.health += 50
        self.appearance = "O|O"

class FastEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.move_by += 1
        self.appearance = "(|)"
