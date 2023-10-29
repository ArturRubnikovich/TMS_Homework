# 1
#
# numbers = [1, 3, 4, 7, 8, 10, 14, 17, 20, 25, 27, 29, 30]
# new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#
# print(new_numbers)

# 2

# list_tuple = [("Alex", 25), ("Max", 30), ("Igor", 28), ("Elena", 22)]
# new_list = list(sorted(list_tuple, key=lambda x: x[1]))
#
# print

# 3

# list_s = ["Александр", "Максим", "Елена", "Алиса", "Дмитрий", "Ёцуба"]
# vowels = {'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}
# new_list = list(filter(lambda x: x[0].lower() in vowels, list_s))
#
# print(new_list)

# 4

# numbers = [1, 3, 4, 7, 8, 10, 14, 17, 20, 25, 27, 29, 30]
# new_numbers = list(map(lambda x: x ** 2, numbers))
#
# print(new_numbers)

# 5

# list_s = ["Александр", "футбол", "Антананариву", "лось", "жук", "высокопревосходительство"]
# new_list = list(sorted(list_s, key=len, reverse=True))
#
# print(new_list)

# 6

# s = "It's better to have ideals and dreams than nothing"
# list_set = {'p', 'y', 't', 'h', 'o', 'n'}
# new_list = list(filter(lambda x: x in list_set, s.lower()))
#
# print(new_list)

# 7

# numbers = [1, 3, 4, 7, 8, 10, 14, 17, 20, 25, 27, 29, 30]
# new_numbers = list(map(lambda x: x * 10, numbers))
#
# print(new_numbers)

# 8

# list_s = ["футбол", "Антананариву", "лось", "жук", "высокопревосходительство", "розы", "тротуар", "Ямайка"]
# new_list_s = list(sorted(list_s, key=lambda x: x[0].lower()))
#
# print(new_list_s)

# 9

# list_s = ["заказ", "футбол", "мадам", "лось", "жук", "розы", "око", "тротуар", "Ямайка", "доход"]
# new_list_s = list(filter(lambda x: x == x[::-1], list_s))
#
# print(new_list_s)

# 10

# list_s = ["футбол", "Антананариву", "ёрничество", "бананы", "жук", "высокопревосходительство", "республика", "Ямайка"]
# new_list_s = list(sorted(list_s, key=lambda x: sum(i in "аеёиоуыэюя" for i in x)))
#
# print(new_list_s)

# 11

# list_s = ["заказ", "футбол", "мадам", "лось", "жук", "розы", "око"]
# new_list_s = list(map(lambda x: x.upper(), list_s))
#
# print(new_list_s)

# 12

# list_s = ["Max", "Alex", "Helen", "Igor", "Alice"]
# new_list_s = list(map(lambda x: "Hello " + x, list_s))
#
# print(new_list_s)

# 13

# list_s = ["Антарктида", "арбуз", "канава", "скачок", "Антананариву"]
# new_list_s = list(sorted(list_s, key=lambda x: sum(i in "а" for i in x)))
#
# print(new_list_s)


