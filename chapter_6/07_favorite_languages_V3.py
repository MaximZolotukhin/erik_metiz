# Модифицируем программу до версии 3
# Создаем словарь
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Выбор значений из словарая
for prog_lang in favorite_languages.values():
    print(f"Языки программирования: {prog_lang}")

print("\n")
# Используем множество для вывода только уникальных значений.
for prog_lang in set(favorite_languages.values()):
    print(f"Языки программирования: {prog_lang}")
