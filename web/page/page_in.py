from web.page.page_add_coupon import PageAddCoupon
from web.page.page_add_goods import PageAddGoods
from web.page.page_app_login import PageAppLogin
from web.page.page_app_search import PageAppSearch
from web.page.page_delete_coupon import PageDeleteCoupon
from web.page.page_login import PageLogin
from web.page.page_object_storage import PageObjectStorage
from web.page.page_search_coupon import PageSearchCoupon
from web.page.page_search_goods import PageSearchGoods


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

    def page_get_PageAddCoupon(self):
        return PageAddCoupon(self.driver)

    def page_get_PageSearchCoupon(self):
        return PageSearchCoupon(self.driver)

    def page_get_PageDeleteCoupon(self):
        return PageDeleteCoupon(self.driver)

    def page_get_PageObjectStorage(self):
        return PageObjectStorage(self.driver)