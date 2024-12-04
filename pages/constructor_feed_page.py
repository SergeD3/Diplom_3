import allure
import data as dt

from pages.base_page import BasePage


class ConstructorFeedPage(BasePage):

    @allure.step("Нажимаю на ингредиент")
    def click_on_ingredient(self):
        expected_url = f"{dt.MAIN_PAGE_URL}ingredient/61c0c5a71d1f82001bdaaa72"

        element = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_SAUCE_ING)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("Нажимаю на крестик в модальном окне")
    def click_on_close_button_detail_window(self):
        element = self.find_element_by_locator(self.cf_locators.OF_CLOSE_BTN_WINDOW)
        self.click_on_element_js(element)

    @allure.step("Нажмаю на кнопку Оформить заказ")
    def click_place_order_button(self):
        self.basic_wait_element(locator=self.cf_locators.MAIN_PAGE_PLACE_ORDER_BTN, by_clickable=True)

        element = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_PLACE_ORDER_BTN)
        self.click_on_element_js(element)

    @allure.step("Добавляю ингредиент в заказ")
    def add_ingredient_to_order(self):
        source = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_SAUCE_ING)
        target = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_BASKET)

        self.move_elements(source=source, target=target)

    @allure.step("Добавляю несколько ингредиентов в заказ")
    def add_ingredients_to_order(self):
        source = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_SAUCE_ING)
        target = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_BASKET)
        self.move_elements(source=source, target=target)

        source_2 = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_BUN)
        self.move_elements(source=source_2, target=target)

    @allure.step("Проверяю увеличилось ли значение в счетчике ингредиента")
    def is_counter_increased(self):
        text = self.get_text_from_element(self.cf_locators.MAIN_PAGE_ING_COUNTER)

        return int(text)

    @allure.step("Проверяю открыто ли всплывающее окно с деталями ингредиента")
    def ingredient_window_is_opened(self):
        self.find_element_by_locator(self.cf_locators.OF_ING_WINDOW)

        return self.find_element_by_locator(self.cf_locators.OF_ING_WINDOW).is_displayed()

    @allure.step("Проверяю закрыто ли всплывающее окно с деталями ингредиента")
    def ingredient_window_is_closed(self):
        attr = "class"
        expected_value = "Modal_modal_opened"

        attr_first_section = self.get_element_attribute(locator=self.cf_locators.OF_ING_WINDOW, attribute=attr)

        return expected_value not in attr_first_section

    @allure.step("Проверяю открыто ли окно заказа")
    def order_window_is_displayed(self):
        self.basic_wait_until_not_visibility(self.cf_locators.MODAL_OVERLAY)
        element = self.find_element_by_locator(self.cf_locators.MAIN_PAGE_ORDER_WINDOW)

        return element.is_displayed()

    # все эти ожидания в основном нужны для FF
    # решение может и костыльное, но оно значительно повысило стабильность тестов в FF
    @allure.step("Беру номер заказа из всплывающего окна")
    def get_order_number(self):
        self.basic_wait_element(self.cf_locators.ORDER_MODAL_WINDOW, by_presence=True)
        self.basic_wait_until_not_visibility(self.cf_locators.MODAL_OVERLAY)
        self.basic_wait_until_not_visibility(self.cf_locators.DEFAULT_ID)
        self.basic_wait_element(self.cf_locators.OF_CLOSE_BTN_WINDOW, by_clickable=True)

        full_number = f"#0{self.get_text_from_element(self.cf_locators.ORDER_ID)}"
        just_number = self.get_text_from_element(self.cf_locators.ORDER_ID)

        return full_number, just_number
