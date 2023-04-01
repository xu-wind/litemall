from web import page
from web.base.web_base import WebBase


class PageAddGoods(WebBase):
    # 点击商品管理
    def page_click_goods_manage(self):
        self.base_click(page.li_goods_manage)

    # 点击商品上架
    def page_click_goods_groud(self):
        self.base_click(page.li_goods_groud)

    # 输入商品编号
    def page_input_goods_num(self, num):
        self.base_input(page.li_goods_num, num)

    # 输入商品名称
    def page_input_goods_name(self, name):
        self.base_input(page.li_goods_name, name)

    # 选择品牌商
    def page_choose_brander(self, text):
        self.web_base_choose_brander(text)

    # 点击上架
    def page_click_groud_btn(self):
        self.base_click(page.li_groud_btn)

    # 商品上架组合业务
    def page_goods_groud(self, num, name, text):
        self.page_click_goods_manage()
        self.page_click_goods_groud()
        self.page_input_goods_num(num)
        self.page_input_goods_name(name)
        self.page_choose_brander(text)
        self.page_click_groud_btn()
