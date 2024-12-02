from selenium.webdriver.common.by import By


class OrderFeedLocators:
    OF_ING_WINDOW = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]/parent::div/parent::div")
    MAIN_PAGE_SINGLE_ING = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]/parent::a")
