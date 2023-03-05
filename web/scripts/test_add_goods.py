import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep


class TestAddGoods:
    def setup_class(self):
        self.driver = GetDriver().get_web_driver(page.url)
        PageIn(self.driver).page_get_PageLogin().page_login_success()
        self.add = PageIn(self.driver).page_get_PageAddGoods()

    def teardown_class(self):
        GetDriver().quit_web_driver()

    def test_add_goods(self, num="test6666", name="test6666", text="优衣库制造商"):
        self.add.page_goods_groud(num, name, text)
        sleep(2)
