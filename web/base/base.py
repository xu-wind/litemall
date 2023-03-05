import allure
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=10, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击元素
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入元素
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        # 输入前先清空
        el.clear()
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 获取截图
    def base_get_screen(self):
        # self.driver.get_screenshot_as_file("../img/{}.png".format(time.strftime("%Y %m %d-%H %M %S")))
        self.driver.get_screenshot_as_file("./img/err.png")
        self.base_img_to_allure()

    # 将截图添加到allure报告
    def base_img_to_allure(self):
        # with open("./img/err.png", "rb") as f:
        #     allure.attach("错误原因:", f.read(), allure.attachment_type.PNG)
        allure.attach.file("./img/err.png", name="错误原因", attachment_type=allure.attachment_type.PNG)
