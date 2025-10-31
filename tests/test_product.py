from src.product import Product

def test_product_init():
    product = Product("Тестовый товар", "Описание", 30000.5, 15)
    assert product.name
    assert product.description == "Описание"
    assert product.price == 30000.5
    assert product.quantity == 15

def test_product_price_and_quantity():
    product = Product("Товар", "Описание", 50000, 2)
    product.price = 60000
    assert product.price == 60000
    product.quantity = 3
    assert product.quantity == 3
    product.price = -100
    assert product.price == 0
