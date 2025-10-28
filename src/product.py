from typing import Union


class Product:
    """
    Класс для описания товара в магазине.
    """

    def __init__(
        self, name: str, description: str, price: Union[int, float], quantity: int
    ):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: Union[int, float]) -> None:
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self._price = value
