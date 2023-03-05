import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    arr = []
    file = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file, "r", encoding="utf-8") as f:
        for data in yaml.load(f, Loader=yaml.FullLoader).values():
            arr.append(tuple(data.values()))
    return arr
