user_list = ['maxim', 'olga', 'natasha', 'admin']

if user_list:
    for user in user_list:
        if user == 'admin':
            print(f'Привет {user}, вывести отчет о случившемся?')
        else:
            print(f'Привет {user}, спасибо что зашли снова?')
else:
    print('Список пользователей пуст!')
