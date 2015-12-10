import unittest
from ccn_safety2 import ccn_safety

text = """Have you ever noticed, in television and movies, that phone numbers and credit cards
are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number
that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and
security experts."""

class TestRegex(unittest.TestCase):

    def test_ccn_safety(self):
        response = ccn_safety(text)
        self.assertFalse("5555-5555-5555-5555" in response)
        self.assertTrue("CCN REMOVED FOR YOUR SAFETY" in response)

if __name__ == "__main__":
    unittest.main()
