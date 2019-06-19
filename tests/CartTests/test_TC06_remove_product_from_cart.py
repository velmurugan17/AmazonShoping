import pytest
import logging


@pytest.mark.usefixtures("store_launch","setup")
class TestRemoveProductFromCart:

    @pytest.fixture(scope='function')
    def setup(cls):
        cls.cart.clear_cart()
        cls.cart.add_product_to_cart()

    def test_tc06_remove_product_from_cart(self):
        """
            TC06 : remove added product from cart
        """
        logging.info("Add product to cart test Started")
        self.cart.navigate_to_cart()
        assert self.cart.remove_first_product_from_cart(),"Failed to remove product from cart"
