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
