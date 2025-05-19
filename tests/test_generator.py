import unittest
from adagency import generate_ad_copy, generator


class GeneratorTestCase(unittest.TestCase):
    def test_generate_ad_copy(self):
        product = generator.ProductInfo(name='Widget')
        result = generate_ad_copy(product)
        self.assertIn('Widget', result)


if __name__ == '__main__':
    unittest.main()
