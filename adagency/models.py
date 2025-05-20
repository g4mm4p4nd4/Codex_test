from dataclasses import dataclass


@dataclass
class ProductInfo:
    name: str
    description: str = ""
    audience: str = ""


@dataclass
class User:
    username: str
    password_hash: str
