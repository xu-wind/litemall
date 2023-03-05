import pytest

from api.api_goods import ApiGoods
from tools.common import Common
from tools.read_file import read_yaml


class TestGoods:
    def setup_class(self):
        self.goods = ApiGoods()

    @pytest.mark.parametrize("username,passwd", read_yaml("li_login.yaml"))
    def test01_add_goods(self, username, passwd, goodsSn="jjjjj", name="cxk"):
        r = self.goods.api_login(username, passwd)
        Common.get_token(r)
        self.goods.api_add_goods(goodsSn, name)
        r = self.goods.api_goods_list(goodsSn, name)
        Common.assert_response(r, goodsSn, name)
