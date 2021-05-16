"""
Пользователи:
создайте класс с именем User. Создайте два атрибута first_name и last_name, а затем еще
несколько атрибутов, которые обычно хранятся в профиле пользователя. Напишите метод describe_user(),
который выводит сводку с информацией о пользователе. Создайте еще один метод greet_user()
для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей.
Вызовите оба метода для каждого пользователя.
"""


class User():
    """Описание пользователя"""
    def __init__(self, first_name, last_name, age, work="Секретный агент"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.work = work

    def describe_user(self):
        """Вывод полной информации о пользователе"""
        print(f"Краткая информация о новом агенте 007:")
        print(f"Имя {self.first_name}")
        print(f"Фамилия {self.last_name}")
        print(f"Возраст {self.age}")
        print(f"Работа {self.work}")

    def greet_user(self):
        """Вывод сообщения"""
        print(f"Привет {self.first_name} {self.last_name}, вы завербованы!")


sean = User("Шен", "Коннери", 37)
valera = User("Валений", "Попов", 22, "Архитектор")

sean.describe_user()
sean.greet_user()
print()
valera.describe_user()
valera.greet_user()
