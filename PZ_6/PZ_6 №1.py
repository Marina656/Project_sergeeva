"""
Дан список размера N и целые числа K и L (1<K<L<N). Найти сумму элементов списка с номерами от К до L включительно
"""
try:
    import random

    N = random.randint(10, 20)
    K = random.randint(2, N - 3)
    L = random.randint(K + 1, N - 1)

    print(f"N = {N}, K = {K}, L = {L}")

    if 1 < K < L < N:
        sum_n = 0
        for i in range(K, L + 1):
            sum_n += i

        print(f"Сумма элементов с номерами от {K} до {L}: {sum_n}")
        print(f"Элементы для суммирования: числа от {K} до {L}")
    else:
        print("Ошибка: условие 1 < K < L < N не выполняется")
except ValueError:
    print("Ошибка! Введите корректные числа.")
