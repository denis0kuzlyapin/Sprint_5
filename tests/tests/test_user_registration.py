from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LOGIN_AND_REG_BTN, EMAIL_INPUT, NO_ACCOUNT_BTN, PASSWORD_INPUT, SUBMIT_PASSWORD_INPUT, CREATE_ACCOUNT_BTN, USER_AVATAR, PROFILE_NAME, HOME_PAGE, INPUT_EMAIL_ERROR, PASSWORD_INPUT_ERROR, SUBMIT_PASSWORD_INPUT_ERROR, ERROR_MESSAGE_EMAIL, ENTER_BTN,EXIT_BTN


def test_registration(driver, random_email, random_password):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))

    driver.find_element(*NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(EMAIL_INPUT))

    driver.find_element(*EMAIL_INPUT).send_keys(random_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(random_password)
    driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(random_password)
    driver.find_element(*CREATE_ACCOUNT_BTN).click()
    # Проверка, что мы на домашней странице
    assert WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HOME_PAGE))
    # Проверка, что появился аватар юзера
    assert WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable(USER_AVATAR))
    # Создаем переменную, в которой хранится элемент с именем юзера
    name = driver.find_element(*PROFILE_NAME).text
    # Проверка, что на странице есть элемент с именем юзера — "User" (Сделал через in т.к. точка похожа на баг)
    assert 'User' in name

    driver.quit()


def test_registration_by_email_without_mask_get_error(driver, random_invalid_email, random_password):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))

    driver.find_element(*NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(EMAIL_INPUT))

    driver.find_element(*EMAIL_INPUT).send_keys(random_invalid_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(random_password)
    driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(random_password)
    driver.find_element(*CREATE_ACCOUNT_BTN).click()
    # Проверяем, что у инпута "Email" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(INPUT_EMAIL_ERROR))
    # Проверяем, что у инпута "Пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PASSWORD_INPUT_ERROR))
    # Проверяем, что у инпута "Повторите пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(SUBMIT_PASSWORD_INPUT_ERROR))
    # Проверяем, что появилось сообщение "Ошибка"
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ERROR_MESSAGE_EMAIL))
    
    driver.quit()
    
    
def test_registering_existing_user_get_error(driver,existing_password,existing_email):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    
    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))

    driver.find_element(*NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(EMAIL_INPUT))
    
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*SUBMIT_PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*CREATE_ACCOUNT_BTN).click()
    # Проверяем, что у инпута "Email" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(INPUT_EMAIL_ERROR))
    # Проверяем, что у инпута "Пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PASSWORD_INPUT_ERROR))
    # Проверяем, что у инпута "Повторите пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(SUBMIT_PASSWORD_INPUT_ERROR))
    # Проверяем, что появилось сообщение "Ошибка"
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ERROR_MESSAGE_EMAIL))
    
    driver.quit()
    
    
def test_login_user_success(driver,existing_password,existing_email):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    
    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))
    
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*ENTER_BTN).click()
    # Проверка, что мы на домашней странице
    assert WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HOME_PAGE))
    # Проверка, что появился аватар юзера
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(USER_AVATAR))
    # Создаем переменную, в которой хранится элемент с именем юзера
    name = driver.find_element(*PROFILE_NAME).text
    # Проверка, что на странице есть элемент с именем юзера — "User" (Сделал через in т.к. точка похожа на баг)
    assert 'User' in name

    driver.quit()
    
    
def test_logout_user_success(driver,existing_password,existing_email):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    
    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))
    
    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*ENTER_BTN).click()
    # Проверка, что появился аватар юзера
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(USER_AVATAR))
    
    driver.find_element(*EXIT_BTN).click()
    # Проверка, что нет аватара пользователя
    assert WebDriverWait(driver, 3).until(
    expected_conditions.invisibility_of_element_located(USER_AVATAR)
)
    # Проверка, что нет имени пользователя
    assert WebDriverWait(driver, 3).until(
    expected_conditions.invisibility_of_element_located(PROFILE_NAME)
)
    # Проверка, что появилась кнопка "Вход и регистрация"
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LOGIN_AND_REG_BTN))
    
    driver.quit()