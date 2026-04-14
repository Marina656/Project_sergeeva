'''
В матрице найти среднее арифметическое элементов последних двух столбцов
'''
import numpy as np

Matr2 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12],
    [13,14,15,16] ])
print("Исходная матрица Matr2:")
print(Matr2)

last_two_cols = Matr2[:, -2:]

average = last_two_cols.mean()

print("\nПоследние два столбца:")
print(last_two_cols)
print("Среднее арифметическое:", average)
