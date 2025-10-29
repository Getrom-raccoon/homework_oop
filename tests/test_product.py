from src.product import Product


def test_product_init():
    product = Product("Телевизор", "40-дюймовый телевизор", 30000.5, 15)
    assert product.name == "Телевизор"
    assert product.description == "40-дюймовый телевизор"
    assert product.price == 30000.5
    assert product.quantity == 15


def test_product_price_and_quantity():
    product = Product("Ноутбук", "Мощный", 50000, 2)
    product.price = 60000
    assert product.price == 60000
    product.quantity = 3
    assert product.quantity == 3
