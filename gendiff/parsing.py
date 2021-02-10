import json
import yaml


def parse(path, data):
    if path.endswith('.yaml') or path.endswith('.yml'):
        return yaml.safe_load(data)
    return json.load(data)
