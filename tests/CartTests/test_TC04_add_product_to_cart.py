import pytest
import logging


@pytest.mark.usefixtures("store_launch","setup")
class TestAddProductToCart:

    @pytest.fixture(scope='function')
    def setup(cls):
        cls.cart.clear_cart()
        yield
        cls.cart.clear_cart()

    def test_tc04_add_product_to_cart(self):
        """
            TC04 : Add single product to cart
        """
        logging.info("Add product to cart test Started")
        added_product_title = self.cart.add_product_to_cart()
        assert len(added_product_title)==1,"Add product to cart failed"
        logging.info("Add product to cart test completed")