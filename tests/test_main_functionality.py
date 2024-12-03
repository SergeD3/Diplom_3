import time

import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.constructor_feed_page import ConstructorFeedPage


class TestMainFunctionality:

    @allure.title("Проверяю переход по клику на Конструктор")
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.click_to_personal_account_before_auth()
        main_page.click_on_constructor()

        assert main_page.is_constructor_active()

    @allure.title("Проверяю переход по клику на Ленту заказов")
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.click_to_personal_account_before_auth()
        main_page.click_on_order_feed()

        assert main_page.is_order_feed_active()

    @allure.title("Проверяю, что клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_on_ingredient_opens_ingredient_details_window(self, driver):
        main_page = MainPage(driver)
        constructor_feed = ConstructorFeedPage(driver)

        constructor_feed.click_on_ingredient()

        assert constructor_feed.ingredient_window_is_opened()

    @allure.title("Проверяю, что всплывающее окно закрывается при клике по крестику")
    def test_click_on_close_closes_detail_window(self, driver):
        main_page = MainPage(driver)
        constructor_feed = ConstructorFeedPage(driver)

        constructor_feed.click_on_ingredient()
        constructor_feed.click_on_close_button_detail_window()

        assert constructor_feed.ingredient_window_is_closed()

    @allure.title("Проверяю, что при добавлении ингредиента в заказ, увеличивается счётчик добавленного ингредиента")
    def test_adding_ingredient_increases_value_in_counter(self, driver):
        main_page = MainPage(driver)
        constructor_feed = ConstructorFeedPage(driver)
        counter_number = 0

        constructor_feed.add_ingredient_to_order()
        actual_result = int(constructor_feed.is_counter_increased())

        assert actual_result > counter_number

    @allure.title("Проверяю, что залогиненный пользователь может оформить заказ")
    def test_authorized_user_can_make_order(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        constructor_feed = ConstructorFeedPage(driver)
        login_page = LoginPage(driver)

        email = create_user_and_get_credentials.get('email')
        password = create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()
        constructor_feed.add_ingredients_to_order()
        constructor_feed.click_place_order_button()

        assert constructor_feed.order_window_is_displayed()
