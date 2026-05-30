'''
Вариант 19 https://www.bestfree.ru/uslugi/constructors/SozdanieSaytaNaUcoz_3.png
'''
from tkinter import *

root = Tk()
root.title("Регистрация")
root.geometry("600x750+300+100")
root.resizable(False, False)

COLOR_BLUE_TEXT = "#0066CC"
COLOR_GREY_TEXT = "#808080"
COLOR_BG_HEADER = "#0099CC"
COLOR_BORDER = "#CCCCCC"
FONT_LABEL = "Arial 12"
FONT_ENTRY = "Arial 12"

header_frame = Frame(root, bg=COLOR_BG_HEADER, height=60)
header_frame.pack(fill=X)
header_label = Label(header_frame, text="Создание нового сайта", bg=COLOR_BG_HEADER, fg="white", font="Arial 16 bold")
header_label.pack(pady=15)

form_frame = Frame(root)
form_frame.pack(pady=10, padx=20)

def on_focus_in(entry_widget, placeholder_text):
    if entry_widget.get() == placeholder_text:
        entry_widget.delete(0, END)
        entry_widget.config(fg="black")

def on_focus_out(entry_widget, placeholder_text):
    if entry_widget.get() == "":
        entry_widget.insert(0, placeholder_text)
        entry_widget.config(fg="grey")

