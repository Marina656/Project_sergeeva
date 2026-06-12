'''
Дана строка, состоящая из русских слов, набранных заглавными буквами и
разделенных пробелами (одним или несколькими). Преобразовать каждое слово в
строке, заменив в нем все предыдущие вхождения его последней буквы на символ
«.» (точка). Например, слово «МИНИМУМ» надо преобразовать в «.ИНИ.УМ».
Количество пробелов между словами не изменять.
'''
def process_words(text):
    parts = text.split(' ')
    result_parts = []

    for part in parts:
        if part == '':
            result_parts.append('')
        else:
            last_char = part[-1]
            new_part = part[:-1].replace(last_char, '.') + last_char

            result_parts.append(new_part)
    return ' '.join(result_parts)

print("\nТест задания 2:")
test_str1 = "МИНИМУМ"
print(f"'{test_str1}' -> '{process_words(test_str1)}'")

test_str2 = "АБВГДЕ   ЖЖЖ  З"
print(f"'{test_str2}' -> '{process_words(test_str2)}'")