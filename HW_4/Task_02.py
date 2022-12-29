# Задача 2: Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('poly_01.txt', 'w') as file:
    file.write('2*x^2 + 5*x^5')
with open('poly_02.txt', 'w') as file:
    file.write('23*x^4 + 9*x^6')

with open('poly_01.txt','r') as file:
    poly_01 = file.readline()
    list_of_poly_01 = poly_01.split()

with open('poly_02.txt','r') as file:
    poly_02 = file.readline()
    list_of_poly_02 = poly_02.split()

print(f'{list_of_poly_01} + {list_of_poly_02}')
summa_poly = list_of_poly_01 + list_of_poly_02

with open('summa_polys.txt', 'w') as file:
    file.write(f'{list_of_poly_01} + {list_of_poly_02}')