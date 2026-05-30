'''
Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
водителя, даты отправки и прибытия, масса груза.
'''
import sqlite3 as sq
import os

DB = "gruzoperevozki.db"


def init_db():
    if os.path.exists(DB):
        os.remove(DB)

    with sq.connect(DB) as con:
        cur = con.cursor()

        cur.execute("""CREATE TABLE Perevozki (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marshrut TEXT NOT NULL,
            voditel TEXT NOT NULL,
            data_otpr TEXT,
            data_prib TEXT,
            massa REAL CHECK(massa > 0)
        )""")

        data = [
            ("Москва - Санкт-Петербург", "Иванов И.И.", "2026-05-01", "2026-05-03", 12.5),
            ("Казань - Самара", "Петров П.П.", "2026-05-02", "2026-05-02", 5.0),
            ("Новосибирск - Омск", "Сидоров С.С.", "2026-05-03", "2026-05-04", 20.1),
            ("Екатеринбург - Челябинск", "Иванов И.И.", "2026-05-04", "2026-05-04", 8.3),
            ("Ростов - Краснодар", "Кузнецов К.К.", "2026-05-05", "2026-05-06", 15.0),
            ("Воронеж - Белгород", "Петров П.П.", "2026-05-06", "2026-05-06", 2.5),
            ("Тюмень - Ханты-Мансийск", "Смирнов А.А.", "2026-05-07", "2026-05-09", 30.0),
            ("Калининград - Минск", "Волков В.В.", "2026-05-08", "2026-05-10", 18.7),
            ("Сочи - Ставрополь", "Кузнецов К.К.", "2026-05-09", "2026-05-10", 10.2),
            ("Уфа - Оренбург", "Сидоров С.С.", "2026-05-10", "2026-05-11", 7.8)
        ]

        cur.executemany("INSERT INTO Perevozki (marshrut, voditel, data_otpr, data_prib, massa) VALUES (?,?,?,?,?)",
                        data)


def search_by_driver():
    driver_name = input("Введите фамилию водителя для поиска (или часть): ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Perevozki WHERE voditel LIKE ?", (f"%{driver_name}%",))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Записи не найдены.")


def search_by_route():
    route_name = input("Введите название маршрута (или часть, например 'Москва'): ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Perevozki WHERE marshrut LIKE ?", (f"%{route_name}%",))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Записи не найдены.")


def search_by_date_dep():
    date_val = input("Введите дату отправки (формат ГГГГ-ММ-ДД): ")
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Perevozki WHERE data_otpr = ?", (date_val,))
        results = cur.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("Записи на эту дату не найдены.")


def edit_mass():
    try:
        pid = int(input("Введите ID перевозки для изменения массы: "))
        new_mass = float(input("Введите новую массу груза (тонн): "))

        if new_mass <= 0:
            print("Ошибка: Масса должна быть положительным числом!")
            return

        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Perevozki SET massa = ? WHERE id = ?", (new_mass, pid))
            if cur.rowcount > 0:
                print(f"Масса для ID {pid} успешно обновлена.")
            else:
                print("Запись с таким ID не найдена.")
    except ValueError:
        print("Ошибка ввода! ID должен быть целым числом, масса - числом.")


def edit_driver():
    try:
        pid = int(input("Введите ID перевозки для смены водителя: "))
        new_driver = input("Введите новую фамилию водителя: ")

        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Perevozki SET voditel = ? WHERE id = ?", (new_driver, pid))
            if cur.rowcount > 0:
                print(f"Водитель для ID {pid} успешно обновлен.")
            else:
                print("Запись с таким ID не найдена.")
    except ValueError:
        print("Ошибка ввода! ID должен быть целым числом.")


def edit_dates():
    try:
        pid = int(input("Введите ID перевозки для изменения дат: "))
        new_otpr = input("Введите новую дату отправки (ГГГГ-ММ-ДД): ")
        new_prib = input("Введите новую дату прибытия (ГГГГ-ММ-ДД): ")

        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("UPDATE Perevozki SET data_otpr = ?, data_prib = ? WHERE id = ?",
                        (new_otpr, new_prib, pid))
            if cur.rowcount > 0:
                print(f"Даты для ID {pid} успешно обновлены.")
            else:
                print("Запись с таким ID не найдена.")
    except ValueError:
        print("Ошибка ввода! ID должен быть целым числом.")


def delete_by_id():
    try:
        pid = int(input("Введите ID перевозки для удаления: "))
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Perevozki WHERE id = ?", (pid,))
            print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Ошибка ввода! ID должен быть целым числом.")


def delete_by_driver():
    driver_name = input("Введите фамилию водителя, чьи перевозки нужно удалить: ")
    confirm = input(f"Вы уверены, что хотите удалить все перевозки водителя '{driver_name}'? (да/нет): ")

    if confirm.lower() == 'да':
        with sq.connect(DB) as con:
            cur = con.cursor()
            cur.execute("DELETE FROM Perevozki WHERE voditel LIKE ?", (f"%{driver_name}%",))
            print(f"Удалено записей: {cur.rowcount}")
    else:
        print("Удаление отменено.")


def delete_by_mass_range():
    try:
        min_mass = float(input("Удалить перевозки с массой ОТ (тонн): "))
        max_mass = float(input("Удалить перевозки с массой ДО (тонн): "))

        confirm = input(f"Удалить записи с массой от {min_mass} до {max_mass}? (да/нет): ")
        if confirm.lower() == 'да':
            with sq.connect(DB) as con:
                cur = con.cursor()
                cur.execute("DELETE FROM Perevozki WHERE massa BETWEEN ? AND ?", (min_mass, max_mass))
                print(f"Удалено записей: {cur.rowcount}")
    except ValueError:
        print("Ошибка ввода! Введите числа.")


def show_all():
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Perevozki")
        rows = cur.fetchall()
        if not rows:
            print("База данных пуста.")
        else:
            print("\n--- Список всех перевозок ---")
            print(f"{'ID':<4} {'Маршрут':<30} {'Водитель':<15} {'Отпр.':<12} {'Приб.':<12} {'Масса(т)':<8}")
            print("-" * 85)
            for row in rows:
                print(f"{row[0]:<4} {row[1]:<30} {row[2]:<15} {row[3]:<12} {row[4]:<12} {row[5]:<8}")
            print("-" * 85)


init_db()

while True:
    print("\n=== МЕНЮ ПРИЛОЖЕНИЯ 'ГРУЗОВЫЕ ПЕРЕВОЗКИ' ===")
    print("1 - Показать все перевозки")
    print("2 - Поиск по водителю")
    print("3 - Поиск по маршруту")
    print("4 - Поиск по дате отправки")
    print("5 - Изменить массу груза")
    print("6 - Изменить водителя")
    print("7 - Изменить даты отправки/прибытия")
    print("8 - Удалить по ID")
    print("9 - Удалить по водителю")
    print("10 - Удалить по диапазону массы")
    print("0 - Выход")

    cmd = input("Выберите действие: ")

    if cmd == '1':
        show_all()
    elif cmd == '2':
        search_by_driver()
    elif cmd == '3':
        search_by_route()
    elif cmd == '4':
        search_by_date_dep()
    elif cmd == '5':
        edit_mass()
    elif cmd == '6':
        edit_driver()
    elif cmd == '7':
        edit_dates()
    elif cmd == '8':
        delete_by_id()
    elif cmd == '9':
        delete_by_driver()
    elif cmd == '10':
        delete_by_mass_range()
    elif cmd == '0':
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор! Попробуйте снова.")