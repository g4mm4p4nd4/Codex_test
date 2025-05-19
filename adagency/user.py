import hashlib
from dataclasses import dataclass
from typing import Dict


@dataclass
class User:
    username: str
    password_hash: str


_users: Dict[str, User] = {}


def _hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def register_user(username: str, password: str) -> bool:
    """Register a new user. Returns False if user already exists."""
    if username in _users:
        return False
    _users[username] = User(username, _hash_password(password))
    return True


def authenticate(username: str, password: str) -> bool:
    """Authenticate a user with the given password."""
    user = _users.get(username)
    if not user:
        return False
    return user.password_hash == _hash_password(password)
