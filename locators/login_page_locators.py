from selenium.webdriver.common.by import By


class LoginPageLocators:
    LP_TITLE = (By.XPATH, "//h2[contains(text(), 'Вход')]")
    LP_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    LP_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")

    FORGOT_PASSWORD_BTN = (By.XPATH, "//div/p/a[@href='/forgot-password']")
    ENTER_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
