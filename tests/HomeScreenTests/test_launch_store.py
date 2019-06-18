import pytest
import logging

logger = logging.getLogger("current test")
logger.setLevel(level=logging.INFO)

@pytest.mark.usefixtures("driver_init")
class TestLaunchStore:
    def test_tc01_launch_store(self):
        self.driver.get("https://www.amazon.in/")
        title = self.driver.title
        assert "Amazon" in title,"Failed to load store"
