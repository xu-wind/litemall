import pytest

from web import page
from web.page.page_in import PageIn
from web.tools.get_driver import GetDriver
from time import sleep

from web.tools.read_yaml import read_yaml


class TestCoupon:
    def setup(self):
        self.driver = GetDriver().get_web_driver(page.url)
        self.page = PageIn(self.driver)
        self.login = self.page.page_get_PageLogin()
        self.coupon = self.page.page_get_PageAddCoupon()
        self.search = self.page.page_get_PageSearchCoupon()
        self.delete = self.page.page_get_PageDeleteCoupon()

    def teardown(self):
        GetDriver().quit_web_driver()

    # 添加优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_add_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        self.login.page_login_success()
        # 添加优惠券
        self.coupon.page_add_coupon(name, introduce, label, consume, full, text, limit, num, time)
        # 搜索优惠卷
        self.search.page_add_coupon_search(name, text, "正常")
        sleep(3)
        try:
            assert self.search.page_get_coupon_name() == name
        except Exception as e:
            print(e)
            raise

    # 搜索优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_search_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        self.login.page_login_success()
        # 搜索优惠卷
        self.search.page_search_coupon(name, text, "正常")
        sleep(3)
        try:
            assert self.search.page_get_coupon_name() == name
        except Exception as e:
            print(e)
            raise

    # 删除优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_delete_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        self.login.page_login_success()
        # 删除优惠卷
        self.delete.page_delete_coupon(name, text, "正常")
        sleep(2)
        if self.delete.page_exist_coupon(name):
            print("删除优惠券失败")
        else:
            print("删除优惠券成功")
