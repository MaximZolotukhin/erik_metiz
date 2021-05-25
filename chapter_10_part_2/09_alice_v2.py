"""Анализ текста"""

filename = "alice.txt"
try:
    with open(filename, encoding='utf=8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Извините, файл {filename}, не найден.")
else:
    #Подсчет прибилизительного количества строк в файле.
    words = contents.split()
    num_words = len(words)
    print(f"В файле {filename}, есть {num_words} слов")
