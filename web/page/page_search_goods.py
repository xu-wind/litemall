import page
from base.web_base import WebBase


class PageSearchGoods(WebBase):
    # 点击商品管理
    def page_click_goods_manage(self):
        self.base_click(page.li_goods_manage)

    # 点击商品列表
    def page_click_goods_list(self):
        self.base_click(page.li_goods_list)

    # 输入商品编号
    def page_input_goods_num(self, num):
        self.base_input(page.li_input_goods_num, num)

    # 输入商品名称
    def page_input_goods_name(self, name):
        self.base_input(page.li_input_goods_name, name)

    # 点击查找
    def page_click_search_btn(self):
        self.base_click(page.li_search_btn)

    # 判断商品是否存在
    def page_goods_is_exist(self, text):
        return self.web_base_goods_is_exist(text)

    # 组合搜索商品业务
    def page_search_goods(self, num, name):
        self.page_click_goods_manage()
        self.page_click_goods_list()
        self.page_input_goods_num(num)
        self.page_input_goods_name(name)
        self.page_click_search_btn()
