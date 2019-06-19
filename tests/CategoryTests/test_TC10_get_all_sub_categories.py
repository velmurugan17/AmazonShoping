import pytest
import logging


@pytest.mark.usefixtures("store_launch")
class TestGetAllSubCategories:


    def test_tc10_get_all_sub_categories(self):
        """
            TC10 : verify all sub categories in 'shop by categories' menu
        """
        logging.info("Get all sub categories test Started")
        assert self.category.select_shop_by_category()
        sub_categories = self.category.get_all_sub_categories()
        logging.info("Sub categories : {}".format(sub_categories))
        assert sub_categories,"Sub category is not found"
        assert len(sub_categories)>0,"No item found in sub category"
        logging.info("Get all sub categories test is completed")