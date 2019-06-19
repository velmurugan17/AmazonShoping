import pytest
import logging


@pytest.mark.usefixtures("store_launch")
class TestSignedUser:

    def test_tc08_signedin_user(self):
        """
        TC08 : Verify signed in username
        """
        logging.info("Signin user test started")
        current_signed_in_user = self.home.get_current_signedin_user_name()
        logging.info("Current signed in user : {}".format(current_signed_in_user))
        assert self.username == current_signed_in_user, "Incorrect username.Expected : {},Actual : {}".format(
            self.username, current_signed_in_user)
        logging.info("Signin user test completed")