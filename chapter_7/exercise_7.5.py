"""
Билеты в кино:
кинотеатр установил несколько вариантов цены на билет в зависимости от возраста посетителя.
Для посетителей младше 3 лет билет бесплатный;
в возрасте от 3 до 12 билет состоит 10 долларов;
наконец, если возраст посетителя больше 12 лет, билет стоит 15 долларов.
Напишите цикл, который предлагает пользователю ввести возраст и выводит цену билета.
"""
prompt = f"Пожалуйста введите сколько вам лет: "
prompt += f"\nдля выхода введите 'выход': "

action = True
while action:
    age = input("Пожалуйста введите сколько вам лет: ")
    if age == "quit":
        break
    elif age == "выход": # Проверка на вводе слова "выход"
        action = False
    else:
        age = int(age)
        if age < 3:
            print(f"Так как вам {age} билет вы получаетет бесплатно.")
        elif age >= 3 and age < 12:
            print(f"Так как вам {age} билет стоит 10$.")
        elif age >= 12:
            print(f"Так как вам {age} билет стоит 15$.")
