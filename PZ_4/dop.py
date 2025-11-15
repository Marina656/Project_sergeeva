"""
print("Введите 4 числа:")
a = int(input("Первое число: "))
b = int(input("Второе число: "))
c = int(input("Третье число: "))
d = int(input("Четвертое число: "))

count_even = 0

if a % 2 == 0:
    count_even += 1

if b % 2 == 0:
    count_even += 1

if c % 2 == 0:
    count_even += 1

if d % 2 == 0:
    count_even += 1

print(f"Количество четных чисел: {count_even}")

"""
3.Найти и вывести на экран квадраты и кубы чисел от 2 до 5.

"""
number = 2
print("Число | Квадрат | Куб")
print("-" * 21)

while number <= 5:
    square = number * number
    cube = number * number * number
    print(f"{number:5} | {square:7} | {cube:4}")
    number += 1

"""
Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).
"""
n = int(input("Введите n (n > 1): "))

if n <= 1:
    print("Ошибка: n должно быть больше 1")
else:
    total_sum = 0
    factorial = 1
    i = 1

    while i <= n:
        factorial *= i
        total_sum += factorial
        i += 1

    print(f"S = 1! + 2! + ... + {n}! = {total_sum}")
5
"""
Ввести N чисел. Найти и вывести их среднее арифметическое
"""
try:
    n = int(input("Введите количество чисел: "))

    if n <= 0:
        print("Количество чисел должно быть положительным!")
    else:
        total = 0
        i = 0
        print(f"Введите {n} чисел:")

        while i < n:
            num = float(input(f"Число {i + 1}: "))
            total += num
            i += 1

        average = total / n
        print(f"Среднее арифметическое: {average:.2f}")

except ValueError:
    print("Ошибка: введите корректные числа!")
"""
6.Ввести N чисел. Посчитать и вывести количество чисел равных нулю
"""
n = int(input("Введите количество чисел: "))
count_zero = 0
i = 0
print(f"Введите {n} чисел:")

while i < n:
    num = float(input(f"Число {i+1}: "))
    if num == 0:
        count_zero += 1
    i += 1

print(f"Количество чисел равных нулю: {count_zero}")

"""
7.Даны два целых числа А и В (А < В). Вывести в порядке убывания все целые числа,
расположенные между А и В (включая сами числа А и В), а также количество этих
чисел (использовать оператор цикла).
"""

A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A >= B:
    print("Ошибка: A должно быть меньше B")
else:
    count = 0
    current = B

    print("Числа в порядке убывания:")
    while current >= A:
        print(current, end=" ")
        count += 1
        current -= 1

    print(f"\nКоличество чисел: {count}")


"""
8.Даны два целых числа А и В (А < В). Найти сумму всех целых чисел от А до В
включительно (использовать оператор цикла).
"""
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

if A >= B:
    print("Ошибка: A должно быть меньше B")
else:
    total = 0
    current = A

    while current <= B:
        total += current
        current += 1

    print(f"Сумма чисел от {A} до {B} включительно: {total}")

"""
9.Посчитать и вывести количество элементов арифметической прогрессии,
удовлетворяющих условию 10<ai<30.
"""
a1 = float(input("Введите первый элемент прогрессии a1: "))
d = float(input("Введите разность прогрессии d: "))
n = int(input("Введите количество элементов n: "))

count = 0
i = 0
print("Элементы прогрессии, удовлетворяющие условию 10 < ai < 30:")

while i < n:
    ai = a1 + i * d
    if 10 < ai < 30:
        print(f"a{i+1} = {ai}")
        count += 1
    i += 1

print(f"Количество элементов, удовлетворяющих условию: {count}")

"""
10.Вывести первые N (N≥3) чисел Фибоначчи и посчитать количество четных чисел.
"""

N = int(input("Введите N (N ≥ 3): "))

if N < 3:
    print("Ошибка: N должно быть не меньше 3")
else:
    fib1, fib2 = 1, 1
    even_count = 0

    print(f"Первые {N} чисел Фибоначчи:")
    print(fib1, fib2, end=" ")

    if fib1 % 2 == 0:
        even_count += 1
    if fib2 % 2 == 0:
        even_count += 1

    i = 3
    while i <= N:
        fib_next = fib1 + fib2
        print(fib_next, end=" ")

        if fib_next % 2 == 0:
            even_count += 1

        fib1, fib2 = fib2, fib_next
        i += 1

    print(f"\nКоличество четных чисел: {even_count}")

"""
   11.  Дана арифметическая прогрессия а1=1, а2=4, а3=7, а4=10, а5=13, … Составить
программу, которая каждый элемент прогрессии разделит на 2 и результат округлит
до ближайшего целого.
    """

a1 = 1
d = 3

print("Исходная прогрессия и результаты деления на 2:")
i = 0
while i < 10:
    ai = a1 + i * d
    result = ai / 2
    rounded = round(result)

    print(f"a{i + 1} = {ai} → {ai}/2 = {result} → округлено: {rounded}")
    i += 1
