class Product:
    """
    Базовый класс продукта.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price if price > 0 else 0
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value if value > 0 else 0

    def __str__(self):
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, type(self)):
            raise TypeError("Складывать можно только объекты одного типа!")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        return cls(
            data.get("name"),
            data.get("description"),
            data.get("price"),
            data.get("quantity"),
        )


class Smartphone(Product):
    """
    Класс смартфонов, наследуется от Product.
    """

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """
    Класс газонной травы, наследуется от Product.
    """

    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
