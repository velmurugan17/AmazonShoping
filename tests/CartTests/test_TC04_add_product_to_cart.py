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
            Note : ideally more validation should be done to ensure if the product is added to cart.
            For now I have kept assertion points simple by focusing more on building framework architecture
        """
        logging.info("Add product to cart test Started")
        added_product_title = self.cart.add_product_to_cart()
        assert len(added_product_title)==1,"Add product to cart failed"
        logging.info("Add product to cart test completed")