import allure

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаю на Восстановить пароль")
    def click_to_forgot_password(self):
        element = self.find_element_by_locator(self.lp_locators.FORGOT_PASSWORD_BTN)
        self.basic_wait_element(self.lp_locators.FORGOT_PASSWORD_BTN, by_visibility=True)
        self.click_on_element_js(element)

    @allure.step("Проверяю отрисовалась и кликабельна ли кнопка Войти")
    def is_enter_btn_clickable(self):
        expected_text = 'Войти'
        self.basic_wait_element(self.lp_locators.SAVE_BTN, by_clickable=True)

        return self.check_element_text(locator=self.lp_locators.SAVE_BTN, text=expected_text)