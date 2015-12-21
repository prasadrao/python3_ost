import unittest
from mathquiz import *

class TestMathquiz(unittest.TestCase):

    def setUp(self):
        self.x = 5
        self.y = 4
        self.ques = Q(a=self.x,b=self.y)

    def test_add_func(self):
        self.assertEqual(self.x + self.y, self.ques.answer)

    def test_time_taken(self):
        self.ques.start = 9 # start time in seconds
        self.ques.end = 15 # end time in seconds
        self.assertEqual((15 - 9), self.ques.time_taken())

if __name__ == "__main__":
    unittest.main()
