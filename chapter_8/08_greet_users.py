# Передача данных с помощью списка
def greet_users(names):
    """Вывод простого приветсвия для каждого пользователя в списке"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
