# Передача неограниченного числа именованных аргументов
def build_profile(firs_name, last_name, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['firs_name'] = firs_name
    user_info['last_name'] = last_name
    return user_info


user_profile = build_profile('Альберт', 'Эйнштейн', location='Принстон', field='физика')

print(user_profile)
