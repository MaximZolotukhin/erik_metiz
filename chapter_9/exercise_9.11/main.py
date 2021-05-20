"""
Импортирование класса Admin:
начните с версии класса из упражнения 9.8 (с. 186).
Сохраните классы User, Privileges и Admin в одном модуле. Создайте отдельный файл,
создайте экземпляр Admin и вызовите метод show_privileges(), чтобы показать,
что все работает правильно.
"""

from users import Admin, User

super_user = Admin("Эцио", "Аудиторе", 19, work="Ассасин")
super_user.privileges.show_privileges()
