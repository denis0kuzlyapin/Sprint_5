import pytest
import random
import string

from selenium import webdriver
# Добавил настройки, чтоб отключить менеджер паролей т.к. 5-й тест падал из-за предупреждения утекшего пароля


@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver


@pytest.fixture(scope='function')
def random_email():
    user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=7))
    domain = ''.join(random.choices(string.ascii_lowercase, k=7))
    tld = ''.join(random.choices(string.ascii_lowercase, k=3))
    return f"{user}@{domain}.{tld}"


@pytest.fixture(scope='function')
def random_password():
    password = random.randint(10000000, 99999999)
    return str(password)


@pytest.fixture(scope='function')
def random_invalid_email():
    email = ''.join(random.choices(
        string.ascii_lowercase + string.digits, k=7))
    return email


@pytest.fixture(scope='function')
def existing_password():
    existing_password = '12345678'
    return existing_password


@pytest.fixture(scope='function')
def existing_email():
    existing_email = 'user777@gmail.com'
    return existing_email


# Создание названия объявления. (Как сделать его рандомным и затем найти с учетом пагинации страниц объявлений — ещё не проходили, приходится так)
@pytest.fixture(scope='class')
def item_name():
    item_name = 'Тестовое объявление для прогона'
    return item_name


@pytest.fixture(scope='function')
def random_item_description():
    random_item_description = ''.join(random.choices(
        string.ascii_letters + string.digits, k=50))
    return random_item_description


@pytest.fixture(scope='function')
def random_price():
    random_price = random.randint(1000000, 9999999)
    return random_price
