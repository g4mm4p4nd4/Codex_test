import unittest
from adagency import generate_ad_copy, ProductInfo


class GeneratorTestCase(unittest.TestCase):
    def test_generate_ad_copy(self):
        product = ProductInfo(name='Widget', description='Fantastic')
        result = generate_ad_copy(product)
        self.assertIn('Widget', result)
        self.assertIn('Fantastic', result)


if __name__ == '__main__':
    unittest.main()
