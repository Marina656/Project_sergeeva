'''
Перенести в новую матрицу Matr1, элементы которые не находятся в первых и последних строках и столбцах
матрицы Mat2 произвольного номера
'''
import random
Matr2 = [[random.randint(1, 100) for matematika in range(4)] for matematika in range(4)]

print("Исходная матрица Matr2:")
for i in Matr2:
    print(i)

Matr1 = [i[1:-1] for i in Matr2[1:-1]]

print("\nНовая матрица Matr1:")
for i in Matr1:
    print(i)
