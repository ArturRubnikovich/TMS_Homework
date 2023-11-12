# 1
from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float

# 2
@dataclass
class Pizza (Product):
    topping: list
    spicy: str
    diameter: int

@dataclass
class Coffee(Product):
    cup_volume: float
    coffee_type: str

# 3




