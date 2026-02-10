import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from config.config_reader import ConfigReader
from tests.driver_singleton import Driver

@pytest.fixture(scope="function")
def driver():
    driver = Driver()
    yield driver
    Driver.quit()

# @pytest.fixture
# def wait(driver):
#     timeout_conf = ConfigReader()
#     return WebDriverWait(driver, timeout_conf.get_timeout())

