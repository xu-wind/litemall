import page
from base.base import Base


class PageAppLogin(Base):
    # 点击我的
    def page_click_myself(self):
        self.base_click(page.app_myself)

    # 点击立即登录
    def page_click_login(self):
        self.base_click(page.app_login)

    # 输入账户
    def page_input_username(self, username):
        self.base_input(page.app_username, username)

    # 点击下一步
    def page_click_next(self):
        self.base_click(page.app_next)

    # 输入密码
    def page_input_passwd(self, passwd):
        self.base_input(page.app_passwd, passwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.app_login_btn)

    # 组合app登录业务
    def page_app_login(self, username, passwd):
        self.page_click_myself()
        self.page_click_login()
        self.page_input_username(username)
        self.page_click_next()
        self.page_input_passwd(passwd)
        self.page_click_login_btn()
