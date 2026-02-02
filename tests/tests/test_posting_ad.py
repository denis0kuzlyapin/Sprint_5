from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import PROD_STAND
from helpers import (AuthCredentials, FieldsAd)

from locators import (UserProfile, HomePage, PostingAd, AuthPade, Header)


def test_posting_ad_by_unauthorized_user_getting_modal_for_auth(driver):

    driver.get(PROD_STAND)

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePage.HOME_PAGE))

    driver.find_element(*PostingAd.POSTING_AD_BTN).click()
    # Проверка, что появилась модалка при попытке размещения объявления

    assert WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(PostingAd.HEADER_LOGIN_MODAL_FOR_POSTING_AD))
    # Проверка названия заголовка модалки при попытке размещения объявления
    assert driver.find_element(
        *PostingAd.HEADER_LOGIN_MODAL_FOR_POSTING_AD).text == 'Чтобы разместить объявление, авторизуйтесь'


def test_posting_ad_by_authorized_user_success(driver):
    existing_email = AuthCredentials.gen_existing_email()
    existing_password = AuthCredentials.gen_existing_password()
    item_name = FieldsAd.gen_item_name()
    item_description = FieldsAd.gen_item_description()
    price = FieldsAd.gen_price()

    driver.get(PROD_STAND)
    # Ожидаем загрузки домашней страницы
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(HomePage.HOME_PAGE))

    driver.find_element(*AuthPade.LOGIN_AND_REG_BTN).click()
    # Ожидание окна авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.element_to_be_clickable(AuthPade.NO_ACCOUNT_BTN))

    driver.find_element(*AuthPade.EMAIL_INPUT).send_keys(existing_email)
    driver.find_element(*AuthPade.PASSWORD_INPUT).send_keys(existing_password)
    driver.find_element(*AuthPade.ENTER_BTN).click()
    # Ожидание аватара юзера
    WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable(Header.USER_AVATAR))

    driver.find_element(*PostingAd.POSTING_AD_BTN).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable(PostingAd.NAME_ITEM_INPUT))

    driver.find_element(*PostingAd.NAME_ITEM_INPUT).send_keys(item_name)
    driver.find_element(
        *PostingAd.DESCRIPTION_ITEM_INPUT).send_keys(item_description)
    driver.find_element(*PostingAd.PRICE_IPUT).send_keys(price)
    driver.find_element(*PostingAd.DROPDOWN_CATEGORIES).click()
    driver.find_element(*PostingAd.BOOK_CATEGORY).click()
    driver.find_element(*PostingAd.DROPDOWN_CITIES).click()
    driver.find_element(*PostingAd.SAINT_PETERSBURG_SITY).click()
    driver.find_element(*PostingAd.USED_RBTN).click()
    driver.find_element(*PostingAd.POST_BTN).click()
    # Дожидаемся появления карточек с объявлениями
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePage.ADS_PAGE))
    # Прокрутка вверх до аватара пользователя
    avatar = driver.find_element(*Header.USER_AVATAR)
    driver.execute_script("arguments[0].scrollIntoView();", avatar)

    driver.find_element(*Header.USER_AVATAR).click()

    # Дожидаемся появления кнопки "Сохранить изменения"
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(UserProfile.SAVE_CHANGES_BTN))

    # Прокрутка вниз до объявлений пользователя
    last_profile_ad = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located(UserProfile.LAST_PROFILE_AD))
    driver.execute_script("arguments[0].scrollIntoView();", last_profile_ad)

    # Првоеряем, что название последнего созданного объявления совпадает с тем, что мы указывали при создании
    name_ad = driver.find_element(*UserProfile.FIRST_AD_NAME_IN_PROFILE).text
    assert item_name in name_ad
