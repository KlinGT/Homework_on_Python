# Задача 1: Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum_of_digits(number):
    while number != int(number):
        number *= 10
    summa = 0
    while number > 0:
        summa += number % 10
        number //= 10
    print(f'Сумма: -> {int(summa)}')


number = float(input("\nВведите вещественное число: "))
sum_of_digits(number)
