

import copy

class Base:
    def __init__(self):
        self.max_stats = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'mana': 0
        }
        self.curr_stats = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'mana': 0
        }
        self.move_modifiers = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'mana': 0
        }
        self.moves = [
            self.attack
        ]
    
    def reset_move_modifiers(self):
        mods = copy.copy(self.move_modifiers)
        self.move_modifiers = {
            'health': 0,
            'attack': 0,
            'defense': 0,
            'mana': 0
        }
        return mods