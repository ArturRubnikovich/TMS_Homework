# 1

numbers_string = input("Введите числа: ")
numbers_list = numbers_string.split()
i = 0
summ = 0
while i < len(numbers_list):
    summ += int(numbers_list[i])
    i += 1
print("Сумма всех элементов списка: ", summ)

# 2

lower_vowel = "аеиоуыэюя"
lower_upper_vowel = lower_vowel + lower_vowel.upper()
words_string = input("Введите строку: ")
i = 0
vowel_count = 0
while i < len(words_string):
    if words_string[i] in lower_upper_vowel:
        vowel_count += 1
    i += 1
print("Количество гласных букв в строке: ", vowel_count)

# 3

words_string = input("Введите слова: ")
words_list = words_string.split()

print("Самое длинное слово: ", max(words_list), "длина этого слова: ", len(max(words_list)))







# 5

numbers_string = input("Введите список чисел: ")
numbers_list = numbers_string.split()
numbers_list_sorted = sorted(numbers_list)
print(f"""
    Значение минимального элемента: {numbers_list_sorted[0]}
    Индекс минимального элемента: {numbers_list.index(numbers_list_sorted[0])}
""")

# 6
print("-" * 100)
input_string = input("Введите список слов через пробел: ")
input_list = input_string.split()
print("Перевёрнутая строка: ", " ".join(list(reversed(input_list))))
