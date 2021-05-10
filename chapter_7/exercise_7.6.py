"""
Три выхода:
напишите альтернативную версию упражения 7.4 или упражнения 7.5, в которой
каждый пункт следующего списка встречается хотя бы один раз.
    Завершение цикла по  проверке условия в команде while:

    Управление продолженительностю цикла в зависимости от
    переменной active.

    Выход из цикла по команде break, если пользователь вводит 'quit'.
"""

prompt = f"Пожалуйста введите сколько вам лет: "
prompt += f"\nдля выхода введите 'выход': "

action = True
while action:
    age = input("Пожалуйста введите сколько вам лет: ")
    if age != "выход":
        age = int(age)
        if age < 3:
            print(f"Так как вам {age} билет вы получаетет бесплатно.")
        elif age >=3 and age < 12:
            print(f"Так как вам {age} билет стоит 10$.")
        elif age >= 12:
            print(f"Так как вам {age} билет стоит 15$.")
    else:
        action = False