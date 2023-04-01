import requests

from interface import api
from interface.tools.read_file import read_json


class ApiCoupon:
    def __init__(self):
        self.login = api.url + "/admin/auth/login"
        self.coupon_list = api.url + "/admin/coupon/list"
        self.category = api.url + "/admin/category/list"
        self.goods_list = api.url + "/admin/goods/list?limit=0"
        self.add_coupon = api.url + "/admin/coupon/create"
        self.del_coupon = api.url + "/admin/coupon/delete"

    # 登录接口
    def api_login(self):
        data = {"username": api.login_username, "password": api.login_password, "code": ""}
        return requests.post(self.login, json=data, headers=api.header)

    # 优惠券列表接口
    def api_coupon_list(self, name, types, status):
        data = {"page": 1, "limit": 20, "name": name, "type": types, "status": status}
        return requests.get(self.coupon_list, params=data, headers=api.header)

    # 商品分类列表接口
    def api_goods_category(self):
        return requests.get(self.category, headers=api.header)

    # 商品列表接口
    def api_goods_list(self):
        return requests.get(self.goods_list, headers=api.header)

    # 创建优惠券接口
    def api_add_coupon(self, name, introduce, label, consume, full, text, limit, num, time):
        data = read_json("add_coupon.json")
        data["name"] = name
        data["desc"] = introduce
        data["tag"] = label
        data["min"] = consume
        data["discount"] = full
        data["limit"] = limit
        data["total"] = num
        data["type"] = text
        data["days"] = time
        return requests.post(self.add_coupon, json=data, headers=api.header)

    # 删除优惠券接口
    def api_del_coupon(self, id, name, introduce, label, consume, full, text, limit, num, time):
        data = read_json("del_coupon.json")
        data["id"] = id
        data["name"] = name
        data["desc"] = introduce
        data["tag"] = label
        data["min"] = consume
        data["discount"] = full
        data["limit"] = limit
        data["total"] = num
        data["type"] = text
        data["days"] = time
        return requests.post(self.del_coupon, json=data, headers=api.header)
