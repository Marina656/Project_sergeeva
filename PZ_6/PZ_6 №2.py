"""
Дан целочисленный список размера N . Найти количество различных элементов в данном списке.
"""
import random

N = random.randint(5, 15)
print(f"N = {N}")

elements1 = []

for _ in range(N):
    element = random.randint(1, 10)
    print(f"Сгенерирован элемент: {element}")

    if element not in elements1:
        elements1.append(element)

m = 0
for element in elements1:
    m += 1

print(f"Количество различных элементов: {m}")
