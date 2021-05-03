# Модифицируем программу до версии 2
# Создаем словарь
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Перебор значений словаря с помощью цикла for с использованием метода items()
for name, languages in favorite_languages.items():
    print(f"{name.title()} любимый язык это: {languages.title()}")

print()

frends_select = ['jen', 'phil']
for name in favorite_languages.keys():
    print(f"Имя пользователя: {name.title()}")

    if name in frends_select:
        print(f"    Привет {name.title()}, я тоже учу {favorite_languages[name].title()}")

# Так как в языке Python по умолчанию используется вызов ключа в словаре, то метод keys() можно не использовать.
if 'erin' not in favorite_languages.keys():
    print(f"Erin присоединяйся к нашему опросу =)")
