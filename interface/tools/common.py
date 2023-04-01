from interface import api
import json


class Common:
    @classmethod
    def get_token(cls, r):
        token = r.json().get("data").get("token")
        api.header["x-litemall-admin-token"] = token
        api.object_header["x-litemall-admin-token"] = token

    @classmethod
    def assert_goods_response(cls, r, goodsSn, name):
        # assert goodsSn == r.json()["data"]["list"][0]["goodsSn"]
        # assert name == r.json()["data"]["list"][0]["name"]
        assert goodsSn == r.json().get("data").get("list")[0].get("goodsSn")
        assert name == r.json().get("data").get("list")[0].get("name")

    @classmethod
    def assert_is_exist(cls, r, name):
        try:
            assert name == r.json().get("data").get("list")[0].get("name")
            return True
        except Exception as e:
            return False

    # 获取测试开发实战教程商品的id
    @classmethod
    def get_goods_id(cls, r):
        for i in r.json().get("data").get("list"):
            if i.get("name") == "测试开发实战教程":
                return i.get("id")

    # 断言对象存储是否添加成功
    @classmethod
    def save_object_information(cls, r):
        with open("../data/del_object.json", "w", encoding="utf8") as f:
            f.write(json.dumps(r.json().get("data").get("list")[0]))
