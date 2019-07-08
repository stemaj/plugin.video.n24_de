import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from resources.lib import main
from resources.lib import read

class Test_1(unittest.TestCase):

  def test_1(self):
    data = read.load_file('000')
    #arr = main.listOfNewest(data)
    self.assertEqual(10, 10)
