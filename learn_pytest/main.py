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
    PAGE = (By.XPATH, "//div[@id='global_header']")
    LOGIN_BUTTON = (By.XPATH, "//a[contains(@class, 'global_action_link')]")
    LOGIN_FIELD = (By.XPATH,"//div[contains(@data-featuretarget, 'login')]//input[contains(@type, 'text')]")
    PASSWORD_FIELD = (By.XPATH,"//input[contains(@type, 'password')]")
    ENTER_BUTTON = (By.XPATH,"//div[contains(@class, 'login_featuretarget_ctn')]//button")
    ERROR_TEXT = (By.XPATH,"//div[contains(@class, 'login_featuretarget_ctn')]//form//div[5]")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, TIMEOUT)

def test_sign_in(driver, wait):
    driver.get(MAIN_URL)
    wait.until(EC.presence_of_element_located(Locators.PAGE))

    login_button = wait.until(EC.element_to_be_clickable(Locators.LOGIN_BUTTON))
    login_button.click()
    wait.until(EC.presence_of_element_located(Locators.PAGE))

    login_field = wait.until(EC.visibility_of_element_located(Locators.LOGIN_FIELD))
    login_field.click()
    login_field.send_keys(fake.email())

    password_field = wait.until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
    password_field.click()
    password_field.send_keys(fake.password())

    enter_button = wait.until(EC.element_to_be_clickable(Locators.ENTER_BUTTON))
    enter_button.click()

    wait.until(EC.text_to_be_present_in_element(Locators.ERROR_TEXT, 'П'))
    error_element = wait.until(EC.visibility_of_element_located(Locators.ERROR_TEXT))
    expected_text = 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.'

    assert error_element.text == expected_text, "Сообщение об ошибке отображается"