import pytest
from learn_pytest.pages.search_page import SearchPage
from learn_pytest.pages.home_page import HomePage
from learn_pytest.config.config_reader import ConfigReader

def parse_prices(text):
    return float(text[:-4].replace(',', '.'))

def get_list_of_games(list_of_games):
    prices = [parse_prices(game.text) for game in list_of_games]
    sorted_prices = sorted(prices, reverse=True)
    error_text = ""

    if not prices == sorted_prices:
        error_text = (
            "Sorted wrong!\n"
            f"Actual order:   {prices}\n"
            f"Expected order: {sorted_prices}"
        )
    return prices == sorted_prices, error_text

@pytest.mark.parametrize("title, n", [("The Witcher", 10), ("Fallout", 20)])
def test_search_n_games(n, title, driver, wait):
    base_url = ConfigReader()
    driver.get(base_url.get_base_url())
    home_page = HomePage(driver)
    search_page = SearchPage(driver)

    home_page.wait_for_page_loading()
    home_page.click_on_search_field()
    home_page.input_request(title)
    home_page.click_searching_button(search_page)

    search_page.wait_for_page_loading()
    search_page.click_sort_dropdown()
    search_page.choose_option_price_desc()
    list_of_results = get_list_of_games(search_page.get_n_games(n))

    assert list_of_results[0], list_of_results[1]
