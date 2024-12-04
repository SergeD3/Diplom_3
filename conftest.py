import pytest
import data
import json
import requests

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
def create_user_and_get_credentials():
    payload = hp.get_random_user_credentials()
    created_response = requests.post(
        url=f"{data.MAIN_PAGE_URL}{data.USER_REGISTRATION_PATH}",
        headers=data.COMMON_HEADERS,
        json=payload
    )
    assert created_response.ok, "Ошибка создания пользователя"

    yield payload

    access_token = created_response.json()['accessToken']
    headers = {'Authorization': access_token}

    requests.delete(
        url=f"{data.MAIN_PAGE_URL}{data.USER_EDIT_PATH}",
        headers=headers
    )
