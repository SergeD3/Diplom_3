import allure
import data as dt

from pages.base_page import BasePage


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверяю открыт ли Личный кабинет")
    def is_personal_account_opened(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('account_profile')}"
        actual_url = self.get_current_url()

        self.basic_wait_element(self.pa_locators.SAVE_BTN, by_clickable=True)

        return actual_url == expected_url

    @allure.step("Проверяю отображается ли текст подсказки на странице")
    def is_info_text_present(self):
        self.basic_wait_element(self.pa_locators.PA_INFO_TEXT, by_visibility=True)

        return self.find_element_by_locator(self.pa_locators.PA_INFO_TEXT)

    @allure.step("Проверяю открыта ли История заказов")
    def is_order_history_opened(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('order_history')}"
        current_url = self.get_current_url()

        return current_url == expected_url

    @allure.step("Нажимаю на кнопку История заказов")
    def click_to_order_history(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('order_history')}"

        self.basic_wait_element(self.pa_locators.ORDER_HISTORY, by_visibility=True)
        element = self.find_element_by_locator(locator=self.pa_locators.ORDER_HISTORY)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("Нажимаю на кнопку Выход")
    def click_logout(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('login_page')}"

        self.basic_wait_element(self.pa_locators.LOGOUT, by_visibility=True)
        element = self.find_element_by_locator(locator=self.pa_locators.LOGOUT)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("Проверяю, что определённый заказ есть в списке Истории заказов")
    def specific_order_in_order_history_is_displayed(self, locator):
        element = self.find_element_by_locator(locator)

        return element.is_displayed()
