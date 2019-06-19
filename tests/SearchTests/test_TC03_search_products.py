import pytest
import logging


@pytest.mark.usefixtures("store_launch")
class TestSearchProducts:


    def test_tc03_search_products_in_store(self):
        """
            Test : TC02 - Verify search is working fine
            Note : the current validation needs to be enhanced to check
            if the search items are appropriate for search input by checking its label in the product.
            But currently just checking if the product list is found and their type is string
        """
        logging.info("Search test started")
        product_title_list = self.search.get_search_product_title("mobile")
        assert len(product_title_list)>0,"No product found.Search failed"
        for title in product_title_list:
            assert isinstance(title,unicode),"Product title is incorrect.Search failed"
        logging.info("Search test is completed")