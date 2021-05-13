# Обучение использованию модулей.
from print_models import print_models

def show_completed_models(complited_models):
    """Выводит информацию обо всех напечатанных моделях"""
    # Вывод всех готовых моделей
    print("\nСледующая модель была распечатана: ")
    for complited_model in complited_models:
        print(complited_model)


# Список моделей, которые необходимо напечатать.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
complited_models = []

print_models(unprinted_designs, complited_models)
show_completed_models(complited_models)
