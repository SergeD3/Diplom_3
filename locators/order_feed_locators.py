from selenium.webdriver.common.by import By


class OrderFeedLocators:
    OF_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    OF_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    OF_RANDOM_ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]/a")

    OF_ORDER_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2")
    DONE_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number') and starts-with(text(), '16')]")
    DONE_COUNTERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number')]")

    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")

