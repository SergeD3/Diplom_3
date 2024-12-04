import allure

from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаю на кнопку показать/скрыть пароль")
    def click_eye_password_field(self):
        self.basic_wait_element(self.rs_locators.PASSWORD_FIELD)
        element = self.find_element_by_locator(self.rs_locators.EYE_BTN)
        self.click_on_element_js(element)

    @allure.step("Проверяю, что поле стало активным")
    def is_password_field_active(self):
        expected_value = 'text'
        expected_attr = 'type'
        value = self.get_element_attribute(self.rs_locators.PASSWORD_FIELD, expected_attr)

        return value == expected_value
