import unittest
from adagency.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_generate_ad_endpoint(self):
        resp = self.client.post('/generate_ad_copy', json={'name': 'Widget', 'description': 'Great'})
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertIn('Widget', data['ad_copy'])


if __name__ == '__main__':
    unittest.main()
