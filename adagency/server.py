import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Tuple

from .generator import ProductInfo, generate_ad_copy


class AdRequestHandler(BaseHTTPRequestHandler):
    def _json_response(self, code: int, payload: dict):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode('utf-8'))

    def do_POST(self):
        if self.path != '/generate_ad_copy':
            self._json_response(404, {'error': 'Not Found'})
            return
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length)
        try:
            data = json.loads(body.decode('utf-8'))
            product = ProductInfo(name=data.get('product', ''))
            ad_copy = generate_ad_copy(product)
            self._json_response(200, {'ad_copy': ad_copy})
        except Exception as exc:
            self._json_response(400, {'error': str(exc)})


def create_server(host: str = '127.0.0.1', port: int = 8000) -> HTTPServer:
    return HTTPServer((host, port), AdRequestHandler)


def run_server(host: str = '127.0.0.1', port: int = 8000) -> None:
    server = create_server(host, port)
    try:
        print(f'Serving on http://{host}:{port}')
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
