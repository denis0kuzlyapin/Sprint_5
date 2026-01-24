import random
import string


class AuthCredentials:
    @staticmethod
    def gen_email():
        user = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=7))
        domain = ''.join(random.choices(string.ascii_lowercase, k=7))
        tld = ''.join(random.choices(string.ascii_lowercase, k=3))
        return f"{user}@{domain}.{tld}"
    @staticmethod
    def gen_password():
        password = random.randint(10000000, 99999999)
        return str(password)
    @staticmethod
    def gen_invalid_email():
        email = ''.join(random.choices(
            string.ascii_lowercase + string.digits, k=7))
        return email
    @staticmethod
    def gen_existing_password():
        existing_password = '12345678'
        return existing_password
    @staticmethod
    def gen_existing_email():
        existing_email = 'user666@gmail.com'
        return existing_email


class FieldsAd:
    # Создание названия объявления. (Как сделать его рандомным и затем найти с учетом пагинации страниц объявлений — ещё не проходили, приходится так)
    @staticmethod
    def gen_item_name():
        item_name = 'Тестовое объявление для прогона'
        return item_name
    @staticmethod
    def gen_item_description():
        random_item_description = ''.join(random.choices(
            string.ascii_letters + string.digits, k=50))
        return random_item_description
    @staticmethod
    def gen_price():
        random_price = str(random.randint(1000000, 9999999))
        return random_price
