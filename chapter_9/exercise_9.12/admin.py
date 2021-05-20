from privileges import Privileges
from user import User

class Admin(User):
    """Описание администратора"""
    def __init__(self, first_name, last_name, age, work="Супер Админ"):
        super().__init__(first_name, last_name, age, work)
        self.privileges = Privileges()
