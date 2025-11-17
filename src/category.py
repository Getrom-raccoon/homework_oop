from typing import List

from src.product import Product


class Category:

    category_count = 0
    product_total = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализация Category.
        """
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_total += len(self.__products)

    @property
    def products(self) -> List[Product]:
        """
        Возвращает список товаров в категории.
        """
        return self.__products

    def add_product(self, product: Product) -> None:
        """
        Добавляет товар в категорию.
        """
        self.__products.append(product)
        Category.product_total += 1

    @property
    def product_count(self) -> int:
        """
        Возвращает количество товаров в категории.
        """
        return len(self.__products)

    def __str__(self) -> str:
        """
        Возвращает строковое представление категории.
        """
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
