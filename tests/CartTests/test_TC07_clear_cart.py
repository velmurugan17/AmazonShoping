import pytest
import logging


@pytest.mark.usefixtures("store_launch")
class TestClearCart:


    def test_tc07_clear_cart(self):
        """
            TC07
        """
        logging.info("Clear cart test Started")
        assert self.cart.clear_cart()
        logging.info("Clear cart test completed")