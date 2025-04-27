from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self):
        self.browser.get('https://www.demoblaze.com/')

    def click_galaxy_s6(self):
        galaxy_s6 = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Samsung galaxy s6"]'))
        )
        galaxy_s6.click()

    def click_monitor(self):
        monitor_link = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '''[onclick="byCat('monitor')"]'''))
        )
        monitor_link.click()

    def check_products_count(self, count):
        WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[text()="Apple monitor 24"]'))
        )
        monitors = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".card-title"))
        )
        assert len(monitors) == count

