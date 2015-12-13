import unittest
from furnishing import *

class test_map_the_home(unittest.TestCase):

    def setUp(self):
        self.home = [Bed('BedRoom'), Sofa('Living Room') ]

    def test_map_the_home(self):
        m = map_the_home(self.home)
        self.assertEqual(Bed, type(m['BedRoom'][0]))
        self.assertEqual(Sofa, type(m['Living Room'][0]))

if __name__ == "__main__":
    unittest.main()
