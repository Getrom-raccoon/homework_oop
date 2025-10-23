import pytest
from src.products.product import Product
from src.products.category import Category

@pytest.fixture
def sample_products():
    return [
        Product("Телевизор", "40-дюймовый телевизор", 30000, 10),
        Product("Холодильник", "Двухкамерный холодильник", 45000, 5)
    ]

def test_category_init(sample_products):
    category = Category("Бытовая техника", "Категория бытовой техники", sample_products)
    assert category.name == "Бытовая техника"
    assert category.description == "Категория бытовой техники"
    assert len(category._Category__products) == 2

def test_category_counters(sample_products):
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Техника", "Описание", sample_products[:1])
    assert Category.category_count == 1
    assert Category.product_count == 1

    category2 = Category("Электроника", "Описание", sample_products[1:])
    assert Category.category_count == 2
    assert Category.product_count == 2
