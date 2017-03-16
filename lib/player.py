from skills import *
from base import Base
import copy

class Player(Base):

    def __init__(self):
        # starting values
        Base.__init__(self)
        self.max_stats = {
            'health': 100,
            'attack': 10,
            'defense': 0,
            'mana': 5
        }
        self.curr_stats = copy.copy(self.max_stats)
        self.skills = [
            StrongAttack()
        ]
        self.level = 0
    
    def attack(self):
        self.move_modifiers['attack'] += self.curr_stats['attack']
        mods = self.reset_move_modifiers()
        return mods

    def levelup(self):
        pass

    def defend(self):
        pass

    def choose_move(self):
        choice = input("What will you do? attack OR defend\n> ")
        if choice == 'attack':
            return self.attack