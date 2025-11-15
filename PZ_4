'''
Дано вещественное число xлое число N  (>0). Найти значение выражения 1+x+x^2/(2!)+...+x^N/(N!)(N=12...N).
Полученное число является приближенным значением функции exp  в точке Х.
'''
try:
    X = int(input("Введите число X: "))
    N = int(input("Введите целое число N (>0): "))

    summa = 0

    for k in range(N + 1):
        chislitel = 1
        for i in range(k):
            chislitel *= -1

        stepen = 2 * k + 1
        X_stepen = 1
        for i in range(stepen):
          X_stepen *= X

        znamenatel = 1
        for i in range(1, stepen + 1):
            znamenatel *= i

        chlen_ryada = chislitel * X_stepen / znamenatel
        summa += chlen_ryada

    print(f"Приближенное значение sin({X}) = {summa}")
except ValueError:
        print("Ошибка: Введите корректные числовые значения")
