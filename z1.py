# Напишите программу, которая принимает на вход список чисел и выводит на
# экран сумму всех элементов списка. Используйте цикл while и переменную-счетчик

my_list = input([1, 5, 7, -1, 25, -10])
n = 0
summ = 0
while n < len(my_list):
    summ = summ + int(my_list[n])
    n += 1
print("Сумма элементов списка равна:", summ)