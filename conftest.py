import pytest
from helpers import (FieldsAd, AuthCredentials)
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
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def random_email():
    return AuthCredentials.gen_email()


@pytest.fixture(scope='function')
def random_password():
    return AuthCredentials.gen_password()


@pytest.fixture(scope='function')
def random_invalid_email():
    return AuthCredentials.gen_invalid_email()


@pytest.fixture(scope='function')
def existing_password():
    return AuthCredentials.gen_existing_password()


@pytest.fixture(scope='function')
def existing_email():
    return AuthCredentials.gen_existing_email()


# Создание названия объявления. (Как сделать его рандомным и затем найти с учетом пагинации страниц объявлений — ещё не проходили, приходится так)
@pytest.fixture(scope='function')
def item_name():
    return FieldsAd.gen_item_name()


@pytest.fixture(scope='function')
def random_item_description():
    return FieldsAd.gen_item_description()


@pytest.fixture(scope='function')
def random_price():
    return FieldsAd.gen_price()
