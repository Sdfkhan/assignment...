from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import pytest


class TableSortSearchPage:
    URL = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
    SEARCH_BOX = (By.CSS_SELECTOR, "#example_filter input")
    TABLE_ROWS = (By.CSS_SELECTOR, "#example tbody tr")
    TOTAL_ENTRIES_TEXT = (By.ID, "example_info")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, query):
        search_box = self.driver.find_element(*self.SEARCH_BOX)
        search_box.clear()
        search_box.send_keys(query)

    def get_table_row_count(self):
        rows = self.driver.find_elements(*self.TABLE_ROWS)
        return len([row for row in rows if row.is_displayed()])

    def get_total_entries_text(self):
        return self.driver.find_element(*self.TOTAL_ENTRIES_TEXT).text
