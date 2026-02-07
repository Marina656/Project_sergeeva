"""
Используя словарь посчитать количество уникальных слов в заданном предложении "Изучаем язык Питон"
Вывести на экран каждую пару "ключ:значение"
"""
sentence = "Изучаем язык язык Питон"
word = ""
word_count = {}
for char in sentence:
    if char != " ":
        word += char
    else:
        if word:
            word_count[word] = word_count.get(word, 0) + 1
        word = ""
if word:
    word_count[word] = word_count.get(word, 0) + 1
for key, value in word_count.items():
    print(f"{key}: {value}")
unique_count = len(word_count)
print(f"Количество уникальных слов: {unique_count}")
