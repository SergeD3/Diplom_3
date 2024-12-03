import time

import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.constructor_feed_page import ConstructorFeedPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeedPage:

    @allure.title("Проверяю, что при клике на заказ открывается окно с деталями заказа")
    def test_click_on_order_opens_order_window(self, driver):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)

        main_page.click_on_order_feed()
        order_page.click_on_order()

        assert order_page.order_window_is_opened()

    @allure.title("Проверяю, что заказ из истории заказов отображается на странице Ленты заказов")
    def test_order_from_users_history_is_in_order_feed(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        personal_acc_page = PersonalAccountPage(driver)
        login_page = LoginPage(driver)
        constructor_feed_page = ConstructorFeedPage(driver)
        email, password = create_user_and_get_credentials.get('email'), create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()

        constructor_feed_page.add_ingredients_to_order()
        constructor_feed_page.click_place_order_button()
        main_page.click_on_order_feed()
        order_number = constructor_feed_page.get_order_number()[0]
        new_locator = order_page.get_formated_order_locator(order_number)
        constructor_feed_page.click_on_close_button_detail_window()
        spec_order_in_order_feed = order_page.specific_order_in_order_feed_is_displayed(order_number)

        main_page.click_to_personal_account_after_auth()
        personal_acc_page.click_to_order_history()
        spec_order_in_history = personal_acc_page.specific_order_in_order_history_is_displayed(new_locator)

        assert spec_order_in_order_feed and spec_order_in_history

    @allure.title("Проверяю, что при создании нового заказа значение в счетчике Выполнено за всё время увеличивается")
    def test_creating_order_increases_done_all_time_counter(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_feed_page = ConstructorFeedPage(driver)
        email, password = create_user_and_get_credentials.get('email'), create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()

        main_page.click_on_order_feed()
        before = order_page.get_done_all_time_counter_value()
        main_page.click_on_constructor()
        constructor_feed_page.add_ingredients_to_order()
        constructor_feed_page.click_place_order_button()
        constructor_feed_page.click_on_close_button_detail_window()

        main_page.click_on_order_feed()
        after = order_page.get_done_all_time_counter_value()

        assert after > before

    @allure.title(""
                  "Проверяю, что при создании нового заказа значение в счетчике Выполнено за сегодня увеличивается"
                  )
    def test_creating_order_increases_done_today_counter(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_feed_page = ConstructorFeedPage(driver)
        email, password = create_user_and_get_credentials.get('email'), create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()

        main_page.click_on_order_feed()
        before = order_page.get_done_today_counter_value()
        main_page.click_on_constructor()
        constructor_feed_page.add_ingredients_to_order()
        constructor_feed_page.click_place_order_button()
        constructor_feed_page.click_on_close_button_detail_window()

        main_page.click_on_order_feed()
        after = order_page.get_done_today_counter_value()

        assert after > before

    @allure.title("Проверяю, что после оформления заказа его номер появляется в разделе В работе.")
    def test_after_creating_order_it_number_is_in_progress_section(self, driver, create_user_and_get_credentials):
        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        login_page = LoginPage(driver)
        constructor_feed_page = ConstructorFeedPage(driver)
        email, password = create_user_and_get_credentials.get('email'), create_user_and_get_credentials.get('password')

        main_page.click_to_personal_account_before_auth()
        login_page.form_field_filling(email=email, password=password)
        main_page.wait_page_to_be_loaded()

        constructor_feed_page.add_ingredients_to_order()
        constructor_feed_page.click_place_order_button()
        order_number = constructor_feed_page.get_order_number()[1]
        constructor_feed_page.click_on_close_button_detail_window()
