import json
import os
import yaml

from config import BASE_PATH


def read_json(filename):
    file = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def read_yaml(filename):
    data = []
    file = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file, "r", encoding="utf-8") as f:
        for i in yaml.load(f, Loader=yaml.Loader).values():
            data.append(tuple(i.values()))
    return data


if __name__ == '__main__':
    print(read_yaml("li_login.yaml"))