label_email = Label(form_frame, text="Email", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_email.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_email = Entry(form_frame, width=30, font=FONT_ENTRY, fg="grey", bd=1, relief="solid")
entry_email.insert(0, "email")
entry_email.grid(row=0, column=1, padx=10, pady=5)
entry_email.bind("<FocusIn>", lambda e: on_focus_in(entry_email, "email"))
entry_email.bind("<FocusOut>", lambda e: on_focus_out(entry_email, "email"))

check_email = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_email.grid(row=0, column=2, padx=5)

label_pass = Label(form_frame, text="Пароль", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_pass.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_pass = Entry(form_frame, width=30, font=FONT_ENTRY, show="*", fg="grey", bd=1, relief="solid")
entry_pass.insert(0, "••••••••")
entry_pass.grid(row=1, column=1, padx=10, pady=5)
entry_pass.bind("<FocusIn>", lambda e: on_focus_in(entry_pass, "••••••••"))
entry_pass.bind("<FocusOut>", lambda e: on_focus_out(entry_pass, "••••••••"))

check_pass = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_pass.grid(row=1, column=2, padx=5)

label_name = Label(form_frame, text="Имя", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_name.grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_name = Entry(form_frame, width=30, font=FONT_ENTRY, fg=COLOR_GREY_TEXT, bd=1, relief="solid")
entry_name.insert(0, "Руслан")
entry_name.grid(row=2, column=1, padx=10, pady=5)
check_name = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_name.grid(row=2, column=2, padx=5)

label_surname = Label(form_frame, text="Фамилия", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_surname.grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_surname = Entry(form_frame, width=30, font=FONT_ENTRY, fg=COLOR_GREY_TEXT, bd=1, relief="solid")
entry_surname.insert(0, "Тертышный")
entry_surname.grid(row=3, column=1, padx=10, pady=5)
check_surname = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_surname.grid(row=3, column=2, padx=5)

label_nick = Label(form_frame, text="Никнейм", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_nick.grid(row=4, column=0, padx=10, pady=5, sticky="e")
entry_nick = Entry(form_frame, width=30, font=FONT_ENTRY, fg=COLOR_GREY_TEXT, bd=1, relief="solid")
entry_nick.insert(0, "TRos")
entry_nick.grid(row=4, column=1, padx=10, pady=5)
check_nick = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_nick.grid(row=4, column=2, padx=5)

label_dob = Label(form_frame, text="Дата рождения", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_dob.grid(row=5, column=0, padx=10, pady=5, sticky="e")

frame_dob = Frame(form_frame)
frame_dob.grid(row=5, column=1, padx=10, pady=5, sticky="w")

def update_entry_from_listbox(listbox, entry):
    selection = listbox.curselection()
    if selection:
        value = listbox.get(selection[0])
        entry.delete(0, END)
        entry.insert(0, value)
        listbox.place_forget()

frame_day = Frame(frame_dob)
frame_day.pack(side="left")
entry_day = Entry(frame_day, width=3, font=FONT_ENTRY, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
entry_day.pack(side="left")
entry_day.insert(0, "1")
button_day_arrow = Button(frame_day, text="▼", font="Arial 8", command=lambda: list_day.place(x=0, y=entry_day.winfo_height()))
button_day_arrow.pack(side="left")

list_day = Listbox(frame_day, height=5, width=3, selectmode=SINGLE, exportselection=0, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
for i in range(1, 32):
    list_day.insert(END, str(i))
list_day.bind('<Double-Button-1>', lambda e: update_entry_from_listbox(list_day, entry_day))
list_day.place_forget()


frame_month = Frame(frame_dob)
frame_month.pack(side="left", padx=5)
entry_month = Entry(frame_month, width=10, font=FONT_ENTRY, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
entry_month.pack(side="left")
entry_month.insert(0, "январь")
button_month_arrow = Button(frame_month, text="▼", font="Arial 8", command=lambda: list_month.place(x=0, y=entry_month.winfo_height()))
button_month_arrow.pack(side="left")

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
list_month = Listbox(frame_month, height=5, width=10, selectmode=SINGLE, exportselection=0, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
for month in months:
    list_month.insert(END, month)
list_month.bind('<Double-Button-1>', lambda e: update_entry_from_listbox(list_month, entry_month))
list_month.place_forget()


frame_year = Frame(frame_dob)
frame_year.pack(side="left", padx=5)
entry_year = Entry(frame_year, width=5, font=FONT_ENTRY, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
entry_year.pack(side="left")
entry_year.insert(0, "1988")
button_year_arrow = Button(frame_year, text="▼", font="Arial 8", command=lambda: list_year.place(x=0, y=entry_year.winfo_height()))
button_year_arrow.pack(side="left")

list_year = Listbox(frame_year, height=5, width=5, selectmode=SINGLE, exportselection=0, fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
for i in range(1900, 2027):
    list_year.insert(END, str(i))
list_year.bind('<Double-Button-1>', lambda e: update_entry_from_listbox(list_year, entry_year))
list_year.place_forget()


check_dob = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_dob.grid(row=5, column=2, padx=5)

label_gender = Label(form_frame, text="Пол", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_gender.grid(row=6, column=0, padx=10, pady=5, sticky="e")

var_gender = IntVar()
rbutton_male = Radiobutton(form_frame, text="Мужчина", variable=var_gender, value=1, font=FONT_LABEL)
rbutton_male.grid(row=6, column=1, padx=10, pady=5, sticky="w")
rbutton_female = Radiobutton(form_frame, text="Женщина", variable=var_gender, value=2, font=FONT_LABEL)
rbutton_female.grid(row=6, column=1, padx=80, pady=5, sticky="w")

check_gender = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_gender.grid(row=6, column=2, padx=5)

label_city = Label(form_frame, text="Место проживания", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_city.grid(row=7, column=0, padx=10, pady=5, sticky="e")

list_city = Listbox(form_frame, height=1, width=30, selectmode=SINGLE,
                    fg=COLOR_BLUE_TEXT, bd=1, relief="solid")
list_city.grid(row=7, column=1, padx=10, pady=5, sticky="w")
list_city.insert(END, "Другой город...")

label_captcha = Label(form_frame, text="Код безопасности", font=FONT_LABEL, fg=COLOR_BLUE_TEXT)
label_captcha.grid(row=8, column=0, padx=10, pady=5, sticky="e")

frame_captcha = Frame(form_frame)
frame_captcha.grid(row=8, column=1, padx=10, pady=5, sticky="w")

entry_captcha = Entry(frame_captcha, width=10, font=FONT_ENTRY, bd=1, relief="solid")
entry_captcha.pack(side="left")
entry_captcha.insert(0, "VPyJL")

label_captcha_img = Label(frame_captcha, text="VPYJL", font="Arial 14 bold",
                          fg=COLOR_BLUE_TEXT, bg="#E0F7FA", bd=1, relief="solid")
label_captcha_img.pack(side="left", padx=5)

button_refresh = Button(frame_captcha, text="↻", font=FONT_LABEL)
button_refresh.pack(side="left")

check_captcha = Label(form_frame, text="✓", fg="green", font=FONT_LABEL)
check_captcha.grid(row=8, column=2, padx=5)

var_terms = IntVar()
check_terms = Checkbutton(form_frame, text="Подтверждаю условия использования uID сообщества",
                          variable=var_terms, onvalue=1, offvalue=0, font="Arial 10", fg=COLOR_BLUE_TEXT)
check_terms.grid(row=9, column=0, columnspan=2, padx=10, pady=15, sticky="w")

button_register = Button(root, text="Регистрация", bg=COLOR_BLUE_TEXT, fg="white",
                         font="Arial 14 bold", width=30, height=2)
button_register.pack(pady=20)

root.mainloop()