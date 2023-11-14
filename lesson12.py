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


# 3
class AbstractShop(ABC):
    @abstractmethod
    def add_product(self, product: Product):
        pass

    @abstractmethod
    def sell_product(self, product: Product):
        pass

    @abstractmethod
    def all_products(self) -> list[Product]:
        pass


# 4-5
class NonProductError(ValueError):
    pass


class RealShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: Product):
        self.product_shop.append(product)

    def sell_product(self, product: Product):
        self.product_shop.remove(product)

    def all_products(self) -> list[Product]:
        return self.product_shop

    def is_valid(self, product: Product):
        if not isinstance(product, Product):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True


# 6
@dataclass
class Furniture(Product):
    pass


@dataclass
class Table(Furniture):
    table_type: str
    form: str


@dataclass
class Chair(Furniture):
    chair_type: str
    color: str


@dataclass
class Cabinet(Furniture):
    cabinet_type: str
    purpose: str


# 7
class FurnitureShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: Furniture):
        self.product_shop.append(product)

    def sell_product(self, product: Furniture):
        self.product_shop.remove(product)

    def all_products(self) -> list[Furniture]:
        return self.product_shop

    def is_valid(self, product: Furniture):
        if not isinstance(product, Furniture):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True


pizza1 = Pizza(2, "Гавайская", 35, ["ананас", "курица"], False, 36)
coffee1 = Coffee(1, "Латте", 5, 300)
new_real_shop = RealShop()
new_real_shop.add_product(pizza1)
new_real_shop.add_product(coffee1)
print(new_real_shop.all_products())
new_real_shop.sell_product(coffee1)
print(new_real_shop.all_products())
print(new_real_shop.is_valid(pizza1))

table1 = Table(10, "Mio Tesoro", 300, "обеденный", "круглый")
chair1 = Chair(25, "Sheffilton SHT-S75", 170, "для жилой комнаты", "черный")
cabinet1 = Cabinet(14, "Eligard Locarno 3", 620, "шкаф", "для прихожей")
new_furniture_shop = FurnitureShop()
new_furniture_shop.add_product(table1)
new_furniture_shop.add_product(chair1)
new_furniture_shop.add_product(cabinet1)
print(new_furniture_shop.all_products())
new_furniture_shop.sell_product(cabinet1)
print(new_furniture_shop.all_products())
print(new_furniture_shop.is_valid(cabinet1))
