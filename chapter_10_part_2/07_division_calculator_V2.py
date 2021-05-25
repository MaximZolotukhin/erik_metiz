"""Использование исключений для предотвращения аварийного завершения программы"""
print("Дайте мне два числа и я поделю их")
print("Введите 'q' для выхода.")

while True:
    first_number = input("\nВведите первое число: ")
    if first_number == 'q':
        break
    second_number = input("\nВведите второе число: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("Запрещенное делить на ноль!!!")
    else:
        print(answer)
