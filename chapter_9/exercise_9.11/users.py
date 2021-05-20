"""Классы касающиеся пользователей"""
class Privileges():

    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print("Привелегии Админстратора: ")
        for privilege in self.privileges:
            print(f"- {privilege}")


class User():
    """Описание пользователя"""

    def __init__(self, first_name, last_name, age, work="Секретный агент"):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.work = work
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """При каждом вызове увеличивает количество зарегистрировавшихся человек на 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Обнуляет количество зарегестрированных пользователей"""
        self.login_attempts = 0


class Admin(User):
    """Описание администратора"""
    def __init__(self, first_name, last_name, age, work="Супер Админ"):
        super().__init__(first_name, last_name, age, work)
        self.privileges = Privileges()
