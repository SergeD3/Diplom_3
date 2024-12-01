from selenium.webdriver.common.by import By


class MainPageLocators:
    # элементы основной страницы сайта
    MAIN_PAGE_LOG_IN_BUTTON = (
        By.XPATH,
        '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button[contains(text(), "Войти в аккаунт")]'
    )  # кнопка Войти в аккаунт
    MAIN_PAGE_PLACE_ORDER_BUTTON = (
        By.XPATH, '//div[@class="BurgerConstructor_basket__container__2fUl3 mt-10"]/button[text()="Оформить заказ"]'
    )  # кнопка Оформить заказ
    MAIN_PAGE_BURGER_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')  # заголовок конструктора

    MENU_PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH,
        '//nav/a/p[@class="AppHeader_header__linkText__3q_va ml-2"]'
    )  # кнопка меню Личный кабинет
