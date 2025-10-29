import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def sample_products():
    return [
        Product("Телевизор", "40-дюймовый телевизор", 30000, 10),
        Product("Холодильник", "Двухкамерный холодильник", 45000, 5),
    ]


def test_category_init_and_products(sample_products):
    category = Category("Бытовая техника", "Описание", sample_products)
    assert category.name == "Бытовая техника"
    assert category.description == "Описание"
    assert len(category.products) == 2
    assert all(isinstance(p, Product) for p in category.products)


def test_category_counters(sample_products):
    Category.category_count = 0
    Category.product_count = 0

    category1 = Category("Техника 1", "desc", [sample_products[0]])
    assert isinstance(category1, Category)
    assert Category.category_count == 1
    assert Category.product_count == 1

    category2 = Category("Техника 2", "desc", [sample_products[1]])
    assert isinstance(category2, Category)
    assert Category.category_count == 2
    assert Category.product_count == 2

    category3 = Category("Пусто", "desc", [])
    assert isinstance(category3, Category)
    assert Category.category_count == 3
    assert Category.product_count == 2


def test_category_empty_products():
    category = Category("Книги", "Раздел книг", [])
    assert isinstance(category.products, list)
    assert len(category.products) == 0
