from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SAVE_BTN = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    EYE_BTN = (By.XPATH, "//div[contains(@class,'input__icon')]")
