from dataclasses import dataclass


@dataclass
class ProductInfo:
    name: str


def generate_ad_copy(product: ProductInfo) -> str:
    """Generate simple advertisement copy from product information."""
    return f"Buy {product.name} now!"
