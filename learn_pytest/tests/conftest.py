import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from learn_pytest.config.config_reader import ConfigReader
from driver_singleton import Driver

@pytest.fixture(scope="function")
def driver():
    driver = Driver()
    driver.restart()
    yield driver.get_driver()
    driver.quit()

@pytest.fixture
def wait(driver):
    timeout_conf = ConfigReader()
    return WebDriverWait(driver, timeout_conf.get_timeout())

