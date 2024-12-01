import allure

from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.mp_locators = MainPageLocators()
        self.lp_locators = LoginPageLocators()
        self.fpp_locators = ForgotPasswordPageLocators()

