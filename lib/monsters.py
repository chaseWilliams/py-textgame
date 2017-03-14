import random

class BaseMonster():
    def __init__(self):
        self.stats = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'speed': 0,
            'mana': 0
        }
        self.move_modifiers = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'speed': 0,
            'mana': 0
        }
        self.level_spawn
        self.moves = [
            self.attack
        ]

    def choose_move(self):
        self.rand_move()
        return self.move_modifiers

    def rand_move(self):
        move = random.choice(self.moves)
        move()

    def attack(self):
        self.move_modifiers['attack'] = self.stats['attack']

class Spider(BaseMonster):
    def __init__(self):
        BaseMonster.__init__(self)
        self.stats = {
            'health': 25,
            'attack': 5,
            'defense': 0,
            'speed': 1,
            'mana': 0
        }
        self.level_spawn = 0