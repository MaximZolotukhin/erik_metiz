"""
Проверка имен пользователей: выполните следующие действия для создания программы, моделирующей проверку
уникальности имен пользователей.

    Создайте список current_users, содержащий пять и более имен пользователей.

    Создайте другой список, new_users, содержащий пять имен пользователей. Убедитесь в том,
    что одно или два новых имени также присутствуют в списке current_users.

    Переберите список new_users и для каждого имени в этом списке проверьте,
    было ли оно использовано ранее. Если имя уже использовалось, выведите сообщение о том,
    что пользователь должен выбрать новое имя. Если имя не использовалось, выведите сообщение
    о его доступности.

    Проследите за тем, чтобы сравнение выполнялось без учета регистра символов.
    Если имя 'John' уже используется, в регистрации имени 'JOHN' следует отказать.
    (Для этого необходимо создать копию current_users, содержащую версию всех существующих имен
    пользователей в нижнем регистре.)
"""
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
