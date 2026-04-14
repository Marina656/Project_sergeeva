"""
Из предложенного текстового файла (text18-19.txt) вывести на экран его содержимое, количество символов,
принадлежащих к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме
предварительно заменив символы верхнего регистра на нижний.
"""

with open('text18-19.txt', 'r', encoding='utf-8') as f:
    content = f.read()

print("\nСодержимое файла:")
print(content)

letter_count = 0
for ch in content:
    if ch.isalpha():
        letter_count += 1
print(f"Количество букв в тексте: {letter_count}")

total_chars = len(content)
print(f"Общее количество символов: {total_chars}")

lower_content = content.lower()

with open('lower_poem.txt', 'w', encoding='utf-8') as f:
    f.write(lower_content)

print(f"\nТекст в нижнем регистре сохранен в файл: lower_poem.txt ")

print("\nТекст в нижнем регистре:")
print(lower_content)
