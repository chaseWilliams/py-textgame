import random
from lib.base import Base
import copy

class BaseMonster(Base):
    def __init__(self):
        Base.__init__(self)
        self.level_spawn = 0
        self.player_death_msg = ''
        self.monster_death_msg = ''

    def choose_move(self):
        self.rand_move()
        mods = self.reset_move_modifiers()
        return mods

    def rand_move(self):
        move = random.choice(self.moves)
        move()

    def attack(self):
        self.move_modifiers['attack'] = self.curr_stats['attack']

class Spider(BaseMonster):
    def __init__(self):
        BaseMonster.__init__(self)
        self.max_stats = {
            'health': 25,
            'attack': 5,
            'defense': 0,
            'mana': 0
        }
        self.curr_stats = copy.copy(self.max_stats)
        self.level_spawn = 0
        self.player_death_msg = "You were eviscerated by the spider's fangs"
        self.monster_death_msg = "You slayed the spider!"
