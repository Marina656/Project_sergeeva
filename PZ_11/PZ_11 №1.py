'''
1. В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
'''
import random
from functools import reduce

def average_first_third(seq):
    fts = len(seq) // 3
    ft = seq[:fts]

    total = reduce(lambda x, y: x + y, ft, 0)

    return total / len(ft) if ft else 0
n = int(input("Введите количество элементов: "))

nums = [random.randint(1, 100) for matematika in range(n)]
print("Список:", nums)

print(f"Среднее первой трети:", average_first_third(nums))
