from typing import List
from src.products.product import Product

class Category:
    """
    Класс для категорий товаров.
    """
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(products)
