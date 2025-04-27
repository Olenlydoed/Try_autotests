from pages.homepage import HomePage
from pages.product import ProductPage
from conftest import browser


def test_open_s6(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(browser)
    product_page.check_title_is("Samsung galaxy s6")

def test_two_monitors(browser):
    homepage = HomePage(browser)
    homepage.open()
    homepage.click_monitor()
    homepage.check_products_count(2)