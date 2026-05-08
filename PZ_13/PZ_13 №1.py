'''
Из исходного текстового файла (pazzl.html) выбрать все html-коды изображений.
Посчитать их количество.
'''
import re

with open('pazzl.html', 'r', encoding='utf-8') as f:
    text = f.read()

images = re.findall(r'<[Ii][Mm][Gg][^>]*>', text)

print(f"Количество изображений: {len(images)}\n")
print("Коды изображений:")
print("\n".join(images))