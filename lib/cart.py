import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class Cart:
    def __init__(self,driver):
        self.driver = driver

    def add_product_to_cart(self,count):
        pass

    def remove_product_from_cart(self):
        pass

    def clear_cart(self):
        pass