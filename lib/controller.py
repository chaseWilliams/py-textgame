from player import Player
from monsters import Spider
import math

monsters = [
    Spider
]

def start_game():
    player = Player()
    fight()


def fight():
    monster = create_monster(player.level)
    while end_fight == False:
        pass

def create_monster(level):
    possible_monsters = []
    for monster in monsters:
        if math.abs(monster.spawn_level - level) <= 5:
            possible_monsters.append(monster)
    monster = random.choice(possible_monsters)
    return monster()