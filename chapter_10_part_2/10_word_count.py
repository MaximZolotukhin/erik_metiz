"""Работа с несколькими файлами"""
def count_words(filename):
    """Подсчет приблизительного количества слов в файле"""
    try:
        with open(filename, encoding='utf=8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Извините, файл {filename}, не найден.")
    else:
        # Подсчет прибилизительного количества строк в файле.
        words = contents.split()
        num_words = len(words)
        print(f"В файле {filename}, есть {num_words} слов")


filenames = ['alice.txt', 'siffhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
