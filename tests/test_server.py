import json
import threading
import time
import unittest
import urllib.request

from adagency import server


class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpd = server.create_server(port=8001)
        cls.thread = threading.Thread(target=cls.httpd.serve_forever, daemon=True)
        cls.thread.start()
        time.sleep(0.1)

    @classmethod
    def tearDownClass(cls):
        cls.httpd.shutdown()
        cls.thread.join()

    def test_generate_endpoint(self):
        data = json.dumps({'product': 'Widget'}).encode()
        req = urllib.request.Request('http://127.0.0.1:8001/generate_ad_copy', data=data, method='POST', headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as resp:
            self.assertEqual(resp.status, 200)
            body = json.loads(resp.read())
            self.assertIn('Widget', body['ad_copy'])


if __name__ == '__main__':
    unittest.main()
