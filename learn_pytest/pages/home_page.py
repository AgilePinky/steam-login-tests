from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver=None, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    SEARCH_FIELD = (By.XPATH, "//input[contains(@type, 'text')]")
    SEARCHING_BUTTON = (By.XPATH, "//button[contains(@type, 'submit')]")
    GLOBAL_HEADER_ELEMENT = (By.XPATH, "//*[@id = 'global_header']")

    def wait_for_page_loading(self):
        self.wait.until(EC.visibility_of_element_located(self.GLOBAL_HEADER_ELEMENT))

    def click_on_search_field(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD)).click()

    def input_request(self, name_of_game):
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        search_field.clear()
        search_field.send_keys(name_of_game)

    def click_searching_button(self, searching_page):
        self.wait.until(EC.element_to_be_clickable(self.SEARCHING_BUTTON)).click()
        return searching_page
