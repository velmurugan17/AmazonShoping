import pytest
import logging

@pytest.mark.usefixtures("store_launch")
class TestSearchProducts:


    def test_tc02_search_products_in_store(self):
        """
            Test : TC02 - Verify search is working fine
        """

        title = self.driver.title
        assert "Amazon" in title
