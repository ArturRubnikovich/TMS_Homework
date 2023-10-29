# # 1. Напишите функцию root(x), которая возвращает квадрат своего аргумента
#
# def root(x):
#     return x * x
#
#
# number = int(input("Введите число: "))
# res = root(number)
# print(res)


# 2. Напишите функцию is_even(n), которая проверяет, является ли число
# четным или нечетным. Функция должна возвращать True, если число четное,
# и False, если число нечетное.
#
# def is_even(n):
#     return n % 2 == 0
#
#
# number = int(input("Введите число: "))
# res = is_even(number)
# print(res)


# 3. Напишите функцию factorial(n), которая вычисляет факториал своего
# аргумента. Факториал числа n — это произведение всех натуральных чисел от
# 1 до n. Например, factorial(4) = 4×3×2×1 = 24.
# Функция должна возвращать факториал числа или -1, если число
# отрицательное.
#
# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     elif n > 1:
#         return factorial(n - 1) * n
#     else:
#         return -1
#
#
# number = int(input("Введите любое число: "))
# res = factorial(number)
# print(res)


# 4. Напишите функцию reverse(s), которая принимает строку s и возвращает
# ее в обратном порядке. Например, reverse("hello") должна вернуть
# "olleh"
#
# def reverse(s):
#     return s[::-1]
#
#
# enter_str = input("Введите любое слово или фразу: ")
# reversed_str = reverse(enter_str)
# print(reversed_str)

# 5. Напишите функцию fibonacci(n), которая возвращает n-ый член
# последовательности Фибоначчи. Первые два числа равны 1.

# def fibonacci(n):    # посл-ть Ф: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...
#     if n in (1, 2):  # первые два числа
#        return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# number = int(input("Введите номер члена последовательности Фибоначчи: "))
# res = fibonacci(number)
# print(res)

# 6. Напишите функцию count_vowels(s), которая подсчитывает количество гласных букв в строке s. Гласные буквы —
# это а, е, ё, и, о, у, ы, э, ю, я. Например, count_vowels("привет") должна вернуть 2.
#
# def count_vowels(s):
#     count = 0
#     for letter in s:
#         if letter in ('а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'):
#             count += 1
#
#     return count
#
#
# enter_str = input("Введите любое слово или фразу: ")
# lowercase_enter_str = enter_str.lower()
# res = count_vowels(lowercase_enter_str)
# print(res)

# 7. Напишите функцию is_palindrome(s), которая проверяет, является ли строка s палиндромом.
# Палиндром — это слово или фраза, которая читается одинаково слева направо и справа налево. Функция должна
# возвращать True, если строка палиндром, и False, если нет. Например, is_palindrome("топот") должна вернуть True, а
# is_palindrome("привет") должна вернуть False.
#
# def is_palindrome(s):
#     return s == s[::-1]
#
#
# enter_str = input("Введите любое слово: ")
# lowercase_enter_str = enter_str.lower()
# res = is_palindrome(lowercase_enter_str)
# print(res)

# 8. Напишите функцию power(x, n), которая возводит число x в степень n.
# Например, power(2, 3) должна вернуть 2**3 = 8.
#
# def power(x, n):
#     return x ** n
#
#
# number_x = int(input("Введите первое число: "))
# number_n = int(input("Введите второе число: "))
# res = power(number_x, number_n)
# print(res)

# 9. Напишите функцию is_anagram(s1, s2), которая проверяет, являются ли две строки s1 и s2 анаграммами.
# Анаграмма — это слово, составленное из перестановки букв другого слова. Функция должна возвращать True, если
# строки анаграммы, и False, если нет. Например, is_anagram("кот", "ток") должна вернуть True, а
# is_anagram("кот", "собака") должна вернуть False.
#
#
# def is_anagram(s1, s2):
#     return sorted(s1) == sorted(s2)
#
#
# enter_s1 = input("Введите любое слово: ")
# enter_s2 = input("Введите любое слово: ")
# lowercase_enter_s1 = enter_s1.lower()
# lowercase_enter_s2 = enter_s2.lower()
# res = is_anagram(lowercase_enter_s1, lowercase_enter_s2)
# print(res)

# 10. Напишите функцию is_pangram(s), которая проверяет, является ли строка s панграммой или нет.
# Панграмма — это строка, которая содержит все буквы алфавита хотя бы один раз. Функция должна возвращать True,
# если строка панграмма, и False, если нет. Например, is_pangram("Аэрофотосъёмка ландшафта уже выявила
# земли богачей и процветающих крестьян.") должна вернуть True, а is_pangram("Привет, мир") должна вернуть False.


# def is_pangram(s):
#     list_letters = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
#                     'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#     for letter in list_letters:
#         if letter not in s:
#             return False
#     return True
#
#
# enter_s = input("Введите любое слово или предложение: ")
# lowercase_enter_s = enter_s.lower()
# res = is_pangram(lowercase_enter_s)
# print(res)
