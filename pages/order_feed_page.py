import allure
import data as dt

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderFeedPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаю на заказ")
    def click_on_order(self):
        self.basic_wait_element(self.of_locators.OF_ORDERS, by_visibility=True)
        element = self.find_element_by_locator(self.of_locators.OF_RANDOM_ORDER)
        self.click_on_element_js(element)

    @allure.step("Проверяю, что карточка заказа открыта")
    def order_window_is_opened(self):
        element = self.find_element_by_locator(self.of_locators.OF_ORDER_TITLE)

        return element.is_displayed()

    @allure.step("Изменяю локатор с учётом его номера")
    def get_formated_order_locator(self, order_number):
        order_locator = self.cf_locators.FORMAT_ORDER_ID
        new_locator = order_locator.format(num=order_number)

        return By.XPATH, new_locator

    @allure.step("Прокручиваю страницу до нужного заказа")
    def scroll_to_specific_order(self, order_number):
        self.basic_wait_element(self.of_locators.OF_ORDERS_LIST, by_visibility=True)
        new_order_locator = self.get_formated_order_locator(order_number)
        self.scroll_to_element(new_order_locator)

        return new_order_locator

    @allure.title("Получаю список заказов в Ленте заказов")
    def get_orders(self):
        self.basic_wait_element(self.of_locators.OF_ORDERS_LIST, by_visibility=True)
        elements = self.find_elements(self.of_locators.OF_ORDERS_LIST)

        return elements

    @allure.step("Проверяю, что в списке заказов есть определённый заказ")
    def specific_order_in_order_feed_is_displayed(self, order_number):
        new_order_locator = self.get_formated_order_locator(order_number)
        self.scroll_to_specific_order(order_number)
        element = self.find_element_by_locator(new_order_locator)

        return element.is_displayed()

    @allure.step("Получение текущего значения счетчика Выполнено за всё время")
    def get_done_all_time_counter_value(self):
        self.basic_wait_element(self.of_locators.DONE_COUNTER, by_visibility=True)
        number = self.get_text_from_element(self.of_locators.DONE_COUNTER)

        return int(number)

    @allure.step("Получение текущего значения счетчика Выполнено за сегодня")
    def get_done_today_counter_value(self):
        self.basic_wait_element(self.of_locators.DONE_COUNTERS, by_visibility=True)
        number = self.find_elements(self.of_locators.DONE_COUNTERS)[1].text

        return number

