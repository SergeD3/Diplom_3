import data as dt
import allure

from pages.forgot_password_page import SiteNavigation
from helpers import helpers as hp
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestNavigation:

    @allure.title("Проверяю переход на страницу восстановления пароля по кнопке Восстановить пароль")
    def test_password_reset_page_via_personal_account(self, driver):
        nav = SiteNavigation(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('forgot_password')}"

        main_page.click_to_personal_account()
        login_page.click_to_forgot_password()

        assert nav.check_current_url(expected_url) and nav.check_forgot_password_title()

    @allure.title("Проверяю переход на страницу сброса пароля после ввода emain и нажатия кнопки Восстановить")
    def test_enter_email_click_restore_password(self, driver):
        nav = SiteNavigation(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        expected_value = hp.get_random_email()
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('reset_password')}"

        main_page.click_to_personal_account()
        login_page.click_to_forgot_password()
        nav.enter_email_and_click_restore_btn(expected_value)

        assert nav.check_current_url(expected_url)

    @allure.title("Проверяю, что клик по глазу показывает или скрывает пароль и делает поле активным")
    def test_show_hide_password(self, driver):
        nav = SiteNavigation(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        repass = ResetPasswordPage(driver)

        expected_value = hp.get_random_email()

        main_page.click_to_personal_account()
        login_page.click_to_forgot_password()
        nav.enter_email_and_click_restore_btn(expected_value)
        repass.click_eye_password_field()

        assert repass.is_password_field_active()
