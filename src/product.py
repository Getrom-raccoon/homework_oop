from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех товаров.
    Предписывает атрибуты: название, описание, цена, количество.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация основных свойств товара.
        """
        self.name = name
        self.description = description
        self.price = price if price >= 0 else 0
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
        Устанавливает цену товара (отрицательная цена становится 0).
        """
        self._price = value if value >= 0 else 0

    def __add__(self, other):
        """
        Складывает сумму товаров
        Разрешено только для экземпляров одного класса.
        """
        if not isinstance(other, type(self)):
            raise TypeError("Операция сложения допустима только для одного типа товаров!")
        return self.price * self.quantity + other.price * other.quantity

    def __str__(self):
        """
        Форматированная строка для печати информации о товаре.
        """
        return f"{self.name}, {int(self.price)} руб. {self.quantity} шт."

    @classmethod
    def new_product(cls, data: dict):
        """
        Создает новый экземпляр класса из словаря с ключами
        """
        return cls(
            data.get("name", ""),
            data.get("description", ""),
            data.get("price", 0),
            data.get("quantity", 0)
        )

class Product(BaseProduct):
    """
    Класс универсального продукта.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта.
        """
        super().__init__(name, description, price, quantity)

class Smartphone(Product):
    """
    Класс продукта — смартфон.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, model: str, memory: str, color: str, camera: str):
        """
        Инициализация смартфона спецификой товара.
        """
        super().__init__(name, description, price, quantity)
        self.model = model
        self.memory = memory
        self.color = color
        self.camera = camera

class LawnGrass(Product):
    """
    Класс продукта — газонная трава.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str, color: str):
        """
        Инициализация газонной травы спецификой товара.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
