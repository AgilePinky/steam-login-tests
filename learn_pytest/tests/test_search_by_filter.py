import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as  EC
from learn_pytest.pages.search_page import SearchPage
from learn_pytest.pages.home_page import HomePage

HOME_PAGE_URL = 'https://store.steampowered.com'
SEARCH_PAGE_URL = 'https://store.steampowered.com/search'
TIMEOUT = 10
LIST_WITH_N_GAMES = 10

class Locators:
    GLOBAL_HEADER_ELEMENT = (By.XPATH, "//div[contains(@id, 'global_header')]")

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, TIMEOUT)

@pytest.mark.parametrize("title, n", [("The Witcher", 10), ("Fallout", 20)])
def test_search_n_games(n, title, driver, wait):
    driver.get(HOME_PAGE_URL)
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    wait.until(EC.visibility_of_element_located(Locators.GLOBAL_HEADER_ELEMENT))
    home_page.click_on_search_field()
    home_page.input_request(title)
    home_page.click_searching_button(search_page)

    search_page.click_sort_dropdown()
    search_page.choose_option_price_desc()
    list_of_games = search_page.get_n_games(n)

    print()
    for i in list_of_games:
        print(i.text)
    print()

    list_of_games = []