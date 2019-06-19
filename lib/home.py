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
        except (TimeoutException, WebDriverException) as e:
            logging.error("Exception occured : {}".format(str(e)))
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
            login_title = self.driver.title
            if "Amazon" in login_title:
                logging.info("LOGIN SUCCESSFUL")
                return True
            else:
                logging.error("Failed to login : {}".format(login_title))
                return False
        except NoSuchElementException:
            logging.error("Element not found.")
            return False

    def get_current_signedin_user_name(self):
        try:
            elements = self.driver.find_elements_by_xpath('//a[@id="nav-link-accountList"]/*')
            return elements[0].text.split(' ')[1]
        except:
            return None


    def get_all_categories(self):
        pass

    def select_category(self,index):
        pass
