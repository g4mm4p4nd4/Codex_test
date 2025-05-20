import unittest
from adagency import auth


class AuthTestCase(unittest.TestCase):
    def test_registration_and_login(self):
        username = 'user1'
        password = 'secret'
        self.assertTrue(auth.register_user(username, password))
        self.assertFalse(auth.register_user(username, password))
        self.assertTrue(auth.authenticate(username, password))
        self.assertFalse(auth.authenticate(username, 'wrong'))


if __name__ == '__main__':
    unittest.main()
