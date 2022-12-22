# Задача 3: Реализуйте алгоритм перемешивания списка.
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int.
import random


def creating_list():
    values = range(1, 10)
    origin_list = list(values)
    print(f'\nИсходный список: {origin_list}')
    return origin_list


def mixed_list(final_list):
    for i in range(len(final_list) - 1, 0, -1):
        j = random.randint(0, i + 1)
        final_list[i], final_list[j] = final_list[j], final_list[i]
    return final_list


final_list = creating_list()
print(f'Перемешанный список: {mixed_list(final_list)}')
