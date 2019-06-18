import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException


class Home:
    def __init__(self, driver):
        self.driver = driver

    def launch_store(self):
        """

        :return: None
        """
        try:
            self.driver.get("https://www.amazon.in/")
        except (TimeoutException, WebDriverException):
            logging.error("Exception occured")
            return False
        return True

    def login(self, un, pw, wait_time=30):
        """

        :return:
        """
        try:
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, 'nav-link-accountList'))).click()
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, 'ap_email'))).send_keys(un)
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, 'continue'))).click()

            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, 'ap_password'))).send_keys(pw)
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, 'signInSubmit'))).click()
            logging.info("LOGIN SUCCESSFUL")
        except NoSuchElementException:
            logging.error("Element not found.")
            return False
        return True
