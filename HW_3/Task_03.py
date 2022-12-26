# Задача 3: Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
from random import randint

list_size = int(input('\nВведите кол-во значений списка числом: '))
random_list = []
fraction_list = []

for i in range(list_size):
    random_list.append(round(random.uniform(1, 9), 2))

fraction_list = [round(i % 1, 2) for i in random_list if i % 1 != 0]

print(f'{random_list} => {max(fraction_list) - min(fraction_list)}')