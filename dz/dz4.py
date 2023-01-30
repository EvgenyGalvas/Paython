# Задача 1
# import random
# a = random.randint(1, 100)
# b = 1
# while True:
#     n = int(input("Введите число от 1 до 100: "))
#     if a > n:
#         print("Загаданное число больше")
#         b += 1
#     elif a < n:
#         print("Загаданное число меньше")
#         b += 1
#     else:
#         print("Вы угадали загаданное число c", b, "раз")
#         break

# Задача 2
# n = [5, 1, 9, 7, 6, 3]
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i], end=" ")

# Задача3
# 1 вариант решения
# n = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# a = []
#
# for i in n:
#     b = 0
#     for j in n:
#         if i == j:
#             b += 1
#     if b == 1:
#         a.append(i)
# print(a)

# второй вариант решения
# n = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# a = []
# for i in n:
#     if n.count(i) == 1:
#         a.append(i)
# print(a)

# Задача 4
# for i in range(8):
#     for j in range(1):
#         print("*" * (8 - i))
