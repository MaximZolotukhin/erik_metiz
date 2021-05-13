"""
Профиль:
начните с копии программы user_profile.py(c.162). Создайте собственный
профиль вызовом build_profile(), укажите имя, фамилию и три другие пары
"ключ-значение" для вашего описания.
"""

def build_profile(firs_name, last_name, **user_info):
    """Строит словарь с информацией о пользователе"""
    user_info['firs_name'] = firs_name
    user_info['last_name'] = last_name
    return user_info


user_profile = build_profile('Максим', 'Золотухин', location='Курск', field='Python', year=1983)

print(user_profile)
