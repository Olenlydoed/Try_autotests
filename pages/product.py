from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    def __init__(self, browser):
        self.browser = browser

    def check_title_is(self, title):
        page_title = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h2'))
        )
        assert page_title.text == title
