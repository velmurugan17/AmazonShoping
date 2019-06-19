import pytest
import logging


@pytest.mark.usefixtures("store_launch")
class TestGetAllMajorCategories:


    def test_tc09_get_all_major_categories(self):
        """
            TC09
        """
        logging.info("Get all major Categories test Started")
        assert self.category.select_shop_by_category()
        major_categories = self.category.get_all_major_category()
        logging.info("Major categories : {}".format(major_categories))
        assert major_categories,"Major category is not found"
        assert len(major_categories)>0,"No item found in major category"
        logging.info("Get all major Categories test is completed")