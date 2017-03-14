from skills import *

class Player:

    def __init__(self):
        # starting values
        self.health = 100
        self.level = 1
        self.strength = 10
        self.mana = 5
        self.speed = 1
        self.skills = [
            StrongAttack()
        ]
    
    def attack():
        return self.strength

    def levelup():
        pass

    def defend():
        pass