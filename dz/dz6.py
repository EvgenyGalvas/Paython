import math
from random import randint

# Задача 1

# print("Выбор фигуры:\n1 - треугольни\n2 - прямоуголник\n3 - круг")
# form = int(input("Введите номер фигуры = "))
# if form == 1:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     c = float(input("Введите сторону c = "))
#     p = (a + b + c) / 2
#     s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
# elif form == 2:
#     a = float(input("Введите сторону a = "))
#     b = float(input("Введите сторону b = "))
#     s = a * b
# elif form == 3:
#     r = float(input("Введите радиус r = "))
#     s = math.pi * (r ** 2)
# print("Площадь фигуры = ", s)

# Задача 2

# arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# for row in arr:
#     print(row)
# print()
# new_arr = [[0]*(len(arr)) for x in (arr[0])]
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         new_arr[j][i] = arr[i][j]
# for row in new_arr:
#     print(row)

# Задача №3


a = [[randint(0, 10) for i in range(6)] for i in range(6)]
for row in a:
    for x in row:
        print(x, end="\t")
    print()
b = [randint(0, 10) for i in range(6)]

print()
print(b)
print()
for i in range(6):
    if i % 2 == 0:
        a[i] = b

for row in a:
    for x in row:
        print(x, end="\t")
    print()

# Задача №4
# a = [[randint(0, 10) for i in range(6)] for i in range(6)]
# for row in a:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# new_arr = [[0] * (len(a)) for x in (a[0])]
# new_arr[0], new_arr[2], new_arr[4] = a[1], a[3], a[5]
# new_arr[1], new_arr[3], new_arr[5] = a[0], a[2], a[4]
# print()
# for row in new_arr:
#     for x in row:
#         print(x, end="\t")
#     print()
