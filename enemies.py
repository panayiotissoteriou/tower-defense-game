import pygame


class Enemy:
    def __init__(self):
        self.health = 50
        self.max_health = self.health
        self.attack = 5
        self.position = [5, 5]
        self.move_by_x = 1
        self.move_by_y = 0.75
        # self.appearance = ""
        self.money_worth = 50
        self.colour = "white"

    def lose_health(self, hit):
        self.health -= hit
        self.health = max(0, self.health)

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

    def draw_health(self, screen):
        if self.position[0] is None or self.position[1] is None:
            return

        bar_width = 40
        bar_height = 6
        x, y = self.position
        bar_x = x - bar_width // 2
        bar_y = y - 18

        pygame.draw.rect(screen, (40, 40, 40), (bar_x, bar_y, bar_width, bar_height))
        if self.max_health > 0:
            health_width = int((self.health / self.max_health) * bar_width)
            health_width = max(0, min(bar_width, health_width))
            pygame.draw.rect(screen, (0, 220, 0), (bar_x, bar_y, health_width, bar_height))


class weakEnemy(Enemy):
    def __init__(self):
        super().__init__()
        # self.appearance = "w|w"
        self.colour = "red"
        self.max_health = self.health


class tankEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.health += 100
        self.max_health = self.health
        self.move_by_x /= 1.5
        self.move_by_y /= 1.5
        # self.appearance = "O|O"
        self.colour = "blue"
        self.money_worth *= 2


class fastEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.move_by_x += 1
        self.move_by_y += 1
        self.health -= 20
        self.max_health = self.health
        # self.appearance = "(|)"
        self.colour = "yellow"
        self.money_worth *= 1.2
