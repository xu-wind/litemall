from time import sleep

import pytest

from web.page.page_in import PageIn
from web.tools.get_driver import GetDriver
from web import page


class TestGoods:
    def setup(self):
        self.driver = GetDriver().get_web_driver(page.url)
        self.page = PageIn(self.driver)
        self.login = self.page.page_get_PageLogin()
        self.add = self.page.page_get_PageAddGoods()
        self.search = self.page.page_get_PageSearchGoods()

    def teardown(self):
        GetDriver().quit_web_driver()

    # @pytest.mark.parametrize("num,name,text", read_yaml("li_add_goods.yaml"))
    def test_add_goods(self, num="test12345s", name="test12345", text="优衣库制造商"):
        # 登录
        self.login.page_login_success()
        # 添加商品
        self.add.page_goods_groud(num, name, text)
        # 搜索商品
        self.search.page_search_goods(num, name)
        if self.search.page_goods_is_exist(num, name):
            print("商品存在，添加成功")
        else:
            print("商品不存在，添加失败")
        sleep(2)

    # @pytest.mark.parametrize("num,name,text", read_yaml("li_add_goods.yaml"))
    @pytest.mark.skip()
    def test_search_goods(self, num="test123456s", name="test123456", text="优衣库制造商"):
        # 登录
        self.login.page_login_success()
        # 添加商品
        self.add.page_goods_groud(num, name, text)
        # 搜索商品
        self.search.page_search_goods(num, name)
        if self.search.page_goods_is_exist(num, name):
            print("商品存在，添加成功")
        else:
            print("商品不存在，添加失败")
        sleep(2)
