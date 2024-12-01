from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PASSWORD_BTN = (By.XPATH, "//div/p/a[@href='/forgot-password']")

    SAVE_BTN = (By.XPATH, "//button[contains(text(), 'Войти')]")
