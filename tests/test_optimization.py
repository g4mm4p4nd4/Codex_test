import unittest
from adagency import recommend_budget


class OptimizationTestCase(unittest.TestCase):
    def test_recommend_budget(self):
        performance = {'A': 10.0, 'B': 30.0}
        result = recommend_budget(performance)
        self.assertAlmostEqual(result['A'] + result['B'], 1.0)


if __name__ == '__main__':
    unittest.main()
