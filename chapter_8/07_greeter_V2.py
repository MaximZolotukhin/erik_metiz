# Первая функция доработанный вариант
def get_formatted_name(first_name, last_name):
    """Возвращает аккуратно отформатированное полное имя."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Бесконечный цикл!
while True:
    print("\nПожалуйста скажите мне ваше имя: ")
    print("(введите 'q' для выхода!): ")
    f_name = input()
    if f_name == 'q':
        break

    l_name = input()
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
