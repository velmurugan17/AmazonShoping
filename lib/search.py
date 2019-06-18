import logging
from selenium.common.exceptions import WebDriverException,NoSuchElementException,TimeoutException


class Search:
    def __init__(self,driver):
        self.driver = driver

    def search_by_keyword(self,search_input):
        """

        :param search_input:
        :return:
        """
        try:
            self.driver.get("https://www.amazon.in/")
        except (TimeoutException,WebDriverException):
            logging.error("Exception occured")

