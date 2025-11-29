"""
Составить функцию решения задачи: из заданного числа вычли сумму его цифр.
Из результата вновь вычли сумму его цифр и т.д. Через сколько таких действий получится нуль?
"""
try:
    number = int(input('Введите число:'))
    def zero(n):
        steps = 0
        current_number = n

        while current_number > 0:
            num = current_number
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num = num // 10
            current_number -= digit_sum
            steps += 1
        return steps

    result = zero(number)
    print(f"Через {result} действий получится нуль")
except ValueError:
    print('Ошибка! Введите коректные числа.')
