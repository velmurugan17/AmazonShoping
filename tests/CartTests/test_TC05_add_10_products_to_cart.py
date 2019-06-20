import pytest
import logging


@pytest.mark.usefixtures("store_launch","setup")
class TestAdd10ProductToCart:

    @pytest.fixture(scope='function')
    def setup(cls):
        cls.cart.clear_cart()
        yield
        cls.cart.clear_cart()

    def test_tc05_add_10_product_to_cart(self):
        """
            TC05 : Add 10 product to cart
            Note : ideally more validation should be done to ensure if the expected product is added to cart and
            check if actually 10 product exist in cart.
            For now I have kept assertion points simple by focusing more on building framework architecture
        """
        logging.info("Add product to cart test Started")
        added_product_title = self.cart.add_product_to_cart(count=10)
        assert len(added_product_title)==10,"Add product to cart failed"
        logging.info("Add product to cart test completed")