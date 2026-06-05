'''
Создание базового класса "Животное" и его наследование для создания классов
"Собака" и "Кошка". В классе "Животное" будут общие методы, такие как "дышать"
и "питаться", а классы-наследники будут иметь свои уникальные методы и свойства,
такие как "гавкать" и "мурлыкать".
'''
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def breathe(self):
        print(f"{self.name} ({self.species}) делает вдох и выдох.")

    def eat(self, food):
        print(f"{self.name} с удовольствием ест {food}.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Собака")
        self.breed = breed

    def bark(self):
        print(f"{self.name} (порода: {self.breed}) громко гавкает: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Кошка")
        self.color = color

    def purr(self):
        print(f"{self.name} (цвет: {self.color}) тихо мурлычет: Мур-мур-мур...")

dog1 = Dog("Бобик", "Корги")
dog2 = Dog("Рекс", "Немецкая овчарка")
cat1 = Cat("Мурка", "Рыжая")
cat2 = Cat("Барсик", "Серый")

print(" Собаки:")
dog1.breathe()
dog1.eat("косточку")
dog1.bark()
print()

dog2.breathe()
dog2.bark()
print()

print("Кошки:")
cat1.breathe()
cat1.eat("рыбку")
cat1.purr()
print()

cat2.purr()