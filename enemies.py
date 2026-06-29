from abc import ABC, abstractmethod

class Enemy(ABC):
    def __init__(self):
        self.health = 50
        self.attack = 5
        self.position = [0,0]
        self.x_or_y = "x"
        self.move_by = 1
        self.appearance = ""

    def lose_health(self, hit):
        # hit is a damage from a tower
        self.health -= hit

    def attack_defender():
        #not sure if needed, or if func in defender is needed
        pass

    def move(self, move_by):
        # TODO: introduce some randomness, and somehow to always be going in the correct direction
        x = self.position[0]
        y = self.position[1]

        if x > y:
            self.x_or_y = "y"
            self.position[0] += move_by
        else:
            self.x_or_y = "x"
            self.position[1] += move_by

    @abstractmethod
    def appear():
        # get position
        # make icon appear at those coordinates
        pass
        

class weakEnemy(Enemy):
    def __init__(self):
        super().__init__()
        self.appearance = "w|w"


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
