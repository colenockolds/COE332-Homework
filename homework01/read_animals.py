import json
from random import randrange

animals = {}
with open('animals.json','r') as f:
    animals = json.load(f)

print(animals['animals'][(randrange(1,20,1))])
