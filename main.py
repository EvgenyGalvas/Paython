# name = "Elena"
# print("Hello", name)
# age = 20
# print(type(age))
# print(id(age))
# age = "hello"
# print(type(age))
import csv
import json

# a = b = c = 1
# print(a, b, c)

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# print(type(True))

# a = "5"
# b = 2
# print(int(a) + b)

# a = 10
# b = 20
# print("a =", a)
# print("b =", b)
# # c = a
# # a = b
# # b = c
# # a = a + b  # a = 1 + 2 = 3
# # b = a - b  # b = 3 - 2 = 1
# # a = a - b  # a = 3 - 1 = 2
# a, b = b, a
# print("a =", a)
# print("b =", b)

# print("строка \
# символов")
# print('строка \rсимволов')

# print("\tДокумент       \"file.txt\" D:\\folder\\file.py")

# s1 = "Hello"  # комментарий
# s2 = "Python"
# s3 = s1 + " " + s2 + "!\t\t"
# print(s3)
# print(s3 * 5)

# print(5456454564564546546416546)
# print(5.456454564564546546416546)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(7 // 2)
# print(7 ** 2)
# print(7 % 2)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)
#
# number = (6 + 4) * 5 ** (2 + 7)
# print(number)


# a = 5
# b = 7
# c = 3
# sum1 = a + b + c
# um = a * b * c
# sr = sum1 / 3
# print("Сумма:", sum1)
# print("Произведение:", um)
# print("Среднее арифметическое:", sr)

# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
#
# num -= 3  # num = num - 3
# print(num)  # 12

# num = 4321  # 43
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
#
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10  # 432
# res += num % 10 * 100
# num //= 10  # 43
# res += num % 10 * 10
# num //= 10  # 4
# res += num % 10
# print(res)

# Функции явного преобразования типов
# str()
# int()
# float()
# bool()

# num1 = '2.5'
# num2 = 3
# res = int(float(num1)) + num2
# print(res)

# print(int(3.8))
# a = round(3.8)
# print(a)
# print(type(a))
# b = round(3.89446546, 2)
# print(b)
# print(type(b))

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="--", end=" ")
# print("Я учу Python.")

# name = input("Ваше имя: ")
# print(name)


# Число 5 в степени 2 равно 25

# num = int(input("Число: "))
# st = int(input("Степень: "))
# # num = int(num)
# # st = int(st)
# res = num ** st
# print('Число', num, 'в степени', st, 'равно', res)


# b1 = True  # 1
# b2 = False  # 0
# print(b1 + 5)
# print(b2 + 5)

# print(bool("Python"))
# print(bool(""))  # False
# print(bool(" "))
# print(bool(5))
# print(bool(0))  # False
# print(bool(False))  # False
# print(bool(None))  # False
#
# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 < 7)
# print(8 <= 8)
# print(8 >= 8)

# print(2 < 10 < 9)  # True && False
# print(3 * 3 <= 7 >= 2)  # False && True

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True:False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True:True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True:False)

# print(not 9 - 5)
# print(not 5 - 5)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")


# a = 35
# b = 35
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# side1 = input("Введите первую сторону: ")
# side2 = input("Введите вторую сторону: ")
# side3 = input("Введите третью сторону: ")
# if side1 == side2 == side3:
#     print("Треугольник равносторонний")
# elif side1 == side2 or side1 == side3 or side2 == side3:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")


# season = int(input("Введите номер месяца(цифрой): "))
# if season == 12 or season == 1 or season == 2:
#     print("Зима")
# elif 3 <= season <= 5:
#     print("Весна")
# elif 6 <= season <= 8:
#     print("Лето")
# elif 9 <= season <= 11:
#     print("Осень")
# else:
#     print("Такого времени года не существует для вашего месяца")


# mon = int(input("Введите номер месяца: "))
# if mon == 12 or mon == 1 or mon == 2:
#     print("Время года зима")
# elif mon == 3 or mon == 4 or mon == 5:
#     print("Время года весна")
# elif mon == 6 or mon == 7 or mon == 8:
#     print("Время года Лето")
# elif mon == 9 or mon == 10 or mon == 11:
#     print("Время года Осень")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2 <= n <= 4:
#         print("вороны")
#     else:  # 5 <= n <= 9 or n == 0
#         print("ворон")
# else:
#     print("Ошибка ввода")


# n = int(input("Введите число от 1 до 99: "))
# kop = n
# if 11 <= kop <= 14:
#     print(n, "копеек")
# elif 0 <= n <= 10 or 15 <= n <= 99:  # 89
#     kop = kop % 10
#     if kop == 1:
#         print(n, "копейка")
#     elif 2 <= kop <= 4:
#         print(n, "копейки")
#     else:  # 5 <= n <= 9 or n == 0
#         print(n, "копеек")
# else:
#     print("Ошибка ввода")

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print("Пароль не верен")

# day = 'вторник'
# time = 10
# a = 2
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16 and a > 1:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")


# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)


# x = int(input('Делимое: '))
# y = int(input('Делитель: '))
# print(x / y if y != 0 else 'На ноль делить нельзя!')


# Исключения

# a = 5
# b = 0
# print(a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")


# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводит строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):  # исключение
#     print("Нельзя вводит строки и делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")


# x = input('Введите первое число: ')
# y = input('Введите второе число: ')
#
# try:
#     x = int(x)  # 2
#     y = int(y)  # пять
# except ValueError:
#     x = str(x)  # '2'
# finally:
#     print(x + y)

# Циклы
# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2


# i = 1
# while i <= 10:
#     print(i * 2, end=" ")
#     i += 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# try:
#     x = int(input('Количество: '))
#     while x > 0:
#         print('*', end='')
#         x -= 1
# except ValueError:
#     print('Введите число!')

# x = int(input('Количество: '))
# i = 0
# while i < x:
#     print('*', end='')
#     i += 1

# num = int(input("Введите число: "))
# i = 0
# string = ""
# while i < num:
#     string += "*"
#     i += 1
# print(string)


# x = int(input('Количество: '))
# print('*' * x)


# a = int(input('Начало диапазона: '))
# b = int(input('Конец диапазона: '))
# if a % 2 == 0:
#     a += 1
# sum1 = 0
# while a <= b:
#     sum1 += a
#     a += 2
# print('Сумма нечетных: ', sum1)


# i = int(input("Start: "))  # 1
# j = int(input("End: "))  # 3
# sum1 = 0
# if i > j:
#     i, j = j, i
# while i <= j:  # i != j
#     if i % 2 != 0:
#         sum1 += i  # 1 + 3
#     i += 1
#
# print(sum1)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# m = 1
# while True:
#     n = int(input('Число: '))
#     if n == 0:
#         break
#     m *= n
# print('Произведение равно:', m)


# i = 0
# while i < 10:
#     if i == 9:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

#
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, '\t\t', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     тело цикла

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

# range(start, stop, step)

# for i in range(-16, -8, 1):
#     print(i, end=" ")
#
# print()
# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")


# num = input('Введите целое число: ')
# try:
#     num = int(num)
#     for i in range(1, num):
#         if i % 10 == i // 10:
#             print(i, end=' ')
# except ValueError:
#     print('Вас просили число!')

# for i in range(10, 100):  # 98  98 % 10 = 8  ==  98 // 10 = 9
#     if i % 10 == i // 10:
#         print(i, end=' ')


# for i in range(11, 101, 11):
#     print(i, end=" ")


# for i in range(3):
#     print(i, end=" ")
#     if i == 1:
#         break
# else:
#     print('\ndone')


# for i in range(3):
#     print("+++", i)
#     for j in range(2):
#         print("-----", j)


# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         print("*", end="")
#     print()

# w = int(input('W = '))
# h = int(input('H = '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# print([i for i in "Hello"])
#
# for i in "Hello":
#     print(i)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)


# Списки (list)

# nums = [8, 3, 9, 4, 1, "Hello", 2.3]
# print(nums)
# print(type(nums))
# print(id(nums))
# print(nums[0])
# print(nums[-1])
#
# nums[-2] = 2
# nums[1] += 100
# print(nums)
# print(id(nums))
# print(len(nums))

# s = []
# print(s)
# b = list()
# print(b)
#
# c = list("Hello")
# print(c)

# s = [5, 2] * 6
# print(s)
#
# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)


# n = list(range(2, 10, 2))
# print(n)

# [выражение for переменная in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# n = 5
# a = [i * 3 for i in "Hello"]
# print(a)

# a = [0] * int(input("Количество элементов в списке: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# nums = [8, 3, 9, 4, 1]
# print(nums * 2)
# for i in range(len(nums)):  # 0 1 2 3 4
#     print(nums[i] * 2, end=" ")
# print()
# for elem in nums:  # 8 3 9 4 1
#     print(elem * 2, end=" ")


# a = [int(input('-->')) for i in range(int(input('n: ')))]
# summa = 0
# for i in a:
#     if i < 0:
#         summa += i
# print(summa)

# a = list(range(21, 41))
# print(a)
# print()
# b = [i for i in range(21, 41)]
# print(b)


# a = list(range(21, 41))
# print(a)
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         odd += 1
#     else:
#         even += i
# print('Четных: ', odd, '\nНечетных: ', even)


# a = [int(input('-> ')) for num in [0] * int(input('Count: '))]
#
# count = sum1 = 0
# for i in a:
#     if i != 0:
#         count += 1
#         sum1 += i
# print('Среднее: ', sum1 / count)


# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:  #
#         print(a[i], end=" ")

# a = [9, 1, 3, 4, 5]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


# список[start:stop:step]

# a = [9, 4, 3, 1, 5, 17]
# print(id(a))
# print(a[-1:0:-1])
# print(a[1:3:-1])
# print(a[4:20])

# [1, 2, 3, 4, 5, 6, 7]
# a = list(range(1, 8))
# print(a)
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[0:1])
# print(a[-1:])
# print(a[3:4])
# print(a[-3:])
# print(a[-3:1:-1])
# print(a[2:5])


# a = list(range(1, 8))
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:3] = [20]
# print(a)
# a[2] = 50
# print(a)
# a[3:5] = []
# print(a)
# del a[:]
# print(a)

# Методы списков
# a = list(range(1, 8))
# print(a)
# a.append(99)  # добавляет элемент в конец списка
# print(a)
# a.extend([22, 11, 9])  # добавляет множество элементов в конец списка
# print(a)
# a.insert(0, 100)  # добавляет элемент в список. Первый параметр - индекс, второй - добавляемое значение
# print(a)
# a.extend('add')
# print(a)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("-> "))
#     s.append(x)
# print(s)

# s = []
# n = int(input('Введите количество элементов списка: '))
# for i in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'не делится на 3 без остатка')
#     else:
#         s.append(x)
# print(s)
#
# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input('Введите число кратное 3:  '))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, 'не делится на 3 без остатка')
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3]
# b = [11, 12, 13, 2, 4]
# c = []

# if len(b) < len(a):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# b = [11, 13, 12, 13, 2, 4, 13]
# b.remove(13)  # удаляет элемент из списка по значению, если элементов с заданным значением несколько, то удаляется
# # только первый
# print(b)
# a = 3
# if a in b:
#     b.remove(a)
# print(b)
#
# last = b.pop(1)  # c пустыми скобками - удаляет последний элемент из списка, с заданным индексом в скобках - удаление
# # по индексу
# print(b)
# print(last)
#
# b.clear()
# print(b)  # очищает список

# a = [int(input('-> ')) for num in ' ' * int(input('Count: '))]
# b = int(input('Index: '))
# a.pop(b)
# print(a)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# num = a.count(2)  # количество заданных значений в списке
# print(num)
# ind = a.index(2, 2, -1)  # возвращает первый индекс искомого значения. Также можно указать значения start и end
# print(ind)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# b = a.copy()
# print("a:", id(a))
# print("b:", id(b))
# a.append(20)
# b.remove(9)
# print("a:", a)
# print("b:", b)

# a = [9, 2, 7, 2, 4, 2, 3, 2]
# print(a)
# # a.reverse()  # перестраивает элементы списка в обратном порядке
# # print(a)
# a.sort()  # сортирует список, по умолчанию - по возрастанию, reverse=True - по убыванию
# print(a)
# #
# # b = ["Виталий", "Сергей", "Александр", "Анна"]
# # b.sort(key=len, reverse=True)
# # print(b)
#
# c = sorted(a)
# print(c)
# print(a)

# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(2, 9))  # от 2 по 9 (включительно)
# print(random.randrange(1, 9, 2))

# from random import randint, randrange
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))

# from random import *
#
# print(randint(2, 9))
# print(randrange(1, 9, 2))


# import random as r
#
# print(r.randint(2, 9))
# print(r.randrange(1, 9, 2))
# print(r.uniform(10.5, 25.5))
# print(round(r.uniform(10.5, 25.5), 3))
#
# city = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# # city = [5, 3, 9, 7, 8, 6, 4, 2, 1]
# # print(r.choice(city))
# print(r.choices(city, k=2))
# r.shuffle(city)
# print(city)

# import random as r

# mas = [r.randint(-30, 30) for i in range(5)]
# print(mas)

# lst = ["5, 3, 2, 4, 1", "abc"]
# print(len(lst))
# print(max(lst))
# print(min(lst))
# print(sum(lst))

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
#
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)

# x = list('1a2b3c4c')
# print(x)
# # print('a' in x)
# print('w' in x)
# # print('a' not in x)
# print('w' not in x)

# lst = []
# # if len(lst) == 0:
# if not lst:
#     print("Список пустой")
# print(bool(lst))

# from random import randint
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# k = int(input("Размер списка: "))
# s = []

# import random
#
# n = int(input("Размер списка: "))
# s = []
# for i in range(100):
#     num = random.randrange(10)
#     if num not in s:
#         s.append(num)
# print(s)


# from random import randint
#
# a = []
# step = 0
# n1 = int(input('Введите размер первого списка: '))
# while len(a) < n1:
#     i = randint(0, n1-1)
#     if i not in a:
#         a.append(i)
#     # else:
#     #     step -= 1
#     # step += 1
# print(a)

# import random
#
# n = int(input("Размер списка: "))
# s = []
# while len(s) < n:
#     num = random.randrange(n)
#     if num not in s:
#         s.append(num)
# print(s)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]

# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# from random import randint
# w, h = 5, 3
# matrix = [[0 for x in range(w)] for y in range(h)]
#
# matrix = []
# for y in range(h):  # 3
#     new_row = []
#     for x in range(w):  # 5
#         new_row.append(0)
#     matrix.append(new_row)

# print(matrix)
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# print([[x for x in row] for row in matrix])
# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# from random import randint
#
# w, h = 5, 3
# matrix = [[randint(10, 100) for x in range(w)] for y in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()


# from random import randint
#
# w, h = 3, 4
# count = 0
# matrix = [[randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#         if x < 0:
#             count += 1
#     print()
# print('Количество отрицательных чисел:', count)

# from random import randint

# w, h = 3, 4
# n = 1
# matrix = [[randint(0, 4) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         if x != 0:
#             n *= x
#         print(x, end='\t\t')
#     print()
# print('n=', n)


