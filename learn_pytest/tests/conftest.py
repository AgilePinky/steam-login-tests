import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from learn_pytest.config.config_reader import ConfigReader

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    timeout_conf = ConfigReader()
    return WebDriverWait(driver, timeout_conf.get_timeout())

