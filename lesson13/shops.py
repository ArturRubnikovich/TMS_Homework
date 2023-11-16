from .abstract import AbstractShop
from .products import Product, Furniture, PrintedMedia, ComputerHardware
from .exception import NonProductError


class RealShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: Product):
        self.is_valid(product)
        self.product_shop.append(product)

    def sell_product(self, product: Product):
        self.is_valid(product)
        self.product_shop.remove(product)

    def all_products(self) -> list[Product]:
        return self.product_shop

    def is_valid(self, product: Product):
        if not isinstance(product, Product):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True


class FurnitureShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: Furniture):
        self.is_valid(product)
        self.product_shop.append(product)

    def sell_product(self, product: Furniture):
        self.is_valid(product)
        self.product_shop.remove(product)

    def all_products(self) -> list[Furniture]:
        return self.product_shop

    def is_valid(self, product: Furniture):
        if not isinstance(product, Furniture):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True


class BookShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: PrintedMedia):
        self.is_valid(product)
        self.product_shop.append(product)

    def sell_product(self, product: PrintedMedia):
        self.is_valid(product)
        self.product_shop.remove(product)

    def all_products(self) -> list[PrintedMedia]:
        return self.product_shop

    def is_valid(self, product: PrintedMedia):
        if not isinstance(product, PrintedMedia):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True


class ComputerShop(AbstractShop):
    def __init__(self):
        self.product_shop = []

    def add_product(self, product: ComputerHardware):
        self.is_valid(product)
        self.product_shop.append(product)

    def sell_product(self, product: ComputerHardware):
        self.is_valid(product)
        self.product_shop.remove(product)

    def all_products(self) -> list[ComputerHardware]:
        return self.product_shop

    def is_valid(self, product: ComputerHardware):
        if not isinstance(product, ComputerHardware):
            raise NonProductError(f"{product} не является продуктом")
        else:
            return True
