# name = "Евгений"
# print("Hello", name)
# age = 20
# print(type(age))
# print(id(age))
# age = "hello"
# print(age)
# print(type(age))

# a = b = c = 1
# print(a, b, c)
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
#
# PI=3.14
# print(PI)
# PI=2
# print(PI)
# print()

# a = "5"
# b = 2
# print(int(a) + b)

# a = 1
# b = 2
# print("a=", a)
# print("b=", b)
# a = a + b
# b = a - b
# a = a - b
# a, b = b, a
# print("a=", a)
# print("b=", b)

# print("Строка \
# символов")
# print('Строка \nсимволов')
# print('Строка \rсимволов')
# print('\tДокумент "file.text"')
# s1="Hello"
# s2="Python"
# s3=s1+" "+s2+"!\t\t"
# print(s3)
# print(s3*3)

# num = input("Введите число: ")
# step = input("Введите степень: ")
# res = int(num) ** int(step)
# print("Число:",num,"в степени:",step,"равно:",res)
#
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

# for i in "Hello", "red", "blue", "yellow", 20, 0.3:
#     print(i)

# print(range(5))

# for i in range(1,5):
#     print(i,end=" ")

# num = input('Введите целое число: ')
# try:
#     num = int(num)
#     for i in range(1, num):
#         if i % 10 == i // 10:
#             print(i, end=' ')
# except ValueError:
#     print('Вас просили число!')

# for i in range(11, 101, 11):
#     print(i, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# s = [8, 9, 6, 4, 7, 8, 2, 3]
# res = []
# for i in s:
#     if i % 2 == 0:
#         res.append(i)
#
# print(res)

# x = list('1a2b3c4c')
# print(x)
# print('a' in x)
# print('w' in x)
# # print('a' not in x)
# print('w' not in x)
#
# lst = []
# # if len(lst) == 0:
# # if not lst:
# #     print('писок пустой')
# print(bool(lst))

from random import randint


# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Первый список: ", b)
# c = a + b
# print('Третий список: ', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общии для двух списков: ", c)
#
# c = [min(a), min(b), max(a), max(b)]

# k = int(input("Размер списка: "))
# s = []

# import random
#
# n = int(input("Размер списка: "))
# s = []
# for i in range(n):
#     num = random.randrange(10)
#     if num not in s:
#         s.append(num)
# print(s)

# from random import randint
#
# a = []
# step = 0
# n1 = int(input('Введите размер первого списка'))
# while len(a) < n1:
#     i = randint(0, n1-1)
#     if i not in a:
#         a.append(i)
# print(a)

# import random
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
# print(m[2][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x,end="\t")
#     print()

# w, h = 10, 10
# matrix = [[x * y for x in range(1, w)] for y in range(1, h)]
# print(matrix)
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
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
#
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

# import math as m
# from math import sqrt, ceil, floor, pi
#
# num1 = sqrt(2)
# num2 = ceil(3.2)
# num3 = floor(3.8)
# print(num1)
# print(num2)
# print(num3)
# print(pi)

# studs = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     studs[sname] = point
#     s += point
# print(studs)
# avrg = s / n
# print(avrg)
# for i in studs:
#     if studs[i] > avrg:
#         print(i)

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['c'])
# value = d.get('f', 'Такого ключа не существует') #получитить значение по заданному ключу
# print(value)
# n=d.keys()# список ключей
# print(n)
# n=d.values() #ситсок значений
# print(n)
# n=d.items() #список кортежей ключ + значение
# print(n)
#
# for i,j in d.items():
#     print(i,"->",j)

# d = {'a': 1, 'b': 2, 'c': 3}
# d2 = d.copy()
# print("D-", d)
# print("D-", d2)
# d["d"] = 5
# d2['e'] = 7
# print("D-", d)
# print("D-", d2)

# d = {'a': 1, 'b': 2, 'c': 3}
# item = d.pop('b')  # удал элем словаря по ключу, возвращает значение ключа
# print(item)
# print(d)
# item = d.popitem() #удаляет произвольную пару ключ + значение и возвращает их
# print(item)
# print(d)

# item = d.setdefault('f') #добовляет ключ со значение по умолчанию, если ключа несуществует
# print(item)
# print(d)

# d.update({'a': 20, 'w': 10})  # обновление словоря
# print(d)
# d.update([('q', 7), ('t', 9)])
# print(d)

# x = {'a': 1, 'b': 2}
# y = {'c': 3, 'd': 4}
# # q = x.copy()
# # q.update(y)
# q = x | y
# print(q)

