'''
из пз 9 задание 1.
'''
from tkinter import *

root = Tk()
root.title("Анализ сельскохозяйственных культур")
root.geometry("800x600+200+100")
root.resizable(False, False)

COLOR_BG = "#F0F8FF"
COLOR_U1 = "#FFE4B5"
COLOR_U2 = "#E0FFFF"
COLOR_U3 = "#F0FFF0"
COLOR_RESULT_BG = "#FFFFFF"
COLOR_TEXT = "#333333"
COLOR_BLUE_BTN = "#0066CC"
COLOR_WHITE_TEXT = "#FFFFFF"

uchastok1 = {"картофель", "морковь", "горох"}
uchastok2 = {"картофель", "морковь", "капуста"}
uchastok3 = {"редис", "капуста", "картофель"}
vse_kulturi = {"картофель", "лук", "морковь", "горох", "капуста", "редис"}


def calculate_sets():
    label_res1.config(text="")
    label_res2.config(text="")
    label_res3.config(text="")

    try:
        common = uchastok1 & uchastok2 & uchastok3
        union = uchastok1 | uchastok2 | uchastok3
        none_present = vse_kulturi - uchastok1 - uchastok2 - uchastok3

        text_common = ", ".join(sorted(common)) if common else "Нет общих культур"
        text_union = ", ".join(sorted(union))
        text_none = ", ".join(
            sorted(none_present)) if none_present else "Все культуры присутствуют хотя бы на одном участке"

        label_res1.config(text=f"На каждом участке: {text_common}")
        label_res2.config(text=f"Хотя бы на одном: {text_union}")
        label_res3.config(text=f"Ни на одном: {text_none}")

    except Exception as e:
        label_res1.config(text=f"Ошибка: {str(e)}", fg="red")


header_label = Label(root, text="Распределение культур по участкам",
                     font="Arial 16 bold", bg=COLOR_BG, fg=COLOR_TEXT)
header_label.pack(pady=15)

frame_uchastki = Frame(root, bg=COLOR_BG)
frame_uchastki.pack(padx=20, pady=10, fill=X)

frame_u1 = Frame(frame_uchastki, bg=COLOR_U1, bd=2, relief="groove")
frame_u1.grid(row=0, column=0, padx=10, sticky="nsew")
label_u1_title = Label(frame_u1, text="Участок 1", font="Arial 12 bold", bg=COLOR_U1)
label_u1_title.pack(pady=5)
list_u1 = ", ".join(sorted(uchastok1))
label_u1_content = Label(frame_u1, text=list_u1, font="Arial 11", bg=COLOR_U1, justify=CENTER)
label_u1_content.pack(pady=5, padx=10)

frame_u2 = Frame(frame_uchastki, bg=COLOR_U2, bd=2, relief="groove")
frame_u2.grid(row=0, column=1, padx=10, sticky="nsew")
label_u2_title = Label(frame_u2, text="Участок 2", font="Arial 12 bold", bg=COLOR_U2)
label_u2_title.pack(pady=5)
list_u2 = ", ".join(sorted(uchastok2))
label_u2_content = Label(frame_u2, text=list_u2, font="Arial 11", bg=COLOR_U2, justify=CENTER)
label_u2_content.pack(pady=5, padx=10)

frame_u3 = Frame(frame_uchastki, bg=COLOR_U3, bd=2, relief="groove")
frame_u3.grid(row=0, column=2, padx=10, sticky="nsew")
label_u3_title = Label(frame_u3, text="Участок 3", font="Arial 12 bold", bg=COLOR_U3)
label_u3_title.pack(pady=5)
list_u3 = ", ".join(sorted(uchastok3))
label_u3_content = Label(frame_u3, text=list_u3, font="Arial 11", bg=COLOR_U3, justify=CENTER)
label_u3_content.pack(pady=5, padx=10)

frame_uchastki.columnconfigure(0, weight=1)
frame_uchastki.columnconfigure(1, weight=1)
frame_uchastki.columnconfigure(2, weight=1)

btn_calc = Button(root, text="Рассчитать пересечения и объединения",
                  command=calculate_sets,
                  bg=COLOR_BLUE_BTN, fg=COLOR_WHITE_TEXT,
                  font="Arial 14 bold", width=40, height=2)
btn_calc.pack(pady=20)

frame_results = Frame(root, bg=COLOR_BG, bd=1, relief="solid")
frame_results.pack(padx=20, pady=10, fill=X)

label_res1_title = Label(frame_results, text="1. Имеются на КАЖДОМ участке (&):",
                         font="Arial 12 bold", bg=COLOR_BG, fg=COLOR_TEXT, anchor="w")
label_res1_title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
label_res1 = Label(frame_results, text="", font="Arial 12", bg=COLOR_RESULT_BG,
                   fg="green", bd=1, relief="sunken", width=50, anchor="w")
label_res1.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

label_res2_title = Label(frame_results, text="2. Имеются ХОТЯ БЫ НА ОДНОМ (|):",
                         font="Arial 12 bold", bg=COLOR_BG, fg=COLOR_TEXT, anchor="w")
label_res2_title.grid(row=1, column=0, padx=10, pady=5, sticky="w")
label_res2 = Label(frame_results, text="", font="Arial 12", bg=COLOR_RESULT_BG,
                   fg="blue", bd=1, relief="sunken", width=50, anchor="w")
label_res2.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

label_res3_title = Label(frame_results, text="3. НЕ имеются ни на одном (-):",
                         font="Arial 12 bold", bg=COLOR_BG, fg=COLOR_TEXT, anchor="w")
label_res3_title.grid(row=2, column=0, padx=10, pady=5, sticky="w")
label_res3 = Label(frame_results, text="", font="Arial 12", bg=COLOR_RESULT_BG,
                   fg="red", bd=1, relief="sunken", width=50, anchor="w")
label_res3.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

frame_results.columnconfigure(1, weight=1)

root.mainloop()