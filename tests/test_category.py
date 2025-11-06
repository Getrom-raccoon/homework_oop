import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    return [
        Product("Товар A", "описание A", 30000, 10),
        Product("Товар B", "описание B", 45000, 5),
    ]


def test_category_init_and_products(sample_products):
    category = Category("Категория", "описание", sample_products)
    assert category.name
    assert category.description
    assert len(category.products) == 2
    assert all(isinstance(p, Product) for p in category.products)


def test_category_counters(sample_products):
    Category.category_count = 0
    Category.product_total = 0
    category1 = Category("1", "desc", [sample_products[0]])
    assert isinstance(category1, Category)
    assert Category.category_count == 1
    assert Category.product_total == 1
    category2 = Category("2", "desc", [sample_products[1]])
    assert isinstance(category2, Category)
    assert Category.category_count == 2
    assert Category.product_total == 2
    category3 = Category("3", "desc")
    assert isinstance(category3, Category)
    assert Category.category_count == 3
    assert Category.product_total == 2


def test_category_empty_products():
    category = Category("Пустая категория", "нет товаров")
    assert isinstance(category.products, list)
    assert len(category.products) == 0
