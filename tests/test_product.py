from src.product import Product


def test_product_init():
    """Тест инициализации Product."""
    product = Product("Тестовый товар", "Описание", 30000.5, 15)
    assert product.name == "Тестовый товар"
    assert product.description == "Описание"
    assert product.price == 30000.5
    assert product.quantity == 15


def test_product_price_and_quantity():
    """Тест установки цены и количества товара."""
    product = Product("Товар", "Описание", 50000, 2)
    product.price = 60000
    assert product.price == 60000
    product.quantity = 3
    assert product.quantity == 3
    product.price = -100
    assert product.price == 0


def test_product_str_representation():
    """Тест строкового представления Product."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт."


def test_product_add():
    """Тест магического метода сложения продуктов."""
    product1 = Product("Товар A", "описание A", 100, 10)
    product2 = Product("Товар B", "описание B", 200, 2)
    result = product1 + product2
    assert result == 1400


def test_product_add_different_values():
    """Тест магического метода сложения с различными значениями."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB", 210000.0, 8)
    result = product1 + product2
    assert result == 180000.0 * 5 + 210000.0 * 8
    assert result == 2580000.0


def test_product_new_product_from_dict():
    """Тест создания Product из словаря."""
    data = {
        "name": "Тестовый товар",
        "description": "Описание товара",
        "price": 50000,
        "quantity": 10,
    }
    product = Product.new_product(data)
    assert product.name == "Тестовый товар"
    assert product.description == "Описание товара"
    assert product.price == 50000
    assert product.quantity == 10
