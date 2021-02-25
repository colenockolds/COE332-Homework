import json
import sys
from random import randrange

animals = {}
with open(sys.argv[1], 'r') as f:
    animals = json.load(f)

def Breed(parent1,parent2):
   head = animals['animals'][(parent2)]['head']
   body = animals['animals'][(parent1)]['body']
   arms = round((animals['animals'][(parent1)]['arms']+animals['animals'][(parent2)]['arms'])/2)
   legs = round((animals['animals'][(parent1)]['legs']+animals['animals'][(parent2)]['legs'])/2)
   tail = round((animals['animals'][(parent1)]['tail']+animals['animals'][(parent2)]['tail'])/2)
   return head,body,arms,legs,tail

def main():
   r1 = randrange(1,20,1)
   r2 = randrange(1,20,1)

   animal1 = animals['animals'][(r1)]
   animal2 = animals['animals'][(r2)]

   print('Male Parent:')
   print(animal1)
   print('Female Parent:')
   print(animal2)

   h,b,a,l,t = Breed(r1,r2)
   print('Child:')
   print('head:',h,', body:',b,', arms:',a,', legs:',l,', tail:',t)

main()
