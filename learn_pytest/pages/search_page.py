import time

from selenium.common import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_reader import ConfigReader
from tests.driver_singleton import Driver

class SearchPage:

    TRIGGER_FILTER_MENU = (By.XPATH, "//button[contains(@class, 'trigger')]")
    OPTION_PRICE_DESC = (By.ID, "Price_DESC")
    OPTIONS_MENU = (By.ID, "sort_by_droplist")
    ALL_GAMES_TITTLE = (By.XPATH, "//span[@class='title']")
    ALL_GAMES_PRICES = (By.XPATH, "//div[contains(@class, 'discount_final_price')]")
    DYNAMIC_SEARCHING_LABEL = (By.XPATH, "//div[contains(@class, 'tag_dynamic')]//span[contains(@class, 'label')]")
    DYNAMIC_SEARCHING_RESULTS = (By.ID, "search_results_filtered_warning_persistent")
    GLOBAL_HEADER_ELEMENT = (By.ID, "global_header")
    LIST_OF_SORTED_GAMES = (By.ID, "search_result_container")

    config_reader = ConfigReader()

    def __init__(self, timeout=config_reader.get_timeout()):
        self.driver = Driver()
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_text_match(self, current_locator, expected_text):
        def _predicate(driver):
            try:
                return EC.element_to_be_clickable(current_locator)(driver).text == expected_text
            except ElementNotVisibleException:
                return False
        return _predicate

    def wait_until_load_elements(self):
        def check_element_loaded(driver):
            element = self.wait.until(EC.presence_of_element_located(self.LIST_OF_SORTED_GAMES))
            style = element.get_attribute('style')
            opacity = element.value_of_css_property('opacity')

            if opacity != '0.5' and (not style or 'opacity: 0.5' not in style):
                return element
            return False
        return self.wait.until(check_element_loaded)

    def wait_for_page_loading(self):
        self.wait.until(EC.visibility_of_element_located(self.GLOBAL_HEADER_ELEMENT))

    def click_sort_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.TRIGGER_FILTER_MENU)).click()

    def choose_option_price_desc(self):
        self.wait.until(EC.visibility_of_element_located(self.OPTIONS_MENU))
        text_of_filter = self.wait.until(EC.element_to_be_clickable(self.OPTION_PRICE_DESC)).text
        self.wait.until(EC.element_to_be_clickable(self.OPTION_PRICE_DESC)).click()
        self.wait.until(self.wait_text_match(self.TRIGGER_FILTER_MENU, text_of_filter))

    def get_n_games(self, n=10):
        self.wait_for_page_loading()
        self.wait_until_load_elements()
        self.wait.until(EC.visibility_of_element_located(self.DYNAMIC_SEARCHING_RESULTS))
        # time.sleep(1)
        return self.wait.until(EC.presence_of_all_elements_located(self.ALL_GAMES_PRICES))[:n]
