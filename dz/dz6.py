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

arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for row in arr:
    print(row)
print()
new_arr = [[0]*(len(arr)) for x in (arr[0])]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        new_arr[j][i] = arr[i][j]
for row in new_arr:
    print(row)