from lib.skills import *
from lib.base import Base
import copy

class Player(Base):

    def __init__(self):
        # starting values
        Base.__init__(self)
        self.max_stats = {
            'health': 100,
            'attack': 10,
            'defense': 1,
            'mana': 5
        }
        self.curr_stats = copy.copy(self.max_stats)
        self.skills = [
            StrongAttack()
        ]
        self.level = 1
        self.to_next_level = 0
    
    def attack(self):
        self.move_modifiers['attack'] += self.curr_stats['attack']
        mods = self.reset_move_modifiers()
        return mods

    def gain_exp(self, exp):
        gained_exp = 1 / self.level * 20 * exp + self.to_next_level
        while gained_exp < 100:
            self.level += 1
            print('You are now level {0}'.format(self.level))
            gained_exp -= 100
        self.to_next_level = gained_exp
        

    def choose_move(self):
        print("What will you do?\nattack\nnothing")
        for skill in self.skills:
            print(skill.name)
        choice = input("> ")
        if choice == 'attack':
            mods = self.attack()
            return mods
        elif choice == 'nothing':
            return {
                'health': 0,
                'attack': 0,
                'defense': 0,
                'mana': 0
            }
        else:
            for skill in self.skills:
                if choice == skill.name:
                    return skill.use()
