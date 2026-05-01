'''
Перенести в новую матрицу Matr1, элементы которые не находятся в первых и последних строках и столбцах
матрицы Mat2 произвольного номера
'''
import random
n = int(input("Введите размер матрицы:"))
Matr2 = [[random.randint(1, 100) for matematika in range(n)] for matematika in range(n)]

print("Исходная матрица Matr2:")
print(*Matr2, sep="\n")

Matr1 = [i[1:-1] for i in Matr2[1:-1]]

print("\nНовая матрица Matr1:")
print(*Matr1, sep="\n")
import numpy as np

Matr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16]
])
print("Исходная матрица Matr2:")
print(Matr2)
Matr1 = Matr2[1:-1, 1:-1]

print("\nНовая матрица Matr1 (без границ):")
print(Matr1)
