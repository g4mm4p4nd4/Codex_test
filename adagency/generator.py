from .models import ProductInfo


def generate_ad_copy(product: ProductInfo) -> str:
    """Generate advertisement copy from product information."""
    lines = [f"Introducing {product.name}!"]
    if product.description:
        lines.append(product.description)
    lines.append("Order today and see the difference.")
    return " ".join(lines)
