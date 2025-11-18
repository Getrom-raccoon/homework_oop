class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация Product.
        """
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        Возвращает цену товара.
        """
        return self._price

    @price.setter
    def price(self, value):
        """
        Устанавливает цену товара.
        """
        if value < 0:
            self._price = 0
        else:
            self._price = value

    def __str__(self) -> str:
        """
        Возвращает строковое представление товара.
        """
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: 'Product') -> float:
        """
        Складывает два товара, возвращая сумму их стоимости на складе.

        """
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        """
        Создает Product из словаря данных.
        """
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )
