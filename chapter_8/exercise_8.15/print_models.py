# Изменение списка в функции
def print_models(unprinted_designs, complited_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в complited_model.
    """
    # Цикл последовательно печатает каждую модель до конца списка.
    # После печати каждая модель перемещается в список complited_models.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Напечатать модель: {current_design}")
        complited_models.append(current_design)