# w = h = 6
# n = 1
# matrix = [[randint(1, 100) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()
#
# # s = []
# m = 101
# for i in range(w):
#     # s.append(matrix[i][i])
#     if m > matrix[i][i]:
#         m = matrix[i][i]
# print(m)
# print(min(s))

# import geometry as m
# from geometry import sqrt, ceil, floor, pi
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num1)
# print(num2)
# print(num3)
#
# print(pi)

# from geometry import pi
#
# num = int(input('Введите радиус окружности: '))
# print('Длина окружности: ', round(2 * pi * num, 2))


# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# seconds = time.time()
# print(seconds)
#
# local_time = time.ctime(seconds)
# print(local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(4654414541)))
# print("Сегодня:", time.strftime("%B %d, %Y"))

# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res, "sec.")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res, "sec.")


# Функции
# a = 2
#
#
# def hello(name, word):
#     print("Hello, ", name, ". Say ", word, sep="")
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")
# get_sum(2.5, 4.7)

# def symbol(count, a, b):
#     # print((a + b) * (count // 2) + a * (count % 2))
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#     # print("".join([a if i % 2 == 0 else b for i in range(count)]))
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")
#
#
# def get_sum(count, a, b):
#     print(''.join(a * (1 - i % 2) + b * (i % 2) for i in range(count)))
#
#
# get_sum(9, "+", "-")


# def get_sum(a, b):
#     print(a + b)
#     return
#
#
# x = 2
# y = 5
# get_sum(x, y)


# def maximum(one, two):
#     if one > two:
#         return True
#     else:
#         return False
#
#
# if maximum(5, 13):
#     print("Первое число больше")
# else:
#     print("Второе число больше")

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Этот пароль надежный")
# else:
#     print("Это ненадежный пароль")


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     # end = lst.pop()
#     # start = lst.pop(0)
#     # lst.insert(0, end)
#     # lst.append(start)
#     # return lst
#     return [lst[-1]] + lst[1:-1] + [lst[0]]
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

# def get_sum(a, b, c=1, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 2, 5, 7))
# print(get_sum(1, 2, 5))
# print(get_sum(1, 2))
# print(get_sum(1, 2, d=5))

# def digits_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр: ")
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))
# print("Сумма нечетных цифр: ")
# print(digits_sum(9874023, even=False))
# print(digits_sum(38271, even=False))
# print(digits_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info('Igor', age=23, name="Ira")

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(lt1 == lt2)
# print(lt1 is lt2)
# print(id(lt1))
# print(id(lt2))
#
# a = 5
# print(id(a))
# a = 6
# # print(a == b)
# # print(a is b)
#
# print(id(a))


# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))


# s = True
# print(id(s))
# s = True
# print(s)
# print(id(s))

# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple([1, 2, 3, 4, 5])
# print(type(b))
# print(b)

# t = (2,)
# print(type(t))
# print(t)

# t = tuple("Hello")
# print(type(t))
# print(t)
#
# print(t[1])
# print(t[1:3])

# s = tuple(input('-> ') for i in range(3))
# print(s)

# s = input("-> ")
# print(tuple(s))
# from random import randint
#
#
# s = tuple(randint(1, 30) for i in range(20))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("hello")
# t2 = tuple("world")
# t3 = t1 + t2
# print(t3)


# print(len(t3))
#
# print(t3.count('l'))
# print(t3.count('a'))
#
# print(t3.index('l', 4))
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет")

# for i in t3:
#     print(i, end=" ")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def tuple_parse(tup, num):
#     if num not in tup:
#         return tuple()
#     first = tup.index(num)
#     if num not in tup[first + 1:]:
#         return tup[first:]
#     last = tup.index(num, first + 1)
#     return tup[first:last + 1]
#
#
# print(tuple_parse((1, 2, 3), 8))
# print(tuple_parse((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(tuple_parse((1, 2, 8, 5, 1, 2, 9), 8))


