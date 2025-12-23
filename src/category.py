from typing import List

from src.product import Product


class Category:
    """
    Класс категории товаров.
    """

    category_count = 0
    product_total = 0

    def __init__(self, name: str, description: str, products: List[Product] = None):
        """
        Инициализирует категорию и обновляет счётчики.
        """
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.category_count += 1
        Category.product_total += len(self.products)

    @property
    def products(self) -> List[Product]:
        """
        Возвращает список продуктов категории.
        """
        return self._products

    @products.setter
    def products(self, value: List[Product]) -> None:
        """
        Устанавливает список продуктов категории.
        """
        self._products = value

    def add_product(self, product: Product) -> None:
        """
        Добавляет продукт в категорию и обновляет счётчик продуктов.
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только экземпляры Product и его наследников!"
            )
        self.products.append(product)
        Category.product_total += 1

    @property
    def product_count(self) -> int:
        """
        Возвращает количество товаров в категории.
        """
        return len(self.products)

    def middle_price(self) -> float:
        """
        Расчёт среднего ценника всех товаров категории.

        В случае отсутствия товаров возвращает 0 без выброса исключения.
        """
        try:
            total_price = sum(product.price for product in self.products)
            return total_price / len(self.products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.products)
        return f"{self.name}, {total_quantity} шт."
