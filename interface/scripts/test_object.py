import pytest

from interface.api.api_object import ApiObject
from interface.tools.common import Common


class TestObject:
    name = "test.jpg"
    key = None

    def setup(self):
        self.object = ApiObject()

    # 新增对象存储
    def test_add_object(self):
        # 登录
        r = self.object.api_login()
        Common().get_token(r)
        # 添加对象存储
        r = self.object.api_add_object(TestObject.name)
        # print(r.json())
        TestObject.key = r.json().get("data").get("key")
        try:
            assert "成功" == r.json().get("errmsg")
            print("新增对象存储成功！")
        except Exception as e:
            print(e)
            raise

    # 搜索对象存储
    @pytest.mark.skip
    def test_search_object(self):
        r = self.object.api_login()
        Common().get_token(r)
        r = self.object.api_object_list(TestObject.key, TestObject.name)
        Common.save_object_information(r)
        if Common.assert_is_exist(r, TestObject.name):
            print("对象存储存在！")
        else:
            print("对象存储不存在！")

    # 删除对象存储
    @pytest.mark.skip
    def test_delete_object(self):
        r = self.object.api_login()
        Common().get_token(r)
        r = self.object.api_del_object()
        try:
            assert "成功" == r.json().get("errmsg")
            print("删除对象存储成功！")
        except Exception as e:
            print(e)
            raise


if __name__ == '__main__':
    pytest.main(["-s", "test_object.py"])
