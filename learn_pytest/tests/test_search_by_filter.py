import pytest
from pages.search_page import SearchPage
from pages.home_page import HomePage
from config.config_reader import ConfigReader


@pytest.mark.parametrize("title, n", [("The Witcher", 10), ("Fallout", 20)])
def test_search_n_games(n, title, driver):
    base_url = ConfigReader()
    driver.get(base_url.get_base_url())
    home_page = HomePage()
    search_page = SearchPage()

    home_page.wait_for_page_loading()
    home_page.click_on_search_field()
    home_page.input_request(title)
    home_page.click_searching_button()

    search_page.wait_for_page_loading()
    search_page.click_sort_dropdown()
    search_page.choose_option_price_desc()
    search_page.wait_until_load_elements()

    prices_of_games = search_page.get_n_games_prices(n)
    sorted_prices = sorted(prices_of_games, reverse=True)
    assert prices_of_games == sorted_prices, (f"Sorted wrong!\n "
                                              f"Actual order:   {prices_of_games}\n "
                                              f"Expected order: {sorted_prices}")
