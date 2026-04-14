"""
Составить генератор (yield), который преобразует все буквенные символы в заглавные.
"""
def upper_generator(text):
    for char in text:
        if char.isalpha():
            yield char.upper()
        else:
            yield char

text = input("Введите текст: ")
result = ' '.join(upper_generator(text))
print("Результат:", result)
