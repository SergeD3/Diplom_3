import pytest
import data

from selenium import webdriver


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        data.DRIVER_NAME = 'chrome'
        driver = webdriver.Chrome()
    else:
        data.DRIVER_NAME = 'firefox'
        driver = webdriver.Firefox()

    driver.set_window_size(1920, 1080)
    driver.get(data.MAIN_PAGE_URL)

    yield driver
    driver.quit()
