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
