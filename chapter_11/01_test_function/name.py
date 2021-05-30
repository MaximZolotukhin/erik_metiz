from name_function import get_formatted_name

print(f"Введите 'q' чтобы закрыть программу.")
while True:
    first = input("Введите имя: ")
    if first == 'q':
        break
    last = input("Введите фамилия: ")
    if last == 'q':
        break
    middle = input("Введите Отчество: (если отчестов не вводится нажмите 'Enter')")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"Ваше имя и фамилия {formatted_name}")
