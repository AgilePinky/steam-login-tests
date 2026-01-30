from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import search_page

class HomePage:
    instance = None
    driver = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, driver=None):
        if self.driver is None and driver is not None:
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)
        elif HomePage.driver is not None:
            self.driver = driver
            self.wait = WebDriverWait(driver, 10)

    HOME_PAGE_URL = 'https://store.steampowered.com/'

    SEARCH_AREA = (By.XPATH, "//form[contains(@role, 'search')]//div//input")
    SEARCH_BUTTON = (By.XPATH, "//form[contains(@role, 'search')]//button")
    SORT_BY_TRIGGER = (By.XPATH, "//button[contains(@id, 'sort_by_trigger')]")
    HIGHLIGHTED_SELECTION = (By.XPATH, "//a[contains(@class, 'highlighted_selection')]")

    def open_page(self):
        self.driver.get(self.HOME_PAGE_URL)
        return self

    def click_search_area(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_AREA)).click()
        return self

    def enter_request(self, name_of_game):
        search_area = self.wait.until(EC.element_to_be_clickable(self.SEARCH_AREA))
        search_area.clear()
        search_area.send_keys(name_of_game)
        return self

    def click_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        return search_page.SearchPage(self.driver)

    def click_sort_by_trigger(self):
        self.wait.until(EC.element_to_be_clickable(self.SORT_BY_TRIGGER)).click()
        return self

    def choose_highlighted_selection(self):
        self.wait.until(EC.element_to_be_clickable(self.HIGHLIGHTED_SELECTION)).click()
        return self

    def get_game_list(self, quantity):
        for i in range(quantity):
            print