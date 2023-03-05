from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep


class TestLogin:
    def setup_class(self):
        self.driver = GetDriver().get_app_driver()
        self.login = PageIn(self.driver).page_get_PageAppLogin()

    def teardown_class(self):
        GetDriver().quit_app_driver()

    def test_login(self, username="13536297738", passwd="123456"):
        self.login.page_app_login(username, passwd)
        sleep(2)
