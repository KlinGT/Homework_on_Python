# Задача 5: Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fib(n):
    a, b = 0, 1
    result = []
    for i in range(n):
        a, b = b, a + b
        result.append(a)
    return result


n = int(input('\nВведите кол-во чисел Фибоначчи числом: '))

positive_list = fib(n)
reversed_list = list(reversed(fib(n)))
negative_list = [i * -1 for i in reversed_list]
result_list = negative_list + positive_list

print(f'для n = {n} список будет выглядеть так:\n{result_list}')