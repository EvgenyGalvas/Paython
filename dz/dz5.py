from random import randint

# 1 задача

# lst = [randint(-10, 20) for i in range(10)]
# print(lst)
# max_number = max(lst)  # присваиваем максимальное значение списка
# print("Max:", max_number)
# lst.remove(max(lst))  # удаляем максимальное значение из списка
# lst.insert(0, max_number)  # добовляем максимальное значение из первоночального списка в начало
# print(lst)

# 2 задача
# lst = [randint(-10, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)  # сортирует список по умолчанию-по возрастанию, revers=True-по убыванию
# print(lst)

# 3 задача
lst = [randint(-10, 20) for i in range(10)]
print(lst)
print("Min:", min(lst))  # Находим минимальный элемент списка
print("Index min:", lst.index(min(lst)))  # Индекс минимального элемента списка
del lst[:lst.index(min(lst))]  # Удаляем все элементы перед минимальным значением
print(lst)
