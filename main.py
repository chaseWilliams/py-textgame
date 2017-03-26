from lib.controller import Controller, PlayerDeath
import json
import random

game = Controller()
game.start_game()

# beginning scene
begin_file = open('txt/begin.txt', 'r')
begin_dialogue = list(begin_file)
print(begin_dialogue[0])

envs = open('lib/environment.json')
data = json.loads(envs.read())
episodes = data['episodes']

def view(episode):
    print(episode['desc'])
    actions = list(episode['actions'].keys())
    possible_choices = range(len(actions))
    action_map = dict(zip(possible_choices, actions))
    for i in possible_choices:
        key = action_map[i]
        print("{0}: {1}".format(i, key))
    return action_map

def play_episode(episode, choice, action_map):
    action = action_map[choice]
    scenario = episode['actions'][action]
    result = scenario[1]
    if result == 'walk':
        print(scenario[0])
    elif result == 'monster':
        print(scenario[0])
        try:
            monster = game.fight()
        except PlayerDeath:
            pass
        else:
            print(scenario[2])
    elif result == 'regain':
        print(scenario[0])
        game.regain()
        print(scenario[2])

num_episodes = 5

for i in range(num_episodes):
    if game.player_dead:
        break
    random_episode = random.choice(episodes)
    action_map = view(random_episode)
    choice = int(input("> "))
    play_episode(random_episode, choice, action_map)

# ending scene
end_file = open('txt/end.txt', 'r')
end_dialogue = list(end_file)
if game.player_dead:
    print(end_dialogue[1])
else:
    print(end_dialogue[0])