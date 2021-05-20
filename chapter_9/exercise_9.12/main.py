"""
Множественные модули:
сохраните класс User в одном модуле, а классы Privileges и Admin в другом модуле.
В отдельном файле создайте экземпляр Admin и вызовите метод show_privileges(),
чтобы показать, что все работает правильно.
"""
from user import User
from privileges import Privileges
# Два верхних импорта необходимы только при создании других классов.
from admin import Admin


user_as2 = Admin("Эцио", "Аудиторе", 19, work="Ассасин")
user_as2.describe_user()
user_as2.privileges.show_privileges()
print()
super_user = User("Дезмонд", "Объект 17", 21, work="Разносчик")
super_user.describe_user()
