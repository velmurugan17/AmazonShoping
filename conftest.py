import pytest
import json
import logging
from selenium import webdriver
from lib.home import Home
from lib.search import Search
from lib.category import Category
from lib.cart import Cart


def load_config():
    with open('config') as conf:
        config = json.load(conf)
    return config

@pytest.fixture(scope='class')
def driver_init(request):
    logging.info("Initializing the web driver")
    config = load_config()
    chrome_driver = webdriver.Chrome(config["driver"]["chrome"])
    # Credentials can be handled better to avoid security issues
    request.cls.username = config["credentials"]["username"]
    request.cls.email = config["credentials"]["email"]
    request.cls.password = config["credentials"]["password"]
    request.cls.config = config
    request.cls.driver = chrome_driver
    request.cls.home = Home(request.cls.driver)
    request.cls.search = Search(request.cls.driver)
    request.cls.category = Category(request.cls.driver)
    request.cls.cart = Cart(request.cls.driver)
    yield
    chrome_driver.quit()
    logging.info("closing the web driver")

@pytest.fixture(scope="class")
def store_launch(request,driver_init):
    logging.info("Launching store")
    request.cls.home.launch_store()
    request.cls.home.login(request.cls.email,request.cls.password)
    yield
