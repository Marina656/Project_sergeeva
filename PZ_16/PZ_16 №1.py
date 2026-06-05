'''
Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
Добавьте методы для вычисления среднего балла и определения, является ли студент
отличником.
'''
class Student:

    def __init__(self, first_name, last_name, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def is_excellent_student(self):
        return self.calculate_average() >= 4.5

    def __str__(self):
        avg = self.calculate_average()
        status = "Отличник" if self.is_excellent_student() else "Не отличник"
        return (f"Студент: {self.first_name} {self.last_name}, "
                f"Средний балл: {avg:.2f}, Статус: {status}")

student1 = Student("Иван", "Иванов", [5, 5, 4, 5, 5])
student2 = Student("Мария", "Петрова", [3, 4, 3, 4, 3])
student3 = Student("Алексей", "Сидоров", [5, 5, 5, 5, 5])
student4 = Student("Анна", "Смирнова", [])  # Без оценок

print("ИНФОРМАЦИЯ О СТУДЕНТАХ:")

for student in [student1, student2, student3, student4]:
    print(f"\n{student}")

    print(f"  Имя: {student.first_name}")
    print(f"  Фамилия: {student.last_name}")
    print(f"  Оценки: {student.grades}")

    print(f"  Средний балл: {student.calculate_average():.2f}")
    print(f"  Отличник? {student.is_excellent_student()}")