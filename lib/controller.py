from lib.player import Player
from lib.monsters import Spider
import random


class Controller:

    def __init__(self):
        self.status = ''
        self.monsters = [
            Spider
        ]
    def start_game(self):
        self.player = Player()

    def fight(self):
        monster = self.create_monster(self.player.level)
        while True:
            print("player health: {0} \n{1} health: {2}".format(
                self.player.curr_stats['health'],
                monster.name,
                monster.curr_stats['health']
            ))
            player_move = self.player.choose_move()
            self.apply_status_changes(player_move, self.player, monster)
            if self.player.curr_stats['health'] <= 0:
                self.display_death_message(monster)
                break
            self.apply_status_changes(monster.choose_move, monster, self.player)
            if monster.curr_stats['health'] <= 0:
                self.display_success_message(monster)
                break


    def display_death_message(self, monster):
        print(monster.player_death_msg)

    def display_success_message(self, monster):
        print(monster.monster_death_msg)

    def apply_status_changes(self, action, action_doer, action_enemy):
        modifiers = action()
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
