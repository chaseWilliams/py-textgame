from lib.player import Player
from lib.monsters import Spider
import random

class PlayerDeath(Exception):
    pass

class Controller:

    def __init__(self):
        self.status = ''
        self.monsters = [
            Spider
        ]
        self.player_dead = False
        
    def start_game(self):
        self.player = Player()

    def fight(self):
        monster = self.create_monster(self.player.level)
        while True:
            print("player health: {0} player mana: {1}\n{2} health: {3}".format(
                self.player.curr_stats['health'],
                self.player.curr_stats['mana'],
                monster.name,
                monster.curr_stats['health']
            ))
            player_move = self.player.choose_move()
            self.apply_status_changes(player_move, self.player, monster)
            if monster.curr_stats['health'] <= 0:
                self.display_success_message(monster)
                self.player.gain_exp(monster.exp)
                break
            self.apply_status_changes(monster.choose_move(), monster, self.player)
            if self.player.curr_stats['health'] <= 0:
                self.display_death_message(monster)
                self.player_dead = True
                raise PlayerDeath()
                
        return monster

    def display_death_message(self, monster):
        print(monster.player_death_msg)

    def display_success_message(self, monster):
        print(monster.monster_death_msg)

    def apply_status_changes(self, modifiers, action_doer, action_enemy):
        action_doer.curr_stats['health'] += modifiers['health']
        action_doer.curr_stats['mana'] -= modifiers['mana']
        action_doer.curr_stats['defense'] += modifiers['defense']
        action_enemy.curr_stats['health'] -= modifiers['attack']

    def create_monster(self, level):
        possible_monsters = []
        for monster in self.monsters:
            if abs(monster().level_spawn - level) <= 5:
                possible_monsters.append(monster)
        monster_klass = random.choice(possible_monsters)
        return monster_klass()
