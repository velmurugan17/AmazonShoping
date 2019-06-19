import pytest
import logging


@pytest.mark.usefixtures("store_launch","setup")
class TestClearCart:

    @pytest.fixture(scope='function')
    def setup(cls):
        cls.cart.add_product_to_cart()


    def test_tc07_clear_cart(self):
        """
            TC07 : clear cart
        """
        logging.info("Clear cart test Started")
        assert self.cart.clear_cart()
        logging.info("Clear cart test completed")