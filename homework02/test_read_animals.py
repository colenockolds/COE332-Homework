import unittest
import sys

from read_animals import Breed

class TestReadAnimals(unittest.TestCase):

   def test_Breed(self):
      h,b,a,l,t = Breed(1,2)
      self.assertTrue(type(a) is int)
      self.assertTrue(type(l) is int)
      self.assertTrue(type(t) is int)
      #I tested to see if the number of arms, legs, and tails are integers because my Breed function was meant to be set up in a way to avoid any half arms legs or tails.

if __name__ == '__main__':
    unittest.main()
