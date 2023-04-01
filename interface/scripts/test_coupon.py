import pytest
from interface.api.api_coupon import ApiCoupon
from interface.tools.common import Common
from interface.tools.read_file import read_yaml


class TestCoupon:
    coupon_id = None  # 保存优惠券id

    def setup(self):
        self.coupon = ApiCoupon()

    # 增加优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_add_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        r = self.coupon.api_login()
        Common.get_token(r)
        # 增加优惠券
        r = self.coupon.api_add_coupon(name, introduce, label, consume, full, text, limit, num, time)
        TestCoupon.coupon_id = r.json().get("data").get("id")
        # 搜索优惠券
        r = self.coupon.api_coupon_list(name, text, 0)
        # 断言是否增加成功
        if Common.assert_is_exist(r, name):
            print("优惠券新增成功")
        else:
            print("优惠券新增失败")

    # 搜索优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_search_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        r = self.coupon.api_login()
        Common.get_token(r)
        # 搜索优惠券
        r = self.coupon.api_coupon_list(name, text, 0)
        # 断言优惠券是否存在
        if Common.assert_is_exist(r, name):
            print("优惠券存在")
        else:
            print("优惠券不存在")

    # 删除优惠券
    @pytest.mark.parametrize("name,introduce,label,consume,full,text,limit,num,time", read_yaml("li_coupon.yaml"))
    def test_del_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        # 登录
        r = self.coupon.api_login()
        Common.get_token(r)
        # 删除优惠券
        self.coupon.api_del_coupon(TestCoupon.coupon_id, name, introduce, label, consume, full, text, limit, num,
                                   time)
        # 搜索优惠券
        r = self.coupon.api_coupon_list(name, text, 0)
        # 断言是否删除成功
        if not Common.assert_is_exist(r, name):
            print("优惠券删除成功")
        else:
            print("优惠券删除失败")


if __name__ == '__main__':
    pytest.main(["-s", "test_coupon.py"])
