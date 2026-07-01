import pygame


class Enemy:
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.position = [5, 5]
        self.move_by_x = 1
        self.move_by_y = 0.75
        # self.appearance = ""
        self.money_worth = 50
        self.colour = "white"

    def lose_health(self, hit):
        self.health -= hit

    def die(self):
        if self.health <= 0:
            self.position = [None, None]
            return True
        return False

    def move(self, move_by_x=None, move_by_y=None):
        if move_by_x is None:
            move_by_x = self.move_by_x
        if move_by_y is None:
            move_by_y = self.move_by_y

        self.position = [self.position[0] + move_by_x, self.position[1] + move_by_y]
        return self.position

    def appear(self, screen, colour=None, position=None, size=12):
        if colour is None:
            colour = self.colour
        if position is None:
            position = self.position
        return pygame.draw.circle(screen, colour, position, size)


class weakEnemy(Enemy):
    def __init__(self):
        super().__init__()
        # self.appearance = "w|w"
        self.colour = "red"
        self.points = 3


class tankEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.health += 100
        self.move_by_x /= 1.5
        self.move_by_y /= 1.5
        # self.appearance = "O|O"
        self.colour = "blue"


class fastEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.move_by_x += 1
        self.move_by_y += 1
        # self.appearance = "(|)"
        self.colour = "yellow"
