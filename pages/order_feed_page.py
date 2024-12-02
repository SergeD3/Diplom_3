import allure
import data as dt

from pages.base_page import BasePage


class OrderFeedPage(BasePage):

    @allure.step("Нажимаю на ингредиент")
    def click_on_ingredient(self):
        expected_url = f"{dt.MAIN_PAGE_URL}ingredient/61c0c5a71d1f82001bdaaa72"

        element = self.find_element_by_locator(self.of_locators.MAIN_PAGE_SINGLE_ING)
        self.click_on_element_js(element)
        self.wait_for_url_to_be(expected_url)

    @allure.step("")
    def is_ingredient_window_opened(self):
        self.basic_wait_element(self.of_locators.OF_ING_WINDOW, by_visibility=True)
        self.basic_switch_to_opened_window()

        return self.find_element_by_locator(self.of_locators.OF_ING_WINDOW)
