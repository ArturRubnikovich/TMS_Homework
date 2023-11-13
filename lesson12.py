from dataclasses import dataclass
from abc import ABC, abstractmethod


# 1
@dataclass
class Product:
    id: int
    name: str
    price: float


# 2
@dataclass
class Pizza(Product):
    topping: list
    spicy: str
    diameter: int


@dataclass
class Coffee(Product):
    cup_volume: float
    coffee_type: str


# 3
class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, key: Product):
        pass

    @abstractmethod
    def sell_product(self, key: Product):
        pass

    @abstractmethod
    def all_products(self) -> list[Product]:
        pass


class NonProductError(ValueError):
    pass

product unit