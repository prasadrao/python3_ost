import unittest
from find_regex import find_regex
class TestRegEx(unittest.TestCase):
    def test_find_regex(self):
        start = 231
        end = 250
        s, e = find_regex("""In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer. """)
        self.assertEqual(s, start, "Start position is not correct")
        self.assertEqual(e, end, "Start position is not correct")
