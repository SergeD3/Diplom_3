import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


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
        order_feed = OrderFeedPage(driver)

        order_feed.click_on_ingredient()
        assert order_feed.is_ingredient_window_opened()

