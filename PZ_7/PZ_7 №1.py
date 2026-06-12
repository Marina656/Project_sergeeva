'''
Дана строка. Если она представляет собой запись целого числа, то вывести 1, если
вещественного (с дробной частью) — вывести 2; если строку нельзя преобразовать
в число, то вывести 0. Считать, что дробная часть вещественного числа отделяется
от его целой части десятичной точкой «.».
'''
def check_number_type(text):
    try:
        int(text)
        return 1
    except ValueError:
        try:
            float(text)
            return 2
        except ValueError:
            return 0

print("Тест задания 1:")
print(f"'123' -> {check_number_type('123')}")
print(f"'-45.67' -> {check_number_type('-45.67')}")
print(f"'abc' -> {check_number_type('abc')}")
print(f"'3.0' -> {check_number_type('3.0')}")