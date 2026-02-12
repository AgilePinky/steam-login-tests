from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader
from tests.driver_singleton import Driver


class HomePage:
    SEARCH_FIELD = (By.XPATH, "//input[contains(@type, 'text')]")
    SEARCHING_BUTTON = (By.XPATH, "//button[contains(@type, 'submit')]")
    GLOBAL_HEADER_ELEMENT = (By.ID, "global_header")

    config_reader = ConfigReader()

    def __init__(self, timeout=config_reader.get_timeout(),
                 poll_frequency=config_reader.get_poll_frequency()):
        self.driver = Driver()
        self.wait = WebDriverWait(self.driver, timeout, poll_frequency)

    def wait_for_page_loading(self):
        self.wait.until(EC.visibility_of_element_located(self.GLOBAL_HEADER_ELEMENT))

    def click_on_search_field(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD)).click()

    def input_request(self, name_of_game):
        search_field = self.wait.until(EC.element_to_be_clickable(self.SEARCH_FIELD))
        search_field.clear()
        search_field.send_keys(name_of_game)

    def click_searching_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCHING_BUTTON)).click()
