'''
1. В последовательности на n целых элементов найти среднее арифметическое элементов первой трети.
'''
import random

def first_third_generator(a):
    n = len(a) // 3
    for i in range(n):
        yield a[i]

def first_third(a):
    count = len(a) // 3
    total = sum([a[i] for i in range(count)])
    return total / count if count > 0 else 0

n = int(input("Введите количество элементов: "))

nums = [random.randint(1, 10) for _ in range(n)]
print("Список:", nums)

print("Среднее первой трети:", first_third(nums))