import unittest
from adagency import UserProfile, segment_audience


class AudienceTestCase(unittest.TestCase):
    def test_segment_audience(self):
        users = [
            UserProfile(id=1, name='A', age=25, interests=[]),
            UserProfile(id=2, name='B', age=45, interests=[]),
            UserProfile(id=3, name='C', age=70, interests=[]),
        ]
        segments = segment_audience(users)
        self.assertEqual(len(segments), 3)


if __name__ == '__main__':
    unittest.main()
