import time

import data as dt
import allure

from pages.forgot_password_page import SiteNavigation
from helpers import helpers as hp
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from pages.reset_password_page import ResetPasswordPage


class TestPersonalAccountPage:

    @allure.title("Проверяю переход по клику на Личный кабинет")
    def test_navigation_to_personal_account_page(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_acc_page = PersonalAccountPage(driver)

        email = create_user_and_get_credentials.get('email')
        password = create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()
        main_page.click_to_personal_account_after_auth()

        assert personal_acc_page.is_personal_account_opened()

    @allure.title("Проверяю переход в раздел «История заказов»")
    def test_navigation_to_order_history(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_acc_page = PersonalAccountPage(driver)

        email = create_user_and_get_credentials.get('email')
        password = create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()
        main_page.click_to_personal_account_after_auth()
        personal_acc_page.click_to_order_history()

        assert personal_acc_page.is_order_history_opened()

    @allure.title("Проверяю выход из аккаунта")
    def test_logout(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        personal_acc_page = PersonalAccountPage(driver)

        email = create_user_and_get_credentials.get('email')
        password = create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()
        main_page.click_to_personal_account_after_auth()
        personal_acc_page.click_logout()

        assert login_page.is_login_page_opened()
