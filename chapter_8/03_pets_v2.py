# Именованные аргументы.
def describe_pet(animal_type, pet_name):
    """
    Выводит информацию о животном.
    :param animal_type: вид животного
    :param pet_name: кличка животного
    :return:
    """
    print(f"\nУ меня есть {animal_type}")
    print(f"Кличка моей {animal_type} {pet_name.title()}")

describe_pet(animal_type="кошка",pet_name="сима")
