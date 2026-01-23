from selenium.webdriver.common.by import By

# Кнопка "Вход и регистрация"
LOGIN_AND_REG_BTN = (By.XPATH, "//button[text()='Вход и регистрация']")
# Кнопка "Нет аккаунта"
NO_ACCOUNT_BTN = (By.XPATH, "//button[text()='Нет аккаунта']")
# Инпут "Введите Email"
EMAIL_INPUT = (By.NAME, "email")
# Инпут "Пароль"
PASSWORD_INPUT = (By.NAME, "password")
# Инпут "Повторите пароль"
SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
# Кнопка "Создать аакаунт"
CREATE_ACCOUNT_BTN = (By.XPATH, "//button[text()='Создать аккаунт']")
# Аватар юзера
USER_AVATAR = (By.XPATH, "//button[contains(@class,'circleSmall')]")
# Имя профиля
PROFILE_NAME = (By.XPATH, "//h3[contains(@class,'profileText')]")
# Домашняя страница
HOME_PAGE = (By.CSS_SELECTOR, "div.homePage_homepageStyle__WP-Y1")
# Красная обводка у инпута поля email
INPUT_EMAIL_ERROR = (
    By.XPATH, ("//input[@name='email']/parent::div[contains(@class,'input_inputError')]"))
# Красная обводка у инпута "Пароль"
PASSWORD_INPUT_ERROR = (
    By.XPATH, ("//input[@name='password']/parent::div[contains(@class,'input_inputError')]"))
# Красная обводка у инпута "Повторите пароль"
SUBMIT_PASSWORD_INPUT_ERROR = (
    By.XPATH, ("//input[@name='submitPassword']/parent::div[contains(@class,'input_inputError')]"))
# Сообщение "Ошибка" под инпутом "Введите Email"
ERROR_MESSAGE_EMAIL = (
    By.XPATH, ("//input[@name='email']/parent::div/../../span[contains(text(),'Ошибка')]"))
# Кнопка "Войти"
ENTER_BTN = (By.XPATH, "//button[text()='Войти']")
# Кнопка "Выйти"
EXIT_BTN = (By.XPATH, "//button[text()='Выйти']")
# Кнопка "Разместить объявление"
POSTING_AD_BTN = (By.XPATH, "//button[text()='Разместить объявление']")
# Попап авторизации при размещении объявления
LOGIN_MODAL_FOR_POSTING_AD = (By.XPATH, "//form[.//h1]")
# Заголовок модалки при попытке размещения объявления
HEADER_LOGIN_MODAL_FOR_POSTING_AD = (By.XPATH, "//h1[@class='h1']")
# Инпут "Название" товара
NAME_ITEM_INPUT = (
    By.XPATH, "//input[@placeholder='Название' and @name='name']")
# Инпут "Описание" товара
DESCRIPTION_ITEM_INPUT = (
    By.XPATH, "//textarea[@placeholder='Описание товара' and @name='description']")
# Инпут "Стоимость"
PRICE_IPUT = (By.XPATH, "//input[@placeholder='Стоимость' and @name='price']")
# Дропдаун "Категории"
DROPDOWN_CATEGORIES = (
    By.CSS_SELECTOR, 'form > div:nth-child(2) .dropDownMenu_input__itKtw > button')
# Категория "Книги"
BOOK_CATEGORY = (By.XPATH, "//span[text()='Книги']/parent::button")
# Дропдаун "Город"
DROPDOWN_CITIES = (
    By.CSS_SELECTOR, 'form > div.dropDownMenu_dropMenu__sBxhz > div.dropDownMenu_input__itKtw > button')
# Город "Санкт-Петербург"
SAINT_PETERSBURG_SITY = (
    By.XPATH, "//span[text()='Санкт-Петербург']/parent::button")
# Радиокнопка "Б/У"
USED_RBTN = (By.XPATH, "//label[text()='Б/У']")
# Кнопка "Опубликовать"
POST_BTN = (By.XPATH, "//button[text()='Опубликовать']")
# Страница с объявлениями
ADS_PAGE = (By.XPATH, "//div[@class='grid_threeColumns__ldn5D']")
# Кнопка "Сохранить изменения" в ЛК
SAVE_CHANGES_BTN = (By.XPATH, "//button[text()='Сохранить изменения']")
# Контейнер объявления в ЛК
LAST_PROFILE_AD = (
    By.XPATH, "//div[@class='grid_threeColumns__ldn5D']/div[position()=1]")
# Название последнего созданного объявления в ЛК
FIRST_AD_NAME_IN_PROFILE = (
    By.XPATH, "//h2[@class='h2' and contains(text(), 'Тестовое объявление для прогона')]")
