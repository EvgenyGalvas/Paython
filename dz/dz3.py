# Калькулятор
# print(
#     "Выберите операцию:\n1 - \"r\" - применяет унарный минус к операнду\n2 - \"+\" - сложение\n3 - \"-\" - вычитание"
#     "\n4 - \"/\" - деление\n5 - \"*\" - умножение\n6 - \"%\" - деление по модулю (отстаток от деления)"
#     "\n7 - \"<\" - минимальное из двух чисел\n8 - \">\" - максимальное из двух чисел")
# c = int(input("Введите цифру: "))
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if c == 1:
#     if a + b > 0:
#         print(-(a + b))
#     else:
#         print(a+b)
# if c == 2:
#     print(a + b)
# elif c == 3:
#     print(a - b)
# elif c == 5:
#     print(a * b)
# elif c == 4:
#     if b != 0:
#         print(a / b)
#     else:
#         print('На ноль делить нельзя!')
# elif c == 6:
#     print(a % b)
# elif c == 7:
#     if a < b:
#         print(a)
#     elif a > b:
#         print(b)
#     else:
#         print("Числа равны")
# elif c == 8:
#     if a > b:
#         print(a)
#     elif a < b:
#         print(b)
#     else:
#         print("Числа равны")

# a = int(input("Количество символов: "))
# b = input("Тип символа: ")
# c = int(input("0 - горизонтальная\n1 - вертикальная\nориентация линии: "))
# if c == 1:
#     i = 0
#     while True:
#         print(b)
#         i += 1
#         if i == a:
#             break
# elif c == 0:
#     print(b * a)

# i = 0
# while i < 3:
#     print("+" * 16)
#     if i < 2:
#         print("-" * 16)
#     i += 1

# a, b, c = int(input()), int(input()), int(input())
# if b < a > c:
#     print("Максимальное значение: ", a)
# elif b == a > c:
#     print("Максимальное значение: ", a, " и ", b, " равны")
# elif b < a == c:
#     print("Максимальное значение: ", a, " и ", c, " равны")
# elif a < b > c:
#     print("Максимальное значение: ", b)
# elif a < b == c:
#     print("Максимальное значение: ", b, " и ", c, " равны")
# elif a < c > b:
#     print("Максимальное значение: ", c)
# else:
#     print("Все числа равны")
