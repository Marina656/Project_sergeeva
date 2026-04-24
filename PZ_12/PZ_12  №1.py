'''
В матрице найти среднее арифметическое элементов последних двух столбцов
'''
import random

Matr2 = [[random.randint(1, 100) for matematika in range(3)] for matematika in range(3)]

print("Исходная матрица Matr2:")
for row in Matr2:
    print(row)

last_two_cols = [row[-2:] for row in Matr2]

flat_list = [num for row in last_two_cols for num in row]
chet = sum(flat_list)/ len(flat_list)

print("\nПоследние два столбца:")
print(*last_two_cols, sep='\n')
print("Среднее арифметическое:", chet)
