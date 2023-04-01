from time import sleep

from web import page
from web.page.page_in import PageIn
from web.tools.get_driver import GetDriver


class TestObject:
    def setup(self):
        self.driver = GetDriver().get_web_driver(page.url)
        self.page = PageIn(self.driver)
        self.login = self.page.page_get_PageLogin()
        self.object = self.page.page_get_PageObjectStorage()

    def teardown(self):
        GetDriver().quit_web_driver()

    # 添加对象
    def test_add_object(self):
        # 登录
        self.login.page_login_success()
        # 添加对象存储
        self.object.page_object_storage(r"E:\pycharm\Work_place\hmtt\web\data\test.png", "test.png")
        # 断言是否添加成功
        try:
            self.object.page_get_object() == "test.png"
        except Exception as e:
            print(e)
            raise
