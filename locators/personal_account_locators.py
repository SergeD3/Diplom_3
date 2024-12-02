from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    PA_INFO_TEXT = (By.XPATH, "//p[contains(@class, 'Account_text')]")
    ORDER_HISTORY = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")

    SAVE_BTN = (By.XPATH, "//button[contains(text(), 'Сохранить')]")
