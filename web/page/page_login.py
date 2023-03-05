from base.base import Base
import page


class PageLogin(Base):
    # 输入账户
    def page_input_username(self, username):
        self.base_input(page.li_username, username)

    # 输入密码
    def page_input_passwd(self, passwd):
        self.base_input(page.li_password, passwd)

    # 点击登录
    def page_click_login(self):
        self.base_click(page.li_login_btn)

    # 组合登录业务
    def page_login(self, username, passwd):
        self.page_input_username(username)
        self.page_input_passwd(passwd)
        self.page_click_login()

    def page_login_success(self, username="hogwarts", passwd="test12345"):
        self.page_input_username(username)
        self.page_input_passwd(passwd)
        self.page_click_login()