# from random import randint
#
# # def tpl_sum(t1, t2):
# #     print(t1)
# #     print(t2)
# #     print(t1 + t2, (t1 + t2).count(0))
# #
# #
# # tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
#
# # def tpl_sum(a, b):
# #     return tuple(randint(a, b) for _ in range(12))
# #
# #
# # t1 = tpl_sum(0, 5)
# # t1 = tuple(randint(0, 5) for i in range(12))
# # tpl_sum(tuple(randint(0, 5) for i in range(12)), tuple(randint(-5, 0) for j in range(12)))
# # print(t1)
# # t2 = tpl_sum(-5, 0)
# # # t2 = tuple(randint(-5, 0) for j in range(12))
# # print(t2)
# # t3 = t1 + t2
# # print(t3)
# # print(t3.count(0))
#
# # ============================
#
# # point = (10, 20)
# #
# # match point:
# #     case (0, 0):
# #         print("Точка находится в координатах 0:0")
# #     case (x, 0):
# #         print("Точка находится в координате", x, "по оси Х и в координате 0 по оси Y")
# #     case (0, y):
# #         print("!!!Точка находится в координате 0 по оси Х и в координате", y, "по оси Y")
# #     case (x, y):
# #         print("Точка находится в координате", x, "по оси Х и в координате", y, "по оси Y")
# #     case _:
# #         print("Это не координаты точки")
#
#
# # t = [2, 3]
# # print("t =", id(t))
# # print(id(t[0]))
# # t[0] = 5
# # print(t)
# # print(id(t[0]))
# # print("t =", id(t))
# # a = 5
# # print(id(a))
#
#
# # t = (10, 11, [1, 2, 3], [4, 5, 6, 4, 7, 8, 9, 6, 6, 12], ['hello', 'world'])
# # print("t =", t.__sizeof__())
# # print(t, id(t))
# # print(len(t))
# # t[4][0] = 'new'
# # t[4].append('hi')
# # print(t, id(t))
# # print(len(t))
# # print("t =", t.__sizeof__())
#
# # a = tuple(range(2))
# # print(a)
# # print(a.__sizeof__())
# # b = tuple(range(1))
# # print(b)
# # print(b.__sizeof__())
#
# # Распаковка кортежей
#
# # t = (1, 2, 3)
# # # x = t[0]
# # # y = t[1]
# # # z = t[2]
# # x, y, z = t
# # print(x, y, z)
#
# # def get_user():
# #     name = "Tom"
# #     age = 22
# #     is_married = False
# #     return name, age, is_married
#
#
# # name1, age1, married1 = get_user()
# # user = get_user()
# # name1, age1, married1 = user
# # print(name1, age1, married1)
# # print(user[0])
# # print(user[1])
# # print(user[2])
#
# # a = (1, 2)
# # del a
# # print(a)
#
# # lst = [1, 2, 3, 4, 5, 6]
# # print(lst)
# # tpl = tuple(lst)
# # print(tpl)
# # lst = list(tpl)
# # print(lst)
#
# # countries = (
# #     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
# #     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# # )
# #
# # print(countries)
# # print()
# # for country in countries:
# #     countryName, countryPopulation, cities = country
# #     print("\nСтрана:", countryName, "население =", countryPopulation)
# #     for city in cities:
# #         cityName, cityPopulation = city
# #         print("\tГород:", cityName, "население =", cityPopulation)
#
#
# # list()
# # tuple()
# # set() - множество
#
# # s = {'banana', 'apple', 'orange', 'apple', 'orange'}
# # print(s)
# # print(type(s))
# # print(len(s))
#
# # c = ['red', 'green', 'green', 'blue']
# # a = set(c)
# # print(type(a))
# # print(a)
#
# # numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# # s = list({x for x in numbers if x % 2 == 0})
# # print(s)
#
#
# # def to_set(par):
# #     st = set(par)
# #     return st, len(st)
# #
# #
# # print(to_set('я обычная строка'))
# # print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
#
#
# # s = {'banana', 'apple', 'orange'}
# # print('apple' in s)
# # print('apple' not in s)
# # print(s)
# # for i in s:
# #     print(i)
#
# # r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # b = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# # c = {"A" + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# # print(a)
# # print(b)
# # print(c)
# #
# # for i in r:
# #     if i[1] == 'c':
# #         if i[0] == 'a':
# #             print("A" + i[1:])
# #         else:
# #             print('B' + i[1:])
# #
# #
# # for i in r:
# #     if i[0] == 'a':
# #         if i[1] == 'c':
# #             print("A" + i[1:])
# #     else:
# #         if i[1] == 'c':
# #             print('B' + i[1:])
#
#
# # s = {'banana', 'apple', 'orange'}
# # print(s)
# # # s.add(4)  # добавляет элемент во множество
# # # if 44 in s:
# # #     s.remove(44)  # удаляет элемент по значению
# # # s.discard(44)  # удаляет элемент по значению без генерации исключения
# # a = s.pop()  # удаление первого элемента
# # s.clear()  # полная очистка множества
# # print(s)
# # print(a)
#
#
# # Операции над множествами
# # a = {0, 1, 2, 3, 4}
# # b = {4, 3, 2, 1}
# # # c = a.union(b)
# # # c = a | b
# # # c = a & b
# # # a |= b
# # # a &= b
# # # c = b - a
# # # a -= b
# # # c = a ^ b
# # # a ^= b
# # c = a < b
# # print(c)
# # print(a)
#
# # s1 = {1, 2}
# # s2 = {3}
# # s3 = {4, 5}
# # s4 = {3, 2, 6}
# # s5 = {6}
# # s6 = {7, 8}
# # s7 = {9, 8}
# #
# # # s = s1.union(s2, s3, s4, s5, s6, s7)
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# # print(s)
# # print(len(s))
# # print(min(s))
# # print(max(s))
# # print(sum(s))
#
# # s1 = 'Hello'
# # s2 = "How are you"
# # a = set(s1) & set(s2)
# # for i in a:
# #     print(i, end=" ")
#
#
# # s1 = "Python"
# # s2 = "Programming language"
# # print(set(s1).difference(s2))
# #
# # s1 = 'Python'
# # s2 = 'Programing language'
# # print(set(s1) - set(s2))
# #
# # a = "Python"
# # b = "Programming language"
# # c = set(a) - set(b)
# # for i in c:
# #     print(i, end=" ")
#
# # drawing = {'Марина', 'Женя', 'Света'}
# # music = {'Костя', 'Женя', 'Илья'}
# #
# # one_hobby = drawing ^ music
# # print(one_hobby)
# # both_hobby = drawing & music
# # print(both_hobby)
# # drawing = drawing - both_hobby
# # print(drawing)
#
# # ========================================
# # list()
# # tuple()
# # set() - множество
# # frozenset()
#
# # s = frozenset([1, 2, 3, 4, 5])
# # print(s)
# #
# # s1 = frozenset({"hello", "world"})
# # print(s1)
#
#
# # Словарь (dict)
#
# # a = [1, 2, 3]
# # d = {1: 'one', 'two': 2, 'three': 3, 'four': 3}
# # print(a[0])
# # print(d[1])
#
# # d = {'one': 1, 'two': 2}
# # d = dict(one=1, two=2)
# # print(d)
# # print(type(d))
#
# # a = (
# #     ('igor@gmail.com', 'Igor'),
# #     ('irina@gmail.com', 'Irina'),
# #     ('anna@gmail.com', 'Anna'),
# # )
# #
# # b = dict(a)
# # print(b)
#
# # d = {i: 100 for i in range(2, 7)}
# # print(d)
# # print(d[3])
# # d[3] = 15
# # print(d)
#
#
# # d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# # print(d)
# # print(d[42][1])
# # print(d[(1, 2.3)])
# # d[(1, 2.3)] = "Новое значение"
# # print(d)
# # print("one1" in d)
# # key = 'one1'
# # if key in d:
# #     del d[key]
# # print(d["one1"])
# # try:
# #     del d[key]
# # except KeyError:
# #     print("Элемента с ключом " + key + " нет в словаре")
#
# # d = {0: 'text', 'one': 45, (1, 2.3): "Кортеж", 42: [2, 3, 6, 7], True: {1, 0}}
# # print(d)
# #
# # for key in d:
# #     print(key, "-> ", d[key])
#
# # a = {"x1": 3, "x2": 7, "x3": 5, "x4": -1}
# # s = 1
# # for i in a:
# #     s *= a[i]
# # print(s)
#
# # d = dict()
# # d[1] = input("-> ")
# # d[2] = input("-> ")
# # d[3] = input("-> ")
# # d[4] = input("-> ")
# # d = {input("-> "): input("-> ") for i in range(1, 5)}
# # print(d)
# # dislike = int(input("Какой элемент исключить: "))
# # del d[dislike]
# # print(d)
#
# # goods = {
# #     '1': ['Core-i3-4330', 9, 4500],
# #     '2': ['Core i5-4670K', 3, 8500],
# #     '3': ['AMD FX-6300', 6, 3700],
# #     '4': ['Pentium G3220', 8, 2100],
# #     '5': ['Core i5-3450', 5, 6400],
# # }
# #
# # for i in goods:
# #     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
# #
# # while True:
# #     n = input('№: ')
# #     if n != '0':
# #         qty = int(input("Количество: "))
# #         goods[n][1] = qty
# #     else:
# #         break
# #
# # for i in goods:
# #     print(i, ") ", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# # studs = {}
# # n = int(input("Количество студентов: "))
# # s = 0
# # for i in range(n):
# #     sname = input(str(i + 1) + "-й студент: ")
# #     point = int(input("Балл: "))
# #     studs[sname] = point
# #     s += point
# #
# # print(studs)
# # avrg = s / n
# # print(avrg)
# # for i in studs:
# #     if studs[i] > avrg:
# #         print(i)
#
# # d = {'a': 1, 'b': 2, 'c': 3}
# # print(d['c'])
# # value = d.get('f', False)  # получить значение по заданному ключи
# # print(value)
# # n = d.keys()  # список ключей
# # print(n)
# # n = d.values()  # список значений
# # print(n)
# # n = d.items()  # список кортежей ключ + значение
# # print(n)
# #
# # for i, j in d.items():
# #     print(i, "->", j)
#
#
# # d = {'a': 1, 'b': 2, 'c': 3}
# #
# # d2 = d.copy()  # создание копии словаря
# #
# # print("D =", d)
# # print("D2 =", d2)
# #
# # d['b'] = 5
# # d2['e'] = 7
# #
# # print("D =", d)
# # print("D2 =", d2)
#
#
# # d = {'a': 1, 'b': 2, 'c': 3}
# # item = d.pop('b')  # удаляет элемент из словаря по ключу, возвращает значение ключа
# # print(item)
# # print(d)
# # item = d.popitem()  # удаляет произвольную пару ключ + значение и возвращает их
# # print(item)
# # print(d)
# # item = d.setdefault("f", 5)  # добавляет ключ со значением по умолчанию, если ключа не существует
# # print(item)
# # print(d)
#
# # d.update({"a": 20, 'w': 10})  # обновление словаря
# # print(d)
# # d.update([('q', 7), ('t', 9)])
# # print(d)
#
#
# # x = {'a': 1, 'b': 2}
# # y = {'b': 3, 'd': 4}
# # # z = x.copy()
# # # z.update(y)
# # # z = y | x
# # print(z)
#
# # d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# #
# # # new_d = dict()
# # # new_d['name'] = d.pop('name')
# # # new_d['salary'] = d.pop('salary')
# # # new_d = {'name': d.pop('name'), 'salary': d.pop('salary')}
# # # print(d)
# # # print(new_d)
# #
# # d['location'] = d.pop('city')
# # print(d)
#
# # a = {
# #     'first': {
# #         1: 'one',
# #         2: 'two',
# #         3: 'three',
# #     },
# #     'second': {
# #         4: 'four',
# #         5: 'five'
# #     }
# # }
# # print(a)
# # for x in a:
# #     print(x)
# #     for y in a[x]:
# #         print('\t', y, ": ", a[x][y], sep="")
#
# # sales = {
# #     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
# #     "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
# #     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
# #     "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
# # }
# #
# # for x in sales:
# #     print(x)
# #     for y in sales[x]:
# #         print('\t', y, ": ", sales[x][y], sep="")
# #
# # person = input("Имя: ")
# # region = input("Регион: ")
# # print(sales[person][region])
# # new_data = int(input("Новое значение: "))
# # sales[person][region] = new_data
# # print(sales[person])
#
# # ====================================
#
# # d = {'c': 3, 'a': 1, 'b': 2, 'd': 4}
# # w = {k: v for k, v in d.items()}
# # print(w)
# # for i, j in d.items():
# #     if len(d) <= 2:
# #         print(i, ":", j)
#
# # d = {'a': 1, 'b': 2, 'c': 3}
# # count = 0
# # for i in d:
# #     print(i, ':', d[i])
# #     count += 1
# #     if count == 2:
# #         break
#
# # value = int(input("-> "))
# # lt = [7, 8, 9, 10]
# # d = {k: value for k in lt}
# # print(d)
#
# # d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# #
# # value = list(d.keys())
# # print(value)
# # value = list(d.values())
# # print(value)
# # value = list(d.items())
# # print(value)
#
#
# # a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# #
# # d = dict()
# # s = None
# #
# # for i in a:
# #     if type(i) == str:
# #         d[i] = []  # d['two'] = []
# #         s = i  # s = 'two'
# #     else:
# #         d[s].append(i)  # d['two'] = [10, 20]
# #
# # print(d)
#
# # a = ['Dec', 'Jan', 'Feb']
# # b = [12, 1, 2]
# # d = dict(zip(b, a))
# # print(d)
#
#
# # b = [12, 1, 2]
# # d = list(zip(b))
# # print(d)
#
#
# # a = ['Dec', 'Jan', 'Feb']
# # b = [12, 1, 2]
# # c = [2.0, 4.6, 7.5]
# #
# # d = list(zip(a, b, c))
# # print(d)
#
#
# # one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# # two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# #
# # for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
# #     print(k1, '->', v1)
# #     print(k2, '->', v2)
#
# # obj = {
# #     'one': {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'},
# #     'two': {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# # }
# # print(obj)
#
# # pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # a, b = zip(*pairs)
# # print(a)
# # print(b)
#
# # one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.6}
# # two = {'pepper': 0.8, 'onion': 0.55}
# # print({**one, **two})
#
#
# # {{'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55}}
# # {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# # data = ['a', 'b', 'c', 'd']
#
# # for i in data:
# #     print(i, end=" ")
# # print()
# # for i in range(len(data)):
# #     print(i, end=" ")
# # print()
# #
# # j = 1
# #
# # for i in data:
# #     print(j, ":", i)
# #     j += 1
#
# # for j, i in enumerate(data, 100):
# #     print(j, ":", i)
#
# # n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# #
# # for j, (i, v) in enumerate(n.items(), 100):
# #     print(j, ":", i, "->", v)
#
#
# # a = [1, 2, 3]
# # b = [4, *a, 5, 6]
# # print(b)
#
#
# # def func(*args):
# #     res = 0
# #     for i in args:
# #         res += i
# #     return res
# #
# #
# # print(func(3, 2))
# # print(func(3, 4, 6, 9, 5))
# # print(func())
#
#
# # def to_dict(*lst):
# #     print(*lst)
# #     print(lst)
# #     return {i: i for i in lst}
# #
# #
# # print(to_dict(1, 2, 3, 4))
# # print(to_dict('gray', (2, 17), 3.11, -4))
# #
# # def ch(*args):
# #     pass
# #
# #
# # print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# # print(ch(3, 6, 1, 9, 5))
#
#
# # def fun(*a):
# #     return [i for i in a if i < sum(a) / len(a)]
# #
# #
# # print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# # print(fun(3, 6, 1, 9, 5))
#
#
# # def func(*lst):
# #     sum = 0
# #     count = 0
# #     new_lst = []
# #     for i in lst:
# #         sum += i
# #         count += 1
# #     avarange = sum / count
# #     print('Ср. ариф: ', avarange)
# #     for j in lst:
# #         if j < avarange:
# #             new_lst.append(j)
# #     print(new_lst)
# #
# #
# # func(1, 2, 3, 4, 5, 6, 7, 8, 9)
#
# # def func(a, b,  *args):
# #     return a, b, args
# #
# #
# # print(func(2, 3))
# # print(func(2, 3, 4, 'abc'))
#
# # def print_scores(student, *scores):
# #     print("Student Name:", student, end=", scores: ")
# #     a, b = None, ""
# #     for score in scores:
# #         a = str(score) + ", "
# #         b += a
# #     print(b[:-2])
# #
# #
# # print_scores("Kate", 100, 95, 88, 92, 99)
# # print_scores('Rick', 96, 20, 33, 56)
#
#
# # def print_scores(student, *scores):
# #     print("Student Name:", student, end=", scores: ")
# #     count = 0
# #     for score in scores:
# #         count += 1
# #         if count != len(scores):
# #             print(score, end=", ")
# #         else:
# #             print(score)
# #
# #
# # print_scores("Kate", 100, 95, 88, 92, 99)
# # print_scores('Rick', 96, 20, 33, 56)
# # def reverse_num(n):  # 12 => 21
# #     s = str(n)
# #     return int(s[::-1])
# #
# #
# # def func(*args, only_add=False):
# #     res = []
# #     for i in args:
# #         if not only_add or only_add and i % 2:
# #             res.append(reverse_num(i))
# #     return res
# #
# #
# # print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# # print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))
#
#
# # def func(**kwargs):
# #     return kwargs
# #
# #
# # print(func(a=1, b=2, c=3))
# # print(func())
# # print(func(a="python"))
#
# # def func(**data):
# #     for key, value in data.items():
# #         print(key, "is", value)
# #     print()
# #
# #
# # func(name="Irina", surname="Sharma", age=22, phone=1234567890)
# # func(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=9876543210)
#
#
# # def func(**data):
# #     # for key, value in data.items():
# #     #     my_dict[key] = value
# #     # return my_dict
# #     my_dict.update(data)
# #
# #
# # my_dict = {'one': 'first'}
# # func(k1=22, k2=31, k3=11, k4=91)
# # print(my_dict)
# # func(name='Bob', age=31, weight=61, eyes_color='grey')
# # print(my_dict)
#
# # def func(a, *args, b=2, **kwargs):
# #     print(a, kwargs, args, b)
# #
# #
# # func(4, 5, 6, 7, b=3, k1=22, k2=31, k3=11, k4=91)
#
#
# # Области видимости (scope)
#
# # name = "Tom"  # глобальная переменна
# # surname = "sum"
# #
# #
# # def hi():
# #     global name, surname
# #     name = "Sam"  # локальные переменные
# #     surname = "Johnson"
# #     print("Hello", name, surname)
# #
# #
# # def bye():
# #     print("Good bye", name, surname)
# #
# #
# # hi()
# # print(surname)
# # bye()
#
# # i = 5
# #
# #
# # def func(arg=i):
# #     print(arg)
# #
# #
# # i = 6
# # func()  # 5
#
# # x = 5
# #
# #
# # def add_two(a):
# #     # x = 2
# #
# #     def add_some():
# #         # x = 3
# #         return a + x
# #
# #     return add_some()
# #
# #
# # print(add_two(3))
#
# # import builtins
# #
# # name = dir(builtins)
# #
# # for t in name:
# #     print(t)
#
# # type1 = [8, 1, 2, 4, 5, 6, 9]
# # print(min(type1))
# #
# # a = [7, 8, 9, 5]
# # print(type(a))
#
#
# # def outer_func(who):
# #     def inner_func():
# #         print("Hello,", who)
# #
# #     inner_func()
# #
# #
# # outer_func("world!")
#
#
# # def fun1():
# #     a = 6
# #
# #     def fun2(b):
# #         a = 4
# #         print(a + b)
# #
# #     print("a =", a)
# #     fun2(4)
# #
# #
# # fun1()
#
# # x = 25
# # t = 0
# #
# #
# # def fn():
# #     global t
# #     a = 30
# #
# #     def inner():
# #         nonlocal a
# #         a = 35
# #
# #     inner()
# #     t = a
# #
# #
# # fn()
# # z = x + t  # 25 + 30 = 55
# # print(z)  # 25 + 35 = 60
#
# # x = 5
# #
# #
# # def fn1():
# #     x = 25
# #
# #     def fn2():
# #         # x = 33
# #
# #         def fn3():
# #             nonlocal x
# #             x = 55
# #
# #         fn3()
# #         print('fn2.x =', x)
# #
# #     fn2()
# #     print('fn1.x =', x)
# #
# #
# # fn1()
# # print(x)
#
# # def outer(a1, b1, a2, b2):
# #     a = 0
# #     b = 0
# #
# #     def inner():
# #         nonlocal a, b
# #         a = a1 + a2
# #         b = b1 + b2
# #
# #     inner()
# #
# #     return [a, b]
# #
# #
# # res = outer(2, 3, -1, 4)
# # # print(res)
#
# # Замыкание
#
# # def outer(n):
# #     def inner(x):
# #         return n + x
# #
# #     return inner
# #
# #
# # add = outer(5)
# # print(add(10))
# # print(add(20))
# #
# # add1 = outer(6)
# # print(add1(10))
# # print(outer(5)(10))
#
#
# # def func1():
# #     a = 1
# #     b = 'line'
# #     c = [1, 2, 3]
# #
# #     def func2():
# #         nonlocal a, b
# #         c.append(4)
# #         a = a + 1
# #         b = b + "_new"
# #         return a, b, c
# #
# #     return func2
# #
# #
# # func = func1()
# # print(func())
#
# # def rect_paral_square(a, b, c):
# #     def rect_square(i, j):
# #         return i * j
# #
# #     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
# #     return s
# #
# #
# # print(rect_paral_square(2, 4, 6))
# # print(rect_paral_square(5, 8, 2))
# # print(rect_paral_square(1, 6, 8))
# # s = 0
# #
# #
# # def rect_paral_square(a, b, c):
# #     def rect_square(i, j):
# #         return i * j
# #
# #     global s
# #     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
# #
# #
# # rect_paral_square(2, 4, 6)
# # print(s)
# # rect_paral_square(5, 8, 2)
# # print(s)
# # rect_paral_square(1, 6, 8)
# # print(s)
#
#
# # def rect_paral_square(a, b, c):
# #     s = 0
# #
# #     def rect_square(i, j):
# #         nonlocal s
# #         s += i * j
# #
# #     rect_square(a, b)
# #     rect_square(a, c)
# #     rect_square(b, c)
# #     return 2 * s
# #
# #
# # print(rect_paral_square(2, 4, 6))
# # print(rect_paral_square(5, 8, 2))
# # print(rect_paral_square(1, 6, 8))
#
# # def func(city):
# #     s = 0  # 3  2
# #
# #     def wrap():
# #         nonlocal s
# #         s += 1
# #         print(city, s)  # 3
# #
# #     return wrap
# #
# #
# # res1 = func('Москва')
# # res1()
# # res1()
# # res2 = func('Сочи')
# # res2()
# # res2()
# # res1()
#
# # students = {
# #     'Alice': 98,
# #     'Bob': 67,
# #     'Chris': 85,
# #     'David': 75,
# #     'Ella': 54,
# #     'Fiona': 35,
# #     'Grace': 69
# # }
# #
# #
# # def classifier(lower, upper):
# #     def student(exam):
# #         return {k: v for k, v in exam.items() if lower <= v < upper}
# #
# #     return student
# #
# #
# # A = classifier(80, 100)
# # B = classifier(70, 80)
# # C = classifier(50, 70)
# # D = classifier(0, 50)
# # print("A =", A(students))
# # print("B =", B(students))
# # print("C =", C(students))
# # print("D =", D(students))
#
# # def func(a, b):
# #     def add():
# #         return a + b
# #
# #     def sub():
# #         return a - b
# #
# #     def mul():
# #         return a * b
# #
# #     def replace():
# #         print("qqq")
# #
# #     replace.add = add
# #     replace.sub = sub
# #     replace.mul = mul
# #     return replace
# #
# #
# # obj1 = func(5, 2)
# # print(obj1.add())
# # print(obj1.sub())
# # print(obj1.mul())
# # obj1()
#
#
# # lambda (Анонимные функции)
#
# # print((lambda x, y: x + y)(1, 2))
# # c = (lambda x, y: x + y)('a', 'b')
# # print(c)
# # a = 5
# # func = lambda x, y: x + y + a
# # b = func(1, 2)
# # print(b)
# # # print(func('a', 'b'))
# #
# # (lambda: print("Hello"))()
#
#
# # print((lambda x, y: x ** 2 + y ** 2)(2, 5))
#
# # summ = lambda a=1, b=2, c=3: a + b + c
# #
# # print(summ(10, 20, 30))
# # print(summ(10, 20))
# # print(summ(10))
# # print(summ())
#
# # func = lambda *args: args
# # #
# # # print(func(1, 2, 3, 4, 5, 6, 7))
# # # print(func())
# #
# #
# # c = (lambda x: x * 2,
# #      lambda x: x * 3,
# #      lambda x: x * 4)
# #
# # for t in c:
# #     print(t('abc_'))
#
# # def inc(n):
# #     return lambda x: n + x
# #
# #
# # f = inc(42)
# # print(f(3))
# #
# #
# # inc1 = (lambda n: lambda x: n + x)
# #
# # f3 = inc1(42)
# # print(f3(3))
# # print("!!!", (lambda n: lambda x: n + x)(42)(3))
# #
# #
# # def inc2(n):
# #     def wrap(x):
# #         return n + x
# #
# #     return wrap
# #
# #
# # f1 = inc2(42)
# # print(f1(3))
#
# # ====================
#
# # print((lambda i: lambda j: lambda k: i + j + k)(2)(4)(6))
#
#
# # players = [
# #     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
# #     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
# #     {'name': 'Федоров', 'last name': 'Сидоров', 'rating': 4},
# #     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# # ]
# #
# # res = sorted(players, key=lambda item: item['last name'])
# # print(res)
# #
# # res = sorted(players, key=lambda item: item['rating'])
# # print(res)
# #
# # res = sorted(players, key=lambda item: item['rating'], reverse=True)
# # print(res)
#
# # def func(i):
# #     return i[1]
# #
# #
# # d = {'b': 15, 'a': 3, 'c': 7}  # {'a': 3, 'c': 7, 'b': 15}
# # lst = list(d.items())
# # print(lst)
# # # lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# # print(lst)
# # print(dict(lst))
#
# # a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# #
# # print(a[3](12, 3))
#
# # a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# # b = [-3, 10, 0, 4]
# #
# # for i in b:
# #     if i < 0:
# #         print(a['two'](i))
# #     elif i > 0:
# #         print(a['one'](i))
# #     else:
# #         print(a['three'](i))
#
# # d = {
# #     1: lambda: print("Понедельник"),
# #     2: lambda: print("Вторник"),
# #     3: lambda: print("Среда"),
# #     4: lambda: print("Четверг"),
# #     5: lambda: print("Пятница"),
# #     6: lambda: print("Суббота"),
# #     7: lambda: print("Воскресенье")
# # }
# #
# # d[3]()
#
#
# # print((lambda a, b: a if a > b else b)(12, 5))
#
# # m = lambda a, b, c: a if a < b else b if b < c else c
# # print(m(19, 28, 5))
# #
# # print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 18, 15))
#
#
# # map(func, iterable), filter(func, iterable)
#
# # def mul(t):
# #     return t * 2
#
#
# # lst = [2, 8, 12, -5, -10]
# #
# # # lst2 = list(map(mul, lst))
# # lst2 = list(map(lambda t: t * 2, lst))
# # print(lst2)
#
# # t = (2.88, -1.75, 100.03)
# #
# # # t2 = tuple(map(lambda x: int(x), t))
# # t2 = tuple(map(int, t))
# #
# # print(t2)
#
# # area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
# #
# # res = list(map(round, area, range(1, 7)))
# #
# # print(res)
#
# # print(round(3.45612131, 3))
#
# # st = ['a', 'b', 'c', 'd', 'e']
# # num = [1, 2, 3, 4, 5]
# #
# # res = list(map(lambda x, y: (x, y), st, num))
# # print(res)
# #
# # l1 = [1, 2, 3]
# # l2 = [4, 5, 6]
# # print(list(map(lambda x, y: x + y, l1, l2)))
#
#
# # GitHub.com
#
#
# # lst = [3, 6, 8, 9, 1, 2]
# # print(list(map(lambda elem: elem * lst.index(elem) ** 3, lst)))
#
# # filter(func, iterable)
#
# # t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# # t2 = tuple(filter(lambda s: len(s) == 3, t))
# # print(t2)
#
# # b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# # res = list(filter(lambda s: s > 75, b))
# # print(res)
#
# # z = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# # res = list(filter(lambda a: 10 < a <= 20, z))
# # print(res)
#
#
# # from random import randint
# #
# # lst = [randint(1, 40) for i in range(10)]
# # print(lst)
# # lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# # print(lst2)
#
# # nums = [45, 55, 60, 37, 100, 105, 220]
# # res = list(filter(lambda x: x % 15 == 0, nums))
# # print(res)
#
# # m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))  # (1, 3, 5, 7, 9)
# # print(m)
# #
# # m1 = [x ** 2 for x in range(10) if x % 2]
# # print(m1)
#
#
# # Декораторы
#
#
# # def hello():
# #     return 'Hello, I am func "hello"'
# #
# #
# # def super_func(func):
# #     print("Hello, I am func 'super_func'")
# #     print(func())
# #
# #
# # super_func(hello)
#
# # def hello():
# #     return 'Hello, I am func "hello"'
# #
# #
# # test = hello
# # print(test())
#
#
# # def my_decorator(func):
# #     def func_wrapper():
# #         print('Code before')
# #         func()
# #         print('Code after')
# #     return func_wrapper
# #
# #
# # def func_test():
# #     print('Hello, I am func "func_test"')
# #
# #
# # test = my_decorator(func_test)
# # test()
#
#
# # def my_decorator(func):  # декорирующая функция
# #     def func_wrapper():
# #         print('*' * 40)
# #         func()
# #         print('*' * 40)
# #     return func_wrapper
# #
# #
# # @my_decorator  # декоратор
# # def func_test():  # декорируемая функция
# #     print('Hello, I am func "func_test"')
# #
# #
# # func_test()
# # def bold(fn):
# #     def wrap():
# #         return "<b>" + fn() + "</b>"
# #
# #     return wrap
# #
# #
# # def italic(fn):
# #     def wrap():
# #         return "<i>" + fn() + "</i>"
# #
# #     return wrap
# #
# #
# # @bold
# # @italic
# # def hello():
# #     return "text"
# #
# #
# # print(hello())
#
# # def cnt(fn):
# #     count = 0
# #
# #     def wrap():
# #         nonlocal count
# #         count += 1
# #         fn()
# #         print("Вызов функции:", count)
# #
# #     return wrap
# #
# #
# # @cnt
# # def hello():
# #     print("Hello")
# #
# #
# # hello()
# # hello()
# # hello()
# # hello()
# # hello()
#
#
# # def args_decorator(fn):
# #     def wrap(arg1, arg2):
# #         print("Данные:", arg1, arg2)
# #         fn(arg1, arg2)
# #
# #     return wrap
# #
# #
# # @args_decorator
# # def print_full_name(first, last):
# #     print("Меня зовут", first, last)
# #
# #
# # print_full_name("Ирина", "Назарова")
#
# # def args_decorator(fn):
# #     def wrap(*args, **kwargs):
# #         print(*args)
# #         print("args:", args)
# #         print("kwargs:", kwargs)
# #         fn(*args, **kwargs)
# #
# #     return wrap
# #
# #
# # @args_decorator
# # def print_full_name(first, last):
# #     print("Меня зовут", first, last)
# #
# #
# # @args_decorator
# # def print_full_name_1(first, second, last):
# #     print("Меня зовут", first, second, last)
# #
# #
# # print_full_name("Ирина", "Назарова")
# # print()
# # print_full_name_1("Виктор", last="Назаров", second="Федорович")
#
# # def decor(args1, args2):
# #     def args_dec(fn):
# #         def wrap(x, y):
# #             print(args1, x, args2, y, "=", end=" ")
# #             fn(x, y)
# #
# #         return wrap
# #     return args_dec
# #
# #
# # @decor("Сумма:", "+")
# # def summa(a, b):
# #     print(a + b)
# #
# #
# # @decor("Разность:", "-")
# # def sub(a, b):
# #     print(a - b)
# #
# #
# # summa(5, 2)
# # sub(5, 2)
# #
# # def decor(*args):
# #     def args_dec(fn):
# #         def wrap(x, y):
# #             # print(args[0], x, args[1], y, "=", end=" ")
# #             print(*args, end=" ")
# #             fn(x, y)
# #
# #         return wrap
# #     return args_dec
# #
# #
# # @decor("Сумма:", "+")
# # def summa(a, b):
# #     print(a + b)
# #
# #
# # @decor("Разность:", "-")
# # def sub(a, b):
# #     print(a - b)
# #
# #
# # summa(5, 2)
# # sub(5, 2)
#
#
# # def multiply(num):
# #     def decor(fn):
# #         def wrap(mult):
# #             return num * fn(mult)
# #
# #         return wrap
# #
# #     return decor
# #
# #
# # @multiply(3)
# # def return_num(ch):
# #     return ch
# #
# #
# # print(return_num(5))
#
# # def typed(*args, **kwargs):
# #     def wrapper(fn):
# #         def wrap(*f_args, **f_kwargs):
# #
# #             for i in range(len(args)):
# #                 if type(f_args[i]) != args[i]:
# #                     raise TypeError("Некорректный тип данных", f_args[i])  # print("Некорректный тип данных!")
# #             for k in kwargs:
# #                 if type(f_kwargs[k]) != kwargs[k]:
# #                     raise TypeError("Некорректный тип данных", f_kwargs[k])
# #
# #             return fn(*f_args, **f_kwargs)
# #
# #         return wrap
# #     return wrapper
# #
# #
# # @typed(int, int, int)
# # def typed_fn(x, y, z):
# #     return x * y * z
# #
# #
# # @typed(str, str, str)
# # def typed_fn2(x, y, z):
# #     return x + y + z
# #
# #
# # @typed(str, str, z=int)
# # def typed_fn3(x, y, z="Hello"):
# #     return (x + y) * z
# #
# #
# # print(typed_fn(3, 4, 5))
# # # print(typed_fn(3, 4, "Doge"))
# # print(typed_fn2("Hello", "World", "!"))
# # print(typed_fn3("Hello", "World", z=5))
#
#
# # def args_decorator(tx=None, decorator_text=""):
# #     def my_decorator(func):
# #         def wrap(*args):
# #             print(decorator_text, end="")
# #             func(*args)
# #
# #         return wrap
# #
# #     if tx is None:
# #         return my_decorator
# #     else:
# #         return my_decorator(tx)
# #
# #
# # @args_decorator(decorator_text="Hello, ")
# # def hello_world(text):
# #     print(text)
# #
# #
# # @args_decorator
# # def hello_world2(text):
# #     print(text)
# #
# #
# # hello_world("world!")
# # hello_world2("Hi!")
#
# # def avg(fn):
# #     def wrap(*args):
# #         a = ""
# #         for i in args:
# #             a += str(i) + ", "
# #         # a = ", ".join(list(map(str, args)))
# #         print("Среднее арифметическое:", a[:-2], "=", fn(*args) / len(args))
# #
# #     return wrap
# #
# #
# # @avg
# # def summa(*args):
# #     print("Сумма чисел:", *args, "=", sum(args))
# #     return sum(args)
# #
# #
# # summa(2, 3, 3, 4)
#
# # print("Hello")
#
# # a = 5
# # print(a)
#
# # print("Вносим изменения в склонированный проект")
# # print("Вносим изменения в склонированный проект")
#
# # print(int('18'))
# # # print(int('18.5'))
# # print(int(18.5))
#
# # print(int('100', 2))
# # print(int('100', 8))
# # print(int('100', 10))
# # print(int('100', 16))
#
# # print(bin(18))  # 0b10010
# # print(oct(18))  # 0o22
# # print(hex(18))  # 0x12
# #
# # print(0b10010)
# # print(0o22)
# # print(0x12)
#
# # q = 'Pyt'
# # w = "hon"
# # e = q + w
# # print(e)
# # # print(e * 2)
# # # print('q' in e)
# #
# # print(e[-1::-1])
#
#
# # s = "Python"  # Pytton
# # s = s[:3] + 't' + s[4:]
# # print(s)
#
# # def change_char_to_str(s, c_old, c_new):
# #     s2 = ""
# #     for i in range(len(s)):
# #         if s[i] == c_old:
# #             s2 += c_new
# #         else:
# #             s2 += s[i]
# #     return s2
# #
# #
# # str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# # str2 = change_char_to_str(str1, 'N', 'P')
# # print(str1)
# # print(str2)
#
# # print(u"Привет")
# # print("Привет")
#
# # print(r"C:\folder\file.txt")
# # print("C:\\folder\\file.txt\\")
# #
# # print(r"C:\folder\\"[:-1])
# # print(r"C:\folder" + "\\")
#
# # from geometry import pi
# #
# # name = "Дмитрий"
# # age = 25
# # print(f"Меня зовут {name}. Мне {age} лет.")
# # print(f"Значение числа pi: {round(pi, 2)}")
# # print(f"Значение числа pi: {pi:.2f}")
# #
# # x = 5
# # y = 10
# # print(f"{x} x {y} / 2 = {x * y / 2}")
# # print(f"{x = }, {y = }")
#
# # a = 74
# # print(f"{{{{{a}}}}}")
#
#
# # dir_name = "my_doc"
# # file_name = "data.txt"
# # print(fr"home\{dir_name}\{file_name}")
#
#
# # s = """
# #     <div>
# #         <p>Текст</p>
# #     </div>
# # """
# # print(s)
# # '''<div>
# #     <p>Текст</p>
# # </div>
# # '''
# # # print(s1)
# #
# # "Hello"
# # def square(n):
# #     """Принимает число n, возвращает квадрат числа n"""
# #     return n ** 2
# #
# #
# # print(square(5))
# #
# # print(square.__doc__)
# # a = list.__doc__
# # print(a)
#
# # import geometry
# #
# #
# # def cylinder(r, h):
# #     """
# #     Вычисляет площадь цилиндра.
# #
# #     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
# #
# #     :param r: положительно число, радиус основания цилиндра
# #     :param h: положительно число, высота цилиндра
# #     :return: положительно число, площадь цилиндра
# #     """
# #     return 2 * geometry.pi * r * (r + h)
# #
# #
# # print(cylinder(2, 4))
# # print(cylinder.__doc__)
#
# # print(ord('a'))  # 97
#
# # while True:
# #     n = input("-> ")
# #     if n != "-1":
# #         print(ord(n))
# #     else:
# #         break
#
#
# # my_str = "Test string for mee"
# # arr = [ord(x) for x in my_str]
# # print("ASCII коды:", arr)
# # arr = [sum(arr) // len(arr)] + arr
# # print("Среднее арифметическое:", arr)
# # arr += [ord(x) for x in (input("-> ")[:3]) if ord(x) not in arr]
# # print(arr)
# # # if arr[-1] in arr[:-1]:
# # print(arr.count(arr[-1]) - 1)
# # arr.sort(reverse=True)
# # print(arr)
#
# # print(chr(33))
# # print(chr(8364))
#
# # a = 122
# # b = 97
# # if a > b:
# #     a, b = b, a
# # for i in range(a, b + 1):
# #     print(chr(i), end=" ")
#
# # print('apple' < 'banana')
# # print('apple' > 'Apple')
# # print(ord('a'))
# # print(ord("A"))
# #
# # print(9 > 5)
# # print(ord("9"))
# # print(ord("5"))
#
# # arr = ['black', 'blue', 'yellow']
# # arr.sort()
# # print(arr)
#
# # from random import randint
# #
# #
# # def random_password():
# #     rand_len = randint(6, 16)
# #     res = ""
# #
# #     for i in range(rand_len):
# #         rand_char = chr(randint(33, 126))
# #         res += rand_char
# #
# #     return res
# #
# #
# # print("Ваш случайный пароль:", random_password())
#
#
# # print(dir(str))
#
# # s = "hello, WORLD! I am learning Python."
# # print(s.capitalize())  # Hello, world! i am learning python.
# # print(s.lower())  # hello, world! i am learning python.
# # print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# # print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
#
# # print(s.count("h", 1, -4))
# #
# # print(s.find("e"))  # ищет в строке заданную подстроку (возвращает "-1" - если подстрока не найдена)
# # print(s.rfind("e"))
# #
# # print(s.index("e"))  # ищет в строке заданную подстроку (ValueError - если подстрока не найдена)
# # print(s.rindex("e"))
#
# # s = 'Hello world'
# # s = s[s.find(' ') + 1:] + ' ' + s[:s.find(' ')]
# # print(s)
#
# # s = 'ab12c59p7dq'
# # d = list(filter(lambda x: '0' <= x <= '9', s))
# # print(d)
#
# # q = [i for i in s if i in '0123456789']
# # print(q)
#
# # s = 'ab12c59p7dq'
# # digits = []
# # for ch in s:
# #     if '0123456789'.find(ch) != -1:
# #         digits.append(int(ch))
# # print(digits)
#
# # s = 'ab12c59p7dq'
# # digits = []
# # # j = [ord(x) for x in list(s)]
# # # print(j)
# # for i in s:
# #     if 48 <= ord(i) <= 57:
# #         digits.append(i)
# # print(digits)
#
# # print('abc123'.isalnum())  # состоит ли строка из букв и цифр
# # print('abc123!'.isalnum())
# #
# # print('ABCcbf'.isalpha())  # состоит ли строка из букв (любой регистр)
# # print('ABCcbf@'.isalpha())
# #
# # print('123'.isdigit())  # состоит ли строка из цифр
# # print('123#a'.isdigit())
#
# # print('py'.center(11, "-"))
# # print('py'.center(2))
# # print("     py".lstrip())
# # print("py     ".rstrip())
# # print("      py     ".strip())
#
# # print('https://www.python.org'.lstrip('/:pths'))
# # print(";py.$$$".rstrip(";$."))
# # print('https://www.python.orgw'.strip('/:pthsorg.w'))
# # print('https://www.python.orgw'.lstrip('/:pths').rstrip('org.w'))
#
# # print(s.startswith("I am", 14))
# # print(s.endswith("on."))
#
#
# # str1 = "Я изучая Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# # print(str1.replace("Nython", "Python", 2))
#
#
# # st = r"Замените в этой строке все появления буквы 'О', кроме первого и последнего вхождения."
# # ch = 'о'
# # a = st[:st.find(ch) + 1]
# # print(a)
# # b = st[st.find(ch) + 1:st.rfind(ch)]
# # print(b)
# # c = st[st.rfind(ch):]
# # print(c)
# # print(a + b.replace(ch, 'О') + c)
# # print(st.replace("о", "О"))
#
# # print(str1[:str1.find('о') + 1] + str1[str1.find('о') + 1: str1.rfind('о')].replace('о', 'О')  + str1[str1.rfind('о'):])
#
# # s = "-"
# # seq = ("a", "b", "c")
# # print(s.join(seq))
# #
# # print("..".join(['1', '99']))
# # print(":".join("Hello"))
#
# # print("Строка разделенная пробелами".split())
# # print("www.python.org.ru".split(".", 2))
# # print("www.python.org.ru".rsplit(".", 2))
#
# # a = input("-> ").split()
# # a = list(map(int, a))
# # print(a)
#
# # a = input('ФИО: ').split()
# # print(a)
# # print(f'{a[0]} {a[1][0]}. {a[2][0]}.')
#
# # Регулярные выражения
#
# import re
#
# # print(dir(re))
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = 'Я ищу'
# # print(re.findall(reg, s))  # возвращает список, содержащий все совпадения
# # print(re.search(reg, s))  # возвращает первый найденный элемент по шаблону
# # # print(re.search(reg, s).span())
# # # print(re.search(reg, s).start())
# # # print(re.search(reg, s).end())
# # # print(re.search(reg, s).group())
# # print(re.match(reg, s))  # возвращает первый найденный элемент по шаблону с начала строки
# #
# # reg = r'\.'
# # print(re.split(reg, s)[:-1])  # возвращает список, в котором строка разбита по шаблону
# # print(re.sub(reg, "!", s, 1))  # поиск и замена
#
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта. [98_75] Hello"
# # reg = r'[А-яЁё.\[\]-]'
# # reg = r'.[^2]'
# # print(re.findall(reg, s))
# # print(ord("Ё"))
# # print(ord("ё"))
#
# # s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:58. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# # rg = r'[0-2][0-9]:[0-5][0-9]'
# # print(re.findall(rg, s1))
#
# # reg = r'20*'
# # print(re.findall(reg, s))
#
# # d = "Цифры: 7, +17, -42, 0012, 0.3"
# # print(re.findall(r'[+-]?[\d.]+', d))
# # print(re.findall(r'[+-]?\d+\.?\d*', d))
#
#
# # d = "05-03-1987 # Дата рождения"
# #
# # print("Дата рождения:", re.sub(r"#.*", "", d))
# #
# # # Дата рождения: 05.03.1987
# # print('Дата рождения:', re.sub('-', '.', re.sub(r'\s#.*', '', d)))  # re.sub('-', '.', '05-03-1987')
#
# # d = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # # reg = r'\w+\s*=\s*\w+\s*[\w.]+'
# # reg = r'\w+\s*=[^;]+'
# # print(re.findall(reg, d))
#
# # s1 = "12 сентября 2023 года 235682"
# # reg = r'\d{0,4}'
# # # print(re.findall(reg, s1))
# #
# # t = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# # print(re.findall(r'\+?7\d{10}', t))
#
#
# # # reg = r'^\w+\s\w+'
# # reg = r'\w+$'
# # # print(re.findall(reg, s))
#
# # s = "Hello, Привет^"
# # reg = r'[A-zА-я]'
# # print(re.findall(reg, s))
# # print(ord("Я"))
# # print(ord("а"))
#
# # print(re.findall(r'\w+', '12 + й'))
# # print(re.findall(r'\w+', '12 + й', re.A))
#
# # text = 'hello world'
# # print(re.findall(r'\w\+', text, re.DEBUG))
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 200000 - счёта."
# # reg = 'я'
# # print(re.findall(reg, s, re.IGNORECASE))
#
# # text = """
# # one
# # two
# # """
#
# # print(re.findall(r'one.\w+', text))
# # print(re.findall(r'one.\w+', text, re.DOTALL))
# # print(re.findall(r'^ two', text, flags=re.MULTILINE))
#
# # print(re.findall("""
# # [a-z.-]+   # part 1
# # @          # @
# # [a-z.-]+   # part 2
# # """, "test@mail.ru", re.VERBOSE))
#
# # text = """Python,
# # python,
# # PYTHON"""
# # reg = "(?im)^python"
# # print(re.findall(reg, text))
#
# # def valid_name(name):
# #     return re.findall("^[a-z0-9_-]{3,}$", name, re.I)
# #
# #
# # print(valid_name("Python_master"))
# # print(valid_name("Python_master"))
#
#
# # text = "<body>Пример жадного соответствия регулярных выражений</body>"
# # print(re.findall('<.*?>', text))
# #
# # # *, +, ?, {,} - greedy - жадные квантификаторы
# # # *?, +?, ??, {m,n}?, {,n}?, {m,}? - lazy - ленивые квантификаторы
# #
# # s1 = "12 сентября 2023 года 235682"
# # # reg = r'\d{2,4}?'
# # reg = r'\d{2}'
# # print(re.findall(reg, s1))
#
# # s = "<p>Изображение <img alt='картинка' src ='bg.jpg'> - фон страницы</p>"
# # # reg = '<img.*?>'
# # reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# # print(re.findall(reg, s))
#
# # s = 'Ольга и Виталий'
# # reg = "Петр|Ольга|Виталий"
# # print(re.findall(reg, s))
#
# # s = 'int = 4, float = 4.0, double = 8.0f'
# # # reg = r"(?:int|double)\s*=\s*\d+[.\w]*"
# # reg = r"(?:int|double)\s*=\s*(\d+[.\w]*)"
# # print(re.findall(reg, s))
# # print(re.search(reg, s))
#
# # () - сохраняющие скобки
# # (?:) - несохраняющие скобки
#
# # s = '127.0.0.1'
# # s = '192.168.255.255'
# # # reg = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# # reg = r'(?:\d{1,3}\.){3}\d{1,3}'
# # print(re.findall(reg, s))
# # print(re.search(reg, s).group())
#
# # s = "Word2016, PS6, AI5, 88"
# # reg = r'([a-z]+)(\d+)'
# # print(re.findall(reg, s, re.IGNORECASE))
#
# # s = "5 + 7*2 - 4"
# # reg = r'\s*([+*-])\s*'
# # print(re.split(reg, s))
#
# # s = input('Введите дату в формате dd-mm-YYYY: ')
# # print(s)
# # reg = r'(0[1-9]|[12]\d|3[01])-(0[1-9]|1[0-2])-(1[89][0-9][0-9]|20\d{2})'
# # print(re.findall(reg, s))
#
# # s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# # reg = r'([0-9]+)\s(\D+)'
# # print(re.findall(reg, s))
# # print(re.search(reg, s).group())
# # m = re.search(reg, s)
# # print(m[0])
# # print(m[1])
# # print(m[2])
#
#
# # text = """
# # Самара
# # Москва
# # Тверь
# # Уфа
# # Казань
# # """
# # count = 0
# #
# #
# # def repl_find(m):
# #     global count
# #     count += 1
# #     return f"<option value='{count}'>{m.group(1)}</option>\n"
# #
# #
# # print(re.sub(r"\s*(\w+)\s*", repl_find, text))
#
#
# # s = "<p>Изображение <img alt='картинка' src =\"bg.jpg\"> - фон страницы</p>"
# # # reg = r'<img\s+[^>]*src\s*=\s*([\'"])(.+)\1>'
# # reg = r'<img\s+[^>]*(src)\s*=\s*(?P<q>[\'"])(.+)(?P=q)>'
# # print(re.findall(reg, s))
#
#
# # (?P<name>...)  (?P=name)
#
# # s = "Самолет прилетает 10/23/2022. Будем рады вас видеть после 10/24/2022."  # 24.10.2022
# # reg = r"(\d{2})/(\d{2})/(\d{4})"
# # print(re.sub(reg, r'\2.\1.\3', s))
#
#
# # s = "yandex.com and yandex.ru"  # http://yandex.com  and http://yandex.ru
# # reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# # print(re.sub(reg, r'http://\1', s))
#
#
# # Рекурсия
#
# # def elevator(n):
# #     if n == 0:
# #         print("Вы в подвале")
# #         return
# #     # print("=>", n)
# #     elevator(n - 1)
# #     print(n, end=" ")
# #
# #
# # n1 = int(input("На каком Вы этаже: "))
# # elevator(n1)
#
# # def sum_list(lst):
# #     res = 0
# #     for i in lst:
# #         res += i
# #     return res
# #
# #
# # print(sum_list([1, 3, 5, 7, 9]))  # 25
#
# # def sum_list(lst):  # [9]
# #     if len(lst) == 1:
# #         print(lst, "=> lst[0]:", lst[0])
# #         return lst[0]  # 9 +
# #     else:
# #         print(lst, "=> lst[0]:", lst[0])
# #         return lst[0] + sum_list(lst[1:])  # 1 3 5 7
# #
# #
# # print(sum_list([1, 3, 5, 7, 9]))
#
# # def to_str(n, base):  # 15
# #     convert = "0123456789ABCDEF"
# #     if n < base:
# #         return convert[n]  # convert[15] = 'F'
# #     else:
# #         return to_str(n // base, base) + convert[n % base]  # convert[14] = 'E'
# #
# #
# # print(to_str(254, 16))
#
# # names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# # print(names[1][1][0])
# # print(isinstance(names[1][1][0], list))
# # print(names)
#
#
# # def count_items(item_list):
# #     count = 0
# #     for item in item_list:
# #         if isinstance(item, list):
# #             count += count_items(item)
# #         else:
# #             count += 1
# #     return count
# #
# #
# # print(count_items(names))
# #
# # names = ["Adam", ["Bob", ["Chet", "Cat", "aaa"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # count = 0
# # for i in names:
# #     if isinstance(i, list):
# #         for j in i:
# #             if isinstance(j, list):
# #                 # for k in j:
# #                 #     count += 1
# #                 count += len(j)
# #             else:
# #                 count += 1
# #     else:
# #         count += 1
# # print(count)
#
# # def union(s):  # ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# #     if not s:  # len(s) == 0  s == []
# #         return s
# #     if isinstance(s[0], list):
# #         return union(s[0] + union(s[1:]))  # 'Bob' + Chet'
# #     return s[:1] + union(s[1:])  # ['Adam']
# #
# #
# # print(union(names))
#
#
# # def remove(text):  #
# #     if not text:
# #         return ""
# #     if text[0] == "\t" or text[0] == " ":
# #         return remove(text[1:])
# #     else:
# #         return text[0] + remove(text[1:])  # HelloWorld! + ""
# #
# #
# # print(remove(" Hello\tWorld! "))
#
#
# # Линейный (последовательный) поиск
# from random import randint
# import time
#
# # def seq_search(s, item):
# #     found = False  # True
# #     pos = 0  # 2
# #     while pos < len(s) and not found:
# #         if s[pos] == item:
# #             found = True
# #         else:
# #             pos += 1
# #     return found
# #
# #
# # # lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# # lst = [randint(1, 99) for i in range(100000)]
# # start = time.monotonic()
# # # print(lst)
# # # print(seq_search(lst, 32))
# # print(seq_search(lst, 0))
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
#
# # def seq_search(s, item):
# #     found = False  #
# #     pos = 0  # 3
# #     stop = False  # True
# #     while pos < len(s) and not found and not stop:
# #         if s[pos] == item:
# #             found = True
# #         else:
# #             if s[pos] > item:  # 8 > 3
# #                 stop = True
# #             else:
# #                 pos += 1
# #     return found
# #
# #
# # lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# # lst = [randint(1, 99) for i in range(100000)]
# # lst.sort()
# # start = time.monotonic()
# # print(lst)
# # # print(seq_search(lst, 32))
# # print(seq_search(lst, 3))
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
#
# # Бинарный поиск
#
# # def binary_search(s, item):
# #     first = 0
# #     last = len(s) - 1  # 3
# #     found = False
# #
# #     while first <= last and not found:
# #         midpoint = (first + last) // 2  # 4  # 1
# #         if s[midpoint] == item:
# #             found = True
# #         else:
# #             if item < s[midpoint]:  # 1 < 13
# #                 last = midpoint - 1  # 3
# #             else:
# #                 first = midpoint + 1
# #
# #     return found
# #
# #
# # lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# # print(binary_search(lst, 17))
# # print(binary_search(lst, 3))
#
# # def bubble(array):
# #     for i in range(len(array) - 1):
# #         for j in range(len(array) - i - 1):
# #             if array[j] > array[j + 1]:
# #                 array[j], array[j + 1] = array[j + 1], array[j]
# #
# #
# # lst = [randint(1, 99) for i in range(10000)]
# # start = time.monotonic()
# # bubble(lst)
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
# # def merge_sort(a):
# #     n = len(a)
# #     if n < 2:
# #         return a
# #
# #     left = merge_sort(a[:n // 2])
# #     right = merge_sort(a[n // 2: n])
# #
# #     i = j = 0
# #     res = []
# #
# #     while i < len(left) or j < len(right):
# #         if not i < len(left):
# #             res.append(right[j])
# #             j += 1
# #         elif not j < len(right):
# #             res.append(left[i])
# #             i += 1
# #         elif left[i] < right[j]:
# #             res.append(left[i])
# #             i += 1
# #         else:
# #             res.append(right[j])
# #             j += 1
# #     return res
# #
# #
# # array = [randint(1, 99) for i in range(10000)]
# # start = time.monotonic()
# # array = merge_sort(array)
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
# # Сортировка Шелла
# #
# # def shell_sort(s):  # [10, 21, 9, 14, 67, 44, 26, 87]
# #     gap = len(a)  # 1
# #
# #     while gap > 0:
# #         for val in range(gap, len(s)):  # range(2, 8)  val = 2
# #             cur_val = s[val]  # s[3] = 14
# #             pos = val  # 3
# #
# #             while pos >= gap and s[pos - gap] > cur_val:  # 3 >= 2 and s[1] > 14
# #                 s[pos] = s[pos - gap]
# #                 pos -= gap
# #                 s[pos] = cur_val
# #
# #         gap //= 2  # 1
# #     return s
# #
# #
# # # a = [10, 21, 9, 14, 67, 44, 26, 87]
# # a = [randint(1, 99) for i in range(10000)]
# # start = time.monotonic()
# # # print(a)
# # shell_sort(a)
# # # print(a)
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
#
# # Быстрая сортировка
#
# # def quick_sort(a):
# #     if len(a) > 1:
# #         x = a[(len(a) - 1) // 2]  # a[(7 - 1) // 2] = 3  = a[3] = 4
# #
# #         low = [i for i in a if i < x]  # [-3, -8]
# #         eq = [i for i in a if i == x]  # [4]
# #         hi = [i for i in a if i > x]  # [9, 5, 7, 8]
# #         a = quick_sort(low) + eq + quick_sort(hi)
# #
# #     return a
# #
# #
# # # lst = [9, 5, -3, 4, 7, 8, -8]
# # lst = [randint(1, 99) for i in range(1000000)]
# # start = time.monotonic()
# # # print(lst)
# # # lst = quick_sort(lst)
# # # print(lst)
# # lst.sort()
# # res = time.monotonic() - start
# # print(round(res, 3), 'sec')
#
#
# # Файлы
#
# # f = open(r'D:\Python214\214\text.txt')  # mode='r'
# # print(*f)
# # print(f)
# # print(f.mode)
# # print(f.name)
# # print(f.encoding)
# # f.close()
# # print(f.closed)
#
#
# # f = open('text.txt')
# # print(f.read(3))
# # print(f.read())
# # f.close()
#
#
# # f = open('test.txt')
# # # print(f.readline())
# # # print(f.readline(8))
# # # print(f.readline())
# # # print(f.readline())
# # print(f.readlines(16))
# # print(f.readlines())
# # f.close()
#
# # i = 0
# # f = open('test.txt')
# # for line in f:
# #     # print(line)
# #     i += 1
# # f.close()
# # print(i)
# #
# # f = open('test.txt')
# # # print(len(f.readlines()))
# # # print(len([*f]))
# # print([*f])
# # f.close()
#
# # f = open('test1.txt', 'w')
# # f.write('Hello\nWorld!\n')
# # f.close()
# #
# # f = open('test1.txt', 'a')
# # f.write('New text.')
# # f.close()
#
# # f = open('xyz.txt', 'a')
# # lines = ['\nThis is line 1', '\nThis is line 2']
# # f.writelines(lines)
# # f.close()
#
#
# # f = open('xyz.txt', 'w')
# # lst = [str(i ** 5) for i in range(1, 20)]
# # print(lst)
# # for index in lst:
# #     f.write(index + "\t")
# # f.close()
#
# # my_file = open("text1.txt", 'w')
# # my_file.write("Заменить строку в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# # my_file.close()
# #
# # my_file = open("text1.txt", 'r')
# # read_file = my_file.readlines()
# # print(read_file)
# # read_file[1] = "Hello World!\n"
# # print(read_file)
# # my_file.close()
# #
# # my_file = open("text1.txt", 'w')
# # my_file.writelines(read_file)
# # my_file.close()
#
# # my_file = open('text2.txt', 'w')
# # my_file.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;')
# # my_file.close()
# #
# # my_file = open('text2.txt', 'r')
# # lst = my_file.readlines()
# # my_file.close()
# #
# # print(lst)
# # num = int(input('Номер строки для удаления: '))
# # lst.pop(num - 1)  # 2 - 1  = 1
# # print(lst)
# #
# # my_file = open('text2.txt', 'w')
# # my_file.write(''.join([*lst]))
# # my_file.close()
#
# # f = open('text.txt', 'r')
# # print(f.read(3))
# # print(f.tell())
# # print(f.seek(1))
# # print(f.read())
# # print(f.tell())
# # f.close()
#
# # f = open('text.txt', 'a+')
# # print(f.mode)
# # f.mode = 'w+'
# # print(f.mode)
# # print(f.tell())
# # print(f.read())
# # print(f.seek(0))
# # print(f.read())
# # f.close()
#
# # with open('text.txt', 'w+') as f:
# #     print(f.write('12345\n67890'))
# #
# # with open('text.txt', 'r') as f:
# #     for line in f:
# #         print(line[:3])
#
#
# # file_name = 'res.txt'
# # lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
# # print(list(map(str, lst)))
# #
# # with open(file_name, 'w+') as my_file:
# #     my_file.write('\t'.join(map(str, lst)))
#
#
# # with open(file_name, 'r+') as my_file:
# #     new_lst = my_file.read().split('\t')  # ['4.5',	'2.8', '3.9', '1.0', '0.3',	'4.33', '7.77']
# #
# # print(new_lst)
# # print(len(new_lst))
# # print(list(map(float, new_lst)))
# # print(f'Sum = {sum(map(float, new_lst))}')
#
#
# # def longest_world(file):
# #     with open(file, 'r') as text:
# #         w = text.read().split()
# #         max_length = len(max(w, key=len))
# #         print(w)
# #         print(max_length)
# #         res = [word for word in w if len(word) == max_length]
# #         if len(res) == 1:
# #             return res[0]
# #         return res
# #
# #
# # print(longest_world('test.txt'))
#
# # text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
# #
# # with open('one.txt', 'w') as f:
# #     f.write(text)
#
# # read_file = 'one.txt'
# # write_file = 'two.txt'
# #
# # with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
# #     for line in fr:
# #         line = line.replace("Строка", "Линия - ")
# #         fw.write(line)
#
# # Модуль OS или OS.PATH
#
# # import os
# # import os.path
#
#
# # print(os.getcwd())  # текущая директория
#
# # print(os.listdir())  # список директорий и файлов по указанному пути
# # print(os.listdir(".."))
#
# # os.mkdir("folder")  # создать папку
#
# # os.makedirs("nested1/nested12/nested13/3/4")  # создает не только конечную директорию, но и промежуточные папки
#
# # os.remove('text.txt')  # удаление файла
#
# # os.rmdir("folder")  # удаление пустой папки
#
# # os.rename('nested1', 'test')  # переименовывает папки и файлы
# # os.rename('two.txt', 'test/test1.txt')
# # os.renames('text3.txt', 'text/test2.txt')  # переименовывает папки и файлы, создавая промежуточные директории
#
# # for root, dirs, files in os.walk('test', topdown=True):
# #     print("Root:", root)
# #     print("Sub_dirs:", dirs)
# #     print("Files:", files)
#
#
# # def remove_empty_dirs(root_tree):
# #     print(f"Удаление пустых директорий в ветви {root_tree}")
# #     print("-" * 50)
# #     for root, dirs, files in os.walk(root_tree):
# #         if not os.listdir(root):
# #             os.rmdir(root)
# #             print(f"Директория {root} удалена.")
# #     print("-" * 50)
# #
# #
# # remove_empty_dirs('test')
#
#
# # print(os.path.split(r'D:\Python214\214\test\nested12\nested13\text1.txt'))  # разбивает путь на кортеж (head, tail)
# #
# # print(os.path.dirname(r'D:\Python214\214\test\nested12\nested13\text1.txt'))
# # print(os.path.basename(r'D:\Python214\214\test\nested12\nested13\text1.txt'))
#
# # print(os.path.join('test', r'D:\Python214', 'nested12', 'text1.txt'))  # соединяет один или несколько компонентов пути
# # с учетом особенностей OS
# # /Python214/nested12/text1.txt
# # D:\Python214\nested12\text1.txt
#
# # print(os.path.exists(r'D:\Python214\214\test\nested12\nested13\text1.txt'))  # возвращает True, если указанный путь
# # существует
#
# # import time
# #
# # path = r'D:\Python214\214\venv\Scripts\python.exe'
# # print(os.path.getsize(path) // 1024)
# # print(os.path.getmtime(path))  # последнее изменение файла
# # print(os.path.getctime(path))  # создание файла
# # print(os.path.getatime(path))  # последней доступ файла
# #
# # t = time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(os.path.getctime(path)))
# # print(t)
#
# # read1_file = 'one.txt'
# # read2_file = 'two.txt'
# # write_file = 'three.txt'
# #
# # with open(read1_file, 'r') as fr, open(read2_file, 'r') as fw, open(write_file, 'w') as f:
# #     l1 = fr.readlines()
# #     l2 = fw.readlines()
# #     print(l1 + l2)
# #
# #     f.writelines(l1 + l2)
#     # for line in fr:
#     #     line = line.replace("Строка", "Линия - ")
#     #     fw.write(line)
#
# import os

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# files_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in files_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, td):
#     print(f'Обход {root} {"сверху вниз" if td else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=td):
#         print(root)
#         print(dirs)
#         print(fl)
#     print("-" * 50)
#
#
# print_tree("Work", False)
# print_tree("Work", True)
# import time
#
# file_path = r'Work\F2\F21\f212.txt'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f'{name} ({dirs}) - время последнего доступа к файлу: '
#           f'{time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime))}')
# else:
#     print(f"Файл {file_path} не существует!")

