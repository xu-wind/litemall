from selenium.webdriver.common.by import By

from web.base.base import Base


class WebBase(Base):
    # 选择所属品牌商
    def web_base_choose_brander(self, text):
        el = By.XPATH, "//*[text()='所属品牌商']/..//input"
        self.base_click(el)
        el = By.XPATH, "//*[text()='{}']".format(text)
        self.base_click(el)

    # 判断商品是否存在
    def web_base_goods_is_exist(self, num, name):
        loc1 = By.XPATH, "//*[text()='{}']".format(num)
        loc2 = By.XPATH, "//*[text()='{}']".format(name)
        try:
            self.base_find_element(loc1, timeout=3)
            self.base_find_element(loc2, timeout=3)
            # print("找到元素{}！".format(loc))
            return True
        except:
            return False

    # 选择分发类型
    def web_base_choose_distribute(self, text):
        el = By.XPATH, "//*[text()='分发类型']/..//input"
        self.base_click(el)
        el = By.XPATH, "//*[@x-placement='bottom-start' or @x-placement='top-start']//*[text()='{}']".format(text)
        self.base_click(el)

    # 选择优惠券类型
    def web_base_choose_coupon(self, text, types):
        el = By.XPATH, "//*[@placeholder='{}']/../span".format(types)
        self.base_js_click(el)
        el = By.XPATH, "//*[@x-placement='bottom-start']//*[text()='{}']".format(text)
        self.base_click(el)
