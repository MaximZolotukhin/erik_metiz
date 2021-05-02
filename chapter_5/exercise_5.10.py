current_users = ['Maxim', 'olga', 'Natasha', 'admin', 'vasilii', 'valera']
current_users_lower = [user.lower() for user in current_users]

news_users = ['irina', 'maxim', 'ulia', 'olga', 'miroslava']


if current_users or news_users:
    for user in news_users:
        if user in current_users:
            print(f'Извините но имя уже занято')
        else:
            print(f'Вы можете использовать данное имя при регистрации')
else:
    print('Список пользователей пуст!')
