from abc import ABC, abstractmethod

class Tower(ABC):
    # self.position = position
    def __init__(self):
        self.damage = 5
        self.level = 1
        self.range = 5
        self.rate = 5
        self.position = [None, None]
        self.appearance = ""
        self.attack_symbol = ""

    @abstractmethod
    def build_position(self, ):
        pass
    
    @abstractmethod
    def attack_enemy(self, symbol):
        # TODO: if enemy within range, attack enemy with symbol
        pass
    
    @abstractmethod
    def appear(self, position):
        pass

class ArrowTower(Tower):
    def __init__(self):
        super().__init__()
    
class ArtilleryTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage = super().damage + 10
        self.rate = super().rate / 2


class MagicTower(Tower):
    def __init__(self):
        super().__init__()
        self.damage = super().damage + 5

class DefenderTower(Tower):
    # builds a wall
    def __init__(self):
        super().__init__()
        self.health = 50
