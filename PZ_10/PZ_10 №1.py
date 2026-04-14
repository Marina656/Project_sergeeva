"""
Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных
и отрицательных чисел. Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив
требуемую обработку элементов:
Исходные данные:
Количество элементов:
Сумма элементов:
Элементы до n-1 умножены на элемент n:
"""
import random
numbers = []
for i in range (10):
    n = random.randint(-5, 5)
    numbers.append(n)
with open('numbers_data.txt', 'w', encoding='utf-8') as f:
    for num in numbers:
        f.write(str(num) + ' ')

n = len(numbers)
last_element = numbers[-1]
processed_numbers = []
for i in range(n - 1):
    processed_numbers.append(numbers[i] * last_element)

with open('result1.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(str(numbers) + '\n')
    f.write(f"Количество элементов: {len(numbers)}\n")
    f.write(f"Сумма элементов: {sum(numbers)}\n")
    f.write("Элементы до n-1 умножены на элемент n:\n")
    f.write(str(processed_numbers))

with open ('result1.txt', 'r', encoding='utf-8') as file:
    results = file.read()
    print(results)
