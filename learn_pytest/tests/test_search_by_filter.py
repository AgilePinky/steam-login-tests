import pytest
from learn_pytest.pages.search_page import SearchPage
from learn_pytest.pages.home_page import HomePage
from learn_pytest.config.config_reader import ConfigReader

def get_list_of_games(list_of_games):
    print()
    for i in list_of_games:
        print(i.text[:-4])
    print()

    is_ordering_correctly = True
    biggest_price = 100000
    error_text = ''
    biggest_price_number = -1

    for i in list_of_games:
        if biggest_price >= float(i.text[:-4].replace(',', '.')):
            biggest_price = float(i.text[:-4].replace(',', '.'))
            biggest_price_number += 1
        else:
            error_text = (f"Sorted wrong!\n"
                            f"Expected that price at position {biggest_price_number}( eq {biggest_price}) in list will bigger than {float(i.text[:-4].replace(',', '.'))}\n"
                            f"But actually {float(i.text[:-4].replace(',', '.'))} is bigger than {biggest_price}")
            is_ordering_correctly = False
            break
    print()
    return [is_ordering_correctly, error_text]

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
