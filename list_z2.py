# **И наклон

a = input("первая координата: ")   # "0,0"
print(a.split(","))
b = input("вторая координата: ")   # "0,1"
print(b.split(","))
d = int(input("длина отрезка: "))  # "1"
x1 = int(a.split(",")[0])
y1 = int(a.split(",")[1])
x2 = int(b.split(",")[0])
y2 = int(b.split(",")[1])
sin = (y2 - y1) / d
print(sin)