# a = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'thre',
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ': ', a[x][y], sep='')

# sales = {
#     "John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#     "Tom": {"N": 4832, "S": 6786, "E": 4738, "W": 3612},
#     "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#     "Fiona": {"N": 3908, "S": 3645, "E": 8821, "W": 2451}
# }
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ": ", sales[x][y], sep="")
#
# person = input('Имя: ')
# region = input('Регион: ')
# print(sales[person][region])
# new_data = int(input('Новое значение: '))
# (sales[person][region]) = new_data
# print(sales[person])

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# w = {k: v for k, v in d.items() if v <= 2}
# print(w)

# value = int(input('->'))
# lt = [7, 8, 9, 10]
# d = {k: value for k in lt}
# print(d)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# value=list(d)
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'tree', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = list(zip(a, b))
# print(d)

# one = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# two = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# for (k1, v1),(k2,v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)
# print(a)
# print(b)
#
# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})

# data = ['a', 'b', 'c', 'd']

# for i in data:
#     print(i, end=' ')
# print()
# for i in range(len(data)):
#     print(i,end=' ')
# print()
# j=0
# for i in data:
#     print(j,':',i)
#     j+=1

# for j, i in enumerate(data,100):
#     print(j, ':', i)

# n = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# for j, i in enumerate(n, 100):
#     print(j, ':', i, '->', n[i])

# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ',avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def print_scores(student, *scores):
#     print("\nStudent Name:", student, end=", scores: ")
#     for score in scores:
#         print(score, end=", ")
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)
# def to_dict(*lst):
#     print(*lst)
#     print(lst)
#     return {i: i for i in lst}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))
#
# def ch(*args):
#     pass
#
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def fun(*a):
#     return [i for i in a if i < sum(a) / len(a)]
#
#
# print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(fun(3, 6, 1, 9, 5))


# def func(*lst):
#     sum = 0
#     count = 0
#     new_lst = []
#     for i in lst:
#         sum += i
#         count += 1
#     avarange = sum / count
#     print('Ср. ариф: ', avarange)
#     for j in lst:
#         if j < avarange:
#             new_lst.append(j)
#     print(new_lst)
#
#
# func(1, 2, 3, 4, 5, 6, 7, 8, 9)

# def func(a, b,  *args):
#     return a, b, args
#
#
# print(func(2, 3))
# print(func(2, 3, 4, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name:", student, end=", scores: ")
#     a, b = None, ""
#     for score in scores:
#         a = str(score) + ", "
#         b += a
#     print(b[:-2])
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)


# def print_scores(student, *scores):
#     print("Student Name:", student, end=", scores: ")
#     count = 0
#     for score in scores:
#         count += 1
#         if count != len(scores):
#             print(score, end=", ")
#         else:
#             print(score)
#
#
# print_scores("Kate", 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33, 56)
# def reverse_num(n):  # 12 => 21
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or only_add and i % 2:
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="python"))

# def func(**data):
#     for key, value in data.items():
#         print(key, "is", value)
#     print()
#
#
# func(name="Irina", surname="Sharma", age=22, phone=1234567890)
# func(name="Igor", surname="Wood", email="igor@mail.ru", country="Russia", age=25, phone=9876543210)


# def func(**data):
#     # for key, value in data.items():
#     #     my_dict[key] = value
#     # return my_dict
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# func(k1=22, k2=31, k3=11, k4=91)
# print(my_dict)
# func(name='Bob', age=31, weight=61, eyes_color='grey')
# print(my_dict)

# def func(a, *args, b=2, **kwargs):
#     print(a, kwargs, args, b)
#
#
# func(4, 5, 6, 7, b=3, k1=22, k2=31, k3=11, k4=91)


# Области видимости (scope)

# name = "Tom"  # глобальная переменна
# surname = "sum"
#
#
# def hi():
#     global name, surname
#     name = "Sam"  # локальные переменные
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name, surname)
#
#
# hi()
# print(surname)
# bye()

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5

# x = 5
#
#
# def add_two(a):
#     # x = 2
#
#     def add_some():
#         # x = 3
#         return a + x
#
#     return add_some()
#
#
# print(add_two(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# type1 = [8, 1, 2, 4, 5, 6, 9]
# print(min(type1))
#
# a = [7, 8, 9, 5]
# print(type(a))


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")


# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print(a + b)
#
#     print("a =", a)
#     fun2(4)
#
#
# fun1()

# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30 = 55
# print(z)  # 25 + 35 = 60

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()
# print(x)

# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# # print(res)

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add = outer(5)
# print(add(10))
# print(add(20))
#
# add1 = outer(6)
# print(add1(10))
# print(outer(5)(10))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def rect_paral_sqare(a, b, c):
#     def rect_sqare(i, j):
#         return i * j
#
#     s = 2 * (rect_sqare(a, b) + rect_sqare(a, c) + rect_sqare(b, c))
#     return s
#
# print(rect_paral_sqare(2, 4, 6))
# print(rect_paral_sqare(5, 8, 2))
# print(rect_paral_sqare(1, 6, 8))


# s = 0
#
#
# def rect_paral_sqare(a, b, c):
#     def rect_sqare(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_sqare(a, b) + rect_sqare(a, c) + rect_sqare(b, c))
#
#
# rect_paral_sqare(2, 4, 6)
# print(s)
# rect_paral_sqare(5, 8, 2)
# print(s)
# rect_paral_sqare(1, 6, 8)
# print(s)

# def func(city):
#     s = 0
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }


# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print('A=', A(students))
# print('B=', B(students))
# print('C=', C(students))
# print('D=', D(students))

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func=lambda x, y: x + y
# print(func(1,2))
# print(func('a','b'))

# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#     return s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))
# s = 0
#
#
# def rect_paral_square(a, b, c):
#     def rect_square(i, j):
#         return i * j
#
#     global s
#     s = 2 * (rect_square(a, b) + rect_square(a, c) + rect_square(b, c))
#
#
# rect_paral_square(2, 4, 6)
# print(s)
# rect_paral_square(5, 8, 2)
# print(s)
# rect_paral_square(1, 6, 8)
# print(s)


# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(b, c)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# print(rect_paral_square(5, 8, 2))
# print(rect_paral_square(1, 6, 8))

# def func(city):
#     s = 0  # 3  2
#
#     def wrap():
#         nonlocal s
#         s += 1
#         print(city, s)  # 3
#
#     return wrap
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res1()

# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def classifier(lower, upper):
#     def student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return student
#
#
# A = classifier(80, 100)
# B = classifier(70, 80)
# C = classifier(50, 70)
# D = classifier(0, 50)
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print("qqq")
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# obj1()


# lambda (Анонимные функции)

# print((lambda x, y: x + y)(1, 2))
# c = (lambda x, y: x + y)('a', 'b')
# print(c)
# a = 5
# func = lambda x, y: x + y + a
# b = func(1, 2)
# print(b)
# # print(func('a', 'b'))
#
# (lambda: print("Hello"))()


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
#
# print(summ(10, 20, 30))
# print(summ(10, 20))
# print(summ(10))
# print(summ())

# func = lambda *args: args
# #
# # print(func(1, 2, 3, 4, 5, 6, 7))
# # print(func())
#
#
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: n + x
#
#
# f = inc(42)
# print(f(3))


# inc1 = (lambda n: lambda x: n + x)
#
# f3 = inc1(42)
# print(f3(3))
# print("!!!", (lambda n: lambda x: n + x)(42)(3))
#
#
# def inc2(n):
#     def wrap(x):
#         return n + x
#
#     return wrap
#
#
# f1 = inc2(42)
# print(f1(3))

# print((lambda i: lambda j: lambda k: i+j+k)(2)(4)(6))

# print((lambda i: lambda j: lambda k: i + j + k)(2)(4)(6))


# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федоров', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6}
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'])
# print(res)
#
# res = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res)

# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 3, 'c': 7}  # {'a': 3, 'c': 7, 'b': 15}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1])
# lst.sort(key=func)
# print(lst)
# print(dict(lst))

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
#
# print(a[3](12, 3))

# a = {'one': lambda x: x - 1, 'two': lambda x: x - 3, 'three': lambda x: x}
# b = [-3, 10, 0, 4]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье")
# }
#
# d[3]()


# print((lambda a, b: a if a > b else b)(12, 5))

# m = lambda a, b, c: a if a < b else b if b < c else c
# print(m(19, 28, 5))
#
# print((lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c)(9, 18, 15))


# map(func, iterable), filter(func, iterable)

# def mul(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
#
# # lst2 = list(map(mul, lst))
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)

# t = (2.88, -1.75, 100.03)
#
# # t2 = tuple(map(lambda x: int(x), t))
# t2 = tuple(map(int, t))
#
# print(t2)

# area = [3.456789, 5.784569, 4.001256, 7.987426, 1.4523689, 8.7412594]
#
# res = list(map(round, area, range(1, 7)))
#
# print(res)

