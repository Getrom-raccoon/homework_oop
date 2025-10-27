import pytest
from src.product import Product

def test_product_init():
    product = Product("Телевизор", "40-дюймовый телевизор", 30000.5, 15)
    assert product.name == "Телевизор"
    assert product.description == "40-дюймовый телевизор"
    assert product.price == 30000.5
    assert product.quantity == 15

def test_product_price_setter_and_validation(capfd):
    product = Product("Ноутбук", "Описание", 50000, 2)
    product.price = 60000
    assert product.price == 60000

    product.price = 0  # Некорректная цена
    out = capfd.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 60000  # Цена не поменялась

    product.price = -100
    out = capfd.readouterr().out
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 60000

def test_product_quantity():
    product = Product("Мышь", "Обычная мышь", 700, 30)
    assert isinstance(product.quantity, int)
    assert product.quantity > 0
