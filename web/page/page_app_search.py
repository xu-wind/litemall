import page
from base.app_base import AppBase


class PageAppSearch(AppBase):
    # 点击VIP
    def page_click_vip(self):
        self.base_click(page.app_VIP)

    # 从左向右滑动查找指定标签
    def page_right_swipe_left(self, text):
        self.app_base_right_swipe_left(page.app_channel_area, text)

    # 从下到上滑动查找指定美食
    def page_down_swipe_up(self, search_text):
        self.app_base_down_swipe_up(page.app_food_area, search_text)

    # 组合查找美食业务
    def page_app_search_food(self, text, search_text):
        self.page_click_vip()
        self.page_right_swipe_left(text)
        self.page_down_swipe_up(search_text)
