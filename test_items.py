# test_items.py

import time
import selenium
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

class TestProduct():
    
    def test_button_submit(self, browser):
        browser.get(link)
        time.sleep(5)
        # time.sleep(30)
        # submit = browser.find_element(By.CSS_SELECTOR, ".product_page button[type='submit']")
        try:
            browser.find_element(By.CSS_SELECTOR, ".product_page button[type='submit']")
        except selenium.common.exceptions.NoSuchElementException:
            raise AssertionError('Button not found')