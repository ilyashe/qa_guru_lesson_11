import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(autouse=True)
def setting_browser():

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'  # вместо этой строки можно добавить другие опции
    browser.config.driver_options = driver_options

    yield
    browser.quit()
