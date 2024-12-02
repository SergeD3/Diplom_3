import allure

import data as dt

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверяю, что открыта страница аутентификации")
    def is_login_page_opened(self):
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('login_page')}"
        actual_url = self.get_current_url()

        return actual_url == expected_url

    @allure.step("Нажимаю на Восстановить пароль")
    def click_to_forgot_password(self):
        element = self.find_element_by_locator(self.lp_locators.FORGOT_PASSWORD_BTN)
        self.basic_wait_element(self.lp_locators.FORGOT_PASSWORD_BTN, by_visibility=True)
        self.click_on_element_js(element)

    @allure.step("Заполняю поле Email")
    def fill_email(self, email):
        self.basic_wait_element(locator=self.lp_locators.LP_EMAIL_FIELD, by_clickable=True)
        self.add_text_to_element(locator=self.lp_locators.LP_EMAIL_FIELD, text=email)

    @allure.step("Заполняю поле Пароль")
    def fill_password(self, password):
        self.basic_wait_element(locator=self.lp_locators.LP_PASSWORD_FIELD, by_clickable=True)
        self.add_text_to_element(locator=self.lp_locators.LP_PASSWORD_FIELD, text=password)

    @allure.step("Нажимаю на кнопку Войти")
    def click_enter_btn(self):
        self.basic_wait_element(self.lp_locators.ENTER_BTN, by_visibility=True)
        element = self.find_element_by_locator(locator=self.lp_locators.ENTER_BTN)
        self.click_on_element_js(element)

    @allure.step("Заполняю поля на форме аутентификации")
    def form_field_filling(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_enter_btn()
