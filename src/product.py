class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация Product.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество единиц товара.
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

        Args:
            value: Новое значение цены.
        """
        if value < 0:
            self._price = 0
        else:
            self._price = value

    @classmethod
    def new_product(cls, data: dict):
        """
        Создает Product из словаря данных.

        Args:
            data: Словарь с ключами name, description, price, quantity.

        Returns:
            Product: Новый Product.
        """
        return cls(
            name=data.get("name"),
            description=data.get("description"),
            price=data.get("price"),
            quantity=data.get("quantity"),
        )
