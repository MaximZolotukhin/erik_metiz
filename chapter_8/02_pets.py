# Позиционные аргументы
def describe_pet(animal_type, pet_name):
    """
    Выводит информацию о животном.
    :param animal_type: вид животного
    :param pet_name: кличка животного
    :return:
    """
    print(f"\nУ меня есть {animal_type}")
    print(f"Кличка моей {animal_type} {pet_name.title()}")

describe_pet("кошка", "сима")
describe_pet("собака", "вилли")
