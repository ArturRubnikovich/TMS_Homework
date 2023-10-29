# 1. Напишите функцию make_sentence, которая принимает один именованный аргумент words, который должен быть
# списком строк, и возвращает строку, составленную из элементов списка, разделенных пробелами и заканчивающуюся
# точкой. Если аргумент words не указан, то по умолчанию используется список ["This", "is", "a", "sentence"].


# def make_sentence(words=["This", "is", "a", "sentence"]) -> str:
#     created_sentence = " ".join(words)
#     return created_sentence + "."
#
#
# print(make_sentence())

# 2

# def sum_of_squares(*args):
#     sp = [i * i for i in args]
#     return sum(sp)
#
#
# print(sum_of_squares())

# 3
#
# def greet(name: str, language: str = "en"):
#     if language is None or language == "en":
#         return "Hello, " + name + "!"
#     elif language == "ru":
#         return "Привет, " + name + "!"
#     else:
#         return "Bonjour, " + name + "!"
#
#
# s = greet("Artur", "en")
# print(s)


# 4
#
# def print_info(**kwargs):
#     if len(kwargs) == 0:
#         print("No info given.")
#     else:
#         for key in kwargs:
#             print(f"{key}: {kwargs[key]}")
#
#
# print_info(name="Alex", age=22, city="Minsk")

# 5

# def print_table(**kwargs):
#     if len(kwargs) == 0:
#         print("No data given.")
#     else:
#         s_1 = "Key"
#         s_2 = "Value"
#         print(f" | {s_1:<10} | {s_2:<10} | ")
#         print("-" * 29)
#         for key in kwargs:
#             print(f" | {key:<10} | {kwargs[key]:<10} | ")
#
#
# print_table(name="Alex", age=22, city="Minsk")

# 8
#
# def create_post(title: str, content: str, author: str, category: str = "general"):
#     post = {
#         "title": title,
#         "content": content,
#         "author": author,
#         "category": category,
#     }
#     return post
#
#
# dict_post = create_post("English grammar", "Present simple", "BBC", "Foreign language")
# print(dict_post)

# 9

# def create_product(name: str,  price: int | float, category: str, rating: int = 0):
#     product = {
#         "name": name,
#         "price": price,
#         "category": category,
#         "rating": rating,
#     }
#     return product
#
#
# new_product = create_product("clothes", 150, "boots", 9)
# print(new_product)

# 10

def create_student(firstname: str, lastname: str, middlename: str, group: int):
    student = {
        "firstname": firstname,
        "lastname": lastname,
        "middlename": middlename,
        "group": group,
    }
    return student


dict_student = create_student("Maxim", "Smirnov", "Igorevich", 9)
print(dict_student)
