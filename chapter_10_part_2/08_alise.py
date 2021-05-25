"""Обработка исключения FileNotFoundError"""

filename = "alise.txt"
try:
    with open(filename, encoding='utf=8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Извините, файл {filename}, не найден.")
