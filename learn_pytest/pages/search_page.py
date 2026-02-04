from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver=None, timeout=10):
        if not hasattr(self, 'driver') or driver is not None:
            self.driver = driver
            self.wait = WebDriverWait(self.driver, timeout) if driver else None

    TRIGGER_FILTER_MENU = (By.XPATH, "//button[contains(@class, 'trigger')]")
    OPTION_PRICE_DESK = (By.XPATH, "//a[contains(@id, 'Price_DESC')]")
    OPTIONS_MENU = (By.XPATH, "//ul[contains(@id, 'sort_by_droplist')]")
    ALL_GAMES = (By.XPATH, "//span[@class='title']")
    DYNAMIC_SEARCHING_LABEL = (By.XPATH, "//div[contains(@class, 'tag_dynamic')]//span[contains(@class, 'label')]")
    DYNAMIC_SEARCHING_RESULTS = (By.XPATH, "//div[contains(@id, 'search_results_filtered_warning_persistent')]")

    def click_sort_dropdown(self):
        self.wait.until(EC.element_to_be_clickable(self.TRIGGER_FILTER_MENU)).click()
        return self

    def choose_option_price_desc(self):
        self.wait.until(EC.visibility_of_element_located(self.OPTIONS_MENU))
        self.wait.until(EC.element_to_be_clickable(self.OPTION_PRICE_DESK)).click()
        return self

    def get_n_games(self, n=10):
        self.wait.until(EC.visibility_of_element_located(self.DYNAMIC_SEARCHING_RESULTS))
        self.wait.until(EC.element_to_be_clickable(self.ALL_GAMES))
        n_games = self.wait.until(EC.presence_of_all_elements_located(self.ALL_GAMES))[:n]
        return n_games
