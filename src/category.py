from typing import List
from src.product import Product

class Category:
    """
    Класс для представления категории товаров.

    Содержит имя, описание, список товаров.
    """

    category_count = 0
    product_total = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализация категории с продуктами (или пустым списком).
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_total += len(self.products)

    @property
    def products(self) -> List[Product]:
        """
        Геттер для списка продуктов.
        """
        return self._products

    @products.setter
    def products(self, value):
        """
        Сеттер для списка продуктов.
        """
        self._products = value

    def add_product(self, product: Product):
        """
        Добавляет продукт в категорию, только если это экземпляр Product.
        """
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только экземпляр класса Product!")
        self.products.append(product)
        Category.product_total += 1

    @property
    def product_count(self) -> int:
        """
        Количество товаров в категории.
        """
        return len(self.products)

    def __str__(self):
        """
        Форматированная строка: 'Название категории, всего товаров: N'.
        """
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, {total_quantity} шт."
