import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from time import sleep
from lib.search import Search


class Cart:
    def __init__(self,driver):
        self.driver = driver
        self._search = Search(self.driver)

    def navigate_to_cart(self):
        try:
            self.driver.find_element_by_id("nav-cart").click()
            return True
        except NoSuchElementException as e:
            logging.error("Navigate to cart Failed.Exception  {}".format(str(e)))
            return False

    def add_product_to_cart(self,count=1,search_input='mobile'):
        """

        :param count: int number of product to add into cart.Max allowed count is 20.
        :param search_input:
        :return:
        """
        try:
            product_title_added_to_cart = []
            if count>20:
                logging.warning("Maximum 20 products only allowed.Setting counter to 20...")
                count=20
            self._search.search_by_keyword(search_input)
            product_object_list = self.driver.find_elements_by_xpath('//span[@class="a-size-medium a-color-base a-text-normal"]')
            logging.info("PRODUCT LENGTH IS : {}".format(len(product_object_list)))
            for product_index in range(0,count):
                element = product_object_list[product_index]
                title = element.text
                parent_window = self.driver.window_handles[0]
                self.driver.execute_script("window.scrollTo(0,"+str(element.location['y']-150)+")")
                element.click()
                sleep(3)
                new_window = self.driver.window_handles[1]
                self.driver.switch_to.window(new_window)
                self.driver.find_element_by_id("add-to-cart-button").click()
                logging.info("{} is added to the cart successfully...".format(title))
                product_title_added_to_cart.append(title)
                sleep(3)
                self.driver.close()
                self.driver.switch_to.window(parent_window)
            return product_title_added_to_cart
        except NoSuchElementException as e:
            logging.error("Failed to add product to cart. {}".format(str(e)))

    def remove_first_product_from_cart(self):
        try:
            self.driver.find_element_by_xpath('.//input[@value="Delete"]').click()
            sleep(5) # Hardcoded sleep is not recommended.This can be better optimized
            return True
        except NoSuchElementException as e:
            logging.error("No item in cart to delete")
            return False


    def clear_cart(self):
        """
        Usually there will be a backend call to clear cart and entitlement
        :return:
        """

        try:
            if not self.navigate_to_cart():
                return False

            while True:
                cart_header = self.driver.find_element_by_xpath('.//div[@id="sc-active-cart"]')
                if len(cart_header.find_elements_by_xpath(".//h2"))!=0:
                    header_text = cart_header.find_element_by_xpath(".//h2").text
                else:
                    header_text = cart_header.find_element_by_xpath(".//h1").text

                if "Your Shopping Cart is empty" in header_text:
                    logging.info("All product removed from cart.Cart is empty now")
                    return True
                else:
                    logging.info("Removing item from cart")
                    self.remove_first_product_from_cart()

        except Exception as e:
            logging.error("Exception ourred in clear cart. {}".format(str(e)))
            return False

