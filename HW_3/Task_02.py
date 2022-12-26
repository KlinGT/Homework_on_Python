# Задача 2: Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

list_size = int(input('\nВведите кол-во значений списка числом: '))
random_list = []
multiplied_list = []

for i in range(list_size):
    random_list.append(randint(0, 10))

for i in range(len(random_list)):
    while i < len(random_list)/2 < list_size:
        list_size = list_size - 1
        a = random_list[i] * random_list[list_size]
        multiplied_list.append(a)
        i += 1

print(f'{random_list} => {multiplied_list}')