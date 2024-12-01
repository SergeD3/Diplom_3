import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажимаю на Личный кабинет")
    def click_to_personal_account(self):
        element = self.find_element_by_locator(self.mp_locators.MENU_PERSONAL_ACCOUNT_BUTTON)
        self.click_on_element_js(element)

