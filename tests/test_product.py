import pytest
from src.product import Product


def test_product_constructor_zero_negative_price():
    p1 = Product("A", "B", 123, 1)
    assert p1.price == 123
    p2 = Product("A", "B", 0, 2)
    assert p2.price == 0
    p3 = Product("A", "B", -5, 5)
    assert p3.price == 0


def test_product_price_setter_branch():
    p = Product("X", "Y", 50, 1)
    p.price = 77
    assert p.price == 77
    p.price = -77
    assert p.price == 0
    p.price = 0
    assert p.price == 0


def test_product_quantity_init():
    p = Product("A", "B", 11, 5)
    assert p.quantity == 5


def test_product_add_with_zero_quantity():
    product1 = Product("A", "desc", 500, 0)
    product2 = Product("B", "desc", 300, 0)
    assert product1 + product2 == 0


def test_product_new_product_partial_data():
    data = {"name": "Demo", "price": 90, "quantity": 1}
    product = Product.new_product(data)
    assert product.name == "Demo"
    assert product.price == 90
    assert product.quantity == 1


def test_product_str_empty_fields():
    product = Product("", "", 0, 0)
    assert str(product) == ", 0 руб. Остаток: 0 шт."


def test_product_str_representation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
    result = str(product)
    assert result == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_product_add():
    product1 = Product("A", "A", 100, 10)
    product2 = Product("B", "B", 200, 2)
    result = product1 + product2
    assert result == 1400


def test_product_add_different_values():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    result = product1 + product2
    assert result == 180000.0 * 5 + 210000.0 * 8


def test_product_new_product_from_dict():
    data = {"name": "Example", "description": "Desc", "price": 50000, "quantity": 10}
    product = Product.new_product(data)
    assert product.name == "Example"
    assert product.description == "Desc"
    assert product.price == 50000
    assert product.quantity == 10


def test_product_add_type_error():
    product = Product("A", "B", 100, 1)
    with pytest.raises(TypeError):
        product + 5
