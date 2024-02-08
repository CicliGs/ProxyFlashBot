import json


def load_json_config(path="text-values-config.json"):
    with open(path, "r") as json_file:
        data = json.load(json_file)

    return data
