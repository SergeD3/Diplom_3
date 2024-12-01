from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    TITLE = (By.XPATH, "//div/h2[contains(text(), 'Восстановление пароля')]")
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    RESTORE_BTN = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
