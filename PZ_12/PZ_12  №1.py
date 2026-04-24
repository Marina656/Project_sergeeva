'''
В матрице найти среднее арифметическое элементов последних двух столбцов
'''
import random
n = int(input("Введите размер матрицы:"))
Matr2 = [[random.randint(1, 15) for matematika in range(n)] for matematika in range(n)]

print("Исходная матрица Matr2:")
print(*Matr2, sep='\n')

last_two_cols = [i[-2:] for i in Matr2]

flat_list = [num for i in last_two_cols for num in i]
chet = sum(flat_list)/ len(flat_list)

print("\nПоследние два столбца:")
print(*last_two_cols, sep='\n')
print("Среднее арифметическое:", che
