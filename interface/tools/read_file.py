import json
import os
import yaml

from interface.config import BASE_PATH


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


def yaml_to_json(filename):
    file = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file, "r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=yaml.Loader)
    json_data = json.dumps(data)
    print(json_data)


def json_to_yaml(filename):
    file = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    yaml_data = yaml.dump(data)
    print(yaml_data)
