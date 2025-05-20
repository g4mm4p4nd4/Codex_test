"""Flask application exposing the AI Ad Agency API."""
from flask import Flask, jsonify, request

from .generator import generate_ad_copy
from .models import ProductInfo
from .auth import register_user, authenticate

app = Flask(__name__)


@app.post('/generate_ad_copy')
def generate_ad():
    data = request.get_json() or {}
    product = ProductInfo(
        name=data.get('name', ''),
        description=data.get('description', ''),
        audience=data.get('audience', ''),
    )
    ad_copy = generate_ad_copy(product)
    return jsonify({'ad_copy': ad_copy})


@app.post('/register')
def register():
    data = request.get_json() or {}
    if register_user(data.get('username', ''), data.get('password', '')):
        return jsonify({'status': 'registered'}), 201
    return jsonify({'error': 'user_exists'}), 400


@app.post('/login')
def login():
    data = request.get_json() or {}
    if authenticate(data.get('username', ''), data.get('password', '')):
        return jsonify({'status': 'ok'})
    return jsonify({'error': 'invalid_credentials'}), 401


if __name__ == '__main__':  # pragma: no cover
    app.run(debug=True)