# print(round(3.45612131, 3))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# gitHub

# filter(func, interable)

# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 77, 90, 88, 59, 74, 56, 23, 78]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# z = [15,37,36,26,27,35,27,20,24,3]
# res = list(filter(lambda a: 10 < a <= 20, z ))
# print(res)

# from random import randint
# lst = [randint(1, 50) for i in range(10)]
# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)

# nums = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, nums))
# print(res)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m)

# Дикораторы

# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#
#         return wrap
#
#     return decor
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# filter(func, iterable)
# t = ('abcd', 'abc', 'adefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)# z = [15, 37, 36, 26, 27, 35, 27, 20, 24, 3]
# res = list(filter(lambda a: 10 < a <= 20, z))
# print(res)# from random import randint
# ## lst = [randint(1, 40) for i in range(10)]# print(lst)
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst2)# nums = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda x: x % 15 == 0, nums))
# print(res)
# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# (1, 3, 5, 7, 9)# print(m)
# ## m1 = [x ** 2 for x in range(10) if x % 2]# print(m1)
# Декораторы# def hello():
#     return 'Hello, I am func "hello"'
#     ### def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())### super_func(hello)
# def hello():
#     return 'Hello, I am func "hello"'
#     ### test = hello# print(test())
# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#     return func_wrapper
#     ### def func_test():
#     print('Hello, I am func "func_test"')
#     ### test = my_decorator(func_test)
# test()# def my_decorator(func):
# декорирующая функция
#     def func_wrapper():
#         print('*' * 40)
#         func()
#         print('*' * 40)
#     return func_wrapper
#     ### @my_decorator
# декоратор# def func_test():
# декорируемая функция
#     print('Hello, I am func "func_test"')
#     ### func_test()# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#         ##     return wrap
#         ### def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#         ##     return wrap
#         ### @bold
# @italic# def hello():
#     return "text"
#     ### print(hello())
# def cnt(fn):
#     count = 0
#     ##     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции:", count)
#         ##     return wrap
#         ### @cnt# def hello():
#     print("Hello")
#     ### hello()
# hello()
# hello()
# hello()
# hello()
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#         ##     return wrap
#         ### @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#     ### print_full_name("Ирина", "Назарова")
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print(*args)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         fn(*args, **kwargs)
#         ##     return wrap
#         ### @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#     ### @args_decorator
# def print_full_name_1(first, second, last):
#     print("Меня зовут", first, second, last)
#     ### print_full_name("Ирина", "Назарова")
# print()
# print_full_name_1("Виктор", last="Назаров", second="Федорович")
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#             ##         return wrap#     return args_dec
#             ### @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#     ### @decor("Разность:", "-")
# def sub(a, b):#     print(a - b)
# ### summa(5, 2)# sub(5, 2)
# ## def decor(*args):
#     def args_dec(fn):
#         def wrap(x, y):
#             # print(args[0], x, args[1], y, "=", end=" ")
#             print(*args, end=" ")
#             fn(x, y)
#             ##         return wrap
#     return args_dec
#     ### @decor("Сумма:", "+")
# def summa(a, b):#     print(a + b)
# ### @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#     ### summa(5, 2)
# sub(5, 2)# def multiply(num):
#     def decor(fn):
#         def wrap(mult):
#             return num * fn(mult)
#             ##         return wrap
#             ##     return decor
#             ### @multiply(3)
# def return_num(ch):
#     return ch
#     ### print(return_num(5))
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#         ##             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных", f_args[i])
# print("Некорректный тип данных!")
#             for k in kwargs
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных", f_kwargs[k])
#                     ##             return fn(*f_args, **f_kwargs)
#                     ##         return wrap#     return wrapper
#                     ### @typed(int, int, int)# def typed_fn(x, y, z):
#     return x * y * z
#     ### @typed(str, str, str)# def typed_fn2(x, y, z):
#     return x + y + z
#     ### @typed(str, str, z=int)# def typed_fn3(x, y, z="Hello"):
#     return (x + y) * z
#     ### print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello", "World", "!"))
# print(typed_fn3("Hello", "World", z=5))
# def args_decorator(tx=None, decorator_text=""):
# def my_decorator(func):        def wrap(*args):
# print(decorator_text, end="")
# func(*args)
# return wrap
# if tx is None:
# return my_decorator
# else:
# return my_decorator(tx)
# @args_decorator(decorator_text="Hello, ")def hello_world(text):
# print(text)@args_decoratordef hello_world2(text):
# print(text)hello_world("world!")hello_world2("Hi!")

print("hello")