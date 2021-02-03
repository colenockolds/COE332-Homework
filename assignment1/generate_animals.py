import json
import petname
from random import randrange

head_list = ['snake', 'bull', 'lion', 'raven', 'bunny']

data = {}
data['animals'] = []
for i in range(20):
   a = randrange(2, 11, 2)
   l = randrange(3, 13, 3)
   data['animals'].append( {'head': head_list[randrange(1,5,1)], 'body': petname.name()+'-'+petname.name(), 'arms': a, 'legs': l, 'tail' : a+l} )

with open('animals.json', 'w') as out:
    json.dump(data, out, indent=2)
