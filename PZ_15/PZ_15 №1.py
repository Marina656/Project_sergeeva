'''
Приложение ГРУЗОВЫЕ ПЕРЕВОЗКИ для некоторой организации. БД должна
содержать таблицу Перевозки со следующей структурой записи: маршрут, фамилия
водителя, даты отправки и прибытия, масса груза.
'''
import sqlite3 as sq

DB = "cargo_transport.db"

def init_db():
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Перевозки(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                маршрут TEXT NOT NULL,
                фамилия_водителя TEXT NOT NULL,
                дата_отправки TEXT,
                дата_прибытия TEXT,
                масса_груза REAL
            )
        """)
        cur.execute("SELECT COUNT(*) FROM Перевозки")
        if cur.fetchone()[0] == 0:
            data = [
                ("Москва - Казань", "Иванов", "2024-05-10", "2024-05-12", 15.5),
                ("СПб - Минск", "Петров", "2024-05-15", "2024-05-17", 20.0),
                ("Екатеринбург - Новосибирск", "Сидоров", "2024-06-01", "2024-06-04", 8.3),
                ("Самара - Уфа", "Кузнецов", "2024-06-10", "2024-06-11", 12.0),
                ("Краснодар - Сочи", "Иванов", "2024-07-05", "2024-07-06", 5.0),
                ("Воронеж - Ростов", "Петров", "2024-07-10", "2024-07-13", 25.5),
                ("Казань - Уфа", "Сидоров", "2024-08-01", "2024-08-02", 3.2),
                ("Н. Новгород - Москва", "Кузнецов", "2024-08-05", "2024-08-07", 18.0),
                ("Томск - Новосибирск", "Иванов", "2024-09-01", "2024-09-02", 7.5),
                ("Омск - Тюмень", "Петров", "2024-09-10", "2024-09-12", 22.0)
            ]
            cur.executemany("""
                INSERT INTO Перевозки(маршрут, фамилия_водителя, дата_отправки, дата_прибытия, масса_груза)
                VALUES (?, ?, ?, ?, ?)
            """, data)

def search_by_driver():
    driver = input("Фамилия водителя: ").strip()
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Перевозки WHERE фамилия_водителя LIKE ?", (f"%{driver}%",))
        print("Результат поиска:")
        for row in cur: print(row)

def search_by_date_range():
    d1 = input("Дата от (ГГГГ-ММ-ДД): ").strip()
    d2 = input("Дата до (ГГГГ-ММ-ДД): ").strip()
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Перевозки WHERE дата_отправки BETWEEN ? AND ?", (d1, d2))
        print("Результат поиска:")
        for row in cur: print(row)

def search_by_weight():
    try:
        w = float(input("Масса груза больше (тонн): "))
    except ValueError:
        return
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Перевозки WHERE масса_груза > ?", (w,))
        print("Результат поиска:")
        for row in cur: print(row)

def edit_weight_by_driver():
    driver = input("Фамилия водителя: ").strip()
    try:
        new_w = float(input("Новая масса груза (тонн): "))
    except ValueError:
        return
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Перевозки SET масса_груза = ? WHERE фамилия_водителя = ?", (new_w, driver))
        print(f"Обновлено записей: {cur.rowcount}")

def edit_arrival_by_route():
    route = input("Маршрут (часть названия): ").strip()
    new_date = input("Новая дата прибытия (ГГГГ-ММ-ДД): ").strip()
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Перевозки SET дата_прибытия = ? WHERE маршрут LIKE ?", (new_date, f"%{route}%"))
        print(f"Обновлено записей: {cur.rowcount}")

def increase_weight_below():
    try:
        threshold = float(input("Увеличить массу для грузов легче (тонн): "))
        add_w = float(input("На сколько тонн увеличить: "))
    except ValueError:
        return
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("UPDATE Перевозки SET масса_груза = масса_груза + ? WHERE масса_груза < ?", (add_w, threshold))
        print(f"Обновлено записей: {cur.rowcount}")

def delete_by_id():
    try:
        pid = int(input("ID записи для удаления: "))
    except ValueError:
        return
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Перевозки WHERE id = ?", (pid,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_driver():
    driver = input("Удалить все перевозки водителя: ").strip()
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Перевозки WHERE фамилия_водителя = ?", (driver,))
        print(f"Удалено записей: {cur.rowcount}")

def delete_by_weight():
    try:
        w = float(input("Удалить перевозки с массой меньше (тонн): "))
    except ValueError:
        return
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("DELETE FROM Перевозки WHERE масса_груза < ?", (w,))
        print(f"Удалено записей: {cur.rowcount}")

def show_all():
    with sq.connect(DB) as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Перевозки")
        print("Все записи:")
        for row in cur: print(row)

def main():
    init_db()
    while True:
        print("\nГРУЗОВЫЕ ПЕРЕВОЗКИ")
        print("0. Показать все записи")
        print("1. ПОИСК (1-по водителю  2-по датам  3-по массе)")
        print("2. РЕДАКТИРОВАНИЕ (1-масса по водителю  2-дата по маршруту  3-увеличить массу)")
        print("3. УДАЛЕНИЕ (1-по ID  2-по водителю  3-по массе)")
        print("9. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == '0':
            show_all()
        elif choice == '1':
            sub = input("Вариант поиска (1-3): ").strip()
            if sub == '1':
                search_by_driver()
            elif sub == '2':
                search_by_date_range()
            elif sub == '3':
                search_by_weight()
        elif choice == '2':
            sub = input("Вариант редактирования (1-3): ").strip()
            if sub == '1':
                edit_weight_by_driver()
            elif sub == '2':
                edit_arrival_by_route()
            elif sub == '3':
                increase_weight_below()
        elif choice == '3':
            sub = input("Вариант удаления (1-3): ").strip()
            if sub == '1':
                delete_by_id()
            elif sub == '2':
                delete_by_driver()
            elif sub == '3':
                delete_by_weight()
        elif choice == '9':
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Введите 0, 1, 2, 3 или 9.")

if __name__ == "__main__":
    main()