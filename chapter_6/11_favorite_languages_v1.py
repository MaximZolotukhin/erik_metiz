# Создаем словарь c вложенными списками
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', ],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

# Извлекаем данные из славоря.
for name, languages in favorite_languages.items():
    if len(languages) >= 2:
        print(f"\n{name.title()} твой любимые языки: ")
    else:
        print(f"\n{name.title()} твой любимый язык: ")
    for language in languages:
        print(f"\t{language.title()}")
