import pytest
from utils.browser_setup import get_driver
from pages.home_page import HomePage
from pages.result_page import ResultPage

@pytest.fixture
def setup():
    driver = get_driver()
    driver.get("https://agrichain.com")
    yield driver
    driver.quit()

def test_longest_substring(setup):
    driver = setup
    home_page = HomePage(driver)
    result_page = ResultPage(driver)

    home_page.enter_string("abcabcbb")
    home_page.click_submit()
    
    assert result_page.get_result() == "3", "Test Failed: Expected output is 3"
