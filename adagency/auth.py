"""Simple user registration and authentication helpers."""
import hashlib
from typing import Dict

try:
    import bcrypt
except ImportError:  # pragma: no cover - bcrypt may not be installed in tests
    bcrypt = None

from .models import User


_user_store: Dict[str, User] = {}


def _hash_password(password: str) -> str:
    if bcrypt is not None:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    return hashlib.sha256(password.encode()).hexdigest()


def _verify_password(password: str, hashed: str) -> bool:
    if bcrypt is not None:
        return bcrypt.checkpw(password.encode(), hashed.encode())
    return hashlib.sha256(password.encode()).hexdigest() == hashed


def register_user(username: str, password: str) -> bool:
    if username in _user_store:
        return False
    hashed = _hash_password(password)
    _user_store[username] = User(username=username, password_hash=hashed)
    return True


def authenticate(username: str, password: str) -> bool:
    user = _user_store.get(username)
    if not user:
        return False
    return _verify_password(password, user.password_hash)
