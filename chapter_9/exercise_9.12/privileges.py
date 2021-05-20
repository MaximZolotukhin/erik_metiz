class Privileges():
    """
    Привилегие пользователей
    """
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей",
                           "разрешено банить пользователей"]

    def show_privileges(self):
        print("Привелегии Админстратора: ")
        for privilege in self.privileges:
            print(f"- {privilege}")
