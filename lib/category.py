import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class Category:
    def __init__(self, driver):
        self.driver = driver

    def select_shop_by_category(self):
        try:
            self.driver.find_element_by_id("nav-link-shopall").click()
            return True
        except NoSuchElementException as e:
            logging.error("Exception occured. {}".format(str(e)))
            return False

    def get_all_major_category(self):
        try:
            category_root_element = self.driver.find_element_by_id("shopAllLinks")
            all_major_category_elements = category_root_element.find_elements_by_xpath('.//h2[@class="popover-category-name"]')
            major_categories = [cat.text for cat in all_major_category_elements]
            return major_categories
        except NoSuchElementException as e:
            logging.error("Exception occured. {}".format(str(e)))
            return None

    def get_all_sub_categories(self):
        try:
            category_root_element = self.driver.find_element_by_id("shopAllLinks")
            all_sub_category_elements = category_root_element.find_elements_by_xpath('.//a[@class="nav_a"]')
            sub_categories = [cat.text for cat in all_sub_category_elements]
            return sub_categories
        except NoSuchElementException as e:
            logging.error("Exception occured. {}".format(str(e)))
            return None