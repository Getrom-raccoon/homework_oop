import pytest
from src.products.product import Product

def test_product_init():
    product = Product("Телевизор", "40-дюймовый телевизор", 30000, 10)
    assert product.name == "Телевизор"
    assert product.description == "40-дюймовый телевизор"
    assert product.price == 30000
    assert product.quantity == 10
