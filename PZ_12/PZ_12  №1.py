'''
В матрице найти среднее арифметическое элементов последних двух столбцов
'''
import random

Matr2 = [[random.randint(1, 100) for matematika in range(3)] for matematika in range(3)]

print("Исходная матрица Matr2:")
for i in Matr2:
    print(i)

last_two_cols = [i[-2:] for i in Matr2]

flat_list = [num for i in last_two_cols for num in i]
chet = sum(flat_list)/ len(flat_list)

print("\nПоследние два столбца:")
print(*last_two_cols, sep='\n')
print("Среднее арифметическое:", chet)
