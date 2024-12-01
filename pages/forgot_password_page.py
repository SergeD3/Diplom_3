import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class SiteNavigation(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.mp_locators = MainPageLocators()
        self.lp_locators = LoginPageLocators()
        self.fpp_locators = ForgotPasswordPageLocators()
        self.rs_locators = ResetPasswordPageLocators()

    @allure.step("Нажимаю на Личный кабинет")
    def click_to_personal_account(self):
        element = self.find_element_by_locator(self.mp_locators.MENU_PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element_js(element)

    @allure.step("Нажимаю на Восстановить пароль")
    def click_to_forgot_password(self):
        element = self.find_element_by_locator(self.lp_locators.FORGOT_PASSWORD_BTN)
        self.basic_wait_element(self.lp_locators.FORGOT_PASSWORD_BTN, by_visibility=True)
        self.click_on_element_js(element)

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
        # Вызвать метод клика и нажать на кнопку "Личный кабинет"
        self.click_to_personal_account()
        # Дождаться кликабельности кнопки "Восстановить пароль"
        # Вызвать метод клика и нажать на кнопку "Восстановить пароль"
        self.click_to_forgot_password()
        # Вызвать метод заполнения поля Email
        self.set_email_field(expected_email)
        # Вызвать метод нажатия на кнопку "Восстановить"
        self.click_restore_btn()
        # Дождаться загрузки страницы сброса пароля
        self.basic_wait_element(self.rs_locators.SAVE_BTN, by_clickable=True)

    @allure.step("Нажимаю на кнопку показать/скрыть пароль")
    def click_eye_password_field(self):
        self.basic_wait_element(self.rs_locators.PASSWORD_FIELD)
        element = self.find_element_by_locator(self.rs_locators.EYE_BTN)
        self.click_on_element_js(element)

    @allure.step("")
    def click_eye_make_password_field_active(self):
        self.click_eye_password_field()

