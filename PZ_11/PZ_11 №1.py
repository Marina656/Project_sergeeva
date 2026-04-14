'''
1. В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
'''
import random

def first_third_generator(seq):
    n = len(seq) // 3
    for i in range(n):
        yield seq[i]

def average_first_third(seq):
    total = 0
    count = 0

    for num in first_third_generator(seq):
        total += num
        count += 1

    return total / count if count > 0 else 0

n = int(input("Введите количество элементов: "))

nums = [random.randint(1, 100) for _ in range(n)]
print("Список:", nums)

print("Среднее первой трети:", average_first_third(nums))
