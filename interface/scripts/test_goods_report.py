import unittest

from parameterized import parameterized
from interface.api.api_goods import ApiGoods
from interface.tools.common import Common
from interface.tools.read_file import read_yaml


class TestGoods(unittest.TestCase):
    def setUp(self):
        self.goods = ApiGoods()

    @parameterized.expand(read_yaml("li_goods.yaml"))
    def test01_add_goods(self, goodsSn, name):
        r = self.goods.api_login()
        Common.get_token(r)
        self.goods.api_add_goods(goodsSn, name)
        r = self.goods.api_goods_list(goodsSn, name)
        # print(r.json())
        Common.assert_goods_response(r, goodsSn, name)


if __name__ == '__main__':
    unittest.main()
