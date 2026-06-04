'''
из пз 2. Дано трехзначное число. В нём зачеркнули первую справа цифру и приписали её слева.
Вывевсти полученное число.
'''
from tkinter import *

root = Tk()
root.title("Преобразование числа")
root.geometry("400x300+400+200")
root.resizable(False, False)

COLOR_BG = "#F0F8FF"
COLOR_BLUE = "#0066CC"
COLOR_WHITE = "#FFFFFF"
COLOR_RED = "#DC143C"
FONT_TITLE = "Arial 16 bold"
FONT_TEXT = "Arial 12"

def transform_number():
    try:
        num_str = entry_num.get().strip()
        num = int(num_str)

        if num < 100 or num > 999:
            raise ValueError("Число должно быть трёхзначным!")

        last_digit = num % 10
        remaining_digits = num // 10
        new_num = last_digit * 100 + remaining_digits

        label_result.config(text=f"Результат: {new_num}", fg="green")
        label_error.config(text="")

    except ValueError as e:
        label_result.config(text="")
        if "invalid literal" in str(e):
            label_error.config(text="Ошибка: введите целое число!", fg=COLOR_RED)
        else:
            label_error.config(text=f"Ошибка: {e}", fg=COLOR_RED)

header_label = Label(root, text="Перестановка цифр", font=FONT_TITLE, bg=COLOR_BG, fg=COLOR_BLUE)
header_label.pack(pady=15)

frame_input = Frame(root, bg=COLOR_BG)
frame_input.pack(pady=10)

label_prompt = Label(frame_input, text="Введите трёхзначное число:", font=FONT_TEXT, bg=COLOR_BG)
label_prompt.pack(side="left", padx=10)

entry_num = Entry(frame_input, width=10, font=FONT_TEXT, bd=2, relief="solid", justify="center")
entry_num.pack(side="left", padx=10)
entry_num.bind("<Return>", lambda e: transform_number())

button_calc = Button(root, text="Преобразовать", command=transform_number, bg=COLOR_BLUE, fg=COLOR_WHITE,
                     font=FONT_TEXT, width=20, height=2)
button_calc.pack(pady=15)

frame_output = Frame(root, bg=COLOR_BG, bd=1, relief="solid")
frame_output.pack(padx=30, pady=5, fill=X)

label_result = Label(frame_output, text="", font=FONT_TEXT, bg=COLOR_WHITE, fg="green", height=2)
label_result.pack(fill=X, padx=10, pady=5)

label_error = Label(root, text="", font=FONT_TEXT, bg=COLOR_BG, fg=COLOR_RED)
label_error.pack(pady=5)

root.mainloop()