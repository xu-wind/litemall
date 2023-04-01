from web import page
from web.base.web_base import WebBase


class PageAddCoupon(WebBase):
    # 点击推广管理
    def page_click_promote_manage(self):
        self.base_click(page.li_promote_manage)

    # 点击优惠券管理
    def page_click_coupon_manage(self):
        self.base_click(page.li_coupon_manage)

    # 点击添加
    def page_click_add_coupon(self):
        self.base_click(page.li_add_coupon)

    # 输入优惠券名称
    def page_input_coupon_name(self, name):
        self.base_input(page.li_coupon_name, name)

    # 输入介绍
    def page_input_coupon_introduce(self, introduce):
        self.base_input(page.li_coupon_introduce, introduce)

    # 输入标签
    def page_input_coupon_label(self, label):
        self.base_input(page.li_coupon_label, label)

    # 输入最低消费
    def page_input_coupon_consume(self, consume):
        self.base_input(page.li_coupon_consume, consume)

    # 输入满减金额
    def page_input_coupon_full(self, full):
        self.base_input(page.li_coupon_full, full)

    # 输入每人限购
    def page_input_coupon_limit(self, limit):
        self.base_input(page.li_coupon_limit, limit)

    # 选择分发类型
    def page_choose_distribute_type(self, text):
        self.web_base_choose_distribute(text)

    # 有效期选择填写
    def page_input_coupon_validity(self, time):
        self.base_input(page.li_coupon_validity, time)

    # 輸入优惠券数量
    def page_input_coupon_num(self, num):
        self.base_input(page.li_coupon_num, num)

    # 商品限制范围
    def page_goods_limit(self):
        pass

    # 点击确定
    def page_click_coupon_sure(self):
        self.base_click(page.li_coupon_sure)

    # 添加优惠券组合业务
    def page_add_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        self.page_click_promote_manage()
        self.page_click_coupon_manage()
        self.page_click_add_coupon()
        self.page_input_coupon_name(name)
        self.page_input_coupon_introduce(introduce)
        self.page_input_coupon_label(label)
        self.page_input_coupon_consume(consume)
        self.page_input_coupon_full(full)
        self.page_input_coupon_limit(limit)
        self.page_choose_distribute_type(text)
        self.page_input_coupon_num(num)
        self.page_input_coupon_validity(time)
        self.page_click_coupon_sure()
