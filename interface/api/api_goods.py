from interface import api
import requests

from interface.tools.read_file import read_json


class ApiGoods:
    def __init__(self):
        self.login = api.url + "/admin/auth/login"
        self.add = api.url + "/admin/goods/create"
        self.list = api.url + "/admin/goods/list"

    # 登录接口
    def api_login(self):
        data = {"username": api.login_username, "password": api.login_password, "code": ""}
        return requests.post(url=self.login, json=data, headers=api.header)

    # 商品列表接口
    def api_goods_list(self, goodsSn, name):
        data = {"page": 1, "limit": 20, "goodsSn": goodsSn, "name": name}
        return requests.get(url=self.list, params=data, headers=api.header)

    # 创建商品接口
    def api_add_goods(self, goodSn, name):
        data = read_json("add_goods.json")
        data["goods"]["goodsSn"] = goodSn
        data["goods"]["name"] = name
        return requests.post(url=self.add, json=data, headers=api.header)
