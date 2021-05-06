"""
Вложенные словари:
"""
# Создаем вложенный словарь
user = {
    'gvanrosum': {
            'fname': 'Гвидо',
            'lname': 'Ванроссум',
            'pr_lang': 'python'
        },

    'baik': {
                'fname': 'Брендан',
                'lname': 'Айк',
                'pr_lang': 'javaScript'
            },

    'drihci': {
        'fname': 'Деннисом',
        'lname': 'Ритчи',
        'pr_lang': 'c'
    },

    'bstraustrup': {
        'fname': 'Бьерном',
        'lname': 'Страуструпом',
        'pr_lang': 'c++'
    },

    'aheilsberg': {
        'fname': 'Андерса',
        'lname': 'Хейлсберга',
        'pr_lang': 'c#'
    },

    'sviltaumot': {
        'fname': 'Скотта',
        'lname': 'Вильтаумота',
        'pr_lang': 'c#'
    },
}
# Перебор значений из словарая с выводом результатов
list_author = []
for username, user_info in user.items():
    print(f"\nПользовательский ник: {username}")
    full_name = f"{user_info['fname']} {user_info['lname']}"
    programm_lang = user_info['pr_lang']
    if programm_lang == 'c#':
        list_author.append(full_name)
    else:
        print(f"Язык программирования {programm_lang.title()} разработал {full_name}")

# Вывод результата для C#
print(f"Язык программирования {programm_lang.title()} разработали: ", end='')
i = 0
for username in list_author:
    if i == 0:
        print(f"{username.title()}, ", end='')
    else:
        print(f"{username.title()}.", end='')
    i += 1
