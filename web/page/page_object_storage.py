from web import page
from web.base.web_base import WebBase
from time import sleep


class PageObjectStorage(WebBase):
    # 点击系统管理
    def page_click_system_manage(self):
        self.base_click(page.li_system_manage)

    # 点击对象存储
    def page_click_object_storage(self):
        self.base_click(page.li_object_storage)

    # 点击添加
    def page_click_add_object_btn(self):
        self.base_click(page.li_add_object)

    # 上传文件
    def page_submit_file(self, file):
        self.base_send_file(page.li_submit_file, file)
        sleep(2)

    # 关闭上传文件窗口
    def page_click_close_submit(self):
        self.base_click(page.li_close_submit)

    # 输入对象名称
    def page_input_object_name(self, name):
        self.base_input(page.li_input_object_name, name)

    # 点击查找
    def page_click_search_btn(self):
        self.base_click(page.li_search_object)

    # 获取对象名称
    def page_get_object(self):
        return self.base_get_text(page.li_object_name)

    # 对象存储业务组合
    def page_object_storage(self, file, name):
        self.page_click_system_manage()
        self.page_click_object_storage()
        self.page_click_add_object_btn()
        self.page_submit_file(file)
        self.page_click_close_submit()
        self.page_input_object_name(name)
        self.page_click_search_btn()
