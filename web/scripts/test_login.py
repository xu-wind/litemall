import pytest
import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep

from tools.read_yaml import read_yaml


class TestLogin:
    def setup_class(self):
        self.driver = GetDriver().get_web_driver(page.url)
        self.login = PageIn(self.driver).page_get_PageLogin()

    def teardown_class(self):
        GetDriver().quit_web_driver()

    @pytest.mark.parametrize("username,passwd", read_yaml("li_login.yaml"))
    def test_login(self, username, passwd):
        self.login.page_login(username, passwd)
        # try:
        #     assert 1 == 2
        # except Exception as e:
        #     self.login.base_get_screen()
        sleep(2)


if __name__ == '__main__':
    pytest.main(['-s', "test_login.py"])
