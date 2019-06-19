import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class Search:
    def __init__(self,driver):
        self.driver = driver

    def search_by_keyword(self,search_input):
        """

        :param search_input:
        :return: search result selenium object
        """
        try:
            element = self.driver.find_element_by_id("twotabsearchtextbox")
            element.send_keys(search_input)
            element.send_keys(Keys.ENTER)
            search_product = self.driver.find_elements_by_xpath('//div[@class="s-result-list s-search-results sg-row"]/*')
            return search_product
        except NoSuchElementException as e:
            logging.error("Exception occured. {}".format(str(e)))
            return []


    def get_search_product_title(self,search_input):
        """

        :param search_input:
        :return:
        """
        product_list = self.search_by_keyword(search_input)
        product_title_list = [item.find_element_by_xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]').text for item in
         product_list]
        return product_title_list