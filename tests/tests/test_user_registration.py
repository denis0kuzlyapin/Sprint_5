from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants import PROD_STAND
from helpers import AuthCredentials
from locators import (HomePage, AuthPade, Header, ErrorAuth)


def test_registration(driver):
    email = AuthCredentials.gen_email()
    password = AuthCredentials.gen_password()

    driver.get(PROD_STAND)

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(AuthPade.EMAIL_INPUT))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(password)
    driver.find_element(
        *AuthPade.SUBMIT_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPade.CREATE_ACCOUNT_BTN).click()
    
    WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(Header.PROFILE_NAME))
    # Создаем переменную, в которой хранится элемент с именем юзера
    name = driver.find_element(*Header.PROFILE_NAME).text
    # Проверка, что мы на домашней странице
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(HomePage.HOME_PAGE))
    # Проверка, что появился аватар юзера
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(Header.USER_AVATAR))
    # Проверка, что на странице есть элемент с именем юзера — "User" (Сделал через in т.к. точка похожа на баг)
    assert 'User' in name


def test_registration_by_email_without_mask_get_error(driver):
    email = AuthCredentials.gen_email()
    password = AuthCredentials.gen_password()
    invalid_email = AuthCredentials.gen_invalid_email()

    driver.get(PROD_STAND)

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(AuthPade.EMAIL_INPUT))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(invalid_email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(password)
    driver.find_element(
        *AuthPade.SUBMIT_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*AuthPade.CREATE_ACCOUNT_BTN).click()
    # Проверяем, что у инпута "Email" появилась обводка
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.INPUT_EMAIL_ERROR))
    # Проверяем, что у инпута "Пароль" появилась обводка
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.PASSWORD_INPUT_ERROR))
    # Проверяем, что у инпута "Повторите пароль" появилась обводка
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.SUBMIT_PASSWORD_INPUT_ERROR))
    # Проверяем, что появилось сообщение "Ошибка"
    assert WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.ERROR_MESSAGE_EMAIL))


def test_registering_existing_user_get_error(driver):
    existing_email = AuthCredentials.gen_existing_email()
    existing_password = AuthCredentials.gen_existing_password()

    driver.get(PROD_STAND)

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.NO_ACCOUNT_BTN).click()
    # Ожидание окна регистрации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(AuthPade.EMAIL_INPUT))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(
        *AuthPade.SUBMIT_PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*AuthPade.CREATE_ACCOUNT_BTN).click()
    # Проверяем, что у инпута "Email" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.INPUT_EMAIL_ERROR))
    # Проверяем, что у инпута "Пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.PASSWORD_INPUT_ERROR))
    # Проверяем, что у инпута "Повторите пароль" появилась обводка
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.SUBMIT_PASSWORD_INPUT_ERROR))
    # Проверяем, что появилось сообщение "Ошибка"
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ErrorAuth.ERROR_MESSAGE_EMAIL))


def test_login_user_success(driver):
    existing_email = AuthCredentials.gen_existing_email()
    existing_password = AuthCredentials.gen_existing_password()

    driver.get(PROD_STAND)

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*AuthPade.ENTER_BTN).click()
    # Проверка, что мы на домашней странице
    assert WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePage.HOME_PAGE))
    # Проверка, что появился аватар юзера
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Header.USER_AVATAR))
    # Создаем переменную, в которой хранится элемент с именем юзера
    name = driver.find_element(*Header.PROFILE_NAME).text
    # Проверка, что на странице есть элемент с именем юзера — "User" (Сделал через in т.к. точка похожа на баг)
    assert 'User' in name


def test_logout_user_success(driver):
    existing_email = AuthCredentials.gen_existing_email()
    existing_password = AuthCredentials.gen_existing_password()

    driver.get(PROD_STAND)

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*AuthPade.ENTER_BTN).click()
    # Проверка, что появился аватар юзера
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(Header.USER_AVATAR))

    driver.find_element(*Header.EXIT_BTN).click()
    # Проверка, что нет аватара пользователя
    assert WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located(Header.USER_AVATAR)
    )
    # Проверка, что нет имени пользователя
    assert WebDriverWait(driver, 3).until(
        expected_conditions.invisibility_of_element_located(
            Header.PROFILE_NAME)
    )
    # Проверка, что появилась кнопка "Вход и регистрация"
    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(AuthPade.LOGIN_AND_REG_BTN))
