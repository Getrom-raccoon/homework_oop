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


def test_product_price_setter_zero():
    product = Product("Товар", "Описание", 10, 1)
    product.price = 0
    assert product.price == 0


def test_product_add_with_zero_quantity():
    product1 = Product("A", "desc", 500, 0)
    product2 = Product("B", "desc", 300, 0)
    assert product1 + product2 == 0


def test_product_price_setter_negative():
    """Тестирование установки отрицательной цены (setter)."""
    product = Product("Товар", "Описание", 5000, 5)
    product.price = -9999
    assert product.price == 0


def test_product_new_product_partial_data():
    """Тестирование создания Product из словаря с частью ключей."""
    data = {"name": "Demo", "price": 90, "quantity": 1}
    product = Product.new_product(data)
    assert product.name == "Demo"
    assert product.price == 90
    assert product.quantity == 1
    assert getattr(product, "description", None) in ("", None)


def test_product_str_empty_fields():
    """Тест str для товара с пустыми значениями."""
    product = Product("", "", 0, 0)
    assert str(product) == ", 0 руб. Остаток: 0 шт."


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
