from src.product import Product
from src.category import Category

def main():
    p1 = Product("Телевизор", "40-дюймовый телевизор", 30000.0, 10)
    p2 = Product("Холодильник", "Двухкамерный холодильник", 45000.0, 5)
    category = Category("Бытовая техника", "Категория бытовой техники", [p1, p2])

    print(f"Категория: {category.name}, продуктов: {len(category._Category__products)}")
    for product in category._Category__products:
        print(f"Товар: {product.name}, цена: {product.price}, количество: {product.quantity}")

if __name__ == "__main__":
    main()
