import pytest


@pytest.mark.usefixtures("driver_init")
class TestLaunchStore:

    def test_tc01_launch_store(self):
        """
        TC01 : Verify amazon store launch
        """
        store_url = self.config["amazon_site"]
        self.driver.get(store_url)
        title = self.driver.title
        assert "Amazon" in title, "Failed to load store"
