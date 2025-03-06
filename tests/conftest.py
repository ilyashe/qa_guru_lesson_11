import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach
from dotenv import load_dotenv
import os


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()

selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")

@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'  # вместо этой строки можно добавить другие опции
    browser.config.driver_options = driver_options
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options)

    browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser, selenoid_url)

    browser.quit()
