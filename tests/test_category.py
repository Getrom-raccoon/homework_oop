import pytest
from src.category import Category
from src.product import Product

def test_category_add_product_increases_count():
    Category.category_count = 0
    Category.product_total = 0
    c = Category("Test", "Desc")
    p = Product("X", "Y", 100, 1)
    assert c.product_count == 0
    c.add_product(p)
    assert c.product_count == 1
    assert Category.product_total == 1

def test_category_str_empty_category():
    c = Category("Test", "Desc")
    assert str(c) == "Test, 0 шт."

def test_category_products_property_type():
    c = Category("Test", "Desc")
    assert isinstance(c.products, list)

@pytest.fixture
def sample_products():
    return [
        Product("A", "A", 30000, 10),
        Product("B", "B", 45000, 5)
    ]

def test_category_init_and_products(sample_products):
    category = Category("Cat", "Desc", sample_products)
    assert category.name == "Cat"
    assert category.description == "Desc"
    assert len(category.products) == 2
    assert all(isinstance(p, Product) for p in category.products)

def test_category_counters(sample_products):
    Category.category_count = 0
    Category.product_total = 0
    category1 = Category("Cat1", "Desc", [sample_products[0]])
    assert isinstance(category1, Category)
    assert Category.category_count == 1
    assert Category.product_total == 1
    category2 = Category("Cat2", "Desc", [sample_products[1]])
    assert Category.category_count == 2
    assert Category.product_total == 2
    category3 = Category("Cat3", "Desc")
    assert isinstance(category3, Category)
    assert Category.category_count == 3
    assert Category.product_total == 2

def test_category_empty_products():
    category = Category("Name", "Desc")
    assert isinstance(category.products, list)
    assert len(category.products) == 0

def test_category_str_representation(sample_products):
    category = Category("Test", "Desc", sample_products)
    result = str(category)
    assert result == "Test, 15 шт."

def test_category_add_product(sample_products):
    Category.category_count = 0
    Category.product_total = 0
    category = Category("Test", "Desc", [sample_products[0]])
    assert len(category.products) == 1
    category.add_product(sample_products[1])
    assert len(category.products) == 2
    assert Category.product_total == 2

def test_category_add_product_type_error():
    c = Category("Test", "Desc")
    with pytest.raises(TypeError):
        c.add_product("test")
