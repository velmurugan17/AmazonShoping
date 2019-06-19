import pytest


@pytest.mark.usefixtures("driver_init","setup")
class TestLogin:

    @pytest.fixture(scope='function')
    def setup(cls):
        store_url = cls.config["amazon_site"]
        cls.driver.get(store_url)

    def test_tc02_login(self):
        """
        TC02 : Verify login
        """
        assert self.home.login(self.email,self.password),"Login Failed"