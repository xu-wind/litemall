from time import sleep

from page.page_in import PageIn
from tools.get_driver import GetDriver
import page


class Test:
    def setup_class(self):
        self.driver = GetDriver().get_web_driver(page.url)
        self.page = PageIn(self.driver)
        self.login = self.page.page_get_PageLogin()
        self.add = self.page.page_get_PageAddGoods()
        self.search = self.page.page_get_PageSearchGoods()

    def teardown_class(self):
        GetDriver().quit_web_driver()

    def test_merge(self, num="test12345", name="test12345", text="优衣库制造商"):
        self.login.page_login_success()
        self.add.page_goods_groud(num, name, text)
        self.search.page_search_goods(num, name)
        if self.search.page_goods_is_exist(name):
            print("商品存在，添加成功")
        else:
            print("商品不存在，添加失败")
        sleep(2)
