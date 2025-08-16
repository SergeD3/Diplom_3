from selenium.webdriver.common.by import By


class ConstructorFeedLocators:
    MAIN_PAGE_SAUCE_ING = (By.XPATH, "//p[contains(text(), 'Соус Spicy-X')]/parent::a")
    MAIN_PAGE_BUN = (By.XPATH, "//p[contains(text(), 'Флюоресцентная булка R2-D3')]/parent::a")
    MAIN_PAGE_ING_COUNTER = (
        By.XPATH,
        "//p[contains(text(), 'Соус Spicy-X')]/parent::a//p[contains(@class, 'counter_counter')]"
    )
    MAIN_PAGE_BASKET = (
        By.XPATH,
        "//li[contains(@class, 'BurgerConstructor_basket')]/parent::ul"
    )
    MAIN_PAGE_PLACE_ORDER_BTN = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # всплывающее окно с деталями ингредиента
    OF_ING_WINDOW = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    OF_ING_WINDOW_SECTION = (
        By.XPATH,
        "//h2[contains(text(), 'Детали ингредиента')]/parent::div/parent::div/parent::section"
    )
    OF_ING_SECTION = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    OF_CLOSE_BTN_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button")

    # Окно заказа
    ORDER_MODAL_WINDOW = (By.XPATH, "//p[text()='идентификатор заказа']/parent::div/parent::div/parent::section")
    MAIN_PAGE_ORDER_WINDOW = (By.XPATH, "//p[text()='идентификатор заказа']")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow')]")
    MODAL_OVERLAY = (
        By.XPATH,
        "//img[@alt='loading animation']/parent::div[contains(@class, 'Modal_modal_opened')]"
    )
    DEFAULT_ID = (By.XPATH, "//h2[contains(text(), '9999')]")
    FORMAT_ORDER_ID = "//p[contains(text(), '{num}')]/parent::div/parent::a"

