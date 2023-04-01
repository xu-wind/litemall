from web import page
from web.base.web_base import WebBase


class PageSearchCoupon(WebBase):
    # 点击推广管理
    def page_click_promote_manage(self):
        self.base_click(page.li_promote_manage)

    # 点击优惠券管理
    def page_click_coupon_manage(self):
        self.base_click(page.li_coupon_manage)

    def page_input_coupon_name(self, name):
        self.base_input(page.li_input_coupon_name, name)

    def page_choose_coupon_type(self, text, types="请选择优惠券类型"):
        self.web_base_choose_coupon(text, types)

    def page_choose_coupon_status(self, status, types="请选择优惠券状态"):
        self.web_base_choose_coupon(status, types)

    def page_click_search_btn(self):
        self.base_click(page.li_coupon_search)

    def page_click_coupon_details(self):
        self.base_js_click(page.li_coupon_detail)

    def page_get_coupon_name(self):
        return self.base_get_text(page.li_search_coupon_name)

    # 组合查找优惠券业务
    def page_search_coupon(self, name, text, status):
        self.page_click_promote_manage()
        self.page_click_coupon_manage()
        self.page_input_coupon_name(name)
        self.page_choose_coupon_type(text)
        self.page_choose_coupon_status(status)
        self.page_click_search_btn()
        self.page_click_coupon_details()

    def page_add_coupon_search(self, name, text, status):
        self.page_input_coupon_name(name)
        self.page_choose_coupon_type(text)
        self.page_choose_coupon_status(status)
        self.page_click_search_btn()
        self.page_click_coupon_details()
