import allure

from pages.base_page import BasePage


class SiteNavigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Сравнение текущего url и ожидаемого")
    def check_current_url(self, expected_url):
        current_url = self.get_current_url()
        result = current_url == expected_url

        return result

    @allure.step("Сравнение текста текущего заголовка формы и ожидаемого")
    def check_forgot_password_title(self):
        expected_result = "Восстановление пароля"
        self.basic_wait_element(self.fpp_locators.TITLE, by_visibility=True)
        text = self.get_text_from_element(self.fpp_locators.TITLE)

        return text == expected_result

    @allure.step("Заполняю поле Email")
    def set_email_field(self, email=''):
        self.basic_wait_element(self.fpp_locators.EMAIL_FIELD, by_clickable=True)
        self.add_text_to_element(locator=self.fpp_locators.EMAIL_FIELD, text=email)

    @allure.step("Проверяю значение в поле Email")
    def check_entered_email(self, expected_text):
        text = self.get_text_from_element(self.fpp_locators.EMAIL_FIELD)

        return text == expected_text

    @allure.step("Нажимаю кнопку Восстановить")
    def click_restore_btn(self):
        self.basic_wait_element(self.fpp_locators.RESTORE_BTN, by_clickable=True)
        element = self.find_element_by_locator(self.fpp_locators.RESTORE_BTN)
        self.click_on_element_js(element)

    @allure.step("Заполняю поле email и нажимаю кнопку Восстановить")
    def enter_email_and_click_restore_btn(self, expected_email):
        self.set_email_field(expected_email)
        self.click_restore_btn()
        self.basic_wait_element(self.rs_locators.SAVE_BTN, by_clickable=True)