# print(os.path.isfile(r"D:\Python214\214\test\nested12\nested13\text1.txt"))
# print(os.path.isdir(r"D:\Python214\214\test\nested12\nested13"))


# dir_name = 'test'
#
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# p1 = Point()
# print(p1.x)
# print(type(p1))
# print(dir(Point))
# print(Point.__doc__)


# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# Point.x = 100
# p1.x = 20
# # p1.y = 30
# print(p1.x, p1.y)
#
# p2 = Point()
# print(p2.x, p2.y)
#
# print(p1.__dict__)
# print(p2.__dict__)
# print(Point.__dict__)

# print(id(Point))  # 100
# print(id(p1))  # 20
# print(id(p2))  # 100


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coord(5, 10)
# # Point.set_coord(p1)
#
# p2 = Point()
# # p2.x = 100
# # p2.y = 200
# p2.set_coord(100, 200)


# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = '00-00-00'
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first, birthday, phone, country, city, address):
#         self.name = first
#         self.birthday = birthday
#         self.country = country
#         self.phone = phone
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # устанавливаем новое имя
#         self.name = name
#
#     def get_name(self):  # получаем имя
#         return self.name
#
#     def set_birthday(self, val):
#         self.birthday = val
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_country(self):
#         return self.country
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self):
#         return self.city
#
#     def set_address(self, address):
#         self.address = address
#
#     def get_address(self):
#         return self.address
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
#
# h1.set_name("Оля")
# print(h1.get_name())
# h1.set_birthday("26.03.1989")
# print(h1.get_birthday())
# h1.set_country("Германия")
# print(h1.get_country())
# h1.set_phone("11-22-33")
# print(h1.get_phone())
# h1.set_city("Гессен")
# print(h1.get_city())
# h1.set_address("Липпенштрассе, 5")
# print(h1.get_address())


