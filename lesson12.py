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
    spicy: bool
    diameter: int


@dataclass
class Coffee(Product):
    cup_volume: float
    coffee_type: str


# 3
class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, manufactured_product: Product):
        pass

    @abstractmethod
    def sell_product(self, sold_product: Product):
        pass

    @abstractmethod
    def all_products(self) -> list[Product]:
        pass


# 4-5
class NonProductError(ValueError):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self.real_shop = []

    def add_product(self, manufactured_product: Product):
        self.real_shop.append(manufactured_product)

    def sell_product(self, sold_product: Product):
        self.real_shop.remove(sold_product)

    def all_products(self) -> list[Product]:
        return self.real_shop

    def is_valid1(self, manufactured_product: Product):
        if not isinstance(manufactured_product, Product):
            raise NonProductError(f"{manufactured_product} не является изготовленными пиццей либо кофе")
        else:
            return True

    def is_valid2(self, sold_product: Product):
        if not isinstance(sold_product, Product):
            raise NonProductError(f"{sold_product} не является проданными пиццей либо кофе")
        else:
            return True


# 6


