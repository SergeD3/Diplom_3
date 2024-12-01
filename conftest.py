import pytest
import data
import json
import requests as req

from selenium import webdriver
from helpers import helpers as hp


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


@pytest.fixture
def create_user_api():
    creds = hp.get_random_user_credentials()
    creds_json = json.dumps(creds)
    response = req.post(
        url=f"{data.MAIN_PAGE_URL}{data.USER_REGISTRATION_PATH}",
        headers=data.COMMON_HEADERS,
        data=creds_json
    )

    assert response.ok, f"Ошибка: {response.status_code} : {response.text}"

    return creds
