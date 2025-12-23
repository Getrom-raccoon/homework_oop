from abc import ABC, abstractmethod


class CreationLoggerMixin:
    """
    Миксин для логирования создания объектов.

    При инициализации печатает класс и переданные параметры.
    """

    def __init__(self, *args, **kwargs):
        """
        Логирует создание объекта и передаёт управление по цепочке super().
        """
        cls_name = self.__class__.__name__
        print(f"Создан объект {cls_name} с args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для всех продуктов.
    """

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price if price > 0 else 0
        self.quantity = quantity

    @property
    def price(self) -> float:
        """
        Возвращает цену продукта.
        """
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """
        Устанавливает цену продукта, не допускает отрицательные значения.
        """
        self._price = value if value > 0 else 0

    def __str__(self) -> str:
        """
        Возвращает строковое представление продукта.
        """
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Складывает общую стоимость двух продуктов одного типа.
        """
        if not isinstance(other, type(self)):
            raise TypeError("Складывать можно только объекты одного типа!")
        return self.price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, data: dict):
        """
        Создаёт новый продукт из словаря с данными.
        """
        return cls(
            data.get("name", ""),
            data.get("description", ""),
            data.get("price", 0),
            data.get("quantity", 0),
        )


class Product(CreationLoggerMixin, BaseProduct):
    """
    Конкретный класс продукта, наследуется от BaseProduct и миксина.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация продукта с участием миксина и абстрактного класса.
        """
        super().__init__(name, description, price, quantity)


class Smartphone(Product):
    """
    Класс смартфонов, наследуется от Product.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ):
        """
        Инициализирует смартфон с дополнительными характеристиками.
        """
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
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """
        Инициализирует газонную траву с дополнительными характеристиками.
        """
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
