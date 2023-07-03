from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    #TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)

    # Переменная
    current_time = time(hour=23)

    # Функция
    is_dark_theme = current_time.hour >= 22 or current_time.hour <= 6

    # Проверка
    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    #TODO переключите темную тему в зависимости от времени суток,
    #но учтите что темная тема может быть включена вручную

    # Переменные
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    # Функция
    if dark_theme_enabled_by_user is not None:
        is_dark_theme = dark_theme_enabled_by_user
    else: is_dark_theme = current_time.hour >= 22 or current_time.hour <= 6

    # Проверка
    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """

    # Список данных

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    #TODO найдите пользователя с именем "Olga"

    # Функция
    suitable_users = None
    for user in users:
        if user["name"] == "Olga":
            suitable_users = user

    # Проверка
    assert suitable_users == {"name": "Olga", "age": 45}

    #TODO найдите всех пользователей младше 20 лет

    # Функция
    suitable_users = None
    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)

    # Проверка
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")

# Создаем функцию для преобразования самой функции и аргументов
def rename_func(func, *args):
    changed_func = func.__name__.replace('_', ' ').title()
    changed_args = ', '.join([*args])
    result = f"{changed_func} [{changed_args}]"

    print(result)
    return result


def open_browser(browser_name):
    actual_result = rename_func (open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = rename_func (go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = rename_func (find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"
