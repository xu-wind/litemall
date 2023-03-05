from selenium.webdriver.common.by import By

from base.base import Base


class AppBase(Base):
    # 从右向左滑动
    def app_base_right_swipe_left(self, swipe_area, text):
        el = self.base_find_element(swipe_area)
        location = el.location
        size = el.size
        start_x = size["width"] * 0.8
        start_y = location["y"] + size["height"] * 0.5
        end_x = size["width"] * 0.2
        end_y = location["y"] + size["height"] * 0.5
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(text)
        while True:
            page_resource = self.driver.page_source
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            try:
                self.base_find_element(loc, timeout=3)
                self.base_click(loc)
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_resource == self.driver.page_source:
                raise

    # 从下向上滑动
    def app_base_down_swipe_up(self, swipe_area, search_text):
        el = self.base_find_element(swipe_area)
        location = el.location
        size = el.size
        start_x = size["width"] * 0.5
        start_y = location["y"] + size["height"] * 0.8
        end_x = size["width"] * 0.5
        end_y = location["y"] + size["height"] * 0.2
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(search_text)
        while True:
            page_resource = self.driver.page_source
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            try:
                self.base_find_element(loc, timeout=3)
                self.base_click(loc)
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_resource == self.driver.page_source:
                raise e
