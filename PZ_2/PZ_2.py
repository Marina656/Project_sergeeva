# Дано трехзначное число. В нём зачеркнули первую справа цифру и приписали её слева. Вывевсти полученное число.
from multiprocessing.managers import Value

try:
    num = int(input("Введите трёхзначное число:"))
    last_digit = num % 10
    remaining_digits = num // 10
    new_num = last_digit * 100 + remaining_digits
    print(f'Получившиееся число: {new_num}')
except ValueError:
    print('Введите число!')