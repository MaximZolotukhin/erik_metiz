# Создание класса
class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} сидеть!")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} перекатиться!")

my_dog = Dog('Вилли', 6)
your_dog = Dog('Люси', 6)

print(f"Имя моей собаки, {my_dog.name}")
print(f"Моей собаки {my_dog.age} лет")
my_dog.sit()
my_dog.roll_over()

print("\n")

print(f"Имя моей собаки, {your_dog.name}")
print(f"Моей собаки {your_dog.age} лет")
your_dog.sit()
your_dog.roll_over()
