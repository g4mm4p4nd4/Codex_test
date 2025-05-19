import unittest
from adagency import register_user, authenticate


class UserTestCase(unittest.TestCase):
    def test_register_and_authenticate(self):
        self.assertTrue(register_user('alice', 'secret'))
        self.assertFalse(register_user('alice', 'again'))
        self.assertTrue(authenticate('alice', 'secret'))
        self.assertFalse(authenticate('alice', 'wrong'))


if __name__ == '__main__':
    unittest.main()
