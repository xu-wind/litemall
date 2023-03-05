from page.page_add_goods import PageAddGoods
from page.page_app_login import PageAppLogin
from page.page_app_search import PageAppSearch
from page.page_login import PageLogin
from page.page_search_goods import PageSearchGoods


class PageIn:
    def __init__(self, driver):
        self.driver = driver

    def page_get_PageLogin(self):
        return PageLogin(self.driver)

    def page_get_PageAddGoods(self):
        return PageAddGoods(self.driver)

    def page_get_PageSearchGoods(self):
        return PageSearchGoods(self.driver)

    def page_get_PageAppLogin(self):
        return PageAppLogin(self.driver)

    def page_get_PageAppSearch(self):
        return PageAppSearch(self.driver)