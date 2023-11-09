# 1
class Soda:
    def __init__(self, additive: str = ""):
        self.additive = additive

    def show_my_drink(self):
        if self.additive == "":
            print("Обычная газировка")
        else:
            print(f"Газировка и {self.additive}")


a = Soda()
a.show_my_drink()
b = Soda("малина")
b.show_my_drink()


# 3
class KgToPounds:
    def __init__(self, kg: int = 0):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.2046226

    def set_kg(self, number):
        if type(number) == int or type(number) == float:
            self.__kg = number
        else:
            return 0

    def get_kg(self):
        return self.__kg


weight = KgToPounds(127)

print(f"Текущее значение в кг: {weight.get_kg()}")
print(f"Текущее значение в фунтах: {weight.to_pounds()}")

weight.set_kg(155)

print(f"Текущее значение в кг: {weight.get_kg()}")
print(f"Текущее значение в фунтах: {weight.to_pounds()}")


class KgToPounds:
    def __init__(self, kg: int | float = 0):
        self.__kg = kg

    def to_pounds(self) -> int | float:
        return self.__kg * 2.2046226

    @property
    def kg(self) -> int | float:
        return self.__kg

    @kg.setter
    def kg(self, number: int | float):
        if type(number) == int or type(number) == float:
            self.__kg = number
        else:
            print("Wrong value")

    def get_kg(self):
        return self.__kg


weight = KgToPounds(127)

print(f"Текущее значение в кг: {weight.kg}")
print(f"Текущее значение в фунтах: {weight.to_pounds()}")

weight.kg = 155

print(f"Текущее значение в кг: {weight.kg}")
print(f"Текущее значение в фунтах: {weight.to_pounds()}")


# 4
class RealString:
    def __init__(self, s1: str = "Apple", s2: str = "Яблоко"):
        self.__s1 = s1
        self.__s2 = s2

    def is_string_eq(self):
        if len(self.__s1) == len(self.__s2):
            print("Строки равны")
            return True
        else:
            print("Строки не равны")
            return False

    @property
    def s1(self) -> str:
        return self.__s1

    @property
    def s2(self) -> str:
        return self.__s2

    @s1.setter
    def s1(self, s):
        if type(s) == str:
            self.__s1 = s
        else:
            self.__s1 = self.__s1

    @s2.setter
    def s2(self, s):
        if type(s) == str:
            self.__s2 = s
        else:
            self.__s2 = self.__s2


strings = RealString()
strings.is_string_eq()
print(strings.s1)
print(strings.s2)

strings.s1 = "Strawberry"
strings.s2 = "Клубника"

strings.is_string_eq()
print(strings.s1)
print(strings.s2)


# 5
class Rectangle:
    def __init__(self, width: int | float = 0, height: int | float = 0):
        self.__width = width
        self.__height = height

    def get_str(self):
        return f"Прямоугольник с шириной {self.__width} и высотой {self.__height}"

    def get_area(self) -> int | float:
        return self.__width * self.__height

    def get_perimeter(self) -> int | float:
        return 2 * (self.__width + self.__height)

    @property
    def is_square(self) -> bool:
        if self.__width == self.__height:
            return True
        else:
            return False


sides = Rectangle(10, 15)
print(sides.get_str())
print(f"Площадь: {sides.get_area()}")
print(f"Периметр: {sides.get_perimeter()}")
if sides.is_square:
    print("Квадрат")
else:
    print("Прямоугольник")
print(sides.is_square)


# 4 с помощью магических методов

class RealString:
    def __init__(self, s: str = ""):
        self.s = s

    def __lt__(self, other):
        return len(self.s) < len(other.s)

    def __le__(self, other):
        return len(self.s) <= len(other.s)

    def __eq__(self, other):
        return len(self.s) == len(other.s)

    def __ne__(self, other):
        return len(self.s) != len(other.s)

    def __gt__(self, other):
        return len(self.s) > len(other.s)

    def __ge__(self, other):
        return len(self.s) >= len(other.s)


s1 = RealString("привет")
s2 = RealString("как дела?")
print(s1 < s2)
print(s1 > s2)
print(s1 == s2)
print(s1 != s2)
print(s1 <= s2)
print(s1 >= s2)
