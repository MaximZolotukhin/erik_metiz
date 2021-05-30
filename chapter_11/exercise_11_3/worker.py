"""
Работник:
напишите класс Employee, представляющий работника. Метод __init__() должен получать имя,
фамилию и ежегодный оклад; все эти значения должны сохраняться в атрибутах. Напишите метод give_raise(),
который по умолчанию увеличивает ежегодный оклад на $5000 — но при этом может получать другую величину прибавки.
Напишите тестовый сценарий для Employee. Напишите два тестовых метода, test_give_default_raise() и
test_give_custom_raise(). Используйте метод setUp(), чтобы вам не приходилось заново создавать экземпляр
Employee в каждом тестовом метода. Запустите свой тестовый сценарий и убедитесь в том, что оба теста прошли успешно.
"""

class Employee():

    def __init__(self, name, last_name, salary):
        self.name = name
        self.last_name = last_name
        self.salary = salary

    def employee(self):
        """Данные о сотруднике"""
        full_date = f"{self.name} {self.last_name}: оклад {self.salary}"
        return full_date

    def give_raise(self, salary_up=5000):
        """Ежегодное поднятие оклада"""
        self.salary += salary_up
        return self.salary


def info_worker():
    """Внесение информации о сотруднике"""
    name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    salary = input("Введите сумму оклада: ")
    worker_1 = Employee(name, last_name, salary)
    print(worker_1.employee())

# info_worker()