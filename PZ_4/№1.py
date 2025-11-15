'''
Дано вещественное число x и целое число N (>0). Найти значение выражения 1+x+x^2/(2!)+...+x^N/(N!)(N=12...N).
Полученное число является приближенным значением функции exp в точке Х.
'''
try:
    X = int(input("Введите число X: "))
    N = int(input("Введите целое число N (>0): "))

    summa = 0
    k = 0

    while k <= N:
        chislitel = 1
        i = 0
        while i < k:
            chislitel *= -1
            i += 1

        stepen = 2 * k + 1
        X_stepen = 1
        i = 0
        while i < stepen:
            X_stepen *= X
            i += 1

        znamenatel = 1
        i = 1
        while i <= stepen:
            znamenatel *= i
            i += 1

        chlen_ryada = chislitel * X_stepen / znamenatel
        summa += chlen_ryada
        k += 1

    print(f"Приближенное значение sin({X}) = {summa}")
except ValueError:
    print("Ошибка: Введите корректные числовые значения")
