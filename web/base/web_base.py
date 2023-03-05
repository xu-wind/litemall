from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):
    # 选择所属品牌商
    def web_base_choose_brander(self, text="优衣库制造商"):
        el = By.XPATH, "//*[text()='所属品牌商']/..//input"
        self.base_click(el)
        el = By.XPATH, "//*[text()='{}']".format(text)
        self.base_click(el)

    # 判断商品是否存在
    def web_base_goods_is_exist(self, text):
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            self.base_find_element(loc, timeout=3)
            # print("找到元素{}！".format(loc))
            return True
        except:
            return False
