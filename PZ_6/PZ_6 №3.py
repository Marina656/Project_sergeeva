"""
Дан список размером N, все элементы которого, кроме последнего, упорядочены по возрастанию,сделать список упорядоченым
переместив последний элемент на элемент на новую позицию.
"""
import random
m = random.randint(5, 10)
a = []
for _ in range(m):
    a.append(random.randint(1, 100))
a.sort()
a[-1] = random.randint(1, 100)
print(f"Исходный список: {a}")
last = a[-1]
j = 0
while j < m - 1:
    if last < a[j]:
        k = m - 1
        while k > j:
            a[k] = a[k - 1]
            k -= 1
        a[j] = last
        break
    j += 1

print(f"Упорядоченный список: {a}")
