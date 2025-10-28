from src.product import Product
from src.category import Category


def main():
    product1 = Product("Телевизор", "40-дюймовый телевизор", 30000.0, 10)
    product2 = Product("Холодильник", "Двухкамерный холодильник", 45000.0, 5)

    category = Category("Бытовая техника", "Категория для крупной бытовой техники", [product1, product2])

    print(f"Категория: {category.name}")
    print(f"Описание: {category.description}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего продуктов: {Category.product_count}")

    print("Список товаров категории:")
    for pr in category._Category__products:
        print(f"- {pr.name}: {pr.description}, Цена: {pr.price}, Количество: {pr.quantity}")


if __name__ == "__main__":
    main()
