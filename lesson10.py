import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str = " ", weight: int = 1500):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def birthday(self):
        return self.age + 1

    def stop(self):
        print("stop")


class Truck(Auto):

    def __init__(self, brand: str, age: int, mark: str, max_load: int, color: str = " ", weight: int = 1500):
        super().__init__(brand, age, mark, color, weight)
        self.brand = brand
        self.age = age
        self.mark = mark
        self.max_load = max_load
        self.color = color
        self.weight = weight

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand: str, age: int, mark: str, max_speed: int, color: str = " ", weight: int = 1500):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        time.sleep(1)
        print(f"move \n max speed is: {self.max_speed} km/h")
        time.sleep(1)


car1 = Car("Porshe", 10, "911", 110)
print(car1.age)
print(car1.mark)
car1.move()

car2 = Car("Citroen", 17, "C5", 70)
print(car2.brand)
car2.move()

truck1 = Truck("Renault", 15, "Trafic", 600)
print(truck1.brand)
truck1.move()

truck2 = Truck("Fiat", 8, "Ducato", 555, "white")
print(truck2.color)
print(truck2.max_load)
truck2.move()
