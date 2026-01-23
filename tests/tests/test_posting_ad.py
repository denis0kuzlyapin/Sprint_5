from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import HOME_PAGE, POSTING_AD_BTN, LOGIN_MODAL_FOR_POSTING_AD, HEADER_LOGIN_MODAL_FOR_POSTING_AD, LOGIN_AND_REG_BTN, NO_ACCOUNT_BTN, EMAIL_INPUT, PASSWORD_INPUT, ENTER_BTN, USER_AVATAR, NAME_ITEM_INPUT, DESCRIPTION_ITEM_INPUT, PRICE_IPUT, SAVE_CHANGES_BTN, DROPDOWN_CATEGORIES, BOOK_CATEGORY, DROPDOWN_CITIES, SAINT_PETERSBURG_SITY, USED_RBTN, POST_BTN, ADS_PAGE, LAST_PROFILE_AD, FIRST_AD_NAME_IN_PROFILE


def test_posting_ad_by_unauthorized_user_getting_modal_for_auth(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HOME_PAGE))

    driver.find_element(*POSTING_AD_BTN).click()
    # Проверка, что появилась модалка при попытке размещения объявления

    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(LOGIN_MODAL_FOR_POSTING_AD))
    # Проверка названия заголовка модалки при попытке размещения объявления
    assert driver.find_element(
        *HEADER_LOGIN_MODAL_FOR_POSTING_AD).text == 'Чтобы разместить объявление, авторизуйтесь'

    driver.quit()


def test_posting_ad_by_authorized_user_success(driver, existing_password, existing_email, item_name, random_item_description, random_price):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    # Ожидаем загрузки домашней страницы
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(HOME_PAGE))

    driver.find_element(*LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(NO_ACCOUNT_BTN))

    driver.find_element(*EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*ENTER_BTN).click()
    # Ожидание аватара юзера
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(USER_AVATAR))

    driver.find_element(*POSTING_AD_BTN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(NAME_ITEM_INPUT))

    driver.find_element(*NAME_ITEM_INPUT).send_keys(item_name)
    driver.find_element(
        *DESCRIPTION_ITEM_INPUT).send_keys(random_item_description)
    driver.find_element(*PRICE_IPUT).send_keys(random_price)
    driver.find_element(*DROPDOWN_CATEGORIES).click()
    driver.find_element(*BOOK_CATEGORY).click()
    driver.find_element(*DROPDOWN_CITIES).click()
    driver.find_element(*SAINT_PETERSBURG_SITY).click()
    driver.find_element(*USED_RBTN).click()
    driver.find_element(*POST_BTN).click()
    # Дожидаемся появления карточек с объявлениями
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(ADS_PAGE))
    # Прокрутка вверх до аватара пользователя
    avatar = driver.find_element(*USER_AVATAR)
    driver.execute_script("arguments[0].scrollIntoView();", avatar)

    driver.find_element(*USER_AVATAR).click()

    # Дожидаемся появления кнопки "Сохранить изменения"
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(SAVE_CHANGES_BTN))

    # Прокрутка вниз до объявлений пользователя
    last_profile_ad = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(LAST_PROFILE_AD))
    driver.execute_script("arguments[0].scrollIntoView();", last_profile_ad)

    # Првоеряем, что название последнего созданного объявления совпадает с тем, что мы указывали при создании
    name_ad = driver.find_element(*FIRST_AD_NAME_IN_PROFILE).text
    assert item_name in name_ad

    driver.quit()
