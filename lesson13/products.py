from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    price: float


@dataclass
class Pizza(Product):
    topping: list
    spicy: bool
    diameter: int


@dataclass
class Coffee(Product):
    cup_volume: float


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


@dataclass
class PrintedMedia(Product):
    pass


@dataclass
class Book(PrintedMedia):
    pass


@dataclass
class Magazine(PrintedMedia):
    pass


@dataclass
class ComputerHardware(Product):
    pass


@dataclass
class Motherboard(ComputerHardware):
    pass


@dataclass
class GraphicsCard(ComputerHardware):
    pass
