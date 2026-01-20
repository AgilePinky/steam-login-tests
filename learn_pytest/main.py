import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_google_search():
    driver = webdriver.Chrome()

    driver.get("https://store.steampowered.com/")
    login_button = driver.find_element(By.XPATH, "//a[contains(@class, 'global_action_link')]")

    login_button.click()

    login_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@data-featuretarget, 'login')]//input[contains(@type, 'text')]")))
    password_field = driver.find_element(By.XPATH, "//input[contains(@type, 'password')]")
    enter_button = driver.find_element(By.XPATH, "//div[contains(@class, '_16fbihk6Bi9CXuksG7_tLt')]//button[contains(@type, 'submit')]")

    login_field.click()
    login_field.send_keys("sdfgsdfg")
    password_field.click()
    password_field.send_keys("hgfhdg")
    enter_button.click()

    error_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, '_1W_6HXiG4JJ0By1qN_0fGZ')]")))

    assert error_element.is_displayed()
    driver.quit()