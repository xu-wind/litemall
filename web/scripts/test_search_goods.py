import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from time import sleep


class TestSearchGoods:
    def setup_class(self):
        self.driver = GetDriver().get_web_driver(page.url)
        PageIn(self.driver).page_get_PageLogin().page_login_success()
        self.search = PageIn(self.driver).page_get_PageSearchGoods()

    def teardown_class(self):
        GetDriver().quit_web_driver()

    def test_add_goods(self, num="test6666", name="test6666"):
        self.search.page_search_goods(num, name)
        if self.search.page_goods_is_exist(name):
            print("商品存在，添加成功")
        else:
            print("商品不存在，添加失败")
        sleep(2)
