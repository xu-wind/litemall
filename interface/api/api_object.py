import requests
import os
from interface import api
from requests_toolbelt import MultipartEncoder

from interface.config import BASE_PATH
from interface.tools.read_file import read_json


class ApiObject:
    def __init__(self):
        self.login = api.url + "/admin/auth/login"
        self.add_object = api.url + "/admin/storage/create"
        self.object_list = api.url + "/admin/storage/list"
        self.del_object = api.url + "/admin/storage/delete"

    def api_login(self):
        data = {"username": api.login_username, "password": api.login_password, "code": ""}
        return requests.post(self.login, json=data, headers=api.header)

    def api_add_object(self, filename):
        file_path = BASE_PATH + os.sep + "data" + os.sep
        with open(file=file_path + filename, mode='rb') as fis:
            file_content = fis
            files = {
                'filename': file_path + filename,
                'Content-Disposition': 'form-data;',
                'Content-Type': 'image/jpeg',
                'file': (filename, file_content, 'image/jpeg')
            }
            form_data = MultipartEncoder(files)  # 格式转换
            api.object_header['content-type'] = form_data.content_type
            return requests.post(self.add_object, data=form_data, headers=api.object_header)

    def api_object_list(self, key, name):
        data = {"page": 1, "limit": 20, "key": key, "name": name}
        return requests.get(self.object_list, params=data, headers=api.header)

    def api_del_object(self):
        data = read_json("del_object.json")
        return requests.post(self.del_object, json=data, headers=api.header)
