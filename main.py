import numpy as np
from numpy import linalg

size = int(input('Введите размерность  матрицы  от 1 до 31:'))
while (size < 1) or (size > 31):
    size = int(input('Неверное число,введите размерность матрицы от 1 до 31:'))
matrix = np.random.randint(5, size=(size, size))
rangMatrix = np.linalg.matrix_rank(matrix)
print('Матрица:\n', matrix)
print('Ранг матрицы:', rangMatrix)

t = int(input('Введите количество знаков после запятой:'))
t = 0.1**t

factorial = 1
n = 1
summa = 0
fg = 0
difference = 1

while abs(difference) > t:
    fg += summa
    summa += (-1**(n-1))*(np.linalg.det(linalg.matrix_power(matrix, 2 * n))) / factorial
    n += 1
    factorial = factorial * (2*n) * (2*n - 1)
    difference = fg-summa
    fg = 0
    print(n - 1, 'Cумма:', summa, 'разность:', difference)
print('Cумма знакопеременного ряда:', summa)
