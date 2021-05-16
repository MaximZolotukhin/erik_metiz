"""
9.5. Попытки входа:
добавьте атрибут login_attempts в класс User из упражнения 9.3 (с. 175).
Напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1.

Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts.
Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.
Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно,
а затем вызовите reset_login_attempts(). Снова выведите login_attempts и убедитесь в том,
что значение обнулилось.
"""
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


user_0 = User("Шен", "Коннери", 37)
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print(user_0.login_attempts)
user_0.reset_login_attempts()
print(user_0.login_attempts)
