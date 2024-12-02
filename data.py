MAIN_PAGE_URL = "https://stellarburgers.nomoreparties.site/"
ADDITIONAL_URLS = {
    'register_page': 'register',
    'login_page': 'login',
    'account_profile': 'account/profile',
    'forgot_password': 'forgot-password',
    'reset_password': 'reset-password',
    'order_history': 'account/order-history'
}

DRIVER_NAME = None

EMAIL = 'сергей_чичкань_14_589@yandex.ru'
PASSWORD = 'MyL6&@stGn'

# For API
COMMON_HEADERS = {'Content-Type': 'application/json'}

USER_REGISTRATION_PATH = "api/auth/register"
USER_AUTH_PATH = "api/auth/login"
USER_EDIT_PATH = "api/auth/user"

USER_BODY = {
    "email": "{email}",
    "password": "{password}",
    "name": "{username}"
}
