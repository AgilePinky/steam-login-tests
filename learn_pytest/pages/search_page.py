from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver=None, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)

    def wait_text_match(self, current_locator, expected_text):
        def _predicate(driver):
            try:
                return EC.element_to_be_clickable(current_locator)(driver).text == expected_text
            except Exception:
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

    TRIGGER_FILTER_MENU = (By.XPATH, "//button[contains(@class, 'trigger')]")
    OPTION_PRICE_DESC = (By.XPATH, "//*[@id = 'Price_DESC']")
    OPTIONS_MENU = (By.XPATH, "//*[@id = 'sort_by_droplist']")
    ALL_GAMES_TITTLE = (By.XPATH, "//span[@class='title']")
    ALL_GAMES_PRICES = (By.XPATH, "//div[contains(@class, 'discount_final_price')]")
    DYNAMIC_SEARCHING_LABEL = (By.XPATH, "//div[contains(@class, 'tag_dynamic')]//span[contains(@class, 'label')]")
    DYNAMIC_SEARCHING_RESULTS = (By.XPATH, "//*[@id = 'search_results_filtered_warning_persistent']")
    GLOBAL_HEADER_ELEMENT = (By.XPATH, "//*[@id = 'global_header']")
    LIST_OF_SORTED_GAMES = (By.XPATH, "//*[@id = 'search_result_container']")

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
        self.wait_until_load_elements()
        self.wait_for_page_loading()
        self.wait.until(EC.visibility_of_element_located(self.DYNAMIC_SEARCHING_RESULTS))
        return self.wait.until(EC.presence_of_all_elements_located(self.ALL_GAMES_PRICES))[:n]
