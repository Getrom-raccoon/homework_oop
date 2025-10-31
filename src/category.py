from typing import List
from src.product import Product


class Category:

    category_count = 0
    product_total = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализация Category.

        Args:
            name: Название категории.
            description: Описание категории.
            products: Список товаров (по умолчанию пустой).
        """
        self.name = name
        self.description = description
        self.products = products if products else []
        Category.category_count += 1
        Category.product_total += len(self.products)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.

        Args:
            product: Экземпляр товара.
        """
        self.products.append(product)
        Category.product_total += 1

    @property
    def product_count(self):
        """
        Возвращает количество товаров в категории.
        """
        return len(self.products)
