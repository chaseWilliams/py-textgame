from lib.controller import Controller
import json

game = Controller()
game.start_game()
# beginning scene
begin_file = open('txt/begin.txt', 'r')
begin_dialogue = list(begin_file)
print(begin_dialogue[0])

envs = open('lib/environment.json')
print(json.loads(envs.read()))
"""
episodes = 2
for i in range(episodes):
    random_env = 
"""
# ending scene
end_file = open('txt/end.txt', 'r')
end_dialogue = list(end_file)
print(end_dialogue[0])