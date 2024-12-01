MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
ADDITIONAL_URLS = {
    'register_page': 'register',
    'log_in': 'login',
    'account_profile': 'account/profile',
    'forgot_password': 'forgot-password',
    'reset_password': 'reset-password',
}

DRIVER_NAME = None

EMAIL = 'сергей_чичкань_14_589@yandex.ru'
PASSWORD = 'MyL6&@stGn'

# For API
COMMON_HEADERS = {'Content-Type': 'application/json'}

USER_REGISTRATION_PATH = "api/auth/register"
USER_AUTH_PATH = "api/auth/login"

USER_BODY = {
    "email": "{email}",
    "password": "{password}",
    "name": "{username}"
}
