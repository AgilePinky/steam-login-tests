import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

MAIN_URL = "https://store.steampowered.com/"
TIMEOUT = 10
fake = Faker()

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    LOGIN_FIELD = (By.XPATH,"//div[contains(@data-featuretarget, 'login')]//input[contains(@type, 'text')]")
    PASSWORD_FIELD = (By.XPATH,"//input[contains(@type, 'password')]")
    ENTER_BUTTON = (By.XPATH,"//div[contains(@class, '_16fbihk6Bi9CXuksG7_tLt')]//button[contains(@type, 'submit')]")
    ERROR_TEXT = (By.XPATH,"//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(0)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, TIMEOUT)

def wait_for_page_load(driver, wait):
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='global_header']")))

def test_sign_in(driver, wait):
    driver.get(MAIN_URL)
    wait_for_page_load(driver, wait)

    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()

    login_field = wait.until(EC.visibility_of_element_located(Locators.LOGIN_FIELD))
    password_field = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
    enter_button = wait.until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
    login_field.click()

    login_field.send_keys(fake.email())
    password_field.click()
    password_field.send_keys(fake.password())
    enter_button.click()

    error_element = wait.until(EC.visibility_of_element_located(Locators.ERROR_TEXT))

    assert error_element.text == fake.sentence()

    assert error_element.is_displayed(), "Сообщение об ошибке отображается"
    driver.quit()