# class Person:
#     skill = 10
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def print_info(self):
#         print("Данные сотрудника:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print("Квалификация сотрудника:", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print("Экземпляр класса создан!")
#
#     def __del__(self):
#         print("Экземпляр класса удален!")
#
#
# p1 = Point(5, 10)
# print(p1.x, p1.y)
# # del p1
# p1 = 5
# print(type(p1))
# print(p1.__dict__)


# class Point:
#     count = 0  # 3
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p2 = Point(15, 20)
# p3 = Point(20, 40)
# print(p1.count)  # 3
# print(Point.count)  # 3
# print(p2.count)  # 3
# print(p3.count)  # 3


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация робота: {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print(f"Работающих роботов осталось {Robot.k}")
#
#     def say_hi(self):
#         print(f"Приветствую! Меня зовут: {self.name}")
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# droid3 = Robot("TP-4PO")
# droid3.say_hi()
# print(f"Численность роботов: {Robot.k}")
#
# print("\nЗдесь роботы могут проделать какую-то работу.\n\n"
#       "Роботы закончили свою работу. Давайте их выключим.")
#
# del droid3
# del droid1
# del droid2
# print(f"Численность роботов: {Robot.k}")


# class Point:
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата X должны быть числом")
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата Y должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.get_coord())
# # # p1.set_coord(12, 30.8)
# # p1.set_x(15)
# # p1.set_y(23)
# # print(p1.get_x(), p1.get_y())
# # print(p1.get_coord())
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # # p1.y = "abc"
# # # print(p1.x, p1.y)
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 20
# print(p1.__dict__)
#
# p2 = Point(3, 7)
# print(p2.__dict__)
import geometry

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = self.__width = 0
#         if Rectangle.__check_value(length) and Rectangle.__check_value(width):
#             self.__length = length
#             self.__width = width
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_width(self, width):
#         if Rectangle.__check_value(width):
#             self.__width = width
#
#     def set_length(self, length):
#         if Rectangle.__check_value(length):
#             self.__length = length
#
#     def get_width(self):
#         return self.__width
#
#     def get_length(self):
#         return self.__length
#
#     def get_area(self):
#         return self.__width * self.__length
#
#     def get_perimeter(self):
#         return 2 * (self.__length + self.__width)
#
#     def get_hypotenuse(self):
#         return round(geometry.sqrt(self.__length ** 2 + self.__width ** 2), 2)
#
#     def get_draw(self):
#         print(("*" * self.__width + "\n") * self.__length)
#
#
# a = Rectangle(4, 12)
# a.set_width(9)
# a.set_length(3)
# print("Длина прямоугольника:", a.get_length())
# print("Ширина прямоугольника:", a.get_width())
# print("Площадь прямоугольника:", a.get_area())
# print("Периметр прямоугольника:", a.get_perimeter())
# print("Гипотенуза прямоугольника:", a.get_hypotenuse())
# a.get_draw()


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#     count = 0
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(Point.count)
# print(p1.__dict__)

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):
#         self.__x = x
#
#     def __get_x(self):
#         return self.__x
#
#     x = property(__get_x, __set_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# # p1.__set_x(15)
# # print(p1.__get_x())
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 25
# print(p1.x)
# del p1.x
# print(p1.__dict__)

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Килограммы задаются числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight1 = KgToPounds(22)
# print(weight1.kg, "кг => ", end="")
# print(weight1.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")


# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, n):
#         self.__name = n
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# del p1.old
# print(p1.__dict__)

# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     # @staticmethod
#     def get_count():
#         return Point.__count
#
#     get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# import geometry
#
#
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         Area.count += 1
#         p = (a + b + c) / 2
#         return geometry.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print('Площадь треугольника по формуле Герона:', Area.triangle_area(3, 4, 5))
# print('Площадь треугольника по формуле Герона:', Area.triangle_area(3, 4, 5))
# print('Площадь треугольника по формуле Герона:', Area.triangle_area(3, 4, 5))
# print('Площадь треугольника по формуле Герона:', Area.triangle_area(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Area.triangle_area2(6, 7))
# print('Площадь квадрата:', Area.square_area(7))
# print('Площадь прямоугольника:', Area.rect_area(2, 6))
# print(Area.get_count())


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split("."))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count(".") == 2:
#             day, month, year = map(int, date_as_string.split("."))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.day}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '40.01.2021',
#     '31.12.2022'
# ]
# for string_date in dates:
#     if Date.is_date_valid(string_date):
#         date = Date.from_string(string_date)
#         string_to_db = date.string_to_db()
#         print(string_to_db)
#     else:
#         print(f"Неправильная дата или формат строки с датой")

# string_date = '23.10.2022'
# date = Date(23, 10, 2022)

