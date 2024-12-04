import allure
import data as dt

from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаю на Личный кабинет после аутентификации")
    def click_to_personal_account_after_auth(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('account_profile')}"

        element = self.find_element_by_locator(self.mp_locators.MENU_PERSONAL_ACCOUNT_BTN)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("Нажимаю на Личный кабинет до аутентификации")
    def click_to_personal_account_before_auth(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('login_page')}"

        element = self.find_element_by_locator(self.mp_locators.MENU_PERSONAL_ACCOUNT_BTN)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("Проверяю, что нахожусь на главной странице")
    def is_main_page_opened(self):
        expected_url = f"{dt.MAIN_PAGE_URL}"
        actual_url = self.get_current_url()

        return actual_url == expected_url

    @allure.step("Ожидаю загрузки главной страницы")
    def wait_page_to_be_loaded(self):
        self.find_element_by_locator(self.mp_locators.MAIN_PAGE_HEADER)

    @allure.step("Нажимаю на Конструктор")
    def click_on_constructor(self):
        element = self.find_element_by_locator(self.mp_locators.MAIN_PAGE_CONSTRUCTOR)
        self.click_on_element_js(element)

    @allure.step("Проверяю активен ли Конструктор")
    def is_constructor_active(self):
        expected_text = "active"
        self.basic_wait_element(locator=self.mp_locators.MAIN_PAGE_CONSTRUCTOR, by_visibility=True)
        attr = self.get_element_attribute(locator=self.mp_locators.MAIN_PAGE_CONSTRUCTOR, attribute="class")

        return expected_text in attr

    @allure.step("Нажимаю на Ленту заказов")
    def click_on_order_feed(self):
        element = self.find_element_by_locator(self.mp_locators.MAIN_PAGE_ORDER_FEED)
        self.click_on_element_js(element)
        self.basic_wait_element(locator=self.of_locators.OF_ORDERS, by_presence=True)

    @allure.step("Проверяю активна ли Лента заказов")
    def is_order_feed_active(self):
        expected_text = "active"
        self.basic_wait_element(locator=self.mp_locators.MAIN_PAGE_ORDER_FEED, by_visibility=True)
        attr = self.get_element_attribute(locator=self.mp_locators.MAIN_PAGE_ORDER_FEED, attribute="class")

        return expected_text in attr
