import data as dt
import allure

from pages.forgot_password_page import SiteNavigation
from helpers import helpers as hp
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.reset_password_page import ResetPasswordPage


class TestPersonalAccountPage:

    @allure.title("Проверяю переход по клику на Личный кабинет")
    def test_navigation_to_personal_account_page(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        expected_url = f"{dt.MAIN_PAGE_URL}{dt.ADDITIONAL_URLS.get('login_page')}"

        main_page.click_to_personal_account()

        assert main_page.get_current_url() == expected_url and login_page.is_enter_btn_clickable()
