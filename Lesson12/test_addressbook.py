import unittest
import addressbook

class TestEmailHandlers(unittest.TestCase):
    def setUp(self):
        self.email = 'test123@t.com'

    def test_email_delete(self):
        addressbook.email_add(self.email) # ensure the email is active
        self.assertEqual(addressbook.email_delete(self.email)[0], True)
        self.assertEqual(addressbook.email_delete(self.email)[0], False)

    def test_email_add(self):
        self.assertEqual(addressbook.email_add(self.email)[0], True)
        self.assertEqual(addressbook.email_add(self.email)[0], False)

    def test_email_display(self):
        addressbook.email_add(self.email)
        val, display = addressbook.email_display()
        self.assertTrue(self.email in display)

if __name__ == "__main__":
    unittest.main()
