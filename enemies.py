import math
import pygame


class Enemy:
    def __init__(self):
        self.health = 50
        self.max_health = self.health
        self.attack = 5
        self.position = [5, 5]
        self.move_by_x = 1
        self.move_by_y = 0.75
        self.path = None
        self.path_index = 0
        self.path_speed = 2.0
        self.target_point = None
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

    def set_path(self, path):
        if not path:
            self.path = []
            self.path_index = 0
            self.target_point = None
            return

        self.path = [list(point) for point in path]
        self.path_index = 1
        if len(self.path) > 1:
            self.position = list(self.path[0])
            self.target_point = self.path[1]
        else:
            self.position = list(self.path[0])
            self.target_point = self.path[0]

    def move(self, move_by_x=None, move_by_y=None):
        if self.path and len(self.path) > 1:
            if self.target_point is None:
                self.target_point = self.path[1]

            target_x, target_y = self.target_point
            current_x, current_y = self.position
            dx = target_x - current_x
            dy = target_y - current_y
            distance = math.hypot(dx, dy)

            if distance <= self.path_speed:
                self.position = [target_x, target_y]
                self.path_index += 1
                if self.path_index < len(self.path):
                    self.target_point = self.path[self.path_index]
                else:
                    self.target_point = self.path[-1]
                return self.position

            step_x = dx / distance * self.path_speed
            step_y = dy / distance * self.path_speed
            self.position = [current_x + step_x, current_y + step_y]
            return self.position

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
