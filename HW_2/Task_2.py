# Задайте список из n чисел последовательности (1 + 1/n)^n,
# выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def list_of_sequence_numbers(n):
    summ = [((1 + 1/i)**i) for i in range(1, n + 1)]
    print(f'n = {n} -> {summ}')
    return sum(summ)

n = int(input('\nВведите число для последовательности: '))
print(f'Сумма: {round(list_of_sequence_numbers(n), 2)}')