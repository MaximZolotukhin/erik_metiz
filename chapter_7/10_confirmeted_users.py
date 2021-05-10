# Начинаем с двух списков пользователей для проверки и пустого списка для храннения проверенных пользователей.
unconfirmed_users = ['alice', 'brain', 'candace']
confirmed_users = []

# Проверяем каждого пользователя, пока остаются непроверенные пользователи.
# Каждый пользователь, прошедший проверку, перемещается в список проверенных.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Проверенные пользоввтели: {current_user.title()}")
    confirmed_users.append(current_user)

# Вывод провереннхы пользователей.
print("\n Все пользователи проверенны: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())