# date = Date.from_string('23.10.2022')  # Date(23, 10, 2022)
# print(date.string_to_db())
# date2 = Date.from_string('14.12.2022')
# print(date2.string_to_db())

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print("-" * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# acc.set_usd_rate(2)
# acc.convert_to_usd()
# acc.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError("Неверный формат ФИО")
#         # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = "".join(re.findall("[А-яё-]", fio))  # ВолковИгорьНиколаевич
#         for s in f:
#             # print(s.strip(letters))
#             if len(s.strip(letters)) != 0:
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 120 лет")
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError("Вес должен быть вещественным числом от 20 кг и выше")
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#         for p in s:
#             if not p.isdigit():
#                 raise TypeError("Серия и номер паспорта должны быть числами")
#
#     @property
#     def info(self):
#         return self.__fio, self.__old, self.__password, self.__weight
#
#     @info.setter
#     def info(self, *args):
#         # print(args[0][0])
#         self.verify_fio(args[0][0])
#         self.verify_old(args[0][1])
#         self.verify_weight(args[0][3])
#         self.verify_ps(args[0][2])
#
#         self.__fio = args[0][0]
#         self.__old = args[0][1]
#         self.__password = args[0][2]
#         self.__weight = args[0][3]
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, w):
#         self.verify_weight(w)
#         self.__weight = w
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData("Волков Игорь Николаевич", 21, "1234 567890", 80.8)
# # p1.fio = "Соболев Игорь Николаевич"
# p1.old = 26
# p1.password = "9876 543210"
# p1.weight = 90.4
# p1.info = "Соболев Игорь Николаевич", 35, "7834 567890", 98.8
# print(*p1.info)
# print(p1.__dict__)


# Наследование

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#         print("Инициализатор класса Prop")
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#         print("Переопределенный инициализатор Line")
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}")


# class Rect(Prop):
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")


# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()

# print(line._width)
# print(line.__dict__)
# rect = Rect(Point(30, 40), Point(70, 90))
# rect.draw_rect()


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#
#     def area(self):
#         print(f"Площадь {self.color} прямоугольника:", end=" ")
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, "green")
# print(rect.area())


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#
# class Rect(Prop):
#     def draw_rect(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3, 40), Point(100, 200))
# line.draw_line()
#
# rect = Rect(Point(1, 2), Point(10, 20))
# rect.set_coord(Point(30.8, 40), Point(100.8, 200))
# rect.draw_rect()


# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольника:\nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Фон:", self.fon)
#
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         self.border = border
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print("Рамка:", self.border)
#
#
# shape1 = RectFon(400, 200, "yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()

# class Vector(list):
#     def __str__(self):
#         return " ".join(map(str, self))  # " ".join(['1', '2', '3'])
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))


# Перегрузка методов
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#             else:
#                 print("Координата должна быть целым числом")
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#             else:
#                 print("Координаты должны быть целыми числами")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(3, 40), Point(100, 200))
# line.draw_line()
# line.set_coord(Point(-10, -20))
# line.draw_line()
# Перегрузка методов


# Абстрактные методы
# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_digit(self):
#         if isinstance(self.__x, (int, float)) and isinstance(self.__y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.__x, int) and isinstance(self.__y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coord(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     # def draw(self):
#     #     print(f"Рисование эллипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     ...
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовать шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#     count = 0
#
#
# # q = Chess()
# q = Queen()
# q.draw()
# q.move()
# from geometry import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area()")
#
#
# class SqTable(Table):
#     def __init__(self, width=None, length=None, radius=None):
#         print("Прямоугольный стол")
#         super().__init__(width, length, radius)
#
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# t = SqTable(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t2 = SqTable(20)
# print(t2.__dict__)
# print(t2.calc_area())
#
# t1 = RoundTable(radius=20)
# print(t1.__dict__)
# print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     @abstractmethod
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         return self.value * Dollar.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         return self.value * Euro.rate_to_rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# for elem in d:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')
#
#
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# for elem in e:
#     elem.print_value()
#     print(f'= {elem.convert_to_rub():.2f} RUB')


# Интерфейсы

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild")
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print('Я метод внешнего класса')
#
#     def outer_obj_method(self):
#         print("outer_obj_method")
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я метод вложенного класса', MyOuter.age, self.obj.name)  #
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("внешний")
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()


# class Color:
#     def __init__(self):
#         self.name = "Green"
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print("Name:", self.name, self.lg.code)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light Green'
#             self.code = '024avc'
#
#         def display(self):
#             print("Name:", self.name)
#             print("Code:", self.code)
#
#
# outer = Color()
# outer.show()
# g = outer.lg
# g.display()
# class Intern:
#     def __init__(self):
#         self.name = "Intern"
#
#     def display(self):
#         print('Name', self.name)
#
#
# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name', self.name, self.intern.name)
#
#     class Head:
#         def __init__(self):
#             self.name = "Head"
#
#         def display(self):
#             print('Name', self.name)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d1.display()
# d2 = outer.head
# d2.display()


# class Out:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("Out")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("Inner")
#
#         class InnerClass:
#             def show(self):
#                 print("InnerClass")
#
#
# outer = Out()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#
# comp = Computer()
# print(comp.name)
# my_os = comp.os
# my_cpu = comp.cpu
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())


# class Base:
#     # def __init__(self):
#         # self.db = self.Inner()
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner Of Base Class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In SubClass")
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print("Inner Of SubClass")
#
#
# a = SubClass()
# a.display()
# # b = a.db
# b = SubClass.Inner()
# b.display1()
# b.display2()


# Множественное наследование

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is barking")
#
#
# beast = Dog("Buddy")
# beast.bark()
# beast.sleep()
# beast.play()

# class AA:
#     def __init__(self):
#         print("Инициализатор АA")
#
#
# class A:
#     def __init__(self):
#         print("Инициализатор А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор B")
#
#
# class C(AA):
#     def __init__(self):
#         print("Инициализатор C")
#
#
# class D(B, C):
#     def __init__(self):
#         B.__init__(self)
#         C.__init__(self)
#         print("Инициализатор D")
#
#
# d = D()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#
# class Style:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Style")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, color, width):
#         print("Инициализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         # Style.__init__(self, color, width)
#         super().__init__(color, width)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color, width):
#     #     Style.__init__(self, color, width)
#     #     Pos.__init__(self, sp, ep)
#
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
# print(Line.mro())


# Миксины (примеси)

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename="logfile.txt"):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="log.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет напечатана и сохранена в файл")


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.weight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_log(self):
#         print(f"{self.id}: товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_log()
#
# n1 = NoteBook("HP", 1.5, 35000)
# n1.save_log()


# Перегрузка операторов

# Число секунд в одном дне: 24 * 60 * 60 = 86400

# class Clock:
#     DAY = 86400
#
#     def __init__(self, sec):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.get_form(h)}:{Clock.get_form(m)}:{Clock.get_form(s)}"
#
#     @staticmethod
#     def get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#         # if self.sec == other.sec:
#         #     return True
#         # return False
#
#     def __getitem__(self, item):
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if item == "hour":
#             return (self.sec // 3600) % 24
#         elif item == "min":
#             return (self.sec // 60) % 60
#         elif item == "sec":
#             return self.sec % 60
#
#         return "Неверный ключ"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#
#         if not isinstance(value, int):
#             raise ValueError("Значение должно быть целым числом")
#
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#
#         if key == "hour":
#             self.sec = s + 60 * m + value * 3600
#         elif key == "min":
#             self.sec = s + 60 * value + h * 3600
#         elif key == "sec":
#             self.sec = value + 60 * m + h * 3600
#
#
# c1 = Clock(8000)
# print(c1.get_format_time())
# print(c1["hour"], c1["min"], c1["sec"])
# c1["hour"] = 9
# c1["min"] = 61
# c1["sec"] = 30
# print(c1["hour"], c1["min"], c1["sec"])
# print(c1.get_format_time())

# c1 = Clock(100)
# c2 = Clock(200)
# c4 = Clock(300)
# if c1 == c2:
#     print("Время равно")
# else:
#     print("Время разное")

# c3 = c1 + c2 + c4  # c3 = Clock(100 + 200)
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c4.get_format_time())
# print(c3.get_format_time())
# c2 += c1
# print(c2.get_format_time())

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#             # return "Неверный индекс"
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # off = 10 + 1 - 5  = 6
#             self.marks.extend([None] * off)  # self.marks.extend([None, None, None, None, None, None])
#
#         self.marks[key] = value
#
#     def __delitem__(self, key):
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         # del self.marks[key]
#         self.marks[key] = None
#
#
# s1 = Student("Сергей", [5, 5, 3, 4, 5])   # [5, 5, 3, 4, 5, None, None, None, None, None, 4]
# print(s1[13] + 2)

# s1[10] = 4
# print(s1.marks)
# del s1[2]
# print(s1.marks)
# print(s1.marks[2])
# print([None] * 6)


# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f"{self.__class__}: {self.name}"
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)


# class Point:
#     def __init__(self, *args):
#         self.coord = args
#
#     def __len__(self):
#         return len(self.coord)
#
#
# p = Point(5, 7, 3)
# print(len(p))

# from random import choice, randint
#
#
# class Cat:
#     def __init__(self, name, age, pol):
#         self.name = name
#         self.age = age
#         self.pol = pol
#
#     def __str__(self):
#         if self.pol == "M":
#             return f"{self.name} is good boy!!!"
#         if self.pol == "F":
#             return f"{self.name} is good girl!!!"
#         else:
#             return f"{self.name} is good Kitty!!!"
#
#     def __repr__(self):
#         return f"Cat(name='{self.name}', age={self.age}, pol='{self.pol}')"
#
#     def __add__(self, other):
#         if self.pol != other.pol:
#             return [Cat("No name", 0, choice(["M", "F"])) for _ in range(randint(1, 5))]  # 0 до 5
#         else:
#             raise TypeError("Types are not supported!")
#
#
# cat1 = Cat("Tom", 4, "M")
# cat2 = Cat("Else", 5, "F")
# print(cat1)
# print(cat2)
# a = cat1 + cat2
# print(a)
# print(a[0])
# print(len(a))


# Полиморфизм

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())
# if isinstance(g, Rectangle):
#     print(g.get_per_rect())
# else:
#     print(g.get_per_sq())

# print(r1.get_per_rect(), r2.get_per_rect())
# print(s1.get_per_sq(), s2.get_per_sq())

# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + a  # 10 + 35 = 45
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(str(self.value) + str(a))  # len("1035") = 4
#
#
# t1 = Number(10)
# t2 = Text(10)
#
# print(t1.total(35))
# print(t2.total(35))

# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
# for i in group:
#     i.info()


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я кот. Меня зовут {self.name}, Мой возраст {self.age}."
#
#     def make_sound(self):
#         return f"{self.name} мяукает."
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         return f"Я собака. Меня зовут {self.name}, Мой возраст {self.age}."
#
#     def make_sound(self):
#         return f"{self.name} гавкает."
#
#
# cat = Cat("Пушок", 2.5)
# dog = Dog("Мухтар", 4)
# for i in [cat, dog]:
#     print(i.info())
#     print(i.make_sound())

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'\n{self.last_name} {self.first_name} {self.age}', end=" ")
#
#
# class Student(Human):
#     def __init__(self, last_name, first_name, age, speciality, group, rating):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#
#
# class Teacher(Human):
#     def __init__(self, last_name, first_name, age, speciality, experience):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         super().info()
#         print(f"{self.speciality} {self.experience}", end=" ")
#
#
# class Graduate(Student):
#     def __init__(self, last_name, first_name, age, speciality, group, rating, topic):
#         super().__init__(last_name, first_name, age, speciality, group, rating)
#         self.topic = topic
#
#     def info(self):
#         super().info()
#         print(f"{self.topic}", end=" ")
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5),
#     Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110),
#     Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5),
#     Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()


# __slots__

# import geometry
#
#
# class Point:
#     __slots__ = ('x', 'y', '__z')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.z = geometry.sqrt(x * x + y * y)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         self.__z = value
#
#
# p1 = Point(5, 8)
# print(p1.z)
# p1.z = 10
# print(p1.z)
# print(p1.__dict__)


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 8)
# p2 = Point2D(5, 8)
# # print(p2.__dict__)
# print("p1 =", p1.__sizeof__())
# print("p2 =", p2.__sizeof__() + p2.__dict__.__sizeof__())


# class Point:
#     __slots__ = ('x', 'y')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'
#
#
# p3 = Point3D(10, 20)
# p3.z = 30
# print(p3.x, p3.y, p3.z)
# print(p3.__dict__)

# Функторы

# class Counter:
#     def __init__(self):
#         self.__count = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__count += 1
#         print(self.__count)
#
#
# c1 = Counter()
# c1()
# c1()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c1()


# def string_strip(chars):  # "?:!.; "
#     def wrap(string):  # " !Hello world?; "
#         if not isinstance(string, str) or not isinstance(chars, str):
#             raise ValueError("Аргументы должны быть строкой")
#         return string.strip(chars)
#     return wrap
#
#
# s1 = string_strip("?:!.; ")
# print(s1(" !Hello world?; "))
#
#
# class StringStrip:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):  # string
#         if not isinstance(args[0], str) or not isinstance(self.__chars, str):
#             raise ValueError("Аргументы должны быть строкой")
#
#         return args[0].strip(self.__chars)
#
#
# s2 = StringStrip("?:!.; ")
# print(s2(" !Hello world?; "))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print("Перед вызовом функции")
#         self.func()
#         print("После вызова функции")
#
#
# @MyDecorator
# def func():
#     print("Hello")
#
#
# func()


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return f"Перед вызовом функции\n{self.func(a, b)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# print(func(2, 5))


# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         return self.func(a, b) ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))


# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return f"Перед вызовом функции\n{self.func(*args, **kwargs)}\nПосле вызова функции"
#
#
# @MyDecorator
# def func(a, b):
#     return a * b
#
#
# @MyDecorator
# def func1(a, b, c):
#     return a + b + c
#
#
# @MyDecorator
# def func2():
#     return "World"
#
#
# print(func(2, 5))
# print(func1(2, c=5, b=2))
# print(func2())


# class MyDecorator:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print("Перед вызовом функции")
#             print(self.arg)
#             func(a, b)
#             print("После вызова функции")
#
#         return wrap
#
#
# @MyDecorator("text2")
# def func1(a, b):
#     print(a, b)
#
#
# func1(2, 5)


# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             return func(a, b) ** self.arg
#
#         return wrap
#
#
# @Power(3)
# def func1(a, b):
#     return a * b
#
#
# print(func1(2, 2))

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# def decorator(cls):
#     class Wrap(cls):
#         def method2(self, value):
#             return value * 2
#
#     return Wrap
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("ActualClass")
#
#     def method1(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.method1(4))
# print(obj.method2(4))


# Дескриптор

# class String:
#     def __init__(self, value):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         if not isinstance(value, str):
#             raise TypeError("Ожидается строковое строковое значение")
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#     # @property
#     # def name(self):
#     #     return self.__name
#     #
#     # @name.setter
#     # def name(self, value):
#     #     self.__name = value
#     #
#     # @property
#     # def surname(self):
#     #     return self.__surname
#     #
#     # @surname.setter
#     # def surname(self, value):
#     #     self.__surname = value
#
#
# p = Person("Ivan", "Petrov")
# p.surname.set("Oleg")
# print(p.surname.get())


# DRY (Don`t Repeat Youself) - не повторяйся

# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Ivan", "Petrov")
# p.surname = 'Oleg'
# print(p.name)
# print(p.surname)

# class NonNegative:
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Значение должно быть положительным')
#         instance.__dict__[self.name] = value
#
#
# class Order:
#     price = NonNegative()
#     quantity = NonNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# apple.price = -15
# print(apple.total())


# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = '_' + name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         instance.__dict__[self.name] = value
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.__dict__)


# class Integer:
#     @classmethod
#     def verify_coord(cls, coord):
#         if not isinstance(coord, int):
#             raise TypeError(f"Координата {coord} должна быть целым числом")
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         # return instance.__dict__[self.name]
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         self.verify_coord(value)
#         # instance.__dict__[self.name] = value
#         setattr(instance, self.name, value)
#
#
# class Point3D:
#     x = Integer()
#     y = Integer()
#     z = Integer()
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#
# p1 = Point3D(1, 2, 3)
# print(p1.y)
# p1.z = 100
# print(p1.__dict__)


# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimetr(self):
#         return self.a + self.b + self.c
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# t1 = Triangle(1, 2, 3)
# t2 = Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())
# if isinstance(g, Rectangle):
#     print(g.get_per_rect())
# else:
#     print(g.get_per_sq())
#
# print(r1.get_per_rect(), r2.get_per_rect())
# print(s1.get_per_sq(), s2.get_per_sq())

#
# import start
# from start import run
#
# run()

# from car import electrocar
#
#
# def main():
#     car1 = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
#     car1.show_car()
#     car1.description_battery()
#
#
# if __name__ == '__main__':
#     main()


# Упаковка данных (Сериализация)
# Распаковка данных (Десериализация)

# marshal (.рус)
# pickle
# json

# import pickle


# file_name = "basket.txt"
#
# shop_list = {
#     "фрукты": ["яблоки", "манго"],
#     "Овощи": 'морковь',
#     "Бюджет": 1000
# }
#
# with open(file_name, "wb") as fh:
#     pickle.dump(shop_list, fh)
#
# with open(file_name, 'rb') as fh:
#     shop_list2 = pickle.load(fh)
#
# print(shop_list2)

# class Test:
#     num = 35
#     st = "Привет"
#     lst = [1, 2, 3]
#     d = {"first": 'a', "second":
#         2}
#     tpl = (22, 36)
#
#     def __str__(self):
#         return f"Число: {Test.num}\nСтрока: {Test.st}\nСписок: {Test.lst}\nСловарь: {Test.d}\nКортеж: {Test.tpl}"
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(my_obj)
#
# new_obj = pickle.loads(my_obj)
# print(new_obj)

# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         del attr['c']
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ = state
#         self.c = lambda x: x * x
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)

# import json

# data = {
#     'name': 'Oleg',
#     'age': 35,
#     20: None,
#     'hobbies': ('running', "singing"),
#     'children': [
#         {
#             'firstName': 'Alice',
#             'age': 6
#         }
#     ]
# }

# with open("date.json", 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open("date.json", 'r') as fw:
#     data1 = json.load(fw)
#
# print(data1)

# st = json.dumps(data)
# print(st)
#
# data2=json.loads(st)
# print(data2)

# x = {
#     'name': 'Виктор'
# }
# y = {
#     'name': 'Виктор'
# }
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))

# import json
# from random import choice
#
#
# def get_person():
#     name = ""
#     tel = ""
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)
#     with open('person.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person())


# import json
# from random import choice
#
#
# def get_person():
#     name = ""
#     tel = ""
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {
#         'name': name,
#         'tel': tel
#     }
#     return person, tel
#
#
# def write_json(person_dict, num):
#     try:
#         data = json.load(open('person1.json'))
#     except FileNotFoundError:
#         data = {}
#
#     data[num] = person_dict
#     with open('person1.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(get_person()[0], get_person()[1])
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         #     a = ''
#         #     for i in self.marks:
#         #         a += str(i) + ", "
#         #     return f"Студент:{self.marks}: {a[:-2]}"
#         a = ', '.join(map(str, self.marks))
#         return f"Студент:{self.name}: {a}"
#
#     def add_marks(self, mark):
#         self.marks.append(mark)
#
#     def delete_mark(self, index):
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):
#         self.marks[index] = new_mark
#
#     def averange_mark(self):
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     def dump_to_json(self, filename):
#         data = {'name': self.name, 'marks': self.marks}
#         with open(filename, 'w') as f:
#             json.dump(data, f)
#
#     def load_from_file(self, filename):
#         with
#
#
# class Group:
#     def __init__(self, students, group):
#         self.students = students
#         self.group = group
#
#     def __str__(self):
#         a = '\n'.join(map(str, self.students))
#         return f"Группа: {self.group}\n{a}\n"
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, index):
#         self.students.pop(index)
#
#     @staticmethod
#     def change_group(group1, group2, index):
#         return group2.add_student(group1.remove_student(index))
#
#
# st1 = Student('Bodnya', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 2, 5])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# print(st1)
# st1.add_marks(4)
# print(st1)
# st1.delete_mark(3)
# print(st1)
# st1.edit_mark(2, 5)
# print(st1)
# print(st1.averange_mark())
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)


# pip install requests

# import requests
# import json
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# # print(type(todos))
# # print(todos)
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# # print(todos_by_user)
#
# top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
# # print(top_user)
#
# max_complete = top_user[0][1]
# print(max_complete)
#
# users = []
# for user, num_complete in top_user:
#     if num_complete < max_complete:
#         break
#     users.append(str(user))
#
# max_users = ' and '.join(users)
# print(max_users)
# s = 's' if len(users) > 1 else ''
# print(f'User{s} {max_users} completed {max_complete} TODOs')
#
#
# def keep(todo):
#     is_complete = todo['completed']
#     has_max_count = str(todo['userId']) in users
#     return is_complete and has_max_count
#
#
# with open('filtered_data.json', 'w') as f:
#     filtered_todos = list(filter(keep, todos))
#     print(filtered_todos)
#     json.dump(filtered_todos, f, indent=2)

# import json
#
# data = {}
#
#
# class CountryCapital:
#     # def __init__(self, country, capital):
#     #     self.country = country
#     #     self.capital = capital
#     #     data[self.country] = self.capital
#     #
#     # def __str__(self):
#     #     return f"{self.country}: {self.capital}"
#
#     @staticmethod
#     def load(filename):
#         try:
#             data1 = json.load(open(filename))
#         except FileNotFoundError:
#             data1 = {}
#         finally:
#             return data1
#
#     @staticmethod
#     # @load_data
#     def add_country(file_name):
#         new_country = input('Введите название страны: ')
#         new_capital = input('Введите название столицы: ')
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#         data1 = CountryCapital.load(file_name)
#
#         data1[new_country] = new_capital
#
#         with open(file_name, 'w') as f:
#             json.dump(data1, f, indent=2)
#
#     @staticmethod
#     # @load_data
#     def delete_country(file_name):
#         del_country = input('Введите название страны: ')
#         # try:
#         #     data1 = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data1 = {}
#         data1 = CountryCapital.load(file_name)
#
#         if del_country in data1:
#             del data1[del_country]
#
#             with open(file_name, 'w') as f:
#                 json.dump(data1, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     # @load_data
#     def search_data(file_name):
#         # try:
#         #     data1 = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data1 = {}
#         country = input('Введите название страны: ')
#         data1 = CountryCapital.load(file_name)
#
#         if country in data1:
#             print(f"Страна {country} столица {data1[country]} есть в словаре")
#         else:
#             print(f"Страны {country} нет в словаре")
#
#     @staticmethod
#     # @load_data
#     def edit_data(file_name):
#         country = input('Введите страну для корректировки: ')
#         new_capital = input('Введите новое название столицы: ')
#
#         # try:
#         #     data1 = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data1 = {}
#         data1 = CountryCapital.load(file_name)
#
#         if country in data1:
#             data1[country] = new_capital
#             with open(file_name, 'w') as f:
#                 json.dump(data1, f, indent=2)
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name) as f:
#             print(json.load(f))
#
#
# file = 'list_capital.json'
# index = ""
# while True:
#     index = input('Выбор действия:\n1 - добавление данных\n'
#                   '2 - удаление данных\n3 - поиск данных\n'
#                   '4 - редактирование данных\n5 - просмотр данных\n'
#                   '6 - завершение работы\nВвод: ')
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


# csv (Comma Separated Values - переменные, разделенные запятыми)

import csv
#
# with open("data.csv") as f:
#     file_reader = csv.reader(f, delimiter=";")
#     count = 0
#     for row in file_reader:
#         print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки")


# with open("data.csv") as f:
#     fn = ['Имя', 'Профессия', 'Год рождения']
#     file_reader = csv.DictReader(f, delimiter=";", fieldnames=fn)
#     count = 0
#     for row in file_reader:
#         # print(row)
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']}. Родился в {'Год рождения'} году.")
#         count += 1
#     print(f"Всего в файле {count} строки")


# with open('student.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])


# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
#
# with open('sw_data.csv', 'w') as f:
#     writer = csv.writer(f, delimiter=";", lineterminator="\r")
#     # for row in data:
#     #     writer.writerow(row)
#     writer.writerows(data)


# with open('sw_data1.csv', 'w') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": 6})
#     writer.writerow({"Имя": "Маша", "Возраст": 15})
#     writer.writerow({"Имя": "Вова", "Возраст": 14})

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict_data.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=list(data[0].keys()))
#     # ['hostname', 'location', 'model', 'vendor']
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# Парсинг данных с сайтов

# from bs4 import BeautifulSoup

# f = open('index.html').read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", class_="name")
# row = soup.find_all("div", {"class": "name"})
# row = soup.find_all("div", class_="row")[1].find(class_="name").text
# row = soup.find_all("div", {"data-set": "salary"})
# row = soup.find("div", string="Alena").parent
# row = soup.find("div", string="Alena").find_parent(class_="row")
# row = soup.find("div", id="whois3").find_next_sibling()
# row = soup.find("div", id="whois3").find_previous_sibling()
# print(row)

# def get_copywriter(tag):
#     whois = tag.find("div", class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     cw = get_copywriter(i)
#     if cw:
#         copywriter.append(cw)
# print(copywriter)

# import re
# from bs4 import BeautifulSoup
#
#
# def get_salary(s):
#     pattern = r"\d+"
#     # res = re.findall(pattern, s)[0]
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# import requests


# res = requests.get("https://ru.wordpress.org/")
# # print(res.headers['content-type'])
# # print(res.content)
# print(res.text)


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     print(p1)
#
#
# def main():
#     url = "https://ru.wordpress.org/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refined(s):
#     return re.sub(r"\D+", "", s)
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\r")
#         write.writerow((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("section", class_="plugin-section")[1]
#     plugins = p1.find_all("article")
#     for plugin in plugins:
#         name = plugin.find("h3").text
#         # url = plugin.find("h3").find("a").get("href")
#         url = plugin.find("h3").find("a")["href"]
#         rating = plugin.find('span', class_="rating-count").find("a").text
#         r = refined(rating)
#         data = {'name': name, 'url': url, 'rating': r}
#         write_csv(data)
#
#
# def main():
#     url = "https://ru.wordpress.org/plugins/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# import requests
# from bs4 import BeautifulSoup
#
#
# def get_html(url):
#     res = requests.get(url)
#     return res.text
#
#
# def refine_cy(s):
#     return s.split()[-1]
#
#
# def write_csv(data):
#     with open('plugins1.csv', 'a', encoding='utf-8-sig') as f:
#         write = csv.writer(f, delimiter=";", lineterminator="\r")
#         write.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     elements = soup.find_all("article", class_="plugin-card")
#     for el in elements:
#         try:
#             name = el.find('h3').text
#         except ValueError:
#             name = ''
#
#         try:
#             url = el.find('h3').find('a').get("href")
#         except ValueError:
#             url = ''
#
#         try:
#             snippet = el.find('div', class_="entry-excerpt").text.strip()
#         except ValueError:
#             snippet = ''
#
#         try:
#             active = el.find('span', class_="active-installs").text.strip()
#         except ValueError:
#             active = ''
#
#         try:
#             c = el.find('span', class_="tested-with").text.strip()
#             cy = refine_cy(c)
#         except ValueError:
#             cy = ''
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(13, 26):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"
#         get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# from parse import Parser
#
#
# def main():
#     pars = Parser('https://www.ixbt.com/live/index/news/', 'news.txt')
#     pars.run()
#
#
# if __name__ == '__main__':
#     main()


# import socket
# from view import index, blog
#
# URLS = {
#     '/': index,
#     '/blog': blog
# }
#
#
# def parse_request(request):
#     parsed = request.split()
#     method = parsed[0]
#     url = parsed[1]
#     return method, url
#
#
# def generate_headers(method, url):
#     if method != 'GET':
#         return 'HTTP/1.1 405 Method Not Allowed!\n\n', 405
#     if url not in URLS:
#         return 'HTTP/1.1 404 Page Not Found!\n\n', 404
#     return URLS[url]()
#
#
# def generate_content(code, url):
#     if code == 404:
#         return '<h1>404</h1><h3>Not Found</h3>'
#     if code == 405:
#         return '<h1>405</h1><h3>Method Not Allowed</h3>'
#     return URLS[url]
#
#
# def generate_response(request):
#     method, url = parse_request(request)
#     headers, code = generate_headers(method, url)
#     body = generate_content(code, url)
#     return (headers + body).encode()
#
#
# def run():
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind(('127.0.0.1', 5000))
#     server_socket.listen()
#
#     while True:
#         client_socket, addr = server_socket.accept()
#         request = client_socket.recv(1024)
#
#         print(f"Клиент: {addr} => \n{request.decode('utf-8')}\n")
#
#         response = generate_response(request.decode())
#         client_socket.sendall(response)
#         client_socket.close()
#
#
# if __name__ == "__main__":
#     run()


import sqlite3

# con = sqlite3.connect("profile.db")
# cur = con.cursor()
#
# con.close()


with sqlite3.connect('profile.db') as con:
    cur = con.cursor()
    # cur.execute("""CREATE TABLE IF NOT EXISTS users(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT,
    # summa REAL,
    # date TEXT
    # )""")
    cur.execute("DROP TABLE users")