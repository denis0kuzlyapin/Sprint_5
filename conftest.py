import pytest
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
