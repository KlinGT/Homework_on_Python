# Задача 1: Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

values = input('\nВведите числа списка через пробел: ').split()
my_list = [int(item) for item in values]

summ = 0
for i in range(1, len(my_list), 2):
    summ += my_list[i]

print(f'{my_list} -> на нечётных позициях элементы {my_list [1::2]} ответ: {summ}')