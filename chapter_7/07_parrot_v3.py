# Усовершенствованная версии программы parrot
prompt = "\nВведите что нибудь и я отображу это на экране: "
prompt += "\nВведите 'выход' чтобы завершить выполнение программы: "
# Создаем флаг для остановки работы цикла while в случии соответствия условию остановки цикла
active = True


while active:
    message = input(prompt)

    if message.lower() == 'выход':
        active = False # Если пользователь ввел слово выход, переводим флаг в значение False
    else:
        print(message)
