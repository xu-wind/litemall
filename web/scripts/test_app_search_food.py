from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep


class TestLogin:
    def setup_class(self):
        self.driver = GetDriver().get_app_driver()
        self.search = PageIn(self.driver).page_get_PageAppSearch()

    def teardown_class(self):
        GetDriver().quit_app_driver()

    def test_login(self, text="西餐", search_text="面包"):
        self.search.page_app_search_food(text, search_text)
        sleep(2)
