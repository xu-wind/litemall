import api


class Common:
    @classmethod
    def get_token(cls, r):
        token = r.json().get("data").get("token")
        api.header["x-litemall-admin-token"] = token

    @classmethod
    def assert_response(cls, r, goodsSn, name):
        assert goodsSn == r.json()["data"]["list"][0]["goodsSn"]
        assert name == r.json()["data"]["list"][0]["name"]
